import librosa
import numpy as np
def bake_audio():
    path = "./music/tunetank-vlog-beat-background-349853.mp3"
    example = librosa.example("nutcracker")
    y,sr=librosa.load(path)

    beatTrack=librosa.onset.onset_detect(y=y,sr=sr)
    beatSamples=librosa.frames_to_samples(beatTrack)
    beatTime=beatSamples/sr
    totalBeats=len(beatTime)


    bY=np.empty(totalBeats)
    for a,i in enumerate(beatSamples):
        bY[a]=np.abs(y[i])

    #math 
    RMS=np.sqrt(np.mean(np.square(bY)))
    mean= bY[int(len(bY)/2)]
    median=np.median(np.sort(bY))
    max= np.max(np.abs(bY))
    min= np.min(np.abs(bY))

    processedData={
        "y":y,
        "sr":sr,
        "beatSamples":beatSamples,
        "beatTime":beatTime,
        "totalBeats":totalBeats,
        "bY":bY,
        "RMS":RMS,
        "mean":mean,
        "median":median,
        "min":min,
        "max":max
    }

    np.save("processedData.npy", processedData)
    print("baking complete! processedData.npy created.")
if __name__=="__main__":
    bake_audio()