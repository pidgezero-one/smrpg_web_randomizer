from typing import List, Optional, Sequence, Union, cast
from randomizer.types.battles.packs.constants.pack_ids import PACK0000_SNIFIT_FIGHT
from randomizer.types.npcs.objects.classes import NPC, AreaNPC
from randomizer.types.npcs.objects.enums import ShadowSize, VramStore
from randomizer.types.npcs.objects.npcs import Empty
from randomizer.types.numbers.classes import UInt16, UInt4, UInt8
from randomizer.types.overworld_scripts.constants.area_objects import NPC_0
from randomizer.types.overworld_scripts.constants.directions import SOUTHWEST
from randomizer.types.overworld_scripts.constants.misc import (
    TOTAL_ROOMS,
    TOTAL_WORLD_MAP_AREAS,
)
from randomizer.types.overworld_scripts.constants.music_names import M00_CURRENT
from randomizer.types.overworld_scripts.event_scripts.constants.script_ids import (
    E0015_STANDARD_ROOM_LOADER,
    E0256_RETURN,
)
from randomizer.types.overworld_scripts.action_scripts.constants.script_ids import (
    A0000_DO_NOTHING,
)
from randomizer.types.overworld_scripts.event_scripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_EVENTS,
)
from randomizer.types.overworld_scripts.action_scripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_ACTIONSCRIPTS,
)
from randomizer.types.rooms.enums import (
    BufferSpace,
    BufferType,
    EdgeDirection,
    EventInitiator,
    ExitType,
    ExtraSpriteActions,
    ObjectType,
    PostBattleBehaviour,
)
from randomizer.types.overworld_scripts.constants.classes import AreaObject, Direction


class Buffer:
    _buffer_type: BufferType = BufferType.EMPTY_3
    _main_buffer_space: BufferSpace = BufferSpace._0_BYTES
    _index_in_main_buffer: bool = True

    @property
    def buffer_type(self) -> BufferType:
        return self._buffer_type

    def set_buffer_type(self, buffer_type: BufferType) -> None:
        self._buffer_type = buffer_type

    @property
    def main_buffer_space(self) -> BufferSpace:
        return self._main_buffer_space

    def set_main_buffer_space(self, main_buffer_space: BufferSpace) -> None:
        self._main_buffer_space = main_buffer_space

    @property
    def index_in_main_buffer(self) -> bool:
        return self._index_in_main_buffer

    def set_index_in_main_buffer(self, index_in_main_buffer: bool) -> None:
        self._index_in_main_buffer = index_in_main_buffer

    def __init__(
        self,
        buffer_type=BufferType.EMPTY_3,
        main_buffer_space=BufferSpace._0_BYTES,
        index_in_main_buffer=True,
    ) -> None:
        self.set_buffer_type(buffer_type)
        self.set_main_buffer_space(main_buffer_space)
        self.set_index_in_main_buffer(index_in_main_buffer)

    def __str__(self) -> str:

        return "{}, {}, {}".format(
            self.buffer_type, self.main_buffer_space, self.index_in_main_buffer
        )

    def is_same(self, buffer: "Buffer") -> bool:
        return (
            self.buffer_type == buffer.buffer_type
            and self.main_buffer_space == buffer.main_buffer_space
            and self.index_in_main_buffer == buffer.index_in_main_buffer
        )


