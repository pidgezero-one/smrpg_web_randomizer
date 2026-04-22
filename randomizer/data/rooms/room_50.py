# R050_POSTGAME_CHAPEL
# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.levels.classes import (
    ObjectType,
    EventInitiator,
    PostBattleBehaviour,
    Direction,
    EdgeDirection,
    ExitType,
    BufferType,
    BufferSpace,
    VramStore,
    ShadowSize,
    Buffer,
    Partition,
    DestinationProps,
    RoomExit,
    MapExit,
    Event,
    BattlePackNPC,
    RegularNPC,
    ChestNPC,
    BattlePackClone,
    RegularClone,
    ChestClone,
    EffectsNpc
)
from ...types.room import Room
from ...types.ally import SpriteAnimationState
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from . import npcs
from ..variables.room_names import *
from ..variables.overworld_area_names import *
from ..variables.music_names import *
from ..variables.event_script_names import *
from ..variables.action_script_names import *

room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers=[
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True,
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True,
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True,
            ),
        ],
        full_palette_buffer=True,
    ),
    music=M0039_MARRYMORE,
    entrance_event=E0725_CHAPEL_POSTGAME_LOADER,
    exits=[
        RoomExit(
            x=8,
            y=99,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
            show_message=False,
            dst_x=20,
            dst_y=16,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC(  # 0
            npc=npcs.BUNDT_OBJECT_NPC_2,
            initiator=EventInitiator.DO_ANYTHING,
            event_script=E2052_CHAPEL_POSTGAME_BOSS,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=20,
            y=75,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
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
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3,
            directions=VramStore.DIR2_SWSE
        ),
        
        RegularNPC(  # 1
            npc=npcs.TORTE_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E2052_CHAPEL_POSTGAME_BOSS,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=20,
            y=76,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
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
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3,
        ),
        RegularClone(  # 2
            npc=npcs.TORTE_NPC_2,
            event_script=E2052_CHAPEL_POSTGAME_BOSS,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=20,
            y=77,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
    ],
    npc_expected_animations={
        0: ["chapel_laugh"]
    }
)
