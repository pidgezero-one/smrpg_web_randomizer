"""NPC container classes which standardize the sprite IDs, vram properties, and other
related behaviours for each character than can occupy a placeholder.
These classes will be used to define the NPC table in each room,
the overall NPC table for the seed, and the VRAM partition table for the seed."""


from math import ceil
from typing import List, Optional, Type

from randomizer.types.numbers.classes import Int8, UInt16, UInt4, UInt8

from randomizer.types.npcs.objects.animations.types import SpriteAnimationCollection
from randomizer.types.overworld_scripts.action_scripts.commands import (
    SetSpriteSequence,
)
from randomizer.types.overworld_scripts.event_scripts.commands.types import (
    ActionSubcriptCommandPrototype,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    TOTAL_SCRIPTS,
    E0883_CHEST_ITEM_BAG_PACKET,
)
from randomizer.types.overworld_scripts.arguments.types import Packet
from randomizer.types.overworld_scripts.arguments import (
    P005_BRIEF_POOF_BAG,
    P037_ITEM_BAG_FALL,
    P090_BAG_STATIC,
)
from randomizer.types.palettes import Palette
from randomizer.types.scripts_common import ScriptCommandT
from randomizer.types.sprites.ids import TOTAL_SPRITES, SPR1023_EMPTY
from randomizer.types.world.classes import GameWorld

from randomizer.types.npcs.objects import ShadowSize, VramStore
from randomizer.types.npcs.objects.animations import (
    BIRD_ATTACK,
    CROCO_BAG_HIT,
    CROCO_BAG_LOOP,
    CROCO_BAG_SUMMON,
    CROCO_RECOIL,
    FIREBALL_SPIN,
    FIREBALL_SPIN_FAST,
    HAMMER_HIT,
    JINX_PUNCH,
    JINX_RECOIL,
    SHOVELKNIGHT_ALT_TAUNT,
    SHOVELKNIGHT_ATTACK,
    SHOVELKNIGHT_RECOIL,
    SHOVELKNIGHT_TAUNT,
    SHOVELKNIGHT_TILE,
    SMALL_MAGIKOOPA_HIT,
)


class StatueDetails:
    """A collection of properties specifying minor adjustments to make
    to the statue sprite before the room loads."""

    _mold: UInt8
    _horizontal_pixel_shift: Int8
    _vertical_pixel_shift: Int8
    _north_facing_horizontal_pixel_shift: Int8
    _north_facing_vertical_pixel_shift: Int8

    @property
    def mold(self) -> UInt8:
        """The mold of the sequence sprite to be loaded in the room's sequence setter."""
        return self._mold

    def set_mold(self, mold: int) -> None:
        """Specify the mold of the sequence sprite to be loaded in the room's sequence setter."""
        self._mold = UInt8(mold)

    @property
    def horizontal_pixel_shift(self) -> Int8:
        """The X distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift left, positive numbers shift right.
        This only applies when the status is facing southwest or southeast."""
        return self._horizontal_pixel_shift

    def set_horizontal_pixel_shift(self, horizontal_pixel_shift: int) -> None:
        """Set the X distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift left, positive numbers shift right.
        This only applies when the status is facing southwest or southeast."""
        self._horizontal_pixel_shift = Int8(horizontal_pixel_shift)

    @property
    def vertical_pixel_shift(self) -> Int8:
        """The Y distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift down, positive numbers shift up.
        This only applies when the status is facing southwest or southeast."""
        return self._vertical_pixel_shift

    def set_vertical_pixel_shift(self, vertical_pixel_shift: int) -> None:
        """Set the Y distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift down, positive numbers shift up.
        This only applies when the status is facing southwest or southeast."""
        self._vertical_pixel_shift = Int8(vertical_pixel_shift)

    @property
    def north_facing_horizontal_pixel_shift(self) -> Int8:
        """The X distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift left, positive numbers shift right.
        This only applies when the status is facing northwest or northeast."""
        return self._north_facing_horizontal_pixel_shift

    def set_north_facing_horizontal_pixel_shift(
        self, north_facing_horizontal_pixel_shift: int
    ) -> None:
        """Set the X distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift left, positive numbers shift right.
        This only applies when the status is facing northwest or northeast."""
        self._north_facing_horizontal_pixel_shift = Int8(
            north_facing_horizontal_pixel_shift
        )

    @property
    def north_facing_vertical_pixel_shift(self) -> Int8:
        """The Y distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift down, positive numbers shift up.
        This only applies when the status is facing northwest or northeast."""
        return self._north_facing_vertical_pixel_shift

    def set_north_facing_vertical_pixel_shift(
        self, north_facing_vertical_pixel_shift: int
    ) -> None:
        """Set the Y distance, in pixels, to shift the statue in the room's sequence setter.
        Negative numbers shift down, positive numbers shift up.
        This only applies when the status is facing northwest or northeast."""
        self._north_facing_vertical_pixel_shift = Int8(
            north_facing_vertical_pixel_shift
        )

    def __init__(
        self,
        mold: int = 0,
        horizontal_pixel_shift: int = 0,
        vertical_pixel_shift: int = 0,
        north_facing_horizontal_pixel_shift: int = 0,
        north_facing_vertical_pixel_shift: int = 0,
    ):
        self.set_mold(mold)
        self.set_horizontal_pixel_shift(horizontal_pixel_shift)
        self.set_vertical_pixel_shift(vertical_pixel_shift)
        self.set_north_facing_horizontal_pixel_shift(
            north_facing_horizontal_pixel_shift
        )
        self.set_north_facing_vertical_pixel_shift(north_facing_vertical_pixel_shift)


