"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=RedSmallToad,
        initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
        event_script=E0326_MUSHROOM_KINGDOM_CASTLE_GENERIC_TOAD,
        action_script=A0015_DO_NOTHING,
        speed=0,
        visible=True,
        x=28,
        y=92,
        z=0,
        z_half=False,
        direction=SOUTHWEST,
        face_on_trigger=True,
        cant_enter_doors=True,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=True,
        cant_walk_up_stairs=False,
        cant_walk_under=False,
        cant_pass_walls=True,
        cant_jump_through=False,
        cant_pass_npcs=False,
        byte3_bit5=False,
        cant_walk_through=True,
        byte3_bit7=False,
        slidable_along_walls=False,
        cant_move_if_in_air=False,
        byte7_upper2=True,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        cannot_clone=False),
    # NPC_1
    RegularClone(
        occupant=RedSmallToad,
        event_script=E0326_MUSHROOM_KINGDOM_CASTLE_GENERIC_TOAD,
        action_script=A0015_DO_NOTHING,
        visible=True,
        x=29,
        y=95,
        z=0,
        z_half=False,
        direction=SOUTHWEST,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        cannot_clone=False),
]
