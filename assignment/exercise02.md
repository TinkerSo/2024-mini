# Exercise: PWM sound output

PWM (Pulse Width Modulation) can be used to generate analog signals from digital outputs.
The Raspberry Pi Pico has eight PWM groups each with two PWM channels.
The [Pico WH pinout diagram](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf) shows that almost all Pico pins can be used for multiple distinct tasks as configured by MicroPython code or other software.
In this exercise, we will generate a PWM signal to drive a speaker.

GP16 is one of the pins that can be used to generate PWM signals.
Connect the speaker with the black wire (negative) to GND and the red wire (positive) to GP16.

In a more complete project, we would use additional resistors and capacitors with an amplifer to boost the sound output to a louder level with a bigger speaker.
The sound output is quiet but usable for this exercise.

Musical notes correspond to particular base frequencies and typically have rich harmonics in typical musical instruments.
An example soundboard showing note frequencies is [clickable](https://muted.io/note-frequencies/).
Over human history, the corresspondance of notes to frequencies has changed over time and location and musical cultures.
For the question below, feel free to use musical scale of your choice!

## Questions

1. Using the code in exercise_sound.py as a starting point, modify the code to play several notes in a sequence from a song of your choosing.
## Solution
1. Referencing [frequency to notes chart](https://muted.io/note-frequencies/) we defined each note as key and its values as frequency in a dictionary. Then, we search up from the song "Not Like Us" by kendrick Lamar and convert the melody into a list of notes.

Additionally, we played each note for about 0.5 seconds and longer notes we added them twice to the list of notes. We play all the notes through a for loop for 3 times to demonstrate the backing track of "Not Like Us" sufficiently. 

Before playing any of the notes, we also jsut tested if a single frequency worked, utilizing the integration testing methodology. After we verified a single note worked, we tested thte range of notes and verified pico and the speaker was capable of outputting various frequencies. We then verified the song through the speaker and outputting the target note in the output logs. 

### [Demo Video](https://drive.google.com/file/d/1n-NT6gc6mlYI_GhmT9WiNHLh_GMzf1pI/view?usp=sharing)
