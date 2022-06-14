import time
import pygame

pygame.mixer.init(buffer=512)
pygame.mixer.music.load("/home/wjddusqlqkqh/pi/Drum.wav")
#---------------------------
BPM = 100  #Set BPM you want to play
#---------------------------
BPMS = 60/BPM
delay = BPMS
past = 0
note = 1

while True:
    now = time.perf_counter()
    if now >= past + delay:
        if note == 1:
            pygame.mixer.music.play()
        elif note == 2:
            pygame.mixer.music.play()
        elif note == 3:
            pygame.mixer.music.play()
        elif note == 4:
            pygame.mixer.music.play()

        past = now
        note = note + 1
        if note > 4:
            note = 1