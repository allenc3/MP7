from pygame import *
import random

window_x = 500
window_y = 550

init()
window = display.set_mode((window_x, window_y))
display.set_caption('Stick Jump!')
clock = time.Clock()


class Stick_Man:
    def __init__(self):
        self.crouch = image.load('Stick_Man.jpg')
        self.fall = image.load('Stick_Man.jpg')
        self.jumping_right = image.load('Stick_Man.jpg')
        self.jumping_left = transform.flip(self.jumping_right, True, False)
        self.stand = image.load('Stick_Man.jpg')

        self.reset()

    def reset(self):
        self.speed_x = 0
        self.speed_y = 0
        self.max_speed_x = 5
        self.max_speed_y = 15
        self.x_acceleration = 0.5
        self.img = self.jumping_right
        self.jump_speed = 15

        scale = 7
        self.width, self.height = 7 * scale, 12 * scale
        self.scale = scale

        self.x = (window_x - self.width) / 2
        self.y = window_y - self.height

    def update(self, p):
        self.side_control()
        self.physics(p)
        self.move()
        self.show()

        self.x += self.speed_x
        self.y -= self.speed_y

        return (self.img, (self.x, self.y, self.width, self.height))

    def physics(self, p):

        on = False

        for colour, rect in p:
            x, y, w, h = rect

            # X range
            if self.x + self.width / 2 > x and self.x - self.width / 2 < x + w:
                # Y range
                if self.y + self.height >= y and self.y + self.height <= y + h:

                    if self.speed_y < 0:
                        on = True

        if not on and not self.y >= window_y - self.height:
            self.speed_y -= 0.5
        elif on:
            self.speed_y = self.jump_speed
        else:
            self.y = window_y - self.height
            self.speed_x = 0
            self.speed_y = 0
            if self.x != (window_x - self.width) / 2:
                if self.x > (window_x - self.width) / 2:
                    self.x = max((window_x - self.width) / 2, self.x - 6)
                else:
                    self.x = min((window_x - self.width) / 2, self.x + 6)

            else:
                keys = key.get_pressed()
                if keys[K_SPACE]:
                    self.speed_y = self.jump_speed

    def side_control(self):
        if self.x + self.width < 0:
            self.x = window_x - self.scale
        if self.x > window_x:
            self.x = -self.width

    def show(self):
        if self.speed_y > 0:
            if self.speed_x > 0:
                self.img = self.jumping_right
            elif self.speed_x < 0:
                self.img = self.jumping_left
        else:
            self.img = self.fall

    def slow_character(self):
        if self.speed_x < 0: self.speed_x = min(0, self.speed_x + self.x_acceleration / 6)
        if self.speed_x > 0: self.speed_x = max(0, self.speed_x - self.x_acceleration / 6)

    def move(self):
        keys = key.get_pressed()

        if not self.y >= window_y - self.height:

            if keys[K_LEFT] and keys[K_RIGHT]:
                self.slow_character()
            elif keys[K_LEFT]:
                self.speed_x -= self.x_acceleration
            elif keys[K_RIGHT]:
                self.speed_x += self.x_acceleration
            else:
                self.slow_character()

            self.speed_x = max(-self.max_speed_x, min(self.max_speed_x, self.speed_x))
            self.speed_y = max(-self.max_speed_y, min(self.max_speed_y, self.speed_y))


platform_spacing = 100


class Platform_Manager:
    def __init__(self):
        self.platforms = []
        self.spawns = 0
        self.start_spawn = window_y

        scale = 3
        self.width, self.height = 24 * scale, 6 * scale

    def update(self):
        self.spawner()
        return self.manage()

    def spawner(self):
        if window_y - info['screen_y'] > self.spawns * platform_spacing:
            self.spawn()

    def spawn(self):
        y = self.start_spawn - self.spawns * platform_spacing
        x = random.randint(-self.width, window_x)

        self.platforms.append(Platform(x, y, random.choice([1, -1])))
        self.spawns += 1

    def manage(self):
        u = []
        b = []
        for i in self.platforms:
            i.move()
            i.change_direction()
            b.append(i.show())

            if i.on_screen():
                u.append(i)

        self.platforms = u
        return b


class Platform:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 2
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        scale = 3
        self.width, self.height = 24 * scale, 6 * scale

    def move(self):
        self.x += self.speed * self.direction
        self.change_direction()

    def change_direction(self):
        if self.x <= 0:
            self.direction = 1
        if self.x + self.width >= window_x:
            self.direction = -1

    def on_screen(self):
        if self.y > info['screen_y'] + window_y:
            return False
        return True

    def show(self):
        return ((0, 0, 0), (self.x, self.y, self.width, self.height))


def random_colour(l, h):
    return (random.randint(l, h), random.randint(l, h), random.randint(l, h))


def blit_images(x):
    for i in x:
        window.blit(transform.scale(i[0], (i[1][2], i[1][3])), (i[1][0], i[1][1] - info['screen_y']))


def event_loop():
    for loop in event.get():
        if loop.type == KEYDOWN:
            if loop.key == K_ESCAPE:
                quit()
        if loop.type == QUIT:
            quit()


f = font.SysFont('', 50)


def show_score(score, pos):
    message = f.render(str(round(score)), True, (100, 100, 100))
    rect = message.get_rect()

    if pos == 0:
        x = window_x - rect.width - 10
    else:
        x = 10
    y = rect.height + 10

    window.blit(message, (x, y))


info = {
    'screen_y': 0,
    'score': 0,
    'high_score': 0
}

stick_man = Stick_Man()
platform_manager = Platform_Manager()

while True:
    # MATH THINGS

    event_loop()

    platform_blit = platform_manager.update()
    stick_blit = stick_man.update(platform_blit)
    info['screen_y'] = min(min(0, stick_blit[1][1] - window_y * 0.4), info['screen_y'])
    info['score'] = (-stick_blit[1][1] + 470) / 50

    # print(stick_blit[1][1], info['screen_y'])
    if stick_blit[1][1] - 470 > info['screen_y']:
        info['score'] = 0
        info['screen_y'] = 0
        stick_man = Stick_Man()
        platform_manager = Platform_Manager()

    clock.tick(60)

    # DISPLAY THINGS
    window.fill((255, 255, 255))

    blit_images([stick_blit])

    for x in platform_blit:
        i = list(x)
        i[1] = list(i[1])
        i[1][1] -= info['screen_y']
        draw.rect(window, i[0], i[1])

    info['high_score'] = max(info['high_score'], info['score'])

    show_score(info['score'], 1)
    show_score(info['high_score'], 0)

    display.update()