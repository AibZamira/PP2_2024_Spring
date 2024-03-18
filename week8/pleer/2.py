import pygame 
import os 
SCREEN_WIDTH = 400 
SCREEN_HEIGHT = 600 
 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
BLUE = (0, 0, 255) 
PURPLE = (106, 90, 205) 
 
pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
 
FPS = 60 
clock = pygame.time.Clock() 
running = True 
screen.fill(BLACK) 
 
music_files = [] 
songs = os.listdir("music/") 
for song in songs: 
    music_files.append(os.path.join("music/", song)) 
 
current_song_index = 0 
pygame.mixer.music.load(music_files[current_song_index]) 
 
pygame.mixer.music.play() 
 
font = pygame.font.SysFont("ENGRAVERS MT", 24) 
 
next_button_rect = pygame.Rect(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100, 60, 20) 
next_button_text = font.render("NEXT", True, WHITE) 
prev_button_rect = pygame.Rect(100 , SCREEN_HEIGHT - 100, 60, 20) 
prev_button_text = font.render("PREV", True, WHITE) 
 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if next_button_rect.collidepoint(event.pos): 
                current_song_index += 1 
                if current_song_index >= len(music_files): 
                    current_song_index = 0 
                pygame.mixer.music.load(music_files[current_song_index]) 
                pygame.mixer.music.play() 
            elif prev_button_rect.collidepoint(event.pos): 
                current_song_index -= 1 
                if current_song_index < 0: 
                    current_song_index = len(music_files) - 1 
                pygame.mixer.music.load(music_files[current_song_index]) 
                pygame.mixer.music.play() 
 
    screen.fill(BLACK) 
    pygame.draw.rect(screen, BLUE, next_button_rect) 
    pygame.draw.rect(screen, BLUE, prev_button_rect) 
    screen.blit(next_button_text, next_button_rect) 
    screen.blit(prev_button_text, prev_button_rect) 
    current_song_title = font.render(music_files[current_song_index], True, (255, 255, 255)) 
    screen.blit(current_song_title, (320 - current_song_title.get_width() // 2, 100 - current_song_title.get_height() // 2)) 
 
    pygame.display.update() 
    clock.tick(FPS)



    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_RIGHT]:
        music_index += 1
        if music_index >= len(music_files):
            music_index = 0
        pygame.mixer.music.load(music_files[music_index])
        pygame.mixer.music.play() 
    if pressed[pygame.K_LEFT]:
        music_index -= 1
        if music_index < 0:
            music_index = len(music_files) - 1
            pygame.mixer.music.load(music_files[music_index]) 
            pygame.mixer.music.play()
