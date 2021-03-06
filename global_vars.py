import numpy as np
"""
Global variables contained in this module.
"""

WIDTH = 2
CHANNELS = 1
BUFFER_SIZE = 4096
RATE = 44100
ALL_FX = ["Lowpass Filter", "Highpass Filter", "Delay", "Tremolo", "Chorus",
    "Harmonizer", "Distortion", "Wah", "Popcorn", "Sci-Fi Delay"]
ACTIVE_FX = {}

pitches = np.array([55.00, 58.27, 61.74,
   65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5,
   130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.7, 220.0, 233.1, 246.9,
   261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0, 466.2, 493.9,
   523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740.0, 784.0, 830.6, 880.0,   932.3,   987.8,
   1047,  1109,  1175,  1245,  1319,  1397,  1480], dtype=np.float32)

pitch_ratios = {'minor_third': 6.0/5.0, 
                'major_third': 5.0/4.0,
                'fourth': 4.0/3.0,
                'tritone': np.sqrt(2),
                'fifth': 3.0/2.0,
                'octave': 2.0/1.0}
