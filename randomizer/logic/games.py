# Minigame shuffle logic.

import random

from . import flags
from randomizer.data.tadpole_songs import all_songs as tadpole_pond_song_pool
from randomizer.data.eventscripts.utils.tadpole_pond.moleville import script as moleville_blues_script


# ******** Ball solitaire

def _get_potential_ball_kicks(ball_solitaire):
    """

    Args:
        ball_solitaire (randomizer.data.games.BallSolitaireGame):

    Returns:
        list[tuple[randomizer.data.games.BallSolitaireGame.BallSpot|str]]: List of potential spots and directions.

    """
    potential_kicks = []
    spots_with_balls = [s for s in ball_solitaire.spots if s.has_ball]

    for spot in spots_with_balls:
        for direction in ('up', 'down', 'left', 'right'):
            if spot.can_kick(direction, reverse=True):
                potential_kicks.append((spot, direction))

    return potential_kicks


def randomize_ball_solitaire(ball_solitaire):
    """

    Args:
        ball_solitaire (randomizer.data.games.BallSolitaireGame):

    """
    while True:
        # Clear all spots first.
        for spot in ball_solitaire.spots:
            spot.has_ball = False

        # Pick a random spot to have the final ball.
        random.choice(ball_solitaire.spots).has_ball = True

        # Randomly pick an available direction to kick a ball until we can't do any more.
        while True:
            potential_kicks = []
            spots_with_balls = [s for s in ball_solitaire.spots if s.has_ball]

            for spot in spots_with_balls:
                for direction in ('up', 'down', 'left', 'right'):
                    if spot.can_kick(direction, reverse=True):
                        potential_kicks.append((spot, direction))

            # Stop if we have no more potential kicks.
            if not potential_kicks:
                break

            spot, direction = random.choice(potential_kicks)
            spot.reverse_kick(direction)

        # TODO: This is a bad hack, but rarely we generate a low number of balls so just try again for now...
        if ball_solitaire.num_balls > 10:
            break


# ******** Magic buttons

def randomize_magic_buttons(magic_buttons):
    """

    Args:
        magic_buttons (randomizer.data.games.MagicButtonsGame):

    """
    for spot in magic_buttons.spots:
        spot.pressed = True

    # Do 20 presses.
    for _ in range(20):
        potential_spots = [s for s in magic_buttons.spots if s.pressed]
        # If we happened to get back to the vanilla puzzle, we can't go any further.
        if not potential_spots:
            break
        choice = random.choice(potential_spots)
        choice.unpress()


# ******** Main program

def randomize_all(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    """
    # Ball Solitaire shuffle
    if world.settings.is_flag_enabled(flags.BallSolitaireShuffle):
        randomize_ball_solitaire(world.ball_solitaire)
        world.eventscripts[world.ball_solitaire.EVENT][0]["args"][1] = world.ball_solitaire.get_event_value()

    # Magic button shuffle
    if world.settings.is_flag_enabled(flags.MagicButtonShuffle):
        randomize_magic_buttons(world.magic_buttons)
        world.eventscripts[world.magic_buttons.EVENT][0]["args"][1] = world.magic_buttons.get_event_value()

    # Melody Bay shuffle
    if world.settings.is_flag_enabled(flags.RandomTadpolePondSong):
        songs = random.sample(tadpole_pond_song_pool, 3)
        # song 1
        world.eventscripts[1082] = songs[0].generate_input_script(0)
        world.eventscripts[1079] = songs[0].generate_playback_script(0)
        # hints
        world.replace_dialog(2718, songs[0].scroll_text)
        world.replace_dialog(2664, songs[0].apprentice_hint_1)
        # song 2
        world.eventscripts[1083] = songs[1].generate_input_script(1)
        world.eventscripts[1080] = songs[1].generate_playback_script(1)
        # hints
        world.replace_dialog(2665, songs[1].apprentice_hint_2)
        world.replace_dialog(1615, songs[1].mole_hint)
        world.eventscripts[3132] = moleville_blues_script
        # song 3
        world.eventscripts[1084] = songs[2].generate_input_script(2)
        world.eventscripts[1081] = songs[2].generate_playback_script(2)
        # hints
        world.eventscripts[2061][2]["subscript"] = songs[2].generate_starfish_hint(world.eventscripts[2061][2]["subscript"])
        world.eventscripts[1088] = songs[2].generate_tadpole_hint()

        world.tadpole_songs = songs


def get_spoiler(world):
    acc = {}
    
    acc["password"] = world.password.word
    acc["songs"] = [s.scroll_text for s in world.tadpole_songs]

    return acc