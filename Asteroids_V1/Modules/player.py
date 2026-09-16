# Player class file

import pygame
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def move(self, dt: float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector


    def draw(self, screen):
        list_pts = self.triangle()
        pygame.draw.polygon(screen, "white", list_pts, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            pass
        else:
            shot_1 = Shot(self.position.x, self.position.y)
            shot_1.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer = self.shot_cooldown_timer - dt


        if keys[pygame.K_a]:
            # Left Rotation
            dt = -dt
            self.rotate(dt)

        if keys[pygame.K_d]:
            # Right Rotation
            self.rotate(dt)

        if keys[pygame.K_w]:
            # Go Forward
            self.move(dt)

        if keys[pygame.K_s]:
            # Go Forward
            dt = -dt
            self.move(dt)

        if keys[pygame.K_SPACE]:
            # SHOOOOOT HEEER!!
            self.shoot()

        

