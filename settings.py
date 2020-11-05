# Sound location
# "./sounds" on pc, "/media/usb" on raspberry
sound_location = './sounds'

# Global variables
bpm = 124

sounds = []

# Sequencer settings
sounds_in_beat = [[None for x in range(4)] for y in range(16)]
loop = True
delay = int((60 / bpm * 1000))
selected = [0] * 16
stop_sequencer = False

# Screen settings
seq_bits = ['0'] * 16
pad_bits = ['0'] * 16
play_state = False
pitch_shift = 0
