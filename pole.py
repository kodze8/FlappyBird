import random
import pygame.image

number_of_steps = [250, 300, 400, 600]


min_height = 300
max_height = 650

min_height_upper = -500
max_height_upper = -150

CHANGE = 1


class Pole:
    def __init__(self, stx, stx_upper):
        self.__image = pygame.image.load("pole_img.png")
        self.sx = stx  # pole is invisible at that point
        self.sy = 350  # MIN:350  MAX: 600  def:350
        self.figure = pygame.transform.scale(self.__image, (250, 600))
        self.rect = pygame.rect.Rect(self.sx + 90, self.sy, 65, 600)  # customized / MODIFIED as FIGURE SIZE AREN'T REAL
        self.step = 0
        self.down = True
        self.counted = False

        self.removed = False

        self.__image_upper = pygame.image.load("pole_img.png")
        self.sx_upper = stx_upper
        self.sy_upper = -250  # MIN:-500  MAX: -150  def: -250
        self.figure_upper = pygame.transform.rotate(pygame.transform.scale(self.__image, (250, 600)), 180)
        self.rect_upper = pygame.rect.Rect(self.sx_upper + 90, self.sy_upper, 65, 600)
        self.step_upper = 0
        self.down_upper = True
        self.counted_upper = False

    def move(self):
        self.sx -= CHANGE
        self.rect.x -= CHANGE

        if self.sx > 150:
            if self.step > 0:
                if self.sy < max_height and self.down:
                    self.sy += CHANGE
                    self.rect.y += CHANGE
                else:
                    if self.sy - self.sy_upper > 800:
                        self.down = False
                        self.sy -= CHANGE
                        self.rect.y -= CHANGE
                        if not min_height < self.sy < max_height or self.sy - self.sy_upper < 800:
                            self.step = random.choice(number_of_steps)
                            self.down = True

                self.step -= 1
            else:
                self.step = random.choice(number_of_steps)
                self.move()
                self.down = True

    def move_upper(self):
        self.sx_upper -= CHANGE
        self.rect_upper.x -= CHANGE
        # decide what value of y change you should choose
        if self.sx_upper > 150:
            if self.step_upper > 0:
                if self.sy_upper > min_height_upper and self.down_upper:
                    self.sy_upper -= CHANGE
                    self.rect_upper.y -= CHANGE
                else:
                    self.down_upper = False
                    self.sy_upper += CHANGE
                    self.rect_upper.y += CHANGE
                    if not max_height_upper > self.sy_upper or self.sy - self.sy_upper < 800:
                        self.step_upper = random.choice(number_of_steps)
                        self.down_upper = True
                self.step_upper -= 1
            else:
                self.step_upper = random.choice(number_of_steps)
                self.down_upper = True
                self.move_upper()
