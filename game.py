import librosa
import numpy as np
np.set_printoptions(precision=2, suppress=True)

path = "./music/tunetank-vlog-beat-background-349853.mp3"
y,sr=librosa.load(path)

beat_track=librosa.onset.onset_detect(y=y,sr=sr)
beat_times=librosa.frames_to_samples(beat_track)
total_beats=len(beat_times)
#print(f"beat times:\n{beat_times/sr}")
print(len(beat_times)) #total beats

direction=np.array(["Top","Bottom","Left","Right"])

arx=[]
for i in range(total_beats):
    num= np.random.randint(1,4)
    randomize=np.random.randint(0,5,size=(num)).tolist()
    arx.append(randomize)
    #print(arx)
print(arx)



