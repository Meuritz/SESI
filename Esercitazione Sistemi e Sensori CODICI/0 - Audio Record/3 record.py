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

# here we declare ho many plots we want
figure, axis = plt.subplots(1, 3)

# set the window size of the plot
figure.set_size_inches(20, 20)

# plot first channel
axis[0].plot(channel_1, c="g")
axis[0].set_title("canale 1")
axis[0].set_xlabel("Periodo")
axis[0].set_ylabel("Ampiezza")

# plot second channel
axis[1].plot(channel_2, c="r")
axis[1].set_title("canale 2")
axis[1].set_xlabel("Periodo")
axis[1].set_ylabel("Ampiezza")

# plot third channel
axis[2].plot(channel_1, label="Canale 1", c="g")
axis[2].plot(channel_2, label="Canale 2", c="r")
axis[2].set_title("canali sovrapposti")
axis[2].set_xlabel("Periodo")
axis[2].set_ylabel("Ampiezza")
axis[2].legend()

plt.show()