class NPC:
    """Base class for any object that can occupy an NPC placeholder.
    These properties are generally for things that should always be true
    about a given character, such as their collision height, shadow size,
    vram size, etc. Some of these properties can be overridden according
    to the needs of a specific room, so they are not 100% absolute."""

    _sprite_id: UInt16 = UInt16(SPR1023_EMPTY)
    _show_shadow: bool
    _shadow_size = ShadowSize.OVAL_MED
    _acute_axis: UInt4 = UInt4(1)
    _obtuse_axis: UInt4 = UInt4(1)
    _height: UInt8 = UInt8(1)
    _y_shift: Int8 = Int8(0)
    _directions = VramStore.DIR2_SWSE
    _min_vram_size: UInt4 = UInt4(0)
    _byte2_bit0: bool
    _byte2_bit1: bool
    _byte2_bit2: bool
    _byte2_bit3: bool
    _byte2_bit4: bool
    _byte5_bit6: bool
    _byte5_bit7: bool
    _byte6_bit2: bool

    _crown: UInt8 = UInt8(2)

    _animations = SpriteAnimationCollection()
    _eye_height: UInt8 = UInt8(17)
    _tower_entrance_horizontal_shift: UInt4 = UInt4(0)
    _alt_palette: Optional[Palette] = None

    _statue: Optional[StatueDetails] = None

    _world: Optional[GameWorld]

    @property
    def world(self) -> GameWorld:
        """Game world reference"""
        assert self._world is not None
        return self._world

    @property
    def sprite_id(self) -> UInt16:
        """The ID of the sprite that will be loaded into the room for this NPC.\n
        It is recommended to use sprite constant names for this."""
        assert self._sprite_id <= TOTAL_SPRITES
        return UInt16(self._sprite_id)

    @property
    def show_shadow(self) -> bool:
        """If false, a shadow for the NPC when airborne will not be loaded to VRAM."""
        return self._show_shadow

    @property
    def shadow_size(self) -> ShadowSize:
        """The size of the NPC's displayed shadow when airborne."""
        return self._shadow_size

    @property
    def acute_axis(self) -> UInt4:
        """The collision width of this NPC.
        If projected onto a flat plane, this axis would run top right to bottom left."""
        return UInt4(self._acute_axis)

    @property
    def obtuse_axis(self) -> UInt4:
        """The collision length of this NPC.
        If projected onto a flat plane, this axis would run top left to bottom right."""
        return UInt4(self._obtuse_axis)

    @property
    def height(self) -> UInt8:
        """The collision height of this NPC."""
        assert self._height <= 31
        return UInt8(self._height)

    @property
    def y_shift(self) -> Int8:
        """The distance in pixels (from -16 to +15) to shift the sprite up or down
        as displayed, without also moving its collision box."""
        assert -16 <= self.y_shift <= 15
        return Int8(self._y_shift)

    @property
    def directions(self) -> VramStore:
        """The directions which the NPC can be expected to face."""
        return self._directions

    @property
    def min_vram_size(self) -> UInt4:
        """The minimum number (0 to 7) of VRAM chunks the NPC's sprite can be expected to require.\n
        Generally, this number is 0 for gridplane sprites. \n
        For non-gridplane sprites, this number is usually total tiles divided by 4,
        rounded down (where a tile is a group of four subtiles).\n
        This calculation should be based on the largest mold (in terms of tiles used)
        that you expect to see displayed from the sprite."""
        assert self._min_vram_size <= 7
        return UInt4(self._min_vram_size)

    def min_vram_from_mold(self, mold_id: int, offset: int = 0) -> int:
        """Get min vram size from a certain sprite mold ID"""
        assert self.world is not None
        sprite = self.world.sprites[self.sprite_id + offset]
        assert mold_id < len(sprite.animation_data.molds)
        tiles = sprite.animation_data.molds[mold_id].tiles
        return ceil(max(0, len(tiles) - 4) / 4)

    def min_vram_from_sequence(self, sequence_id: int, offset: int = 0) -> int:
        """Get min vram size from a certain sprite sequence ID"""
        assert self.world is not None
        sprite = self.world.sprites[self.sprite_id + offset]
        assert sequence_id < len(sprite.animation_data.sequences)
        min_vram = 0
        frames = sprite.animation_data.sequences[sequence_id].frames
        for frame in frames:
            min_vram = max(min_vram, self.min_vram_from_mold(frame.mold_id))
        return min_vram

    def _min_vram_size_from_script(self, script: List[ScriptCommandT]) -> int:
        min_vram = self.min_vram_from_mold(0)
        for cmd in script:
            if isinstance(cmd, SetSpriteSequence):
                prop_id = cmd.index
                offset = cmd.sprite_offset
                if cmd.is_mold:
                    min_vram = max(min_vram, self.min_vram_from_mold(prop_id, offset))
                else:
                    min_vram = max(
                        min_vram, self.min_vram_from_sequence(prop_id, offset)
                    )
        return min_vram

    def min_vram_from_action_script(self, script_id: int) -> int:
        """Get min vram size from a given action script"""
        assert self.world is not None
        script = self.world.action_scripts.scripts[script_id]
        return self._min_vram_size_from_script(script.contents)

    def min_vram_from_event_script(self, target: int, script_id: int) -> int:
        """Get min vram size from subscripts in a given event script"""
        assert self.world is not None
        min_vram = self.min_vram_from_mold(0)
        script = self.world.event_scripts.get_script_by_id(script_id)
        for cmd in script.contents:
            if isinstance(cmd, ActionSubcriptCommandPrototype) and cmd.target == target:
                min_vram = max(
                    min_vram, self._min_vram_size_from_script(cmd.subscript.contents)
                )
        return min_vram

    @property
    def byte2_bit0(self) -> bool:
        """(unknown)"""
        return self._byte2_bit0

    @property
    def byte2_bit1(self) -> bool:
        """(unknown)"""
        return self._byte2_bit1

    @property
    def byte2_bit2(self) -> bool:
        """(unknown)"""
        return self._byte2_bit2

    @property
    def byte2_bit3(self) -> bool:
        """(unknown)"""
        return self._byte2_bit3

    @property
    def byte2_bit4(self) -> bool:
        """(unknown)"""
        return self._byte2_bit4

    @property
    def byte5_bit6(self) -> bool:
        """(unknown)"""
        return self._byte5_bit6

    @property
    def byte5_bit7(self) -> bool:
        """(unknown)"""
        return self._byte5_bit7

    @property
    def byte6_bit2(self) -> bool:
        """(unknown)"""
        return self._byte6_bit2

    @property
    def crown(self) -> UInt8:
        """If this NPC is the first Tower boss, this value is the height
        at which the dropped wedding gear should sit when it lands on the NPC's head
        in the Marrymore chapel."""
        return UInt8(self._crown)

    @property
    def animations(self) -> SpriteAnimationCollection:
        """The animations that should be performed by this NPC in specific contexts."""
        return self._animations

    @property
    def eye_height(self) -> UInt8:
        """A pixel value representing the height of the NPC's eyes
        relative to the bottom of the sprite.\n
        This is used to calculate the distance
        to shift the sprite in order to show it peering out the tower front door."""
        return UInt8(self._eye_height)

    @property
    def tower_entrance_horizontal_shift(self) -> UInt4:
        """If the NPC's eyes are shifted too far left when peering out the tower door,
        use this pixel value to shift the NPC rightward as needed."""
        return UInt4(self._tower_entrance_horizontal_shift)

    @property
    def alt_palette(self) -> Optional[Palette]:
        """An alternate palette to be used by this NPC's sprite, if the player has
        selected the flag to distinguish similar bosses in the overworld."""
        return self._alt_palette

    @property
    def statue(self) -> Optional[StatueDetails]:
        """A collection of properties specifying minor adjustments to make
        to the statue sprite before the room loads, if this is a statue."""
        return self._statue

    def is_equal(self, npc: "NPC") -> bool:
        """True if this NPC's properties are all equal to another NPC's."""
        return (
            self.sprite_id == npc.sprite_id
            and self.show_shadow == npc.show_shadow
            and self.shadow_size == npc.shadow_size
            and self.acute_axis == npc.acute_axis
            and self.obtuse_axis == npc.obtuse_axis
            and self.height == npc.height
            and self.directions == npc.directions
            and self.min_vram_size == npc.min_vram_size
            and self.byte2_bit0 == npc.byte2_bit0
            and self.byte2_bit1 == npc.byte2_bit1
            and self.byte2_bit2 == npc.byte2_bit2
            and self.byte2_bit3 == npc.byte2_bit3
            and self.byte2_bit4 == npc.byte2_bit4
            and self.byte5_bit6 == npc.byte5_bit6
            and self.byte5_bit7 == npc.byte5_bit7
            and self.byte6_bit2 == npc.byte6_bit2
        )

    def __init__(self, world: Optional[GameWorld] = None):
        self._world = world


