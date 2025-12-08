"""NPC list import"""

from randomizer.entities.rooms.object_imports import *

objects = [
    # NPC_0
    RegularNPC(
        occupant=FakeToad,
        initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
        event_script=E1135_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_OCCUPANT_1,
        action_script=A0147_SEASIDE_HENCHMAN,
        speed=0,
        visible=True,
        x=24,
        y=39,
        z=0,
        z_half=False,
        direction=NORTHEAST,
        face_on_trigger=True,
        cant_enter_doors=True,
        byte2_bit5=False,
        set_sequence_playback=True,
        cant_float=True,
        cant_walk_up_stairs=True,
        cant_walk_under=True,
        cant_pass_walls=True,
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
        cannot_clone=False),
    # NPC_1
    RegularClone(
        occupant=FakeToad,
        event_script=E1136_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_OCCUPANT_2,
        action_script=A0147_SEASIDE_HENCHMAN,
        visible=True,
        x=24,
        y=35,
        z=0,
        z_half=False,
        direction=SOUTHWEST,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        cannot_clone=False),
]
