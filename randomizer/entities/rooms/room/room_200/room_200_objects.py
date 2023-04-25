"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=ItemBag,
        initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
        event_script=E1342_ELDER_KEY_PRIZE_GRANTER,
        action_script=A0000_DO_NOTHING,
        speed=0,
        visible=True,
        x=23,
        y=121,
        z=4,
        z_half=False,
        direction=SOUTHEAST,
        face_on_trigger=True,
        cant_enter_doors=False,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=False,
        cant_walk_up_stairs=True,
        cant_walk_under=True,
        cant_pass_walls=False,
        cant_jump_through=False,
        cant_pass_npcs=False,
        byte3_bit5=False,
        cant_walk_through=True,
        byte3_bit7=False,
        slidable_along_walls=True,
        cant_move_if_in_air=True,
        byte7_upper2=True,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=True,
        height=3,
        cannot_clone=True,
    ),
]