class Statue(NPC):
    """Base class for a statue NPC."""

    details = StatueDetails()


class ItemNPC(NPC):
    """Base class for an NPC object representing an obtainable item."""

    _chest_packet: Packet = P005_BRIEF_POOF_BAG
    _chest_event: int = E0883_CHEST_ITEM_BAG_PACKET
    _static_packet: Packet = P037_ITEM_BAG_FALL
    _falling_packet: Packet = P090_BAG_STATIC
    _shadow_size: ShadowSize = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _height: int = 7
    _chest_70a7_upper: int = 0
    _hover: bool = False

    @property
    def chest_packet(self) -> Packet:
        """The packet to show popping out of a chest that grants this item."""
        return self._chest_packet

    @property
    def chest_event(self) -> UInt16:
        """The event to run that grants this item when obtained from a chest."""
        assert self._chest_event < TOTAL_SCRIPTS
        return UInt16(self._chest_event)

    @property
    def static_packet(self) -> Packet:
        """The packet to use for this item when it is lying on a surface and
        doesn't move."""
        return self._static_packet

    @property
    def falling_packet(self) -> Packet:
        """The packet to use for this item when it falls from the top of the screen,
        such as when awarded by a Sunken Ship minigame."""
        return self._falling_packet

    @property
    def shadow_size(self) -> ShadowSize:
        """The size of the shadow for this item when it is airborne.\n
        Note that this only applies if the item is actually filling a NPC placeholder,
        since generated packets do not have shadows."""
        return self._shadow_size

    @property
    def show_shadow(self) -> bool:
        """If false, a shadow for the NPC when airborne will not be loaded to VRAM.\n
        Note that this only applies if the item is actually filling a NPC placeholder,
        since generated packets do not have shadows."""
        return self._show_shadow

    @property
    def height(self) -> UInt4:
        """The collision height of this NPC."""
        return UInt4(self._height)

    @property
    def chest_70a7_upper(self) -> UInt4:
        """The upper four bits to be written to a chest that grants this item."""
        return UInt4(self._chest_70a7_upper)

    @property
    def hover(self) -> bool:
        """If true, the item will appear as slightly hovering above the surface it rests on.
        This will show its shadow.\n
        Note that this only applies if the item is actually filling a NPC placeholder,
        this property cannot apply to static packets."""
        return self._hover


