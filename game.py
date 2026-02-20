import librosa
import numpy as np
np.set_printoptions(precision=2, suppress=True)

path = "./music/tunetank-vlog-beat-background-349853.mp3"
y,sr=librosa.load(path)

beat_track=librosa.onset.onset_detect(y=y,sr=sr)
beat_times=librosa.frames_to_samples(beat_track)
total_beats=6
#print(f"beat times:\n{beat_times/sr}")

#randomizes the top,bottom,left and right
direction=["Top","Bottom","Left","Right"]
arx=[]
for i in range(total_beats):
    num= np.random.randint(1,4)
    randomize=np.random.randint(0,4,size=(num)).tolist()                           
    arx.append(randomize)
arxd=[]
for i in range(len(arx)):
    for j in range(len(arx[i])):
        match j:
            case 0:
                arxd[i][j]=direction[0]
                
            case 1:
                arxd[i][j]=direction[1]
            case 2:
                arxd[i][j]=direction[2]
            case 3:
                arxd[i][j]=direction[3]

print(arx)
