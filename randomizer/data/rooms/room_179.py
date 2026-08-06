# R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM
# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.levels.classes import (EventInitiator, EdgeDirection, BufferType, BufferSpace, VramStore, Buffer, Partition, RoomExit, RegularNPC, ChestNPC)

from ...types.room import Room
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.scripts_common.classes import UInt4, UInt8
from . import npcs
from ..variables.room_names import *
from ..variables.overworld_area_names import *
from ..variables.music_names import *
from ..variables.event_script_names import *
from ..variables.action_script_names import *
room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=True,
        extra_sprite_buffer_size=1,
        buffers = [
            Buffer(
                buffer_type=BufferType.TREASURE_CHEST,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            # Greaper (sprite 276) and the J puzzle block (sprite 104) are both
            # gridplane format 3. Vanilla ROM partition 58 is b1 82 80 80 =
            # CHEST / THREE / THREE; the FOUR + EMPTY_3 this file used to carry
            # did not match either the ROM or the room's own sprites.
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0041_SUNKENSHIP,
    entrance_event=E3227_SHIP_CLONE_ROOM_LOADER,
    exits=[
        RoomExit(
            x=20,
            y=118,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            show_message=False,
            dst_x=5,
            dst_y=113,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False,
            ),
        RoomExit(
            x=16,
            y=126,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            show_message=False,
            dst_x=2,
            dst_y=120,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.MARIO_WALKING_DOWN_LEFT_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_FRONT,
            event_script=E3229_SHIP_CLONE_TRANSFORM,
            action_script=A0015_DO_NOTHING,
            # The mirror clone copies the player's facing, so it needs all 8
            # directions. Redundant for the vanilla NPC record (already DIR7),
            # but load-bearing on non-Mario seeds: apply.py swaps this slot to
            # ALLY_CLONE_NPC, which defaults to DIR0 (4 directions) because it
            # is shared with the stationary recruitment NPCs.
            directions=VramStore.DIR7_ALL_DIRECTIONS,
            # Everything below pins this slot to the vanilla Mario clone's NPC
            # record (ROM 0x1DB800 + 6*7 = 00 5c 80 a0 45 2c 00), because
            # apply.py swaps the record to ALLY_CLONE_NPC on non-Mario seeds and
            # that record is tuned for the stationary recruitment NPCs it is
            # shared with. cannot_clone is the load-bearing one: an 8-direction
            # DIR7 player sprite needs its own dedicated VRAM allocation and
            # cannot fit in a clone buffer.
            cannot_clone=True,
            vram_size=2,
            y_shift=0,
            show_shadow=True,
            byte5_bit6=False,
            byte5_bit7=False,
            byte6_bit2=False,
            visible=True,
            x=15,
            y=125,
            z=0,
            z_half=False,
            direction=NORTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,
            # Collision box from the vanilla MARIO_WALKING_DOWN_LEFT_NPC_2
            # record, applied to whichever character clones into this slot.
            acute_axis=UInt4(5),
            obtuse_axis=UInt4(4),
            height=UInt8(12),
        ),
        RegularNPC( # 1
            npc=npcs.GREAPER_NPC,
            initiator=EventInitiator.NONE,
            event_script=E0256_RETURN,
            action_script=A0015_DO_NOTHING,
            visible=False,
            x=16,
            y=117,
            z=1,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=False,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        ChestNPC( # 2
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E3310_SHIP_HIDDEN_CHEST,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=6,
            upper_70a7=0,
            visible=True,
            x=16,
            y=118,
            z=5,
            z_half=True,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 3
            npc=npcs.J_PUZZLE_BLOCK_NPC_5,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E3309_SHIP_SPAWN_HIDDEN_CHEST,
            action_script=A0444_SHIP_HIDDEN_CHEST_BLOCK_TRIGGER,
            visible=True,
            x=17,
            y=121,
            z=3,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