class PartyNPC(NPC):
    """Base class representing a recruitable character in the overworld."""

    _minecart_shift: int = 0

    @property
    def minecart_shift(self) -> UInt4:
        """The pixel distance to shift this sprite to the right
        when this character is placed on top of the Moleville minecart
        during recruitment.\n
        The character who rides the back of the minecart uses their Yoshi-riding sprite in
        this scene, which is specially cropped to accommodate for layer
        priority clashes with Yoshies. This cropping looks awkward when
        riding the minecart in the overworld, so the recruited character
        can be shifted backward to cover up the awkward cropping.."""
        return UInt4(self._minecart_shift)

    def __init__(self, world, sprite_id: int):
        super().__init__(world)
        assert 0 <= sprite_id <= TOTAL_SPRITES
        self._sprite_id = UInt16(sprite_id)

        if sprite_id >= 7:
            self._directions = VramStore.DIR0_SWSE_NWNE
        else:
            self._directions = VramStore.DIR7_ALL_DIRECTIONS


class MimicFace(NPC):
    """Base class representing the circular monster face that normally appears
    when you open a mimic chest. In randomizer, these are unique NPCs used to
    represent Pandorite, Hidon, Box Boy, and Chester in contexts when their full
    sprite cannot be loaded."""

    _shadow_size: ShadowSize = ShadowSize.OVAL_SMALL
    _acute_axis: int = 3
    _obtuse_axis: int = 3
    _height: int = 3

    _eye_height: int = 4

    _crown: int = 1


