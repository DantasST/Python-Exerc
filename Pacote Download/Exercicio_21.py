#musica mp3
import pygame
pygame.init()
#print('\n**EXERCICIO 21**\n')
pygame.mixer.music.load('musictest.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()