import random
import pygame

from pole import Pole
from bird import Bird

pygame.init()
screen_info = pygame.display.Info()
SCREEN_HEIGHT = screen_info.current_h - 100
SCREEN_WIDTH = screen_info.current_w
SCREEN_BACKGROUND = (135, 206, 250)
SCORE_COLOR = (255, 255, 0)
END_GAME_COLOR = (250, 250, 200)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)
text = font.render("GAME FINISHED!\nIf you want to restart press SPACE", True, (0, 0, 200))
FPS = 60


def draw(pole, bird):
    screen.blit(pole.figure, (pole.sx, pole.sy))
    screen.blit(pole.figure_upper, (pole.sx_upper, pole.sy_upper))
    screen.blit(bird.figure, (bird.x, bird.y))


def draw_bird(bird):
    screen.blit(bird.figure, (bird.x, bird.y))


def remove_out_bound_poles(poles):
    removed = False
    for p in poles:
        if p.sx <= 0 and p.sx_upper <= 0 and not p.removed:
            removed = True
            p.removed = True
        if p.sx <= -150 and p.sx_upper <= -150 and p.removed:
            poles.remove(p)
            removed = True

    if removed:
        next_x = poles[len(poles) - 1].sx + random_distance_between()
        poles.append(Pole(next_x, next_x + random_distance_up_down()))


def show_score(bird):
    score_text = font.render(f"SCORE: {bird.score}", True, SCORE_COLOR)
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(score_text, text_rect)


def end_game_text():
    end_font = pygame.font.Font(None, 44)
    end_text = end_font.render(f"End of the game! If you want continue press SPACE", True, END_GAME_COLOR)
    text_rect = text.get_rect()
    text_rect.topleft = (10, 50)
    screen.blit(end_text, text_rect)


def random_distance_between():
    return random.choice([300, 350, 400])


def random_distance_up_down():
    return random.choice([0, 50, 100 - 50, -100])


def play():
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    game_continues = True

    bird = Bird()

    poles = [Pole(1300, 1300)]
    for i in range(1, 5):
        next_x = poles[i - 1].sx + random_distance_between()
        poles.append(Pole(next_x, next_x + random_distance_up_down()))

    while running and game_continues:
        clock.tick(FPS)
        screen.fill(SCREEN_BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            bird.up()
        else:
            bird.default_move()

        for pole in poles:
            draw(pole, bird)
            pole.move()
            pole.move_upper()

        if bird.bird_died(poles):
            game_continues = False

        remove_out_bound_poles(poles)
        bird.increase_score(poles)
        show_score(bird)

        while not game_continues:
            end_game_text()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_continues = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_continues = True
                        play()
                        running = False  # with this thing after quit game is closed
        pygame.display.update()


if __name__ == "__main__":
    play()
    pygame.quit()
