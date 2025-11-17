# R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE
from smrpgpatchbuilder.datatypes.levels.classes import ObjectType, EventInitiator, PostBattleBehaviour, Direction, EdgeDirection, ExitType, BufferType, BufferSpace, VramStore, ShadowSize
from smrpgpatchbuilder.datatypes.levels.classes import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone, Room
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from . import npcs
from disassembler_output.variables.room_names import *
from disassembler_output.variables.overworld_area_names import *
from disassembler_output.variables.music_names import *
from disassembler_output.variables.event_script_names import *
from disassembler_output.variables.action_script_names import *
room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0027_DUNGEONISFULLOFMONSTERS,
    entrance_event=E0593_MINES_BOSS_ROOM_LOADER_AFTER_DEFEAT,
    events=[
        Event(
            event=E0595_MINES_BOSS_ROOM_EXIT,
            x=9,
            y=12,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=0,
            length=4,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False,
        ),
        Event(
            event=E0599_MINES_BOSS_ROOM_ENTRANCE_REVERSE,
            x=1,
            y=30,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False,
        ),
    ],
    objects=[
    ]
)
