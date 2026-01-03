
from randomizer.helpers.roomobjecttables import (
    ObjectType,
    Initiator,
    PostBattle,
    RadialDirection,
    Music,
    Edge,
    ExitType,
    Locations,
    Rooms,
    PartitionBufferTypes,
    PartitionMainSpace)
from randomizer.data.rooms.room import (
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
    Room)
from randomizer.data.npcs import npcs
from randomizer.helpers.npcmodeltables import SpriteName, VramStore, ShadowSize
from randomizer.helpers.misc_helpers import ExtraSpriteActions

room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers=[
            Buffer(
                buffer_type=PartitionBufferTypes.EMPTY_3,
                main_buffer_space=PartitionMainSpace._0_BYTES,
                index_in_main_buffer=True),
            Buffer(
                buffer_type=PartitionBufferTypes.EMPTY_3,
                main_buffer_space=PartitionMainSpace._0_BYTES,
                index_in_main_buffer=True),
            Buffer(
                buffer_type=PartitionBufferTypes.EMPTY_3,
                main_buffer_space=PartitionMainSpace._0_BYTES,
                index_in_main_buffer=True),
        ],
        full_palette_buffer=True),
    extra_required_actions=[ExtraSpriteActions.DownPipe],
    music=Music._27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=1778,
    event_tiles=[
        Event(
            event=1680,
            x=20,
            y=74,
            z=1,
            f=Edge.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exit_fields=[
        RoomExit(
            x=12,
            y=81,
            z=1,
            f=Edge.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            show_message=False,
            dst_x=12,
            dst_y=21,
            dst_z=9,
            dst_z_half=0,
            dst_f=RadialDirection.SOUTHWEST,
            x_bit_7=False),
    ])
