import pygame
import pygame_menu
import psycopg2
import settings
from snake import Snake
from fruit import Fruit
from block import Block
import random
import time

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='76141Zam'
)


def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption('Welcome to the Game')
    return screen


def login_menu(screen):
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Welcome', 600, 700, theme=main_theme)
    menu.add.label("Welcome to the game!")
    menu.add.button('Start', checking)
    menu.mainloop(screen)


def checking():
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Menu', 600, 700, theme=main_theme)
    menu.add.label("Please, sign in")
    login = menu.add.text_input('Login: ', default='')
    password = menu.add.text_input('Password: ', default='', password=True)

    def checking_usInfo():
        user_data = get_user_by_login_and_password(login.get_value(), password.get_value())
        if user_data is None:
            checking()
        else:
            game_menu(login.get_value())

    def get_user_by_login_and_password(login, password):
        cur = conn.cursor()
        select_query = f"select * from test_users where login = '{login}' and password = '{password}';"
        cur.execute(select_query)
        return cur.fetchone()

    menu.add.button('Sign in', checking_usInfo)
    menu.add.button('Sign up', sign_up)
    menu.mainloop(screen)


def sign_up():
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Menu', 600, 700, theme=main_theme)

    def checking_usInfo():
        insert_query = f"insert into snake_users (login, password) values ('{login}', '{password}');"
        print("User added sucssesefully!")
        cur.execute(insert_query)
        conn.commit()
        checking()

    login = menu.add.text_input('New login: ', default='')
    password = menu.add.text_input('New password: ', default='', password=True)
    menu.add.button('Sign up', checking_usInfo)
    menu.mainloop(screen)


def start_the_game(login):
    font = pygame.font.SysFont("comicsansms", 30)
    clock = pygame.time.Clock()
    speed = settings.SPEED
    running = True
    snake_obj = Snake()
    fruit_obj = Fruit()
    blocks_group = pygame.sprite.Group()
    step = 4
    counter = 1
    level_counter = 0
    cnt = 0
    field = pygame.image.load('images/field.png')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            pause(screen, font)

        screen.blit(field, (0, 0))
        score = font.render("Score: " + str(cnt) + "   Level: " + str(level_counter), True, (255, 255, 255))
        screen.blit(score, (45, 0))

        blocks_group.draw(screen)
        fruit_obj.draw(screen)
        snake_obj.draw(screen)
        snake_obj.changeSpeed(speed)
        running = snake_obj.move(counter)

        if (counter - 1) > 0 and (counter - 1) % step == 0:
            for _ in range(1):
                new_block = Block()
                blocks_group.add(new_block)
            step += step
            level_counter += 1
            speed += 0.005

        if snake_obj.time > 180:
            fruit_obj.respawn()
            snake_obj.time = 0

        if (snake_obj.head_rect.colliderect(fruit_obj.rect)):
            fruit_obj.__init__()
            cnt += random.randint(1, 3)
            counter += 1
            snake_obj.time = 0

        for block in blocks_group:
            if fruit_obj.rect.colliderect(block.rect):
                fruit_obj.respawn()
                break

        for block in blocks_group:
            if snake_obj.head_rect.colliderect(block.rect):
                time.sleep(0.5)
                running = False

        for x in snake_obj.snake_body[:-1]:
            if x == snake_obj.head:
                time.sleep(0.5)
                running = False

        pygame.display.flip()
        clock.tick(settings.FPS)

    game_over(login, cnt, level_counter)


def pause(screen, font):
    paused = True
    clock = pygame.time.Clock()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text(screen, font, 'Paused. Press enter to continue', 150, 350)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            paused = False
        
        pygame.display.update()
        clock.tick(15)

def print_text(screen, font, message, x, y, font_color=(0, 0, 0)):
    text = font.render(message, True, font_color)
    screen.blit(text, (x, y))



def game_menu(login):
    cur = conn.cursor()
    image = pygame.image.load("images/field.png")
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Menu', 600, 700, theme=main_theme)

    def quit_the_game():
        pygame.quit()
        quit()

    select_query = f"select score, level from snake_users where login = '{login}';"
    cur.execute(select_query)
    p = cur.fetchall()

    if p:
        score_label = f"Score: {p[0][0]}" 
        level_label = f"Level: {p[0][1]}"
    else:
        score_label = "Score: 0"
        level_label = "Level: 0"

    menu.add.label(f"Hello {login}!")
    menu.add.label(score_label + "   " + level_label)
    menu.add.button('Play', lambda: start_the_game(login))
    menu.add.button('Exit', quit_the_game)
    menu.mainloop(screen)


def game_over(login, score, level):
    cur = conn.cursor()
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Game Over', 600, 700, theme=main_theme)
    update_query = f"update snake_users set score = {score}, level = {level} where login = '{login}';"
    cur.execute(update_query)
    conn.commit()

    def start_game_again():
        start_the_game(login)

    def quit_game():
        pygame.quit()
        quit()

    menu.add.label('Game Over!')
    menu.add.label(f'Score: {score}   Level: {level}')
    menu.add.button('Start Again', start_game_again)
    menu.add.button('Quit', quit_game)
    menu.mainloop(screen)


if __name__ == "__main__":
    screen = initialize_game()
    login_menu(screen)
    conn.close()
