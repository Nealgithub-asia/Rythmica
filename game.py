import librosa
import numpy as np
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
    randomize=np.random.randint(0,4,size=(num)).tolist()                           
    randirectionIndex.append(randomize)

randirection=[]
randirection.extend(randirectionIndex)
for i in range(len(randirectionIndex)):
    for j in range(len(randirectionIndex[i])):
        match j:
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

print(beatDirection[:5])