class Partition:
    _ally_sprite_buffer_size: UInt4 = UInt4(1)
    _allow_extra_sprite_buffer: bool = False
    _extra_sprite_buffer_size: UInt4 = UInt4(0)
    _buffers: List[Buffer] = []
    _full_palette_buffer: bool = True

    @property
    def ally_sprite_buffer_size(self) -> UInt4:
        return self._ally_sprite_buffer_size

    def set_ally_sprite_buffer_size(self, ally_sprite_buffer_size: int) -> None:
        assert ally_sprite_buffer_size <= 3
        self._ally_sprite_buffer_size = UInt4(ally_sprite_buffer_size)

    @property
    def allow_extra_sprite_buffer(self) -> bool:
        return self._allow_extra_sprite_buffer

    def set_allow_extra_sprite_buffer(self, allow_extra_sprite_buffer: bool) -> None:
        self._allow_extra_sprite_buffer = allow_extra_sprite_buffer

    @property
    def extra_sprite_buffer_size(self) -> UInt4:
        return self._extra_sprite_buffer_size

    def set_extra_sprite_buffer_size(self, extra_sprite_buffer_size: int) -> None:
        self._extra_sprite_buffer_size = UInt4(extra_sprite_buffer_size)

    @property
    def buffers(self) -> List[Buffer]:
        assert len(self._buffers) == 3
        return self._buffers

    def set_buffers(self, buffers: List[Buffer]) -> None:
        assert len(buffers) == 3
        self._buffers = buffers

    @property
    def full_palette_buffer(self) -> bool:
        return self._full_palette_buffer

    def set_full_palette_buffer(self, full_palette_buffer: bool) -> None:
        self._full_palette_buffer = full_palette_buffer

    def __init__(
        self,
        ally_sprite_buffer_size: int = 1,
        allow_extra_sprite_buffer: bool = False,
        extra_sprite_buffer_size: int = 0,
        buffers: List[Buffer] = [Buffer(), Buffer(), Buffer()],
        full_palette_buffer: bool = True,
    ) -> None:
        self.set_ally_sprite_buffer_size(ally_sprite_buffer_size)
        self.set_allow_extra_sprite_buffer(allow_extra_sprite_buffer)
        self.set_extra_sprite_buffer_size(extra_sprite_buffer_size)
        self.set_buffers(buffers)
        self.set_full_palette_buffer(full_palette_buffer)

    def __str__(self):
        return "ally: {},  packet: {}, {},  buffers: {},  full: {}".format(
            self.ally_sprite_buffer_size,
            self.allow_extra_sprite_buffer,
            self.extra_sprite_buffer_size,
            ";".join([b.__str__() for b in self.buffers]),
            self.full_palette_buffer,
        )

    def is_same(self, partition: "Partition"):
        return (
            self.ally_sprite_buffer_size == partition.ally_sprite_buffer_size
            and self.allow_extra_sprite_buffer == partition.allow_extra_sprite_buffer
            and self.extra_sprite_buffer_size == partition.extra_sprite_buffer_size
            and self.buffers[0].is_same(partition.buffers[0])
            and self.buffers[1].is_same(partition.buffers[1])
            and self.buffers[2].is_same(partition.buffers[2])
            and self.full_palette_buffer == partition.full_palette_buffer
        )

    def is_similar_but_larger_packet_buffer(self, partition: "Partition"):
        return (
            self.ally_sprite_buffer_size == partition.ally_sprite_buffer_size
            and self.allow_extra_sprite_buffer == True
            and partition.allow_extra_sprite_buffer == True
            and self.extra_sprite_buffer_size > partition.extra_sprite_buffer_size
            and self.extra_sprite_buffer_size <= 2
            and self.buffers[0].is_same(partition.buffers[0])
            and self.buffers[1].is_same(partition.buffers[1])
            and self.buffers[2].is_same(partition.buffers[2])
            and self.full_palette_buffer == partition.full_palette_buffer
        )


class DestinationProps:
    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _z_half: bool = False
    _f: Direction = SOUTHWEST
    _x_bit_7: bool = False

    @property
    def x(self) -> UInt8:
        return self._x

    def set_x(self, x: int) -> None:
        assert x <= 63
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        assert y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert z <= 31
        self._z = UInt8(z)

    @property
    def z_half(self) -> bool:
        return self._z_half

    def set_z_half(self, z_half: bool) -> None:
        self._z_half = z_half

    @property
    def f(self) -> Direction:
        return self._f

    def set_f(self, f: Direction) -> None:
        self._f = f

    @property
    def x_bit_7(self) -> bool:
        return self._x_bit_7

    def set_x_bit_7(self, x_bit_7: bool) -> None:
        self._x_bit_7 = x_bit_7

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        f: Direction = SOUTHWEST,
        x_bit_7: bool = False,
    ) -> None:
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_z_half(z_half)
        self.set_f(f)
        self.set_x_bit_7(x_bit_7)


class Exit:
    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _f: EdgeDirection
    _length: UInt8 = UInt8(0)
    _height: UInt4 = UInt4(0)
    _nw_se_edge_active: bool = True
    _ne_sw_edge_active: bool = False
    _destination_type: ExitType = ExitType.ROOM
    _byte_2_bit_2: bool = False
    _destination: Union[UInt8, UInt16]
    _show_message: bool = False
    _destination_props: DestinationProps

    def set_x(self, x: int) -> None:
        assert x <= 63
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        assert y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert z <= 31
        self._z = UInt8(z)

    @property
    def f(self) -> EdgeDirection:
        return self._f

    def set_f(self, f: EdgeDirection) -> None:
        self._f = f

    @property
    def length(self) -> UInt8:
        return self._length

    def set_length(self, length: int) -> None:
        assert 1 <= length <= 16
        self._length = UInt8(length)

    @property
    def height(self) -> UInt4:
        return self._height

    def set_height(self, height: int) -> None:
        assert height <= 7
        self._height = UInt4(height)

    @property
    def nw_se_edge_active(self) -> bool:
        return self._nw_se_edge_active

    def set_nw_se_edge_active(self, nw_se_edge_active: bool) -> None:
        self._nw_se_edge_active = nw_se_edge_active

    @property
    def ne_sw_edge_active(self) -> bool:
        return self._ne_sw_edge_active

    def set_ne_sw_edge_active(self, ne_sw_edge_active: bool) -> None:
        self._ne_sw_edge_active = ne_sw_edge_active

    @property
    def destination_type(self) -> ExitType:
        return self._destination_type

    def set_destination_type(self, destination_type: ExitType) -> None:
        self._destination_type = destination_type

    @property
    def byte_2_bit_2(self) -> bool:
        return self._byte_2_bit_2

    def set_byte_2_bit_2(self, byte_2_bit_2: bool) -> None:
        self._byte_2_bit_2 = byte_2_bit_2

    @property
    def show_message(self) -> bool:
        return self._show_message

    def set_show_message(self, show_message: bool) -> None:
        self._show_message = show_message

    @property
    def destination_props(self) -> DestinationProps:
        return self._destination_props

    def set_destination_props(self, destination_props: DestinationProps) -> None:
        self._destination_props = destination_props


