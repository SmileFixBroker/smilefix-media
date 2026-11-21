# Monta i video settimanali: slide + voce Luca + musica originale con ducking. Uso: python3 build_videos.py w48
import subprocess, sys, pathlib, importlib.util, numpy as np, soundfile as sf
from scipy import signal
WK = sys.argv[1]
spec = importlib.util.spec_from_file_location("c", f"/home/claude/smilefix-media/tools/{WK}_content.py"); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
D = pathlib.Path(f'/home/claude/smilefix-media/{WK}v'); SR = 44100
def mtof(m): return 440*2**((m-69)/12)

def music(N, seed, prog_i):
    rng = np.random.default_rng(seed); BPM = [96, 104, 112][prog_i % 3]; nb = int(60/BPM*SR); bar = 4*nb
    progs = [[[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]], [[62,65,69,72],[58,62,65,69],[60,64,67,70],[57,60,64,67]], [[57,60,64,67],[53,57,60,65],[55,59,62,67],[52,55,59,64]]]
    prog = progs[prog_i % 3]; roots = [p[0]-24 for p in prog]; m = np.zeros(N)
    def add(s, sig):
        e = min(N, s+len(sig))
        if s < N: m[s:e] += sig[:e-s]
    def ep(f, L):
        t = np.arange(L)/SR; return np.sin(2*np.pi*f*t + np.sin(2*np.pi*2*f*t)*np.exp(-t*4)*1.2)*np.exp(-t*2.2)*(1-np.exp(-t*200))
    for b in range(N//bar+1):
        ch = prog[b % 4]
        for hit in (0, 2.5): add(b*bar+int(hit*nb), sum(ep(mtof(x), int(2*nb)) for x in ch)/4*0.55)
        for pos, off in ((0,0),(2,0),(3.5,7)):
            L = int(0.9*nb); t = np.arange(L)/SR; f = mtof(roots[b % 4]+off)
            add(b*bar+int(pos*nb), (np.sin(2*np.pi*f*t)+0.3*np.sin(4*np.pi*f*t))*np.exp(-t*3)*(1-np.exp(-t*300))*0.6)
    L = int(.35*SR); t = np.arange(L)/SR; K = np.sin(2*np.pi*np.cumsum(110*np.exp(-t*18)+45)/SR)*np.exp(-t*9)
    L = int(.06*SR); H = signal.lfilter(*signal.butter(2, 7000/(SR/2), 'high'), rng.standard_normal(L))*np.exp(-np.arange(L)/SR*60)
    for b in range(1, N//bar+1):
        for i in range(4):
            st = b*bar+i*nb
            if i in (0, 2): add(st, K*0.8)
            add(st, H*0.15)
    m = signal.lfilter(*signal.butter(2, 9000/(SR/2), 'low'), m); return m/np.max(np.abs(m))

def build(vid, nsc, seed):
    a, sr = sf.read(D/'voice'/f'{vid}.wav')
    if a.ndim > 1: a = a.mean(1)
    if sr != SR: a = signal.resample_poly(a, SR, sr)
    thr = 0.02*np.max(np.abs(a)); idx = np.where(np.abs(a) > thr)[0]; a = a[max(0, idx[0]-int(.03*SR)): idx[-1]+int(.12*SR)]
    # accorcia le pause interne lunghe (> 0,45 s -> 0,32 s)
    f = int(.02*SR); e = np.array([np.sqrt(np.mean(a[i:i+f]**2)) for i in range(0, len(a), f)]); sil = e < 0.04*e.max()
    keep = np.ones(len(e), bool); i = 0
    while i < len(e):
        if sil[i]:
            j = i
            while j < len(e) and sil[j]: j += 1
            if (j-i)*0.02 > 0.45: keep[i+8:j-8] = False
            i = j
        else: i += 1
    a = np.concatenate([a[k*f:(k+1)*f] for k in range(len(e)) if keep[k]])
    lead, tail, fade = 0.35, 1.3, 0.4
    total = lead + len(a)/SR + tail; N = int(total*SR)
    voice = np.zeros(N); s = int(lead*SR); voice[s:s+len(a)] = a/np.max(np.abs(a))*0.9
    mu = music(N, seed, seed)
    env = np.convolve(np.abs(voice), np.ones(int(.25*SR))/int(.25*SR), 'same'); env /= env.max()
    duck = np.convolve(1-0.55*np.clip(env*4, 0, 1), np.ones(int(.15*SR))/int(.15*SR), 'same')
    mu = mu*0.28*duck; mu[:int(.6*SR)] *= np.linspace(0, 1, int(.6*SR)); mu[-int(1.5*SR):] *= np.linspace(1, 0, int(1.5*SR))
    mix = voice + mu; mix /= max(1.0, np.max(np.abs(mix))/0.97)
    wav = D/f'_{vid}.wav'; sf.write(wav, np.stack([mix, mix], 1), SR)
    durs = [total/nsc]*nsc
    cmd = ['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error']
    for i, d in enumerate(durs): cmd += ['-loop', '1', '-t', f'{d+fade:.2f}', '-i', str(D/'slides'/f'{vid}_{i}.jpg')]
    cmd += ['-i', str(wav)]; filt = []; last = '[0:v]'
    for i in range(1, nsc):
        lab = f'[v{i}]'; filt.append(f'{last}[{i}:v]xfade=transition=slideleft:duration={fade}:offset={sum(durs[:i]):.2f}{lab}'); last = lab
    filt.append(f'{last}format=yuv420p[vout]')
    cmd += ['-filter_complex', ';'.join(filt), '-map', '[vout]', '-map', f'{nsc}:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-r', '30',
            '-c:a', 'aac', '-b:a', '160k', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-t', f'{total:.2f}', '-movflags', '+faststart', str(D/f'{vid}.mp4')]
    subprocess.run(cmd, check=True); wav.unlink(); return round(total, 1)

only = sys.argv[2:]
for k, v in enumerate(C.TT + C.YT):
    if only and v[0] not in only: continue
    print(v[0], build(v[0], len(v[1]), k), flush=True)
