import soundcard as sc
import soundfile as f
import numpy as np
import matplotlib.pyplot as plt

# get the current default speaker on the system:
default_speaker = sc.default_speaker()

# get the current default microphone on the system:
default_mic = sc.default_microphone()

# record ten second of audio
data = default_mic.record(samplerate=48000, numframes=48000*10, channels=[0 , 1])

# play back the recorded audio:
default_speaker.play(data, samplerate=48000, channels=[0,1])

# here we separete the data of the two channels
channel_1 = [sublist[0] for sublist in data]
channel_2 = [sublist[1] for sublist in data]

# plot first channel
plt.figure()
plt.plot(channel_1, c="g")
plt.title("canale 1")
plt.xlabel("Periodo")
plt.ylabel("Ampiezza")
plt.show()

# plot second channel
plt.figure()
plt.plot(channel_2, c="r")
plt.title("canale 2")
plt.xlabel("Periodo")
plt.ylabel("Ampiezza")
plt.show()

# plot third channel
plt.figure()
plt.plot(channel_1, label="Canale 1", c="g")
plt.plot(channel_2, label="Canale 2", c="r")
plt.title("canali sovrapposti")
plt.xlabel("Periodo")
plt.ylabel("Ampiezza")
plt.legend()
plt.show()
