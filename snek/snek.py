import pygame
from random import randrange

pygame.init()
pygame.mixer.init()

#Colors defined in RGB format
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

#display settings

width, height = 400, 400
clock = pygame.time.Clock()
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake.py")

#player

player_size = 10
player_vel = 7

#fonts

fixedsys_font = pygame.font.SysFont("Fixedsys", 30)

#sounds

score_sound = pygame.mixer.Sound("sounds/Coin.mp3")
death_sound = pygame.mixer.Sound("sounds/Death.mp3")

#game functions

def display_score(score):
    score_text = fixedsys_font.render("Score: " + str(score), True, red)
    display.blit(score_text, [width / 3, height / 3 - 30])

def draw_player(player_size, segments):
    for segment in segments:
        pygame.draw.rect(display, green, [segment[0], segment[1], player_size, player_size])

def main():
    game_over = False
    game_ended = False
    x = width / 2
    y = width / 2
    x_vel = 0
    y_vel = 0
    player_length = 1
    segments = []
    apple_x = round(randrange(0, width - player_size) / 10.0) * 10
    apple_y = round(randrange(0, height - player_size) / 10.0) * 10

    while not game_over:
        while game_ended:
            display.fill(black)
            game_over_msg_1 = fixedsys_font.render("Game Over!", True, red)
            game_over_msg_2 = fixedsys_font.render("Press SPACE to play again!", True, red)
            game_over_msg_3 = fixedsys_font.render("Press ESC to exit!", True, red)
            display.blit(game_over_msg_1, [width / 3, height / 3])
            display.blit(game_over_msg_2, [width / 3 - 70, height / 3 + 30])
            display.blit(game_over_msg_3, [width / 3 - 35, height / 3 + 60])
            display_score(player_length - 1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_ended = False
                    elif event.key == pygame.K_SPACE:
                        main()

                elif event.type == pygame.QUIT:
                    game_over = True
                    game_ended = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_vel = -player_size
                    y_vel = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_vel = player_size
                    y_vel = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    x_vel = 0
                    y_vel = player_size
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    x_vel = 0
                    y_vel = -player_size
        if x > width or x < 0 or y > height or y < 0:
            game_ended = True
            death_sound.play()

        x += x_vel
        y += y_vel

        display.fill(black)
        pygame.draw.rect(display, red, [apple_x, apple_y, player_size, player_size])
        segments.append([x, y])

        if len(segments) > player_length:
            del segments[0]


        for segment in segments[:-1]:
            if segment == [x, y]:
                game_ended = True
                death_sound.play()

        draw_player(player_size, segments)
        
        pygame.display.update()

        if x == apple_x and y == apple_y:
            apple_x = round(randrange(0, width - player_size) / 10.0) * 10
            apple_y = round(randrange(0, height - player_size) / 10.0) * 10
            score_sound.play()
            player_length += 1

        clock.tick(player_vel)

    pygame.quit()

main()