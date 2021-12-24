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
    PartitionMainSpace,
)
from randomizer.data import npcs


class Buffer:
    buffer_type = PartitionBufferTypes.EMPTY_3
    main_buffer_space = PartitionMainSpace._0_BYTES
    index_in_main_buffer = True

    def __init__(
        self,
        buffer_type=PartitionBufferTypes.EMPTY_3,
        main_buffer_space=PartitionMainSpace._0_BYTES,
        index_in_main_buffer=True,
    ):
        self.buffer_type = buffer_type
        self.main_buffer_space = main_buffer_space
        self.index_in_main_buffer = index_in_main_buffer


class Partition:
    ally_sprite_buffer_size = 1
    allow_extra_sprite_buffer = False
    extra_sprite_buffer_size = 0
    buffers = [Buffer(), Buffer(), Buffer()]
    full_palette_buffer = True

    def __init__(
        self,
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers=[Buffer(), Buffer(), Buffer()],
        full_palette_buffer=True,
    ):
        self.ally_sprite_buffer_size = ally_sprite_buffer_size
        self.allow_extra_sprite_buffer = allow_extra_sprite_buffer
        self.extra_sprite_buffer_size = extra_sprite_buffer_size
        assert len(buffers) == 3
        self.buffers = buffers
        self.full_palette_buffer = full_palette_buffer


class DestinationProps:
    x = 0
    y = 0
    z = 0
    z_half = False
    f = RadialDirection.SOUTHWEST
    x_bit_7 = False

    def __init__(
        self, x=0, y=0, z=0, z_half=False, f=RadialDirection.SOUTHWEST, x_bit_7=False
    ):
        self.x = x
        self.y = y
        self.z = z
        self.z_half = z_half
        self.f = f
        self.x_bit_7 = x_bit_7


class Exit:
    x = 0
    y = 0
    z = 0
    f = Edge.SOUTHWEST
    length = 2
    height = 0
    nw_se_edge_active = True
    ne_sw_edge_active = False
    destination_type = ExitType.ROOM
    byte_2_bit_0 = False
    destination = None
    show_message = False
    destination_props = None


class RoomExit(Exit):
    destination_type = ExitType.ROOM

    def __init__(
        self,
        x=0,
        y=0,
        z=0,
        f=Edge.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=None,
        show_message=False,
        dst_x=0,
        dst_y=0,
        dst_z=0,
        dst_z_half=0,
        dst_f=RadialDirection.SOUTHWEST,
        x_bit_7=False,
    ):
        self.x = x
        self.y = y
        self.z = z
        self.f = f
        self.length = length
        self.height = height
        self.nw_se_edge_active = nw_se_edge_active
        self.ne_sw_edge_active = ne_sw_edge_active
        self.byte_2_bit_2 = byte_2_bit_2
        self.destination = destination
        self.show_message = show_message
        self.destination_props = DestinationProps(
            dst_x, dst_y, dst_z, dst_z_half, dst_f, x_bit_7
        )


class MapExit(Exit):
    destination_type = ExitType.MAP_LOCATION
    byte_2_bit_1 = False
    byte_2_bit_0 = False

    def __init__(
        self,
        x=0,
        y=0,
        z=0,
        f=Edge.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=None,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False,
    ):
        self.x = x
        self.y = y
        self.z = z
        self.f = f
        self.length = length
        self.height = height
        self.nw_se_edge_active = nw_se_edge_active
        self.ne_sw_edge_active = ne_sw_edge_active
        self.byte_2_bit_2 = byte_2_bit_2
        self.destination = destination
        self.show_message = show_message
        self.byte_2_bit_1 = byte_2_bit_1
        self.byte_2_bit_0 = byte_2_bit_0


class Event:
    event = 0
    x = 0
    y = 0
    z = 0
    f = Edge.SOUTHWEST
    length = 1
    height = 0
    nw_se_edge_active = True
    ne_sw_edge_active = False
    byte_8_bit_4 = False

    def __init__(
        self,
        event=0,
        x=0,
        y=0,
        z=0,
        f=Edge.SOUTHWEST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ):
        self.event = event
        self.x = x
        self.y = y
        self.z = z
        self.f = f
        self.length = length
        self.height = height
        self.nw_se_edge_active = nw_se_edge_active
        self.ne_sw_edge_active = ne_sw_edge_active
        self.byte_8_bit_4 = byte_8_bit_4


class BaseRoomObject:
    id = 0
    model = npcs.AreaNPC(npcs.Empty)
    type = None
    visible = False
    x = 0
    y = 0
    z = 0
    z_half = False
    direction = RadialDirection.SOUTHWEST


class RoomObject(BaseRoomObject):
    id = 0
    model = npcs.AreaNPC(npcs.Empty)
    type = None
    initiator = Initiator.NONE
    action_script = 0
    speed = 0
    face_on_trigger = False
    cant_enter_doors = False
    byte2_bit5 = False
    set_sequence_playback = False
    cant_float = False
    cant_walk_up_stairs = False
    cant_walk_under = False
    cant_pass_walls = False
    cant_jump_through = False
    cant_pass_npcs = False
    byte3_bit5 = False
    cant_walk_through = False
    byte3_bit7 = False
    slidable_along_walls = False
    cant_move_if_in_air = False
    byte7_upper2 = 0

