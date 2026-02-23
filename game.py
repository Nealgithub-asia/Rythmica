import librosa
import numpy as np
import copy
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True)

path = "./music/tunetank-vlog-beat-background-349853.mp3"
example = librosa.example("nutcracker")

y,sr=librosa.load(path)
#22050 = sr
beatTrack=librosa.onset.onset_detect(y=y,sr=sr)
beatSamples=librosa.frames_to_samples(beatTrack)
beatTime=beatSamples/sr

totalBeats=len(beatTime)
#print(f"beat times:\n{beatTime/sr}")

z=np.empty(totalBeats)
for a,i in enumerate(beatSamples):
    z[a]=np.abs(y[i])
x=y.tolist()
#calculating RMS
n=np.sort(z)
print(f"median:{np.median(n) :.3f}")
RMS=np.sqrt(np.mean(np.square(z)))
print(f"mean: {z[int(len(z)/2)] :.3f},max :{max(np.abs(z)) :.3f},min :{min(np.abs(z)) :.3f}")
print(f"RMS: {RMS :.3f}")


#randomizes the top,bottom,left and right
direction=["Top","Bottom","Left","Right"]
randirectionIndex=[]
for i in beatSamples:
    if(np.abs(y[i])>RMS):

        num= np.random.randint(3,4)
    elif(np.abs(y[i])<=RMS):

        num= np.random.randint(1,3)

    randomize=np.random.choice(4,size=(num), replace = False).tolist()                           
    randirectionIndex.append(randomize)

randirection=copy.deepcopy(randirectionIndex)
for i in range(len(randirectionIndex)):
    for j in range(len(randirectionIndex[i])):
        match randirectionIndex[i][j]:
            case 0:
                randirection[i][j]=direction[0]
            case 1:
                randirection[i][j]=direction[1]
            case 2:
                randirection[i][j]=direction[2]
            case 3:
                randirection[i][j]=direction[3]


beatDirection=beatTime.tolist()
#print(beatDirection)
for i in range(totalBeats):
    beatDirection[i]=[beatDirection[i], randirection[i]]




print(z[:5],beatDirection[:5],sep="\n")
#show music graph
"""
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')
plt.show()
"""