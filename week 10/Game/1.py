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
  host = 'localhost',
  database = 'postgres',
  user = 'postgres',
  password = '76141Zam'
)

cur = conn.cursor()


pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption('Welcome to the Game')


def login_menu():
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Welcome', 600, 700, theme=main_theme)

    def sign_in():
        checking()
    text = "Please, Sign in"
    menu.add.label(text) 
    menu.add.button('Start', sign_in)
    
    menu.mainloop(screen)


def checking():
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Menu', 600, 700, theme=main_theme)
    

    def checking_usInfo(login, password):
        user_data = get_user_by_login_and_password(login, password)
        if(user_data is None):
            checking()
        else:
            game_menu(login)

    def get_user_by_login_and_password(login, password):
        select_query = f"select * from test_users where login = '{login}' and password = '{password}';"
        cur.execute(select_query)
        return cur.fetchone()
    def p():
        sign_up()

    login = menu.add.text_input('Login: ', default='')
    password = menu.add.text_input('Password: ', default='', password=True)
    menu.add.button('Sign in', lambda: checking_usInfo(login.get_value(), password.get_value()))
    menu.add.button('Sign up', p)
    menu.mainloop(screen)



def sign_up():
    main_theme = pygame_menu.themes.THEME_BLUE
    menu = pygame_menu.Menu('Menu', 600, 700, theme=main_theme)
    
    
    def checking_usInfo(login, password):
        insert_query = f"insert into snake_users (login, password) values ('{login}', '{password}');"
        cur.execute(insert_query)
        conn.commit()
        checking()

    login = menu.add.text_input('New login: ', default='')
    password = menu.add.text_input('New password: ', default='', password=True)
    menu.add.button('Sign up', lambda: checking_usInfo(login.get_value(), password.get_value()))
    menu.mainloop(screen)



def start_the_game(login):
    font = pygame.font.SysFont("comicsansms", 30)

    clock = pygame.time.Clock()
    speed = settings.SPEED
    running = True

    # Initialization
    snake_obj = Snake()
    fruit_obj = Fruit()
    blocks_group = pygame.sprite.Group()

    step = 4  # the number of fruits after which start new level
    counter = 1
    level_counter = 0
    cnt = 0

    # create background
    field = pygame.image.load('images/field.png')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(field, (0, 0))
        score = font.render("Score: " + str(cnt) + "   Level: " + str(level_counter), True, (255, 255, 255))
        screen.blit(score, (45, 0))

        blocks_group.draw(screen)
        fruit_obj.draw(screen)
        snake_obj.draw(screen)
        snake_obj.changeSpeed(speed)
        running = snake_obj.move(counter)

        # Adding new block
        if (counter - 1) > 0 and (counter - 1) % step == 0:
            for _ in range(1):
                new_block = Block()
                blocks_group.add(new_block)

            # condition of adding new block
            step += step
            level_counter += 1
            speed += 0.005

        if snake_obj.time > 180:  # timer for food
            fruit_obj.respawn()
            snake_obj.time = 0

        # Eat food
        if (snake_obj.head_rect.colliderect(fruit_obj.rect)):
            fruit_obj.__init__()
            cnt += random.randint(1, 3)
            counter += 1
            snake_obj.time = 0

        # Check collisions
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
    return


def game_menu(login):
    image = pygame.image.load("images/field.png")
    main_theme = pygame_menu.themes.THEME_BLUE

    menu = pygame_menu.Menu('Menu', 600, 700, theme=main_theme)
    
    
    def quit_the_game():
        print('Quitting the game!')
        pygame.quit()
        quit()


    select_query = f"select score, level from snake_users where login = '{login}';"
    cur.execute(select_query)
    p = cur.fetchall()
    print(p[0][0])

    menu.add.label(f"Hello {login}")
    menu.add.label(f"Score: {p[0][0]}   level: {p[0][1]}")
    menu.add.button('Play', lambda: start_the_game(login))
    menu.add.button('Exit', quit_the_game)
    menu.mainloop(screen)
    

def game_over(login, score, level):
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

login_menu()
conn.close()