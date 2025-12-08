"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=GreenSmallToad,
        initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
        event_script=E0303_MUSHROOM_KINGDOM_JUMPING_KID,
        action_script=A0022_SLOW_REPEATED_JUMPING,
        speed=0,
        visible=True,
        x=6,
        y=45,
        z=3,
        z_half=False,
        direction=SOUTHWEST,
        face_on_trigger=True,
        cant_enter_doors=False,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=False,
        cant_walk_up_stairs=False,
        cant_walk_under=True,
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
]