class RoomExit(Exit):
    _destination_type = ExitType.ROOM

    @property
    def destination(self) -> UInt16:
        return UInt16(self._destination)

    def set_destination(self, destination: int) -> None:
        assert destination <= TOTAL_ROOMS
        self._destination = UInt16(destination)

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        f: EdgeDirection = EdgeDirection.SOUTHWEST,
        length: int = 2,
        height: int = 0,
        nw_se_edge_active: bool = True,
        ne_sw_edge_active: bool = False,
        byte_2_bit_2: bool = False,
        destination: int = 0,
        show_message: bool = False,
        dst_x: int = 0,
        dst_y: int = 0,
        dst_z: int = 0,
        dst_z_half: bool = False,
        dst_f: Direction = SOUTHWEST,
        x_bit_7: bool = False,
    ) -> None:
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_f(f)
        super().set_length(length)
        super().set_height(height)
        super().set_nw_se_edge_active(nw_se_edge_active)
        super().set_ne_sw_edge_active(ne_sw_edge_active)
        super().set_byte_2_bit_2(byte_2_bit_2)
        self.set_destination(destination)
        super().set_show_message(show_message)
        props = DestinationProps(
            x=dst_x, y=dst_y, z=dst_z, z_half=dst_z_half, f=dst_f, x_bit_7=x_bit_7
        )
        super().set_destination_props(props)


class MapExit(Exit):
    _destination_type: ExitType = ExitType.MAP_LOCATION
    _byte_2_bit_1: bool = False
    _byte_2_bit_0: bool = False

    @property
    def destination(self) -> UInt8:
        return UInt8(self._destination)

    def set_destination(self, destination: int) -> None:
        assert destination < TOTAL_WORLD_MAP_AREAS
        self._destination = UInt8(destination)

    @property
    def byte_2_bit_1(self) -> bool:
        return self._byte_2_bit_1

    def set_byte_2_bit_1(self, byte_2_bit_1: bool) -> None:
        self._byte_2_bit_1 = byte_2_bit_1

    @property
    def byte_2_bit_0(self) -> bool:
        return self._byte_2_bit_0

    def set_byte_2_bit_0(self, byte_2_bit_0: bool) -> None:
        self._byte_2_bit_0 = byte_2_bit_0

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        f: EdgeDirection = EdgeDirection.SOUTHWEST,
        length: int = 2,
        height: int = 0,
        nw_se_edge_active: bool = True,
        ne_sw_edge_active: bool = False,
        byte_2_bit_2: bool = False,
        destination: int = 0,
        show_message: bool = False,
        byte_2_bit_1: bool = False,
        byte_2_bit_0: bool = False,
    ) -> None:
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_f(f)
        super().set_length(length)
        super().set_height(height)
        super().set_nw_se_edge_active(nw_se_edge_active)
        super().set_ne_sw_edge_active(ne_sw_edge_active)
        super().set_byte_2_bit_2(byte_2_bit_2)
        self.set_destination(destination)
        super().set_show_message(show_message)
        super().set_byte_2_bit_2(byte_2_bit_1)
        super().set_byte_2_bit_2(byte_2_bit_0)


class Event:
    _event: UInt16 = UInt16(0)
    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _f: EdgeDirection = EdgeDirection.SOUTHWEST
    _length: UInt8 = UInt8(1)
    _height: UInt4 = UInt4(0)
    _nw_se_edge_active: bool = True
    _ne_sw_edge_active: bool = False
    _byte_8_bit_4: bool = False

    @property
    def event(self) -> UInt16:
        return self._event

    def set_event(self, event: int) -> None:
        assert event < TOTAL_EVENTS
        self._event = UInt16(event)

    @property
    def x(self) -> UInt8:
        return self._x

    def set_x(self, x: int) -> None:
        assert x <= 63
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        assert y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert z <= 31
        self._z = UInt8(z)

    @property
    def f(self) -> EdgeDirection:
        return self._f

    def set_f(self, f: EdgeDirection) -> None:
        self._f = f

    @property
    def length(self) -> UInt8:
        return self._length

    def set_length(self, length: int) -> None:
        assert 1 <= length <= 16
        self._length = UInt8(length)

    @property
    def height(self) -> UInt4:
        return self._height

    def set_height(self, height: int) -> None:
        assert height <= 7
        self._height = UInt4(height)

    @property
    def nw_se_edge_active(self) -> bool:
        return self._nw_se_edge_active

    def set_nw_se_edge_active(self, nw_se_edge_active: bool) -> None:
        self._nw_se_edge_active = nw_se_edge_active

    @property
    def ne_sw_edge_active(self) -> bool:
        return self._ne_sw_edge_active

    def set_ne_sw_edge_active(self, ne_sw_edge_active: bool) -> None:
        self._ne_sw_edge_active = ne_sw_edge_active

    @property
    def byte_8_bit_4(self) -> bool:
        return self._byte_8_bit_4

    def set_byte_8_bit_4(self, byte_8_bit_4: bool) -> None:
        self._byte_8_bit_4 = byte_8_bit_4

    def __init__(
        self,
        event: int,
        x: int,
        y: int,
        z: int,
        f: EdgeDirection,
        length: int,
        height: int,
        nw_se_edge_active: bool,
        ne_sw_edge_active: bool,
        byte_8_bit_4: bool,
    ) -> None:
        self.set_event(event)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_f(f)
        self.set_length(length)
        self.set_height(height)
        self.set_nw_se_edge_active(nw_se_edge_active)
        self.set_ne_sw_edge_active(ne_sw_edge_active)
        self.set_byte_8_bit_4(byte_8_bit_4)


