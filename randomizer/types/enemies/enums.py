"""Enums supporting enemy classes and functions."""

from enum import IntEnum


class HitSound(IntEnum):
    """Enum for the default sound an enemy will make when attacking you."""

    BITE = 0
    PIERCE = 1
    CLAW = 2
    JAB = 3
    SLAP = 4
    KNOCK = 5
    SMASH = 6
    DEEP_KNOCK = 7
    PUNCH = 8
    BONK = 9
    FLOPPING = 10
    DEEP_JAB = 11
    BLAST_1 = 12
    BLAST_2 = 13


class FlowerBonusType(IntEnum):
    """Enum for the type of flower bonus the enemy will award you."""

    NONE = 0
    ATTACK_UP = 1
    DEFENSE_UP = 2
    HP_MAX = 3
    ONCE_AGAIN = 4
    LUCKY = 5


class ApproachSound(IntEnum):
    """Enum for the default sound an enemy will make when approaching you."""

    NONE = 0
    STARSLAP_SPIKEY_ENIGMA = 1
    SPARKY_GOOMBA_BIRDY = 2
    AMANITA_TERRAPIN = 3
    GUERRILLA = 4
    PULSAR = 5
    DRY_BONES = 6
    TORTE = 7