class Clone(BaseRoomObject):
    pass


class BattlePackNPC(RoomObject):
    type = ObjectType.BATTLE
    battle_pack = 0
    after_battle = PostBattle.REMOVE_PERMANENTLY

    def __init__(
        self,
        occupant,
        initiator=Initiator.NONE,
        after_battle=PostBattle.REMOVE_PERMANENTLY,
        battle_pack=0,
        action_script=0,
        speed=0,
        visible=False,
        x=0,
        y=0,
        z=0,
        z_half=False,
        direction=RadialDirection.SOUTHWEST,
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
        slidable_along_walls=False,
        cant_move_if_in_air=False,
        byte7_upper2=0,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=None,
        acute_axis=None,
        obtuse_axis=None,
        height=None,
        directions=None,
        vram_size=None,
        cannot_clone=False,
        byte2_bit0=None,
        byte2_bit1=None,
        byte2_bit2=None,
        byte2_bit3=None,
        byte2_bit4=None,
        byte5_bit6=None,
        byte5_bit7=None,
        byte6_bit2=None,
        y_shift=None,
    ):
        self.self = self
        self.initiator = initiator
        self.after_battle = after_battle
        self.battle_pack = battle_pack
        self.action_script = action_script
        self.speed = speed
        self.x = x
        self.y = y
        self.z = z
        self.z_half = z_half
        self.direction = direction
        self.face_on_trigger = face_on_trigger
        self.cant_enter_doors = cant_enter_doors
        self.byte2_bit5 = byte2_bit5
        self.set_sequence_playback = set_sequence_playback
        self.cant_float = cant_float
        self.cant_walk_up_stairs = cant_walk_up_stairs
        self.cant_walk_under = cant_walk_under
        self.cant_pass_walls = cant_pass_walls
        self.cant_jump_through = cant_jump_through
        self.cant_pass_npcs = cant_pass_npcs
        self.byte3_bit5 = byte3_bit5
        self.cant_walk_through = cant_walk_through
        self.byte3_bit7 = byte3_bit7
        self.slidable_along_walls = slidable_along_walls
        self.cant_move_if_in_air = cant_move_if_in_air
        self.byte7_upper2 = byte7_upper2
        self.model = npcs.AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
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


class RegularNPC(RoomObject):
    type = ObjectType.OBJECT
    event_script = 256

    def __init__(
        self,
        occupant,
        initiator=Initiator.NONE,
        event_script=256,
        action_script=0,
        speed=0,
        visible=False,
        x=0,
        y=0,
        z=0,
        z_half=False,
        direction=RadialDirection.SOUTHWEST,
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
        slidable_along_walls=False,
        cant_move_if_in_air=False,
        byte7_upper2=0,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=None,
        acute_axis=None,
        obtuse_axis=None,
        height=None,
        directions=None,
        vram_size=None,
        cannot_clone=False,
        byte2_bit0=None,
        byte2_bit1=None,
        byte2_bit2=None,
        byte2_bit3=None,
        byte2_bit4=None,
        byte5_bit6=None,
        byte5_bit7=None,
        byte6_bit2=None,
        y_shift=None,
    ):
        self.self = self
        self.initiator = initiator
        self.event_script = event_script
        self.action_script = action_script
        self.speed = speed
        self.visible = visible
        self.x = x
        self.y = y
        self.z = z
        self.z_half = z_half
        self.direction = direction
        self.face_on_trigger = face_on_trigger
        self.cant_enter_doors = cant_enter_doors
        self.byte2_bit5 = byte2_bit5
        self.set_sequence_playback = set_sequence_playback
        self.cant_float = cant_float
        self.cant_walk_up_stairs = cant_walk_up_stairs
        self.cant_walk_under = cant_walk_under
        self.cant_pass_walls = cant_pass_walls
        self.cant_jump_through = cant_jump_through
        self.cant_pass_npcs = cant_pass_npcs
        self.byte3_bit5 = byte3_bit5
        self.cant_walk_through = cant_walk_through
        self.byte3_bit7 = byte3_bit7
        self.slidable_along_walls = slidable_along_walls
        self.cant_move_if_in_air = cant_move_if_in_air
        self.byte7_upper2 = byte7_upper2
        self.model = npcs.AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
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