class BaseRoomObject:
    _id: AreaObject = NPC_0
    _model: AreaNPC = AreaNPC(Empty())
    _type: ObjectType = ObjectType.OBJECT
    _visible: bool = False
    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _z_half: bool = False
    _direction: Direction = SOUTHWEST

    @property
    def id(self) -> int:
        return self._id - 0x14

    def set_id(self, id: AreaObject) -> None:
        self._id = id

    @property
    def model(self) -> AreaNPC:
        return self._model

    def set_model(self, model: AreaNPC) -> None:
        self._model = model

    @property
    def type(self) -> ObjectType:
        return self._type

    def set_type(self, type: ObjectType) -> None:
        self._type = type

    @property
    def visible(self) -> bool:
        return self._visible

    def set_visible(self, visible: bool) -> None:
        self._visible = visible

    @property
    def x(self) -> UInt8:
        return self._x

    def set_x(self, x: int) -> None:
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert z <= 31
        self._z = UInt8(z)

    @property
    def z_half(self) -> bool:
        return self._z_half

    def set_z_half(self, z_half: bool) -> None:
        self._z_half = z_half

    @property
    def direction(self) -> Direction:
        return self._direction

    def set_direction(self, direction: Direction) -> None:
        self._direction = direction


class RoomObject(BaseRoomObject):
    _initiator: EventInitiator = EventInitiator.NONE
    _action_script: UInt16 = UInt16(0)
    _speed: UInt4 = UInt4(0)
    _face_on_trigger: bool = False
    _cant_enter_doors: bool = False
    _byte2_bit5: bool = False
    _set_sequence_playback: bool = False
    _cant_float: bool = False
    _cant_walk_up_stairs: bool = False
    _cant_walk_under: bool = False
    _cant_pass_walls: bool = False
    _cant_jump_through: bool = False
    _cant_pass_npcs: bool = False
    _byte3_bit5: bool = False
    _cant_walk_through: bool = False
    _byte3_bit7: bool = False
    _slidable_along_walls: bool = False
    _cant_move_if_in_air: bool = False
    _byte7_upper2: bool = False

    @property
    def initiator(self) -> EventInitiator:
        return self._initiator

    def set_initiator(self, initiator: EventInitiator) -> None:
        self._initiator = initiator

    @property
    def action_script(self) -> UInt16:
        return self._action_script

    def set_action_script(self, action_script: int) -> None:
        assert action_script < TOTAL_ACTIONSCRIPTS
        self._action_script = UInt16(action_script)

    @property
    def speed(self) -> UInt4:
        return self._speed

    def set_speed(self, speed: int) -> None:
        assert speed <= 7
        self._speed = UInt4(speed)

    @property
    def face_on_trigger(self) -> bool:
        return self._face_on_trigger

    def set_face_on_trigger(self, face_on_trigger: bool) -> None:
        self._face_on_trigger = face_on_trigger

    @property
    def cant_enter_doors(self) -> bool:
        return self._cant_enter_doors

    def set_cant_enter_doors(self, cant_enter_doors: bool) -> None:
        self._cant_enter_doors = cant_enter_doors

    @property
    def byte2_bit5(self) -> bool:
        return self._byte2_bit5

    def set_byte2_bit5(self, byte2_bit5: bool) -> None:
        self._byte2_bit5 = byte2_bit5

    @property
    def set_sequence_playback(self) -> bool:
        return self._set_sequence_playback

    def set_set_sequence_playback(self, set_sequence_playback: bool) -> None:
        self._set_sequence_playback = set_sequence_playback

    @property
    def cant_float(self) -> bool:
        return self._cant_float

    def set_cant_float(self, cant_float: bool) -> None:
        self._cant_float = cant_float

    @property
    def cant_walk_up_stairs(self) -> bool:
        return self._cant_walk_up_stairs

    def set_cant_walk_up_stairs(self, cant_walk_up_stairs: bool) -> None:
        self._cant_walk_up_stairs = cant_walk_up_stairs

    @property
    def cant_walk_under(self) -> bool:
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        self._cant_jump_through = cant_jump_through

    @property
    def cant_pass_npcs(self) -> bool:
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def byte3_bit5(self) -> bool:
        return self._byte3_bit5

    def set_byte3_bit5(self, byte3_bit5: bool) -> None:
        self._byte3_bit5 = byte3_bit5

    @property
    def cant_walk_through(self) -> bool:
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        self._cant_walk_through = cant_walk_through

    @property
    def byte3_bit7(self) -> bool:
        return self._byte3_bit7

    def set_byte3_bit7(self, byte3_bit7: bool) -> None:
        self._byte3_bit7 = byte3_bit7

    @property
    def slidable_along_walls(self) -> bool:
        return self._slidable_along_walls

    def set_slidable_along_walls(self, slidable_along_walls: bool) -> None:
        self._slidable_along_walls = slidable_along_walls

    @property
    def cant_move_if_in_air(self) -> bool:
        return self._cant_move_if_in_air

    def set_cant_move_if_in_air(self, cant_move_if_in_air: bool) -> None:
        self._cant_move_if_in_air = cant_move_if_in_air

    @property
    def byte7_upper2(self) -> bool:
        return self._byte7_upper2

    def set_byte7_upper2(self, byte7_upper2: bool) -> None:
        self._byte7_upper2 = byte7_upper2


