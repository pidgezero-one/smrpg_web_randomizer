"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=FakeToad,
        initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
        event_script=E1137_SEASIDE_OCCUPIED_HEALTH_STORE_OCCUPANT,
        action_script=A0147_SEASIDE_HENCHMAN,
        speed=0,
        visible=True,
        x=25,
        y=9,
        z=2,
        z_half=False,
        direction=SOUTHWEST,
        face_on_trigger=True,
        cant_enter_doors=False,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=True,
        cant_walk_up_stairs=True,
        cant_walk_under=True,
        cant_pass_walls=False,
        cant_jump_through=False,
        cant_pass_npcs=True,
        byte3_bit5=True,
        cant_walk_through=True,
        byte3_bit7=True,
        slidable_along_walls=True,
        cant_move_if_in_air=True,
        byte7_upper2=True,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        cannot_clone=False),
]
