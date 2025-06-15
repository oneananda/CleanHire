import webrtcvad
import pyaudio
import struct
import math
import json
import time
import datetime

# Settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(RATE * FRAME_DURATION / 1000)  # samples per frame

vad = webrtcvad.Vad(1)
audio = pyaudio.PyAudio()

stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAME_SIZE
)

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

        time.sleep(FRAME_DURATION / 1000.0)

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped. Saving to `audio_log.json`...")

    with open("audio_log.json", "w") as f:
        json.dump(log, f, indent=2)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    print("✅ Log saved.")
