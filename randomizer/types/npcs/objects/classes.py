from typing import Optional
from randomizer.types.npcs.animations.animations import (
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
from randomizer.types.npcs.animations.classes import SpriteAnimationCollection
from randomizer.types.numbers.classes import Int8, UInt16, UInt4, UInt8
from randomizer.types.npcs.objects.enums import ShadowSize, VramStore
from randomizer.types.overworld_scripts.event_scripts.constants.misc import (
    TOTAL_SCRIPTS,
)
from randomizer.types.overworld_scripts.event_scripts.constants.script_ids import (
    E0883_CHEST_ITEM_BAG_PACKET,
)
from randomizer.types.overworld_scripts.packets.classes import Packet
from randomizer.types.overworld_scripts.packets.packets import (
    P005_BRIEF_POOF_BAG,
    P037_ITEM_BAG_FALL,
    P090_BAG_STATIC,
)
from randomizer.types.palettes.classes import Palette
from randomizer.types.sprites.constants.misc import TOTAL_SPRITES
from randomizer.types.world.classes import GameWorld


class StatueDetails:
    _mold: UInt8
    _horizontal_pixel_shift: Int8
    _vertical_pixel_shift: Int8
    _north_facing_horizontal_pixel_shift: Int8
    _north_facing_vertical_pixel_shift: Int8

    @property
    def mold(self) -> UInt8:
        return self._mold

    def set_mold(self, mold: int) -> None:
        self._mold = UInt8(mold)

    @property
    def horizontal_pixel_shift(self) -> Int8:
        return self._horizontal_pixel_shift

    def set_horizontal_pixel_shift(self, horizontal_pixel_shift: int) -> None:
        self._horizontal_pixel_shift = Int8(horizontal_pixel_shift)

    @property
    def vertical_pixel_shift(self) -> Int8:
        return self._vertical_pixel_shift

    def set_vertical_pixel_shift(self, vertical_pixel_shift: int) -> None:
        self._vertical_pixel_shift = Int8(vertical_pixel_shift)

    @property
    def north_facing_horizontal_pixel_shift(self) -> Int8:
        return self._north_facing_horizontal_pixel_shift

    def set_north_facing_horizontal_pixel_shift(
        self, north_facing_horizontal_pixel_shift: int
    ) -> None:
        self._north_facing_horizontal_pixel_shift = Int8(
            north_facing_horizontal_pixel_shift
        )

    @property
    def north_facing_vertical_pixel_shift(self) -> Int8:
        return self._north_facing_vertical_pixel_shift

    def set_north_facing_vertical_pixel_shift(
        self, north_facing_vertical_pixel_shift: int
    ) -> None:
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
    _sprite_id: int = 0
    _show_shadow: bool
    _shadow_size = ShadowSize.OVAL_MED
    _acute_axis: int = 0
    _obtuse_axis: int = 0
    _height: int = 0
    _y_shift: int = 0
    _directions = VramStore.DIR2_SWSE
    _min_vram_size: int = 0
    _byte2_bit0: bool
    _byte2_bit1: bool
    _byte2_bit2: bool
    _byte2_bit3: bool
    _byte2_bit4: bool
    _byte5_bit6: bool
    _byte5_bit7: bool
    _byte6_bit2: bool

    _crown: int = 2

    _animations = SpriteAnimationCollection()
    _eye_height: int = 17
    _tower_entrance_horizontal_shift: int = 0
    _alt_palette: Optional[Palette] = None

    _statue: Optional[StatueDetails] = None

    _world: Optional[GameWorld]

    @property
    def world(self) -> GameWorld:
        assert self._world is not None
        return self._world

    @property
    def sprite_id(self) -> UInt16:
        assert self._sprite_id <= TOTAL_SPRITES
        return UInt16(self._sprite_id)

    @property
    def show_shadow(self) -> bool:
        return self._show_shadow

    @property
    def shadow_size(self) -> ShadowSize:
        return self._shadow_size

    @property
    def acute_axis(self) -> UInt4:
        return UInt4(self._acute_axis)

    @property
    def obtuse_axis(self) -> UInt4:
        return UInt4(self._obtuse_axis)

    @property
    def height(self) -> UInt8:
        assert self._height <= 31
        return UInt8(self._height)

    @property
    def y_shift(self) -> Int8:
        assert -16 <= self.y_shift <= 15
        return Int8(self._y_shift)

    @property
    def directions(self) -> VramStore:
        return self._directions

    @property
    def min_vram_size(self) -> UInt4:
        assert self._min_vram_size <= 7
        return UInt4(self._min_vram_size)

    @property
    def byte2_bit0(self) -> bool:
        return self._byte2_bit0

    @property
    def byte2_bit1(self) -> bool:
        return self._byte2_bit1

    @property
    def byte2_bit2(self) -> bool:
        return self._byte2_bit2

    @property
    def byte2_bit3(self) -> bool:
        return self._byte2_bit3

    @property
    def byte2_bit4(self) -> bool:
        return self._byte2_bit4

    @property
    def byte5_bit6(self) -> bool:
        return self._byte5_bit6

    @property
    def byte5_bit7(self) -> bool:
        return self._byte5_bit7

    @property
    def byte6_bit2(self) -> bool:
        return self._byte6_bit2

    @property
    def crown(self) -> UInt8:
        return UInt8(self._crown)

    @property
    def animations(self) -> SpriteAnimationCollection:
        return self._animations

    @property
    def eye_height(self) -> UInt8:
        return UInt8(self._eye_height)

    @property
    def tower_entrance_horizontal_shift(self) -> UInt4:
        return UInt4(self._tower_entrance_horizontal_shift)

    @property
    def alt_palette(self) -> Optional[Palette]:
        return self._alt_palette

    @property
    def statue(self) -> Optional[StatueDetails]:
        return self._statue

    def __init__(self, world: Optional[GameWorld] = None):
        self._world = world


class Statue(NPC):
    details = StatueDetails()


class ItemNPC(NPC):
    _chest_packet: Packet = P005_BRIEF_POOF_BAG
    _chest_event: int = E0883_CHEST_ITEM_BAG_PACKET
    _static_packet: Packet = P037_ITEM_BAG_FALL
    _falling_packet: Packet = P090_BAG_STATIC
    _shadow_size: ShadowSize = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _height: int = 7
    _chest_70A7_upper: int = 0
    _hover: bool = False

    @property
    def chest_packet(self) -> Packet:
        return self._chest_packet

    @property
    def chest_event(self) -> UInt16:
        assert self._chest_event < TOTAL_SCRIPTS
        return UInt16(self._chest_event)

    @property
    def static_packet(self) -> Packet:
        return self._static_packet

    @property
    def falling_packet(self) -> Packet:
        return self._falling_packet

    @property
    def shadow_size(self) -> ShadowSize:
        return self._shadow_size

    @property
    def show_shadow(self) -> bool:
        return self._show_shadow

    @property
    def height(self) -> UInt4:
        return UInt4(self._height)

    @property
    def chest_70A7_upper(self) -> UInt4:
        return UInt4(self._chest_70A7_upper)

    @property
    def hover(self) -> bool:
        return self._hover


class PartyNPC(NPC):
    _minecart_shift: int = 0

    @property
    def minecart_shift(self) -> UInt4:
        return UInt4(self._minecart_shift)

    def __init__(self, world, sprite_id: int):
        super().__init__(world)
        assert 0 <= sprite_id <= TOTAL_SPRITES
        self._sprite_id = sprite_id

        if sprite_id >= 7:
            self._directions = VramStore.DIR0_SWSE_NWNE
        else:
            self._directions = VramStore.DIR7_ALL_DIRECTIONS


class MimicFace(NPC):
    _shadow_size: ShadowSize = ShadowSize.OVAL_SMALL
    _acute_axis: int = 3
    _obtuse_axis: int = 3
    _height: int = 3

    _eye_height: int = 4

    _crown: int = 1


class AreaNPC:
    _occupant: NPC
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
    def occupant(self) -> NPC:
        return self._occupant

    def set_occupant(self, occupant: NPC) -> None:
        self._occupant = occupant

    @property
    def priority_0(self) -> bool:
        return self._priority_0

    def set_priority_0(self, priority_0: bool) -> None:
        self._priority_0 = priority_0

    @property
    def priority_1(self) -> bool:
        return self._priority_1

    def set_priority_1(self, priority_1: bool) -> None:
        self._priority_1 = priority_1

    @property
    def priority_2(self) -> bool:
        return self._priority_2

    def set_priority_2(self, priority_2: bool) -> None:
        self._priority_2 = priority_2

    @property
    def show_shadow(self) -> bool:
        if self._show_shadow is None:
            return self.occupant.show_shadow
        else:
            return self._show_shadow

    def set_show_shadow(self, show_shadow: Optional[bool] = None) -> None:
        self._show_shadow = show_shadow

    @property
    def shadow_size(self) -> ShadowSize:
        if self._shadow_size is None:
            return self.occupant.shadow_size
        else:
            return self._shadow_size

    def set_shadow_size(self, shadow_size: Optional[ShadowSize] = None) -> None:
        self._shadow_size = shadow_size

    @property
    def acute_axis(self) -> UInt4:
        if self._acute_axis is None:
            return self.occupant.acute_axis
        else:
            return UInt4(self._acute_axis)

    def set_acute_axis(self, acute_axis: Optional[int] = None) -> None:
        if acute_axis is None:
            self._acute_axis = None
            return
        assert UInt4(acute_axis)
        self._acute_axis = acute_axis

    @property
    def obtuse_axis(self) -> UInt4:
        if self._obtuse_axis is None:
            return self.occupant.obtuse_axis
        else:
            return UInt4(self._obtuse_axis)

    def set_obtuse_axis(self, obtuse_axis: Optional[int] = None) -> None:
        if obtuse_axis is None:
            self._obtuse_axis = None
            return
        assert UInt4(obtuse_axis)
        self._obtuse_axis = obtuse_axis

    @property
    def height(self) -> UInt8:
        if self._height is None:
            return self.occupant.height
        else:
            assert self._height <= 31
            return UInt8(self._height)

    def set_height(self, height: Optional[int] = None) -> None:
        if height is None:
            self._height = None
            return
        assert 0 <= height <= 31
        self._height = height

    @property
    def y_shift(self) -> Int8:
        if self._y_shift is None:
            return self.occupant.y_shift
        else:
            assert -16 <= self.y_shift <= 15
            return Int8(self._y_shift)

    def set_y_shift(self, y_shift: Optional[int] = None) -> None:
        if y_shift is None:
            self._y_shift = None
            return
        assert -16 <= y_shift <= 15
        self._y_shift = y_shift

    @property
    def directions(self) -> VramStore:
        if self._directions is None:
            return self.occupant.directions
        else:
            return self._directions

    def set_directions(self, directions: Optional[VramStore] = None) -> None:
        self._directions = directions

    @property
    def vram_size(self) -> UInt4:
        if self._vram_size is None:
            return self.occupant.min_vram_size
        else:
            assert self._vram_size <= 7
            return UInt4(self._vram_size)

    def set_vram_size(self, vram_size: Optional[int] = None) -> None:
        if vram_size is None:
            self._vram_size = None
            return
        assert 0 <= vram_size <= 7
        self._vram_size = vram_size

    @property
    def cannot_clone(self) -> bool:
        return self._cannot_clone

    def set_cannot_clone(self, cannot_clone: bool) -> None:
        self._cannot_clone = cannot_clone

    @property
    def byte2_bit0(self) -> bool:
        if self._byte2_bit0 is None:
            return self.occupant.byte2_bit0
        else:
            return self._byte2_bit0

    def set_byte2_bit0(self, byte2_bit0: Optional[bool] = None) -> None:
        self._byte2_bit0 = byte2_bit0

    @property
    def byte2_bit1(self) -> bool:
        if self._byte2_bit1 is None:
            return self.occupant.byte2_bit1
        else:
            return self._byte2_bit1

    def set_byte2_bit1(self, byte2_bit1: Optional[bool] = None) -> None:
        self._byte2_bit1 = byte2_bit1

    @property
    def byte2_bit2(self) -> bool:
        if self._byte2_bit2 is None:
            return self.occupant.byte2_bit2
        else:
            return self._byte2_bit2

    def set_byte2_bit2(self, byte2_bit2: Optional[bool] = None) -> None:
        self._byte2_bit2 = byte2_bit2

    @property
    def byte2_bit3(self) -> bool:
        if self._byte2_bit3 is None:
            return self.occupant.byte2_bit3
        else:
            return self._byte2_bit3

    def set_byte2_bit3(self, byte2_bit3: Optional[bool] = None) -> None:
        self._byte2_bit3 = byte2_bit3

    @property
    def byte2_bit4(self) -> bool:
        if self._byte2_bit4 is None:
            return self.occupant.byte2_bit4
        else:
            return self._byte2_bit4

    def set_byte2_bit4(self, byte2_bit4: Optional[bool] = None) -> None:
        self._byte2_bit4 = byte2_bit4

    @property
    def byte5_bit6(self) -> bool:
        if self._byte5_bit6 is None:
            return self.occupant.byte5_bit6
        else:
            return self._byte5_bit6

    def set_byte5_bit6(self, byte5_bit6: Optional[bool] = None) -> None:
        self._byte5_bit6 = byte5_bit6

    @property
    def byte5_bit7(self) -> bool:
        if self._byte5_bit7 is None:
            return self.occupant.byte5_bit7
        else:
            return self._byte5_bit7

    def set_byte5_bit7(self, byte5_bit7: Optional[bool] = None) -> None:
        self._byte5_bit7 = byte5_bit7

    @property
    def byte6_bit2(self) -> bool:
        if self._byte6_bit2 is None:
            return self.occupant.byte6_bit2
        else:
            return self._byte6_bit2

    def set_byte6_bit2(self, byte6_bit2: Optional[bool] = None) -> None:
        self._byte6_bit2 = byte6_bit2

    def __init__(
        self,
        occupant: NPC,
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
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1
    _y_shift: int = 3


class CrocoBase(NPC):
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
    _directions = VramStore.DIR0_SWSE_NWNE
    _byte5_bit7: bool = True


class SmallToad(Villager):
    _height: int = 7
    _y_shift: int = 2


class BigToad(Villager):
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _y_shift: int = 1


class StarPiece(NPC):
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13
    _y_shift: int = 1


class Trampoline(NPC):
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 10
    _min_vram_size: int = 1


class ShovelKnightBoss(NPC):
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
    pass


class HammerNPC(NPC):
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _y_shift: int = -1
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=HAMMER_HIT, kitchen_prep=HAMMER_HIT, factory_pierce=HAMMER_HIT
    )


class ValentinaBird(NPC):
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 10
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=BIRD_ATTACK, kitchen_prep=BIRD_ATTACK, factory_pierce=BIRD_ATTACK
    )


class Fireball(NPC):
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
    _shadow_size = ShadowSize.BLOCK
    _y_shift: int = 3
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 12
    _min_vram_size: int = 1


class ShovelKnightBossLarge(NPC):
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
    _directions = VramStore.DIR0_SWSE_NWNE
    _byte5_bit6: bool = True
    _byte5_bit7: bool = True
    _byte6_bit2: bool = True
