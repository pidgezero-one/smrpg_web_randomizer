
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
from randomizer.data.rooms.room import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone, Room
from randomizer.data.npcs import npcs
from randomizer.helpers.npcmodeltables import SpriteName, VramStore, ShadowSize
from randomizer.helpers.misc_helpers import ExtraSpriteActions
room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=PartitionBufferTypes.EMPTY_3,
                main_buffer_space=PartitionMainSpace._0_BYTES,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=PartitionBufferTypes.EMPTY_3,
                main_buffer_space=PartitionMainSpace._0_BYTES,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=PartitionBufferTypes.EMPTY_3,
                main_buffer_space=PartitionMainSpace._0_BYTES,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=Music._39_MARRYMORE,
    entrance_event=261,
    event_tiles=[
        Event(
            event=671,
            x=6,
            y=87,
            z=2,
            f=Edge.SOUTHWEST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exit_fields=[
        RoomExit(
            x=2,
            y=92,
            z=0,
            f=Edge.SOUTHEAST,
            length=1,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=Rooms._155_MARRYMORE_CHAPEL_KITCHEN,
            show_message=False,
            dst_x=9,
            dst_y=16,
            dst_z=0,
            dst_z_half=1,
            dst_f=RadialDirection.SOUTHWEST,
            x_bit_7=False),
    ])
