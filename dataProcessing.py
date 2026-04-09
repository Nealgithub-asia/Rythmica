import librosa
import numpy as np
import matplotlib.pyplot as plt

def bake_audio():
    path = "./music/slowBeat.mp3"
    #example = librosa.example("nutcracker")
    y,sr=librosa.load(path)
    #older------------------------
    #    beatTrack=librosa.onset.onset_detect(y=y,sr=sr)
    #Newer------------------------
    # Separate harmonic (melody) and percussive (drums) components
    y_harm, y_perc = librosa.effects.hpss(y)
    S = librosa.feature.melspectrogram(y=y_perc, sr=sr, n_mels=128, fmax=5000)
    onset_env = librosa.onset.onset_strength(S=librosa.power_to_db(S, ref=np.max), sr=sr)

    # Detect beats using ONLY the percussive component
    beatTrack = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr, delta=0.26, wait=1)
    #------------------------------
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

    
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Waveform')
    plt.show()

    print("min", min)
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