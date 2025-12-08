"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=PaMole,
        initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
        event_script=E3186_MOLES_IN_FIRST_MINES_ROOM,
        action_script=A0722_MINES_ENTRANCE_MOLES,
        speed=0,
        visible=True,
        x=18,
        y=31,
        z=0,
        z_half=False,
        direction=NORTHWEST,
        face_on_trigger=True,
        cant_enter_doors=False,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=True,
        cant_walk_up_stairs=False,
        cant_walk_under=False,
        cant_pass_walls=False,
        cant_jump_through=False,
        cant_pass_npcs=True,
        byte3_bit5=False,
        cant_walk_through=True,
        byte3_bit7=False,
        slidable_along_walls=True,
        cant_move_if_in_air=True,
        byte7_upper2=True,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        cannot_clone=False),
    # NPC_1
    RegularClone(
        occupant=PaMole,
        event_script=E3186_MOLES_IN_FIRST_MINES_ROOM,
        action_script=A0722_MINES_ENTRANCE_MOLES,
        visible=True,
        x=16,
        y=29,
        z=0,
        z_half=False,
        direction=SOUTHEAST,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        cannot_clone=False),
]