class Clone(BaseRoomObject):
    _action_script: UInt16 = UInt16(0)

    @property
    def action_script(self) -> UInt16:
        return self._action_script

    def set_action_script(self, action_script: int) -> None:
        assert action_script < TOTAL_ACTIONSCRIPTS
        self._action_script = UInt16(action_script)


class BattlePackNPC(RoomObject):
    _type = ObjectType.BATTLE
    _battle_pack: UInt8 = UInt8(0)
    _after_battle = PostBattleBehaviour.REMOVE_PERMANENTLY

    @property
    def battle_pack(self) -> UInt8:
        return self._battle_pack

    def set_battle_pack(self, battle_pack: int) -> None:
        self._battle_pack = UInt8(battle_pack)

    @property
    def after_battle(self) -> PostBattleBehaviour:
        return self._after_battle

    def set_after_battle(self, after_battle: PostBattleBehaviour) -> None:
        self._after_battle = after_battle

    def __init__(
        self,
        occupant: NPC,
        initiator: EventInitiator = EventInitiator.NONE,
        after_battle: PostBattleBehaviour = PostBattleBehaviour.REMOVE_PERMANENTLY,
        battle_pack: int = PACK0000_SNIFIT_FIGHT,
        action_script: int = A0000_DO_NOTHING,
        speed: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        face_on_trigger: bool = False,
        cant_enter_doors: bool = False,
        byte2_bit5: bool = False,
        set_sequence_playback: bool = False,
        cant_float: bool = False,
        cant_walk_up_stairs: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        cant_pass_npcs: bool = False,
        byte3_bit5: bool = False,
        cant_walk_through: bool = False,
        byte3_bit7: bool = False,
        slidable_along_walls: bool = False,
        cant_move_if_in_air: bool = False,
        byte7_upper2: bool = False,
        priority_0: bool = False,
        priority_1: bool = False,
        priority_2: bool = True,
        show_shadow: Optional[bool] = None,
        shadow_size: Optional[ShadowSize] = None,
        acute_axis: Optional[int] = None,
        obtuse_axis: Optional[int] = None,
        height: Optional[int] = None,
        directions: Optional[VramStore] = None,
        vram_size: Optional[int] = None,
        cannot_clone: bool = False,
        byte2_bit0: Optional[bool] = None,
        byte2_bit1: Optional[bool] = None,
        byte2_bit2: Optional[bool] = None,
        byte2_bit3: Optional[bool] = None,
        byte2_bit4: Optional[bool] = None,
        byte5_bit6: Optional[bool] = None,
        byte5_bit7: Optional[bool] = None,
        byte6_bit2: Optional[bool] = None,
        y_shift: Optional[int] = None,
    ):
        super().set_initiator(initiator)
        self.set_after_battle(after_battle)
        self.set_battle_pack(battle_pack)
        super().set_action_script(action_script)
        super().set_speed(speed)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        super().set_face_on_trigger(face_on_trigger)
        super().set_cant_enter_doors(cant_enter_doors)
        super().set_byte2_bit5(byte2_bit5)
        super().set_set_sequence_playback(set_sequence_playback)
        super().set_cant_float(cant_float)
        super().set_cant_walk_up_stairs(cant_walk_up_stairs)
        super().set_cant_walk_under(cant_walk_under)
        super().set_cant_pass_walls(cant_pass_walls)
        super().set_cant_jump_through(cant_jump_through)
        super().set_cant_pass_npcs(cant_pass_npcs)
        super().set_byte3_bit5(byte3_bit5)
        super().set_cant_walk_through(cant_walk_through)
        super().set_byte3_bit7(byte3_bit7)
        super().set_slidable_along_walls(slidable_along_walls)
        super().set_cant_move_if_in_air(cant_move_if_in_air)
        super().set_byte7_upper2(byte7_upper2)
        model = AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
            shadow_size,
            y_shift,
            acute_axis,
            obtuse_axis,
            height,
            directions,
            vram_size,
            cannot_clone,
            byte2_bit0,
            byte2_bit1,
            byte2_bit2,
            byte2_bit3,
            byte2_bit4,
            byte5_bit6,
            byte5_bit7,
            byte6_bit2,
        )
        super().set_model(model)


