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

def play_birthday_song():#Generated by GPT
    # Frequencies of the first few notes of "Happy Birthday" (in Hz)
    notes = [261, 329, 440, 130, 170, 220, 261, 329, 440, 261, 329, 440, 440, 220, 170, 130]  # G4, G4, A4, G4, C5, B4, G4
    #392, 392, 440, 392, 523, 494, 392, 392, 392, 440, 392, 523, 494, 392, 392, 392, 440, 392, 523, 494, 392
    duration = 0.5  # Each note plays for half a second

    for freq in notes:
        print(f"Playing frequency: {freq} Hz")
        playtone(freq, duration)  # Play the note
    quiet()


freq: float = 30
duration: float = 0.3  # seconds

print("Playing frequency (Hz):")

play_birthday_song()
# for i in range(64):
#     print(freq)
#     playtone(freq, duration)
#     freq = int(freq * 1.1)

# Turn off the PWM
quiet()
