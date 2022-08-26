from re import T
import pygame
pygame.init()

pygame.font.init()

WIDTH, HEIGHT = 1000,500
FLOOR = HEIGHT - 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Devio")

#Background sprites
SKY = pygame.transform.scale(pygame.image.load('assets/sky.png'), (WIDTH, HEIGHT-100))
GROUND = pygame.transform.scale(pygame.image.load('assets/ground_full.png'), (WIDTH, 100))
BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load('assets/black_background.png'), (WIDTH, HEIGHT))

#Object sprites
BRICK = pygame.transform.scale(pygame.image.load('assets/brick.png'), (50,50))
STONE = pygame.transform.scale(pygame.image.load('assets/stone.png'), (50,50))
EDIT_BLOCK = pygame.transform.scale(pygame.image.load('assets/edit_block.png'), (50,50))
END_DOOR = pygame.transform.scale(pygame.image.load('assets/End_Door.png'), (50,100))
SPIKEY_BRICK = pygame.transform.scale(pygame.image.load('assets/spikeybrick.png'), (50,50))

# DEVIO sprites
DEVIO_RIGHT_STANDING_1 = pygame.transform.scale(pygame.image.load('assets/Devio_still1.png'), (50,95))
DEVIO_LEFT_STANDING_1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Devio_still1.png'), (50,95)), True, False)
DEVIO_RIGHT_STANDING_2 = pygame.transform.scale(pygame.image.load('assets/Devio_still2.png'), (50,95))
DEVIO_LEFT_STANDING_2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Devio_still2.png'), (50,95)), True, False)

DEVIO_RIGHT_JUMPING = pygame.transform.scale(pygame.image.load('assets/Devio_jump.png'), (50,95))
DEVIO_LEFT_JUMPING = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Devio_jump.png'), (50,95)), True, False)

DEVIO_RIGHT_WALKING_1 =pygame.transform.scale(pygame.image.load('assets/Devio_walking1.png'), (50,95))
DEVIO_LEFT_WALKING_1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Devio_walking1.png'), (50,95)), True, False)
DEVIO_RIGHT_WALKING_2 =pygame.transform.scale(pygame.image.load('assets/Devio_walking2.png'), (50,95))
DEVIO_LEFT_WALKING_2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Devio_walking2.png'), (50,95)), True, False)
DEVIO = DEVIO_RIGHT_STANDING_1


#ENEMY SPRITES
TURTLE = pygame.transform.scale(pygame.image.load('assets/turtle.png'),(50,50))
ANGRY_BRICK = pygame.transform.scale(pygame.image.load('assets/angrybrick.png'),(100,100))
JUMPER_GUY = pygame.transform.scale(pygame.image.load('assets/kangaroo1.png'),(50,100))


#Sound files
JUMP_SOUND = pygame.mixer.Sound('assets/sounds/jump.wav')
HIT_ENEMY_SOUND = pygame.mixer.Sound('assets/sounds/enemy_jump.wav')
BREAK_BRICK_SOUND = pygame.mixer.Sound('assets/sounds/brick_break.wav')
DEATH_SOUND = pygame.mixer.Sound('assets/sounds/death.wav')

