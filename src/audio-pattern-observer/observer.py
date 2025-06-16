import webrtcvad
import pyaudio
import struct
import math
import json
import time
import datetime
import wave
import os

# Optional: Only import if diarization is needed
try:
    from pyannote.audio import Pipeline
except ImportError:
    Pipeline = None

# Settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(RATE * FRAME_DURATION / 1000)  # samples per frame
AUDIO_FILENAME = "recorded_audio.wav"

vad = webrtcvad.Vad(1)
audio = pyaudio.PyAudio()

stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAME_SIZE
)

frames = []
log = []

def get_rms(frame):
    count = len(frame) // 2
    shorts = struct.unpack('%dh' % count, frame)
    sum_squares = sum(sample * sample for sample in shorts)
    rms = math.sqrt(sum_squares / count) / 32768
    return rms

print("🔊 Audio monitoring started (Ctrl+C to stop)...")

try:
    while True:
        frame = stream.read(FRAME_SIZE, exception_on_overflow=False)
        is_speech = vad.is_speech(frame, RATE)
        volume = get_rms(frame)
        state = "speaking" if is_speech else "silent"

        log.append({
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "state": state,
            "volume": round(volume, 4)
        })

        if is_speech:
            frames.append(frame)

        time.sleep(FRAME_DURATION / 1000.0)

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped. Saving audio and log...")

    # Save recorded speech to WAV
    if frames:
        wf = wave.open(AUDIO_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print(f"✅ Audio saved to {AUDIO_FILENAME}")

    with open("audio_log.json", "w") as f:
        json.dump(log, f, indent=2)
    print("✅ Log saved.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Speaker diarization
    if Pipeline and os.path.exists(AUDIO_FILENAME):
        print("🔎 Running speaker diarization...")
        pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
        diarization = pipeline(AUDIO_FILENAME)
        diarization_log = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            diarization_log.append({
                "start": turn.start,
                "end": turn.end,
                "speaker": speaker
            })
        with open("diarization_log.json", "w") as f:
            json.dump(diarization_log, f, indent=2)
        print("✅ Diarization log saved to diarization_log.json")
    else:
        print("ℹ️ pyannote.audio not installed or no audio recorded. Skipping diarization.")
    