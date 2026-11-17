import subprocess, numpy as np, soundfile as sf, pathlib, glob, os
from scipy import signal
SR = 44100
R = '/tmp/claude-tool-results/5f7896a1-32e9-59b0-b359-e8fae6df1f83/'
FILES = ['mcp-Speko-blob-1794954223678-ozjrfq-68914f70.wav','mcp-Speko-blob-1794954228226-ppuaee-b00549b6.wav',
 'mcp-Speko-blob-1794954230135-6b1n2s-1f6260c0.wav','mcp-Speko-blob-1794954233073-ega5zv-aa4077c0.wav',
 'mcp-Speko-blob-1794954235509-8ndmiz-0cf92d6e.wav','mcp-Speko-blob-1794954237649-dyk9iq-e85b9fc6.wav',
 'mcp-Speko-blob-1794954239725-10rybb-3a6b37c2.wav','mcp-Speko-blob-1794954241993-2ekub9-71120d3c.wav',
 'mcp-Speko-blob-1794954244214-w1ezkc-13f404f2.wav']
W48 = pathlib.Path('/home/claude/smilefix-media/w48'); OUT = pathlib.Path('/home/claude/smilefix-media/w48v')

def load(f):
    a, sr = sf.read(R+f)
    if a.ndim > 1: a = a.mean(1)
    if sr != SR: a = signal.resample_poly(a, SR, sr)
    thr = 0.02*np.max(np.abs(a)); idx = np.where(np.abs(a) > thr)[0]
    return a[max(0, idx[0]-int(.03*SR)): idx[-1]+int(.12*SR)]
clips = [load(f) for f in FILES]
lead, gap, fade = 0.30, 0.45, 0.4
durs = [lead + len(c)/SR + gap for c in clips]; durs[-1] += 1.2
total = sum(durs) + fade
N = int(total*SR) + SR
voice = np.zeros(N); t0 = 0
for c, d in zip(clips, durs):
    s = int((t0+lead)*SR); voice[s:s+len(c)] += c; t0 += d
voice = voice/np.max(np.abs(voice))*0.9

# ---------- original music (royalty-free, generated) ----------
BPM = 104; beat = 60/BPM; nb = int(beat*SR); t = np.arange(N)/SR
rng = np.random.default_rng(7)
def mtof(m): return 440*2**((m-69)/12)
prog = [[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]]  # Cmaj7 Am7 Fmaj7 G7
bass_roots = [36,33,29,31]
music = np.zeros(N)
def add(buf, start, sig):
    e = min(len(buf), start+len(sig));
    if start < len(buf): buf[start:e] += sig[:e-start]
# electric-piano chords (2 beats each hit, 4 beats per chord)
def epiano(f, L):
    tt = np.arange(L)/SR; env = np.exp(-tt*2.2)*(1-np.exp(-tt*200))
    mod = np.sin(2*np.pi*f*2*tt)*np.exp(-tt*4)*1.2
    return np.sin(2*np.pi*f*tt + mod)*env
bar = 4*nb; nbars = N//bar + 1
for b in range(nbars):
    ch = prog[b % 4]
    for hit in (0, 2.5):
        L = int(2*beat*SR)
        sig = sum(epiano(mtof(m), L) for m in ch)/4
        add(music, b*bar+int(hit*nb), sig*0.55)
    # bass: root on 1 and 3, fifth on 4&
    for pos, off in ((0,0),(2,0),(3.5,7)):
        L = int(0.9*beat*SR); tt = np.arange(L)/SR
        f = mtof(bass_roots[b % 4]+off)
        s = (np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt))*np.exp(-tt*3)*(1-np.exp(-tt*300))
        add(music, b*bar+int(pos*nb), s*0.6)
# drums
def kick():
    L = int(.35*SR); tt = np.arange(L)/SR; f = 110*np.exp(-tt*18)+45
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*9)
def snare():
    L = int(.22*SR); tt = np.arange(L)/SR; n = rng.standard_normal(L)
    n = signal.lfilter(*signal.butter(2, [1200/(SR/2), 7000/(SR/2)], 'band'), n)
    return (n*0.7+np.sin(2*np.pi*190*tt)*0.4)*np.exp(-tt*18)
def hat():
    L = int(.06*SR); n = rng.standard_normal(L)
    n = signal.lfilter(*signal.butter(2, 7000/(SR/2), 'high'), n); return n*np.exp(-np.arange(L)/SR*60)
K, S, H = kick(), snare(), hat()
intro = 2  # bars without drums
for b in range(intro, nbars):
    for i in range(4):
        st = b*bar + i*nb
        if i in (0, 2): add(music, st, K*0.9)
        if i in (1, 3): add(music, st, S*0.35)
        add(music, st, H*0.18); add(music, st+nb//2, H*0.12)
# soft reverb
ir_t = np.arange(int(1.2*SR))/SR; ir = rng.standard_normal(len(ir_t))*np.exp(-ir_t*4.5); ir[0] = 1
music = music + 0.12*signal.fftconvolve(music, ir)[:N]/np.max(np.abs(ir))
music = signal.lfilter(*signal.butter(2, 9000/(SR/2), 'low'), music)
music /= np.max(np.abs(music))
# ducking under voice
envv = np.abs(voice); win = int(.25*SR)
envv = np.convolve(envv, np.ones(win)/win, 'same'); envv /= envv.max()
duck = 1 - 0.55*np.clip(envv*4, 0, 1)
duck = np.convolve(duck, np.ones(int(.15*SR))/int(.15*SR), 'same')
music = music*0.30*duck
fi, fo = int(0.8*SR), int(2.0*SR); music[:fi] *= np.linspace(0,1,fi)
end = int(total*SR); music[end-fo:end] *= np.linspace(1,0,fo); music[end:] = 0
mix = voice + music
mix /= max(1.0, np.max(np.abs(mix))/0.97)
sf.write('/tmp/mix_luca.wav', np.stack([mix, mix], 1)[:end], SR)

fs = [str(W48/f'tt_guida_{i:02d}.jpg') for i in range(9)]
cmd = ['ffmpeg','-y','-hide_banner','-loglevel','error']
for f, d in zip(fs, durs): cmd += ['-loop','1','-t',f'{d+fade:.2f}','-i',f]
cmd += ['-i','/tmp/mix_luca.wav']
filt = []; last = '[0:v]'
for i in range(1, len(fs)):
    off = sum(durs[:i]); lab = f'[v{i}]'
    filt.append(f'{last}[{i}:v]xfade=transition=slideleft:duration={fade}:offset={off:.2f}{lab}'); last = lab
filt.append(f'{last}format=yuv420p[vout]')
cmd += ['-filter_complex',';'.join(filt),'-map','[vout]','-map',f'{len(fs)}:a','-c:v','libx264','-preset','medium','-crf','20','-r','30',
        '-c:a','aac','-b:a','192k','-af','loudnorm=I=-14:TP=-1.5:LRA=11','-shortest',str(OUT/'yt_guida_asta_luca.mp4')]
subprocess.run(cmd, check=True)
print([round(d,2) for d in durs], round(total,1))
