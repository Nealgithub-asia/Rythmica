import librosa
import numpy as np
import copy

np.set_printoptions(precision=2, suppress=True)

path = "./music/tunetank-vlog-beat-background-349853.mp3"
y,sr=librosa.load(path)

beatTrack=librosa.onset.onset_detect(y=y,sr=sr)
beatSamples=librosa.frames_to_samples(beatTrack)
beatTime=beatSamples/sr

totalBeats=len(beatTime)
#print(f"beat times:\n{beatTime/sr}")

#randomizes the top,bottom,left and right
direction=["Top","Bottom","Left","Right"]
randirectionIndex=[]
for i in range(totalBeats):
    num= np.random.randint(1,4)
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

print(randirectionIndex[:3])
print(randirection[:3])
print(beatDirection[:3])