class RegularNPC(RoomObject):
    _type = ObjectType.OBJECT
    _event_script: UInt16 = UInt16(E0256_RETURN)

    @property
    def event_script(self) -> UInt16:
        return self._event_script

    def set_event_script(self, event_script: int) -> None:
        self._event_script = UInt16(event_script)

    def __init__(
        self,
        occupant: NPC,
        initiator: EventInitiator = EventInitiator.NONE,
        event_script: int = E0256_RETURN,
        action_script: int = A0000_DO_NOTHING,
        speed: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        face_on_trigger: bool = False,
        cant_enter_doors: bool = False,
        byte2_bit5: bool = False,
        set_sequence_playback: bool = False,
        cant_float: bool = False,
        cant_walk_up_stairs: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        cant_pass_npcs: bool = False,
        byte3_bit5: bool = False,
        cant_walk_through: bool = False,
        byte3_bit7: bool = False,
        slidable_along_walls: bool = False,
        cant_move_if_in_air: bool = False,
        byte7_upper2: bool = False,
        priority_0: bool = False,
        priority_1: bool = False,
        priority_2: bool = True,
        show_shadow: Optional[bool] = None,
        shadow_size: Optional[ShadowSize] = None,
        acute_axis: Optional[int] = None,
        obtuse_axis: Optional[int] = None,
        height: Optional[int] = None,
        directions: Optional[VramStore] = None,
        vram_size: Optional[int] = None,
        cannot_clone: bool = False,
        byte2_bit0: Optional[bool] = None,
        byte2_bit1: Optional[bool] = None,
        byte2_bit2: Optional[bool] = None,
        byte2_bit3: Optional[bool] = None,
        byte2_bit4: Optional[bool] = None,
        byte5_bit6: Optional[bool] = None,
        byte5_bit7: Optional[bool] = None,
        byte6_bit2: Optional[bool] = None,
        y_shift: Optional[int] = None,
    ):
        super().set_initiator(initiator)
        self.set_event_script(event_script)
        super().set_action_script(action_script)
        super().set_speed(speed)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        super().set_face_on_trigger(face_on_trigger)
        super().set_cant_enter_doors(cant_enter_doors)
        super().set_byte2_bit5(byte2_bit5)
        super().set_set_sequence_playback(set_sequence_playback)
        super().set_cant_float(cant_float)
        super().set_cant_walk_up_stairs(cant_walk_up_stairs)
        super().set_cant_walk_under(cant_walk_under)
        super().set_cant_pass_walls(cant_pass_walls)
        super().set_cant_jump_through(cant_jump_through)
        super().set_cant_pass_npcs(cant_pass_npcs)
        super().set_byte3_bit5(byte3_bit5)
        super().set_cant_walk_through(cant_walk_through)
        super().set_byte3_bit7(byte3_bit7)
        super().set_slidable_along_walls(slidable_along_walls)
        super().set_cant_move_if_in_air(cant_move_if_in_air)
        super().set_byte7_upper2(byte7_upper2)
        model = AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
            shadow_size,
            y_shift,
            acute_axis,
            obtuse_axis,
            height,
            directions,
            vram_size,
            cannot_clone,
            byte2_bit0,
            byte2_bit1,
            byte2_bit2,
            byte2_bit3,
            byte2_bit4,
            byte5_bit6,
            byte5_bit7,
            byte6_bit2,
        )
        super().set_model(model)


class ChestNPC(RoomObject):
    _type = ObjectType.CHEST
    _event_script: UInt16 = UInt16(E0256_RETURN)
    _lower_70A7: UInt4 = UInt4(0)
    _upper_70A7: UInt4 = UInt4(0)

    @property
    def event_script(self) -> UInt16:
        return self._event_script

    def set_event_script(self, event_script: int) -> None:
        self._event_script = UInt16(event_script)

    @property
    def lower_70A7(self) -> UInt4:
        return self._lower_70A7

    def set_lower_70A7(self, lower_70A7: int) -> None:
        self._lower_70A7 = UInt4(lower_70A7)

    @property
    def upper_70A7(self) -> UInt4:
        return self._upper_70A7

    def set_upper_70A7(self, upper_70A7: int) -> None:
        self._upper_70A7 = UInt4(upper_70A7)

    def __init__(
        self,
        occupant: NPC,
        initiator: EventInitiator = EventInitiator.NONE,
        event_script: int = E0256_RETURN,
        action_script: int = A0000_DO_NOTHING,
        lower_70A7: int = 0,
        upper_70A7: int = 0,
        speed: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        face_on_trigger: bool = False,
        cant_enter_doors: bool = False,
        byte2_bit5: bool = False,
        set_sequence_playback: bool = False,
        cant_float: bool = False,
        cant_walk_up_stairs: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        cant_pass_npcs: bool = False,
        byte3_bit5: bool = False,
        cant_walk_through: bool = False,
        byte3_bit7: bool = False,
        slidable_along_walls: bool = False,
        cant_move_if_in_air: bool = False,
        byte7_upper2: bool = False,
        priority_0: bool = False,
        priority_1: bool = False,
        priority_2: bool = True,
        show_shadow: Optional[bool] = None,
        shadow_size: Optional[ShadowSize] = None,
        acute_axis: Optional[int] = None,
        obtuse_axis: Optional[int] = None,
        height: Optional[int] = None,
        directions: Optional[VramStore] = None,
        vram_size: Optional[int] = None,
        cannot_clone: bool = False,
        byte2_bit0: Optional[bool] = None,
        byte2_bit1: Optional[bool] = None,
        byte2_bit2: Optional[bool] = None,
        byte2_bit3: Optional[bool] = None,
        byte2_bit4: Optional[bool] = None,
        byte5_bit6: Optional[bool] = None,
        byte5_bit7: Optional[bool] = None,
        byte6_bit2: Optional[bool] = None,
        y_shift: Optional[int] = None,
    ):
        super().set_initiator(initiator)
        self.set_event_script(event_script)
        super().set_action_script(action_script)
        self.set_lower_70A7(lower_70A7)
        self.set_upper_70A7(upper_70A7)
        super().set_speed(speed)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        super().set_face_on_trigger(face_on_trigger)
        super().set_cant_enter_doors(cant_enter_doors)
        super().set_byte2_bit5(byte2_bit5)
        super().set_set_sequence_playback(set_sequence_playback)
        super().set_cant_float(cant_float)
        super().set_cant_walk_up_stairs(cant_walk_up_stairs)
        super().set_cant_walk_under(cant_walk_under)
        super().set_cant_pass_walls(cant_pass_walls)
        super().set_cant_jump_through(cant_jump_through)
        super().set_cant_pass_npcs(cant_pass_npcs)
        super().set_byte3_bit5(byte3_bit5)
        super().set_cant_walk_through(cant_walk_through)
        super().set_byte3_bit7(byte3_bit7)
        super().set_slidable_along_walls(slidable_along_walls)
        super().set_cant_move_if_in_air(cant_move_if_in_air)
        super().set_byte7_upper2(byte7_upper2)
        model = AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
            shadow_size,
            y_shift,
            acute_axis,
            obtuse_axis,
            height,
            directions,
            vram_size,
            cannot_clone,
            byte2_bit0,
            byte2_bit1,
            byte2_bit2,
            byte2_bit3,
            byte2_bit4,
            byte5_bit6,
            byte5_bit7,
            byte6_bit2,
        )
        super().set_model(model)


