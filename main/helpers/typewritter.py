import random

import sys

import time

import pygame

pygame.mixer.init()



def play_voice(v):
    sound = pygame.mixer.Sound(v)

    # Small random pitch variation using playback speed.
    # (Requires pygame-ce. If using normal pygame, remove this block.)
    try:
        pitch = random.uniform(0.95, 1.05)
        sound.set_volume(random.uniform(0.2, 0.3))
        channel = sound.play()
        if channel:
            channel.set_rate(pitch)
    except AttributeError:
        sound.play()


def typewriter(
    text,
    delay=0.05,
    newline=True,
    voice=True,
    voice_file = 'src/assets/sounds/npc.wav',
    skip=' .,!?'
):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if voice and char not in skip:
            play_voice(voice_file)

        time.sleep(delay)

    if newline:
        print()
    else:
        print(end='')