class AreaNPC:
    """Base class representing an NPC placeholder in a room, to be filled by one specific NPC.
    This class is responsible for attributes that may vary from room to room,
    such as how the NPC should be allowed to interact with its environment. \n
    This class also allows you to override some properties of the NPC, such as the shadow,
    Y shift, collision axes, etc.\n
    Not to be confused with ModelFill classes, which are specialized placeholders
    used in boss shuffling, which determine how some AreaNPCs are filled based on the results
    of the boss shuffle."""

    _occupant: Type[NPC]
    _priority_0: bool = False
    _priority_1: bool = False
    _priority_2: bool = True
    _show_shadow: Optional[bool] = None
    _shadow_size: Optional[ShadowSize] = None
    _acute_axis: Optional[int] = None
    _obtuse_axis: Optional[int] = None
    _height: Optional[int] = None
    _y_shift: Optional[int] = None
    _directions: Optional[VramStore] = None
    _vram_size: Optional[int] = None
    _cannot_clone: bool = False
    _byte2_bit0: Optional[bool] = None
    _byte2_bit1: Optional[bool] = None
    _byte2_bit2: Optional[bool] = None
    _byte2_bit3: Optional[bool] = None
    _byte2_bit4: Optional[bool] = None
    _byte5_bit6: Optional[bool] = None
    _byte5_bit7: Optional[bool] = None
    _byte6_bit2: Optional[bool] = None

    @property
    def occupant(self) -> Type[NPC]:
        """The NPC occupying this position in the room."""
        return self._occupant

    def set_occupant(self, occupant: Type[NPC]) -> None:
        """Set the NPC occupying this position in the room."""
        self._occupant = occupant

    @property
    def priority_0(self) -> bool:
        """(unknown exactly how these layers work)"""
        return self._priority_0

    def set_priority_0(self, priority_0: bool) -> None:
        """(unknown exactly how these layers work)"""
        self._priority_0 = priority_0

    @property
    def priority_1(self) -> bool:
        """(unknown exactly how these layers work)"""
        return self._priority_1

    def set_priority_1(self, priority_1: bool) -> None:
        """(unknown exactly how these layers work)"""
        self._priority_1 = priority_1

    @property
    def priority_2(self) -> bool:
        """(unknown exactly how these layers work)"""
        return self._priority_2

    def set_priority_2(self, priority_2: bool) -> None:
        """(unknown exactly how these layers work)"""
        self._priority_2 = priority_2

    @property
    def show_shadow(self) -> bool:
        """If false, a shadow for the NPC when airborne will not be loaded to VRAM."""
        if self._show_shadow is None:
            return self.occupant().show_shadow
        return self._show_shadow

    def set_show_shadow(self, show_shadow: Optional[bool] = None) -> None:
        """If false, a shadow for the NPC when airborne will not be loaded to VRAM.\n
        This overrides the show_shadow property of the occupant NPC. This behaviour can be
        reversed by setting this to None."""
        self._show_shadow = show_shadow

    @property
    def shadow_size(self) -> ShadowSize:
        """The size of the shadow for this NPC when it is airborne."""
        if self._shadow_size is None:
            return self.occupant().shadow_size
        return self._shadow_size

    def set_shadow_size(self, shadow_size: Optional[ShadowSize] = None) -> None:
        """The size of the shadow for this NPC when it is airborne.\n
        This overrides the shadow_size property of the occupant NPC. This behaviour can be
        reversed by setting this to None."""
        self._shadow_size = shadow_size

    @property
    def acute_axis(self) -> UInt4:
        """The collision width of this NPC.
        If projected onto a flat plane, this axis would run top right to bottom left."""
        if self._acute_axis is None:
            return self.occupant().acute_axis
        return UInt4(self._acute_axis)

    def set_acute_axis(self, acute_axis: Optional[int] = None) -> None:
        """The collision width of this NPC.
        If projected onto a flat plane, this axis would run top right to bottom left.\n
        This overrides the acute_axis property of the occupant NPC. This behaviour can be
        reversed by setting this to None."""
        if acute_axis is None:
            self._acute_axis = None
            return
        assert UInt4(acute_axis)
        self._acute_axis = acute_axis

    @property
    def obtuse_axis(self) -> UInt4:
        """The collision length of this NPC.
        If projected onto a flat plane, this axis would run top left to bottom right."""
        if self._obtuse_axis is None:
            return self.occupant().obtuse_axis
        return UInt4(self._obtuse_axis)

    def set_obtuse_axis(self, obtuse_axis: Optional[int] = None) -> None:
        """The collision length of this NPC.
        If projected onto a flat plane, this axis would run top left to bottom right.\n
        This overrides the obtuse_axis property of the occupant NPC. This behaviour can be
        reversed by setting this to None."""
        if obtuse_axis is None:
            self._obtuse_axis = None
            return
        assert UInt4(obtuse_axis)
        self._obtuse_axis = obtuse_axis

    @property
    def height(self) -> UInt8:
        """The collision height of this NPC."""
        if self._height is None:
            return self.occupant().height
        assert self._height <= 31
        return UInt8(self._height)

    def set_height(self, height: Optional[int] = None) -> None:
        """The collision height of this NPC.\n
        This overrides the height property of the occupant NPC. This behaviour can be
        reversed by setting this to None."""
        if height is None:
            self._height = None
            return
        assert 0 <= height <= 31
        self._height = height

    @property
    def y_shift(self) -> Int8:
        """The distance in pixels (from -16 to +15) to shift the sprite up or down
        as displayed, without also moving its collision box."""
        if self._y_shift is None:
            return self.occupant().y_shift
        assert -16 <= self.y_shift <= 15
        return Int8(self._y_shift)

    def set_y_shift(self, y_shift: Optional[int] = None) -> None:
        """The distance in pixels (from -16 to +15) to shift the sprite up or down
        as displayed, without also moving its collision box.\n
        This overrides the y_shift property of the occupant NPC. This behaviour can be
        reversed by setting this to None."""
        if y_shift is None:
            self._y_shift = None
            return
        assert -16 <= y_shift <= 15
        self._y_shift = y_shift

    @property
    def directions(self) -> VramStore:
        """The directions which the NPC can be expected to face."""
        if self._directions is None:
            return self.occupant().directions
        return self._directions

    def set_directions(self, directions: Optional[VramStore] = None) -> None:
        """The directions which the NPC can be expected to face.\n
        This overrides the directions property of the occupant NPC. This behaviour can be
        reversed by setting this to None."""
        self._directions = directions

    @property
    def vram_size(self) -> UInt4:
        """The number (0 to 7) of VRAM chunks the NPC's sprite can be expected to require."""
        if self._vram_size is None:
            return self.occupant().min_vram_size
        assert self._vram_size <= 7
        return UInt4(self._vram_size)

    def set_vram_size(self, vram_size: Optional[int] = None) -> None:
        """The number (0 to 7) of VRAM chunks the NPC's sprite can be expected to require.\n
        If not set, this uses the NPC's min_vram_size property."""
        if vram_size is None:
            self._vram_size = None
            return
        assert 0 <= vram_size <= 7
        self._vram_size = vram_size

    @property
    def cannot_clone(self) -> bool:
        """If true, the NPC will be written to the NPC table with the
        Cannot Clone bit, which has specific implications on how the
        NPC is loaded into vram. (full scope unknown)"""
        return self._cannot_clone

    def set_cannot_clone(self, cannot_clone: bool) -> None:
        """If true, the NPC will be written to the NPC table with the
        Cannot Clone bit, which has specific implications on how the
        NPC is loaded into vram. (full scope unknown)"""
        self._cannot_clone = cannot_clone

    @property
    def byte2_bit0(self) -> bool:
        """(unknown)"""
        if self._byte2_bit0 is None:
            return self.occupant().byte2_bit0
        return self._byte2_bit0

    def set_byte2_bit0(self, byte2_bit0: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte2_bit0 = byte2_bit0

    @property
    def byte2_bit1(self) -> bool:
        """(unknown)"""
        if self._byte2_bit1 is None:
            return self.occupant().byte2_bit1
        return self._byte2_bit1

    def set_byte2_bit1(self, byte2_bit1: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte2_bit1 = byte2_bit1

    @property
    def byte2_bit2(self) -> bool:
        """(unknown)"""
        if self._byte2_bit2 is None:
            return self.occupant().byte2_bit2
        return self._byte2_bit2

    def set_byte2_bit2(self, byte2_bit2: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte2_bit2 = byte2_bit2

    @property
    def byte2_bit3(self) -> bool:
        """(unknown)"""
        if self._byte2_bit3 is None:
            return self.occupant().byte2_bit3
        return self._byte2_bit3

    def set_byte2_bit3(self, byte2_bit3: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte2_bit3 = byte2_bit3

    @property
    def byte2_bit4(self) -> bool:
        """(unknown)"""
        if self._byte2_bit4 is None:
            return self.occupant().byte2_bit4
        return self._byte2_bit4

    def set_byte2_bit4(self, byte2_bit4: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte2_bit4 = byte2_bit4

    @property
    def byte5_bit6(self) -> bool:
        """(unknown)"""
        if self._byte5_bit6 is None:
            return self.occupant().byte5_bit6
        return self._byte5_bit6

    def set_byte5_bit6(self, byte5_bit6: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte5_bit6 = byte5_bit6

    @property
    def byte5_bit7(self) -> bool:
        """(unknown)"""
        if self._byte5_bit7 is None:
            return self.occupant().byte5_bit7
        return self._byte5_bit7

    def set_byte5_bit7(self, byte5_bit7: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte5_bit7 = byte5_bit7

    @property
    def byte6_bit2(self) -> bool:
        """(unknown)"""
        if self._byte6_bit2 is None:
            return self.occupant().byte6_bit2
        return self._byte6_bit2

    def set_byte6_bit2(self, byte6_bit2: Optional[bool] = None) -> None:
        """(unknown)"""
        self._byte6_bit2 = byte6_bit2

    def is_equal(self, npc: "AreaNPC") -> bool:
        """True if this NPC's properties are all equal to another NPC's."""
        return (
            self.occupant.sprite_id == npc.occupant.sprite_id
            and (
                (not self.show_shadow and not npc.show_shadow)
                or (
                    self.show_shadow
                    and npc.show_shadow
                    and self.occupant.shadow_size == npc.shadow_size
                )
            )
            and self.priority_0 == npc.priority_0
            and self.priority_1 == npc.priority_1
            and self.priority_2 == npc.priority_2
            and self.occupant.y_shift == npc.occupant.y_shift
            and self.acute_axis == npc.acute_axis
            and self.obtuse_axis == npc.obtuse_axis
            and self.height == npc.height
            and self.directions == npc.directions
            and self.vram_size == npc.vram_size
            and self.cannot_clone == npc.cannot_clone
            and self.occupant.sprite_id == npc.occupant.sprite_id
            and self.occupant.byte2_bit0 == npc.occupant.byte2_bit0
            and self.occupant.byte2_bit1 == npc.occupant.byte2_bit1
            and self.occupant.byte2_bit2 == npc.occupant.byte2_bit2
            and self.occupant.byte2_bit3 == npc.occupant.byte2_bit3
            and self.occupant.byte2_bit4 == npc.occupant.byte2_bit4
            and self.occupant.byte5_bit6 == npc.occupant.byte5_bit6
            and self.occupant.byte5_bit7 == npc.occupant.byte5_bit7
            and self.occupant.byte6_bit2 == npc.occupant.byte6_bit2
        )

    def __init__(
        self,
        occupant: Type[NPC],
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
        self.set_occupant(occupant)
        self.set_priority_0(priority_0)
        self.set_priority_1(priority_1)
        self.set_priority_2(priority_2)
        self.set_show_shadow(show_shadow)
        self.set_shadow_size(shadow_size)
        self.set_y_shift(y_shift)
        self.set_acute_axis(acute_axis)
        self.set_obtuse_axis(obtuse_axis)
        self.set_height(height)
        self.set_directions(directions)
        self.set_vram_size(vram_size)
        self.set_cannot_clone(cannot_clone)
        self.set_byte2_bit0(byte2_bit0)
        self.set_byte2_bit1(byte2_bit1)
        self.set_byte2_bit2(byte2_bit2)
        self.set_byte2_bit3(byte2_bit3)
        self.set_byte2_bit4(byte2_bit4)
        self.set_byte5_bit6(byte5_bit6)
        self.set_byte5_bit7(byte5_bit7)
        self.set_byte6_bit2(byte6_bit2)


class YoshiNPC(NPC):
    """Base NPC class for various Yoshis"""

    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1
    _y_shift: int = 3


class CrocoBase(NPC):
    """Base NPC class for both iterations of Croco"""

    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 10
    _y_shift: int = 2
    _directions = VramStore.DIR0_SWSE_NWNE
    _tower_entrance_horizontal_shift: int = 9

    _eye_height: int = 16
    _animations = SpriteAnimationCollection(
        recoil=CROCO_RECOIL,
        bandits_way_distracted=CROCO_BAG_LOOP,
        mines_punch=CROCO_BAG_HIT,
        chapel_laugh=CROCO_BAG_LOOP,
        dojo_challenge=CROCO_BAG_SUMMON,
        statue_flustered=CROCO_RECOIL,
        keep_challenge=CROCO_BAG_SUMMON,
        keep_summon=CROCO_BAG_HIT,
        chandelier_challenge=CROCO_BAG_SUMMON,
        endgame_challenge=CROCO_BAG_SUMMON,
    )


class SmallMagikoopa(NPC):
    """Base NPC class for both Magikoopa colours"""

    _directions = VramStore.DIR0_SWSE_NWNE
    _shadow_size = ShadowSize.OVAL_SMALL
    _height: int = 10
    _y_shift: int = 1

    _animations = SpriteAnimationCollection(
        mines_punch=SMALL_MAGIKOOPA_HIT,
        ship_beckon=SMALL_MAGIKOOPA_HIT,
        dojo_challenge=SMALL_MAGIKOOPA_HIT,
        # statue_peck=SMALL_MAGIKOOPA_HIT,
        keep_challenge=SMALL_MAGIKOOPA_HIT,
        keep_summon=SMALL_MAGIKOOPA_HIT,
        chandelier_challenge=SMALL_MAGIKOOPA_HIT,
        endgame_challenge=SMALL_MAGIKOOPA_HIT,
    )


class Villager(NPC):
    """Base NPC class for any town occupant"""

    _directions = VramStore.DIR0_SWSE_NWNE
    _byte5_bit7: bool = True


class SmallToad(Villager):
    """Base NPC class for any short toad"""

    _height: int = 7
    _y_shift: int = 2


class BigToad(Villager):
    """Base NPC class for any large toad"""

    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _y_shift: int = 1


class StarPiece(NPC):
    """Base NPC class for any star piece object"""

    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13
    _y_shift: int = 1


class Trampoline(NPC):
    """Base NPC class for warp trampolines"""

    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 10
    _min_vram_size: int = 1


class ShovelKnightBoss(NPC):
    """Base NPC class for early inner factory worker bosses, standard size"""

    _directions = VramStore.DIR0_SWSE_NWNE
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13

    _animations = SpriteAnimationCollection(
        bandits_way_distracted=SHOVELKNIGHT_TILE,
        chapel_laugh=SHOVELKNIGHT_TILE,
        ship_chair=SHOVELKNIGHT_TILE,
        dojo_challenge=SHOVELKNIGHT_TILE,
        keep_challenge=SHOVELKNIGHT_TILE,
        keep_summon=SHOVELKNIGHT_TILE,
        chandelier_challenge=SHOVELKNIGHT_TILE,
        endgame_challenge=SHOVELKNIGHT_TILE,
    )
    _eye_height: int = 10
    _statue = StatueDetails(
        horizontal_pixel_shift=-3,
        north_facing_horizontal_pixel_shift=-5,
    )


class Jinx(NPC):
    """Base NPC class for all Jinx iterations"""

    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 5
    _directions = VramStore.DIR0_SWSE_NWNE
    _shadow_size = ShadowSize.OVAL_SMALL

    _eye_height: int = 4
    _crown: int = 1
    _animations = SpriteAnimationCollection(
        recoil=JINX_RECOIL,
        mines_punch=JINX_PUNCH,
        ship_beckon=JINX_PUNCH,
        dojo_challenge=JINX_PUNCH,
        statue_intro=JINX_PUNCH,
        statue_peck=JINX_PUNCH,
        keep_challenge=JINX_PUNCH,
        keep_summon=JINX_PUNCH,
        chandelier_challenge=JINX_PUNCH,
        endgame_challenge=JINX_PUNCH,
    )


class Coin(ItemNPC):
    """Base NPC class for coins"""


class HammerNPC(NPC):
    """Base NPC class for standalone hammers"""

    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _y_shift: int = -1
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=HAMMER_HIT, kitchen_prep=HAMMER_HIT, factory_pierce=HAMMER_HIT
    )


class ValentinaBird(NPC):
    """Base NPC class for Nimbus birds"""

    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 10
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=BIRD_ATTACK, kitchen_prep=BIRD_ATTACK, factory_pierce=BIRD_ATTACK
    )


class Fireball(NPC):
    """Base NPC class for animate fireballs"""

    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 3

    _animations = SpriteAnimationCollection(
        tower_bullet=FIREBALL_SPIN,
        kitchen_prep=FIREBALL_SPIN,
        factory_pierce=FIREBALL_SPIN_FAST,
    )


class MimicLarge(NPC):
    """Base NPC class for full-sized mimic enemies"""

    _shadow_size = ShadowSize.BLOCK
    _y_shift: int = 3
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 12
    _min_vram_size: int = 1


class ShovelKnightBossLarge(NPC):
    """Base NPC class for early inner factory worker bosses, larger size"""

    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = -1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13
    _min_vram_size: int = 7

    _animations = SpriteAnimationCollection(
        mines_punch=SHOVELKNIGHT_ATTACK,
        statue_peck=SHOVELKNIGHT_ATTACK,
        statue_intro=SHOVELKNIGHT_ALT_TAUNT,
        statue_flustered=SHOVELKNIGHT_RECOIL,
        chandelier_challenge=SHOVELKNIGHT_TAUNT,
        endgame_challenge=SHOVELKNIGHT_TAUNT,
    )


class CloneNPC(NPC):
    """'Clones' in this context refer to the concept of NPC cloning within a level,
    where a clone re-uses several properties of the parent NPC and has sprite
    and event or battle pack information that falls within a certain range
    of the parent. This saves graphical memory within the room.\n
    In SMRPG rando, if we define one room NPC as a clone of another, the occupants
    of those NPC slots will be written close together in the global NPC table, and have their
    normal behavioural scripts proxied by empty container scripts whose IDs are close
    together."""

    _directions = VramStore.DIR0_SWSE_NWNE
    _byte5_bit6: bool = True
    _byte5_bit7: bool = True
    _byte6_bit2: bool = True