class BattlePackClone(Clone):
    _type = ObjectType.BATTLE
    _battle_pack: UInt8 = UInt8(0)

    @property
    def battle_pack(self) -> UInt8:
        return self._battle_pack

    def set_battle_pack(self, battle_pack: int) -> None:
        self._battle_pack = UInt8(battle_pack)

    def __init__(
        self,
        occupant: NPC,
        battle_pack: int = PACK0000_SNIFIT_FIGHT,
        action_script: int = A0000_DO_NOTHING,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        priority_0: bool = False,
        priority_1: bool = False,
        priority_2: bool = True,
        show_shadow: Optional[bool] = None,
        shadow_size: Optional[ShadowSize] = None,
        y_shift: Optional[int] = None,
        acute_axis: Optional[int] = None,
        obtuse_axis: Optional[int] = None,
        height: Optional[int] = None,
        directions: Optional[VramStore] = None,
        vram_size: Optional[int] = None,
        cannot_clone: bool = False,
        byte2_bit0: Optional[bool] = None,
        byte2_bit1: Optional[bool] = None,
        byte2_bit2: Optional[bool] = None,
        byte2_bit3: Optional[bool] = None,
        byte2_bit4: Optional[bool] = None,
        byte5_bit6: Optional[bool] = None,
        byte5_bit7: Optional[bool] = None,
        byte6_bit2: Optional[bool] = None,
    ):
        self.set_battle_pack(battle_pack)
        super().set_action_script(action_script)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        model = AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
            shadow_size,
            y_shift,
            acute_axis,
            obtuse_axis,
            height,
            directions,
            vram_size,
            cannot_clone,
            byte2_bit0,
            byte2_bit1,
            byte2_bit2,
            byte2_bit3,
            byte2_bit4,
            byte5_bit6,
            byte5_bit7,
            byte6_bit2,
        )
        super().set_model(model)


class RegularClone(Clone):
    _type = ObjectType.OBJECT
    _event_script: UInt16 = UInt16(E0256_RETURN)

    @property
    def event_script(self) -> UInt16:
        return self._event_script

    def set_event_script(self, event_script: int) -> None:
        self._event_script = UInt16(event_script)

    def __init__(
        self,
        occupant: NPC,
        event_script: int = E0256_RETURN,
        action_script: int = A0000_DO_NOTHING,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        priority_0: bool = False,
        priority_1: bool = False,
        priority_2: bool = True,
        show_shadow: Optional[bool] = None,
        shadow_size: Optional[ShadowSize] = None,
        y_shift: Optional[int] = None,
        acute_axis: Optional[int] = None,
        obtuse_axis: Optional[int] = None,
        height: Optional[int] = None,
        directions: Optional[VramStore] = None,
        vram_size: Optional[int] = None,
        cannot_clone: bool = False,
        byte2_bit0: Optional[bool] = None,
        byte2_bit1: Optional[bool] = None,
        byte2_bit2: Optional[bool] = None,
        byte2_bit3: Optional[bool] = None,
        byte2_bit4: Optional[bool] = None,
        byte5_bit6: Optional[bool] = None,
        byte5_bit7: Optional[bool] = None,
        byte6_bit2: Optional[bool] = None,
    ):
        self.set_event_script(event_script)
        super().set_action_script(action_script)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        model = AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
            shadow_size,
            y_shift,
            acute_axis,
            obtuse_axis,
            height,
            directions,
            vram_size,
            cannot_clone,
            byte2_bit0,
            byte2_bit1,
            byte2_bit2,
            byte2_bit3,
            byte2_bit4,
            byte5_bit6,
            byte5_bit7,
            byte6_bit2,
        )
        super().set_model(model)


