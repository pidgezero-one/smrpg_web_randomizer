"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=AxemGreen,
        initiator=EventInitiator.NONE,
        event_script=E0256_RETURN,
        action_script=A0003_SEQUENCE_LOOPING_ON,
        speed=0,
        visible=True,
        x=12,
        y=47,
        z=0,
        z_half=False,
        direction=SOUTHEAST,
        face_on_trigger=False,
        cant_enter_doors=False,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=False,
        cant_walk_up_stairs=False,
        cant_walk_under=False,
        cant_pass_walls=True,
        cant_jump_through=False,
        cant_pass_npcs=False,
        byte3_bit5=False,
        cant_walk_through=False,
        byte3_bit7=False,
        slidable_along_walls=True,
        cant_move_if_in_air=True,
        byte7_upper2=True,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=False,
        cannot_clone=False,
    ),
]
