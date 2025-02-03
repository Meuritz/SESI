import soundcard as sc

# get the current default speaker on the system
default_speaker = sc.default_speaker()

# get the current default microphone on the system
default_mic = sc.default_microphone()

# record ten second of audio
data = default_mic.record(samplerate=48000, numframes=48000*10, channels=[0 , 1])

# play back the recorded audio
default_speaker.play(data, samplerate=48000, channels=[0,1])

# play back the recorded audio at double the speed
default_speaker.play(data, samplerate=48000*2, channels=[0,1])

# play back the recorded audio at half the sped
default_speaker.play(data, samplerate=48000/2, channels=[0,1])