class ChestClone(Clone):
    _type = ObjectType.CHEST
    _lower_70A7: UInt4 = UInt4(0)
    _upper_70A7: UInt4 = UInt4(0)

    @property
    def lower_70A7(self) -> UInt4:
        return self._lower_70A7

    def set_lower_70A7(self, lower_70A7: int) -> None:
        self._lower_70A7 = UInt4(lower_70A7)

    @property
    def upper_70A7(self) -> UInt4:
        return self._upper_70A7

    def set_upper_70A7(self, upper_70A7: int) -> None:
        self._upper_70A7 = UInt4(upper_70A7)

    def __init__(
        self,
        occupant,
        lower_70A7: int = 0,
        upper_70A7: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        priority_0: bool = False,
        priority_1: bool = False,
        priority_2: bool = True,
        show_shadow: Optional[bool] = None,
        shadow_size: Optional[ShadowSize] = None,
        y_shift: Optional[int] = None,
        acute_axis: Optional[int] = None,
        obtuse_axis: Optional[int] = None,
        height: Optional[int] = None,
        directions: Optional[VramStore] = None,
        vram_size: Optional[int] = None,
        cannot_clone: bool = False,
        byte2_bit0: Optional[bool] = None,
        byte2_bit1: Optional[bool] = None,
        byte2_bit2: Optional[bool] = None,
        byte2_bit3: Optional[bool] = None,
        byte2_bit4: Optional[bool] = None,
        byte5_bit6: Optional[bool] = None,
        byte5_bit7: Optional[bool] = None,
        byte6_bit2: Optional[bool] = None,
    ):
        self.set_lower_70A7(lower_70A7)
        self.set_upper_70A7(upper_70A7)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        model = AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
            shadow_size,
            y_shift,
            acute_axis,
            obtuse_axis,
            height,
            directions,
            vram_size,
            cannot_clone,
            byte2_bit0,
            byte2_bit1,
            byte2_bit2,
            byte2_bit3,
            byte2_bit4,
            byte5_bit6,
            byte5_bit7,
            byte6_bit2,
        )
        super().set_model(model)


class Room:
    _partition: Optional[Partition] = None
    _music: UInt8 = UInt8(0)
    _entrance_event: UInt16 = UInt16(0)
    _event_tiles: List[Event] = []
    _exit_fields: List[Union[RoomExit, MapExit]] = []
    _objects: Sequence[BaseRoomObject] = []
    _extra_sprite_actions: List[ExtraSpriteActions] = []

    @property
    def partition(self) -> Optional[Partition]:
        return self._partition

    def set_partition(self, partition: Optional[Partition]) -> None:
        self._partition = partition

    @property
    def music(self) -> UInt8:
        return self._music

    def set_music(self, music: int) -> None:
        self._music = UInt8(music)

    @property
    def entrance_event(self) -> UInt16:
        return self._entrance_event

    def set_entrance_event(self, entrance_event: int) -> None:
        self._entrance_event = UInt16(entrance_event)

    @property
    def event_tiles(self) -> List[Event]:
        return self._event_tiles

    def set_event_tiles(self, event_tiles: List[Event]) -> None:
        self._event_tiles = event_tiles

    @property
    def exit_fields(self) -> List[Union[RoomExit, MapExit]]:
        return self._exit_fields

    def set_exit_fields(self, exit_fields: List[Union[RoomExit, MapExit]]) -> None:
        self._exit_fields = exit_fields

    def add_object(self, item: BaseRoomObject) -> None:
        objects = cast(list[BaseRoomObject], self.objects)
        objects.append(item)
        self._objects = cast(Sequence[BaseRoomObject], objects)

    def add_objects(self, items: List[BaseRoomObject]) -> None:
        objects = cast(list[BaseRoomObject], self.objects)
        objects.extend(items)
        self._objects = cast(Sequence[BaseRoomObject], objects)

    @property
    def objects(
        self,
    ) -> Sequence[BaseRoomObject]:
        return self._objects

    def set_objects(
        self,
        objects: Sequence[BaseRoomObject],
    ) -> None:
        self._objects = objects

    @property
    def extra_sprite_actions(self) -> List[ExtraSpriteActions]:
        return self._extra_sprite_actions

    def set_extra_sprite_actions(
        self, extra_sprite_actions: List[ExtraSpriteActions]
    ) -> None:
        self._extra_sprite_actions = extra_sprite_actions

    def __init__(
        self,
        partition: Partition = Partition(),
        music: int = M00_CURRENT,
        entrance_event: int = E0015_STANDARD_ROOM_LOADER,
        event_tiles: List[Event] = [],
        exit_fields: List[Union[RoomExit, MapExit]] = [],
        objects: Sequence[BaseRoomObject] = [],
        extra_sprite_actions: List[ExtraSpriteActions] = [],
    ):
        self.set_partition(partition)
        self.set_music(music)
        self.set_entrance_event(entrance_event)
        self.set_event_tiles(event_tiles)
        self.set_exit_fields(exit_fields)
        self.set_objects(objects)
        self.set_extra_sprite_actions(extra_sprite_actions)
