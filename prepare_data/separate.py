import glob
import os
import sys
import librosa


def setfiles():
    res = glob.glob('/home/tree/data/SongData/*/*')
    
    for f in res:
        print(f)
        name = f.split('/')
        os.system('cp ' + f + ' /home/tree/data/dataset/' + name[-2] +'_' + name[-1])
        

def sep():
    res = glob.glob('/home/tree/data/dataset/*')
    for f in res:
        print(f)
        os.system('spleeter separate -i ' + f + ' -o /home/tree/data/output')

def sdata():
    res = glob.glob('/home/tree/data/output/*/v*.wav')
    for f in res:
        name = f.split('/')
        print('cp ' + f + ' /home/tree/data/wavdata/' + name[-2] + '.wav')
        os.system('cp ' + f + ' /home/tree/data/wavdata/' + name[-2] + '.wav')


def pic(x, name):
    k = x.shape[0] // 16000
    num = 0
    for i in range(k-4):
        one = x[16000 * i: 16000 * (i + 3)]
        m = librosa.feature.melspectrogram(one)
        if m.mean() > 1:
            print('/home/tree/data/picdata/%s_%03d.wav' % (name, i))
            librosa.output.write_wav('/home/tree/data/picdata/%s_%03d.wav' % (name, num), one, sr=16000)
            num += 1

def sepwav():
    res = glob.glob('/home/tree/data/wavdata/*.wav')
    for f in res:
        x, fs = librosa.load(f, sr=16000)
        name = f.split('/')
        pic(x, name[-1][:-4])

def trans():
    res = glob.glob('/home/tree/data/ace/*.mp3')
    for f in res:
        x, fs = librosa.load(f, sr=16000)
        name = f.replace('mp3', 'wav')
        print(name)
        librosa.output.write_wav(name, x, sr=16000)

if __name__ == '__main__':
   trans() 


