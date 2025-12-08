"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=SavePoint,
        initiator=EventInitiator.JUMP_ON,
        event_script=E0080_SAVE_BLOCK_SUBROUTINE,
        action_script=A0120_EMBEDDED_ROUTINE,
        speed=0,
        visible=True,
        x=29,
        y=121,
        z=0,
        z_half=False,
        direction=SOUTHWEST,
        face_on_trigger=False,
        cant_enter_doors=False,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=False,
        cant_walk_up_stairs=False,
        cant_walk_under=False,
        cant_pass_walls=False,
        cant_jump_through=False,
        cant_pass_npcs=False,
        byte3_bit5=False,
        cant_walk_through=True,
        byte3_bit7=False,
        slidable_along_walls=True,
        cant_move_if_in_air=True,
        byte7_upper2=True,
        priority_0=True,
        priority_1=True,
        priority_2=False,
        show_shadow=False,
        cannot_clone=False),
]
