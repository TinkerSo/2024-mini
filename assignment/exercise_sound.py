#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

#frequencies for the notes round up to the nearest 
F_SHARP = 370
G = 392
Rest = 0

#define the "Not Like Us" melody
melody = [
    (F_SHARP, 0.25),  
    (F_SHARP, 0.25),  
    (G, 0.25),        
    (F_SHARP, 0.25),  
]

# Play the melody
print("Playing the sequence: F# F# G F#")
for i in range(3):
    for note, duration in melody:
        print(f"Playing frequency: {note} Hz")
        playtone(note, duration)
        quiet()
        utime.sleep(0.1)  
    quiet()
    utime.sleep(1)  
    
# Turn off the PWM
quiet()