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
note = {"F#":370, 
         "G":392,
         "Rest":0}


#"Not Like Us" melody definition 
not_like_us_melody = [
    note["F#"],
    note["F#"],
    note["G"],
    note["F#"],
]

# Play "not like us"
print("Playing the sequence: F# F# G F#")
for i in range(3):
    for note in not_like_us_melody:
        print(f"Playing frequency: {note} Hz")
        playtone(note, 0.5)
        quiet()
        utime.sleep(0.1)  
    quiet()
    utime.sleep(1)  
    
# Turn off the PWM
quiet()