class ChestNPC(RoomObject):
    type = ObjectType.CHEST
    event_script = 256
    lower_70A7 = 0
    upper_70A7 = 0

    def __init__(
        self,
        occupant,
        initiator=Initiator.NONE,
        event_script=256,
        action_script=0,
        lower_70A7=0,
        upper_70A7=0,
        speed=0,
        visible=False,
        x=0,
        y=0,
        z=0,
        z_half=False,
        direction=RadialDirection.SOUTHWEST,
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
        slidable_along_walls=False,
        cant_move_if_in_air=False,
        byte7_upper2=0,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=None,
        acute_axis=None,
        obtuse_axis=None,
        height=None,
        directions=None,
        vram_size=None,
        cannot_clone=False,
        byte2_bit0=None,
        byte2_bit1=None,
        byte2_bit2=None,
        byte2_bit3=None,
        byte2_bit4=None,
        byte5_bit6=None,
        byte5_bit7=None,
        byte6_bit2=None,
        y_shift=None,
    ):
        self.self = self
        self.initiator = initiator
        self.event_script = event_script
        self.action_script = action_script
        self.lower_70A7 = lower_70A7
        self.upper_70A7 = upper_70A7
        self.speed = speed
        self.visible = visible
        self.x = x
        self.y = y
        self.z = z
        self.z_half = z_half
        self.direction = direction
        self.face_on_trigger = face_on_trigger
        self.cant_enter_doors = cant_enter_doors
        self.byte2_bit5 = byte2_bit5
        self.set_sequence_playback = set_sequence_playback
        self.cant_float = cant_float
        self.cant_walk_up_stairs = cant_walk_up_stairs
        self.cant_walk_under = cant_walk_under
        self.cant_pass_walls = cant_pass_walls
        self.cant_jump_through = cant_jump_through
        self.cant_pass_npcs = cant_pass_npcs
        self.byte3_bit5 = byte3_bit5
        self.cant_walk_through = cant_walk_through
        self.byte3_bit7 = byte3_bit7
        self.slidable_along_walls = slidable_along_walls
        self.cant_move_if_in_air = cant_move_if_in_air
        self.byte7_upper2 = byte7_upper2
        self.model = npcs.AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
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


class BattlePackClone(Clone):
    type = ObjectType.BATTLE
    battle_pack = 0

    def __init__(
        self,
        occupant,
        battle_pack=0,
        action_script=0,
        visible=False,
        x=0,
        y=0,
        z=0,
        z_half=False,
        direction=RadialDirection.SOUTHWEST,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=None,
        y_shift=None,
        acute_axis=None,
        obtuse_axis=None,
        height=None,
        directions=None,
        vram_size=None,
        cannot_clone=False,
        byte2_bit0=None,
        byte2_bit1=None,
        byte2_bit2=None,
        byte2_bit3=None,
        byte2_bit4=None,
        byte5_bit6=None,
        byte5_bit7=None,
        byte6_bit2=None,
    ):
        self.self = self
        self.battle_pack = battle_pack
        self.action_script = action_script
        self.visible = visible
        self.x = x
        self.y = y
        self.z = z
        self.z_half = z_half
        self.direction = direction
        self.model = npcs.AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
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


class RegularClone(Clone):
    type = ObjectType.OBJECT
    event_script = 256

    def __init__(
        self,
        occupant,
        event_script=256,
        action_script=0,
        visible=False,
        x=0,
        y=0,
        z=0,
        z_half=False,
        direction=RadialDirection.SOUTHWEST,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=None,
        y_shift=None,
        acute_axis=None,
        obtuse_axis=None,
        height=None,
        directions=None,
        vram_size=None,
        cannot_clone=False,
        byte2_bit0=None,
        byte2_bit1=None,
        byte2_bit2=None,
        byte2_bit3=None,
        byte2_bit4=None,
        byte5_bit6=None,
        byte5_bit7=None,
        byte6_bit2=None,
    ):
        self.self = self
        self.event_script = event_script
        self.action_script = action_script
        self.visible = visible
        self.x = x
        self.y = y
        self.z = z
        self.z_half = z_half
        self.direction = direction
        self.model = npcs.AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
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


class ChestClone(Clone):
    type = ObjectType.CHEST
    lower_70A7 = 0
    upper_70A7 = 0

    def __init__(
        self,
        occupant,
        lower_70A7=0,
        upper_70A7=0,
        visible=False,
        x=0,
        y=0,
        z=0,
        z_half=False,
        direction=RadialDirection.SOUTHWEST,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=None,
        y_shift=None,
        acute_axis=None,
        obtuse_axis=None,
        height=None,
        directions=None,
        vram_size=None,
        cannot_clone=False,
        byte2_bit0=None,
        byte2_bit1=None,
        byte2_bit2=None,
        byte2_bit3=None,
        byte2_bit4=None,
        byte5_bit6=None,
        byte5_bit7=None,
        byte6_bit2=None,
    ):
        self.self = self
        self.lower_70A7 = lower_70A7
        self.upper_70A7 = upper_70A7
        self.visible = visible
        self.x = x
        self.y = y
        self.z = z
        self.z_half = z_half
        self.direction = direction
        self.model = npcs.AreaNPC(
            occupant,
            priority_0,
            priority_1,
            priority_2,
            show_shadow,
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


class Room:
    partition = Partition()
    music = Music._00_CURRENT
    entrance_event = 15
    event_tiles = []
    exit_fields = []
    objects = []

    def __init__(
        self,
        partition=Partition(),
        music=Music._00_CURRENT,
        entrance_event=15,
        event_tiles=[],
        exit_fields=[],
        objects=[],
    ):
        self.partition = partition
        self.music = music
        self.entrance_event = entrance_event
        self.event_tiles = event_tiles
        self.exit_fields = exit_fields
        self.objects = objects
