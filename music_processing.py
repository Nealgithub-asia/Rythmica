import librosa
import numpy as np
import matplotlib.pyplot as plt

def process_music(path="./music/slowBeat.mp3"):
    print(f"Baking audio: {path}...")
    
    # 1. Load the audio
    y, sr = librosa.load(path)

    # 2. HPSS - Isolate the percussion
    y_harm, y_perc = librosa.effects.hpss(y)

    # 3. Create a Mel-spectrogram of only the percussive part
    S_perc = librosa.feature.melspectrogram(y=y_perc, sr=sr, n_mels=128)
    
    # --- BAND 1: KICK DRUMS (Lower frequencies) ---
    # We broaden this to catch more deep thump energy
    kick_env = librosa.onset.onset_strength(S=S_perc[:5, :], sr=sr)
    kick_beats = librosa.onset.onset_detect(onset_envelope=kick_env, sr=sr, delta=0.05, wait=9)

    # --- BAND 2: SNARE/CLAP (Mid-high frequencies) ---
    # Broadened to capture more of the "crack" and "snap"
    snare_env = librosa.onset.onset_strength(S=S_perc[10:60, :], sr=sr)
    snare_beats = librosa.onset.onset_detect(onset_envelope=snare_env, sr=sr, delta=0.05, wait=9)

    print(f"DEBUG: Found {len(kick_beats)} kicks and {len(snare_beats)} snares.")

    # 4. Merge and clean up duplicates
    all_beats = np.unique(np.concatenate([kick_beats, snare_beats]))
    all_beats.sort()

    beatSamples = librosa.frames_to_samples(all_beats)
    beatTime = beatSamples / sr
    totalBeats = len(beatTime)

    # 5. Extract amplitudes at beat positions
    bY = np.empty(totalBeats)
    for a, i in enumerate(beatSamples):
        if i < len(y):
            bY[a] = np.abs(y[i])
        else:
            bY[a] = 0

    # 6. Calculate statistics (Required for game.py compatibility)
    RMS = np.sqrt(np.mean(np.square(bY))) if totalBeats > 0 else 0
    mean = np.mean(bY) if totalBeats > 0 else 0
    median = np.median(bY) if totalBeats > 0 else 0
    max_val = np.max(bY) if totalBeats > 0 else 0
    min_val = np.min(bY) if totalBeats > 0 else 0

    # 7. Save data
    processedData = {
        "y": y,
        "sr": sr,
        "beatSamples": beatSamples,
        "beatTime": beatTime,
        "totalBeats": totalBeats,
        "bY": bY,
        "RMS": RMS,
        "mean": mean,
        "median": median,
        "min": min_val,
        "max": max_val
    }

    np.save("processedData.npy", processedData)
    print(f"Baking complete! {totalBeats} drum hits found.")
    print("Check processedData.npy for the results.")

    # Visual proof (Optional but helpful)
    plt.figure(figsize=(12, 6))
    librosa.display.waveshow(y, sr=sr, alpha=0.5)
    plt.vlines(beatTime, -1, 1, color='r', linestyle='--', label='Detected Drums')
    plt.title(f'Multi-Band Drum Detection: {totalBeats} hits')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    process_music()
