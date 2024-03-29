import pygame

SPEED = 3


class Bird:
    def __init__(self):
        self.figure = pygame.transform.scale(pygame.image.load("bird_img.png"), (100, 100))
        self.x = 200
        self.y = 400
        self.rect = pygame.rect.Rect(self.x + 25, self.y + 30, 45, 35)  # png doc size is not actual bird size
        self.score = 0

    def default_move(self):
        self.y += SPEED
        self.rect.y += SPEED

    def up(self):
        self.y -= 5 * SPEED
        self.rect.y -= 5 * SPEED

    def bird_died(self, poles):
        game_end = False
        if self.y <= 0 or self.y >= 675:
            game_end = True
        for p in poles:
            if self.rect.colliderect(p.rect) or self.rect.colliderect(p.rect_upper):
                game_end = True
        return game_end

    def increase_score(self, poles):
        for i in poles:
            if i.rect.x < self.x and not i.counted:
                self.score += 1
                i.counted = True
            if i.rect_upper.x < self.x and not i.counted_upper:
                self.score += 1
                i.counted_upper = True
