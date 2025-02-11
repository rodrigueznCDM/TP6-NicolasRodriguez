import arcade
from enum import Enum


class AttackType(Enum):
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2


class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.50
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type):
        super.__init__()
