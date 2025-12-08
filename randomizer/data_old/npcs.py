from randomizer.helpers.npcmodeltables import SpriteName, VramStore, ShadowSize
from randomizer.helpers.objectsequencetables import SequenceSpeeds, _0x08Flags


class SpriteAnimation:
    sequence_id = 0
    contact_frame = None
    total_duration = None
    new_sprite_id = None
    speed = SequenceSpeeds.NORMAL

    def __init__(
        self,
        sequence_id=0,
        contact_frame=None,
        total_duration=None,
        new_sprite_id=None,
        speed=SequenceSpeeds.NORMAL):
        self.sequence_id = sequence_id
        self.contact_frame = contact_frame
        self.total_duration = total_duration
        self.new_sprite_id = new_sprite_id
        self.speed = speed


class SpriteAnimationCollection:
    recoil = None
    bandits_way_distracted = None
    mines_punch = None
    tower_bullet = None
    chapel_laugh = None
    kitchen_prep = None
    ship_beckon = None
    ship_chair = None
    dojo_challenge = None
    statue_intro = None
    statue_peck = None
    statue_flustered = None
    keep_challenge = None
    keep_summon = None
    chandelier_challenge = None
    factory_pierce = None
    endgame_challenge = None

    def __init__(
        self,
        recoil=None,
        bandits_way_distracted=None,
        mines_punch=None,
        tower_bullet=None,
        chapel_laugh=None,
        kitchen_prep=None,
        ship_beckon=None,
        ship_chair=None,
        dojo_challenge=None,
        statue_intro=None,
        statue_peck=None,
        statue_flustered=None,
        keep_challenge=None,
        keep_summon=None,
        chandelier_challenge=None,
        factory_pierce=None,
        endgame_challenge=None):
        self.recoil = recoil
        self.bandits_way_distracted = bandits_way_distracted
        self.mines_punch = mines_punch
        self.tower_bullet = tower_bullet
        self.chapel_laugh = chapel_laugh
        self.kitchen_prep = kitchen_prep
        self.ship_beckon = ship_beckon
        self.ship_chair = ship_chair
        self.dojo_challenge = dojo_challenge
        self.statue_intro = statue_intro
        self.statue_peck = statue_peck
        self.statue_flustered = statue_flustered
        self.keep_challenge = keep_challenge
        self.keep_summon = keep_summon
        self.chandelier_challenge = chandelier_challenge
        self.factory_pierce = factory_pierce
        self.endgame_challenge = endgame_challenge


class StatueDetails:
    mold = 0
    horizontal_pixel_shift = 0
    vertical_pixel_shift = 0
    north_facing_horizontal_pixel_shift = 0
    north_facing_vertical_pixel_shift = 0

    def __init__(
        self,
        mold=0,
        horizontal_pixel_shift=0,
        vertical_pixel_shift=0,
        north_facing_horizontal_pixel_shift=0,
        north_facing_vertical_pixel_shift=0):
        self.mold = mold
        self.horizontal_pixel_shift = horizontal_pixel_shift
        self.vertical_pixel_shift = vertical_pixel_shift
        self.north_facing_horizontal_pixel_shift = north_facing_horizontal_pixel_shift
        self.north_facing_vertical_pixel_shift = north_facing_vertical_pixel_shift


class NPC:
    sprite_id = 0
    show_shadow = True
    shadow_size = ShadowSize._01_OVAL_MED
    acute_axis = 3
    obtuse_axis = 3
    height = 12
    y_shift = 0
    directions = VramStore._02_SWSE
    min_vram_size = 0
    byte2_bit0 = False
    byte2_bit1 = False
    byte2_bit2 = False
    byte2_bit3 = False
    byte2_bit4 = False
    byte5_bit6 = False
    byte5_bit7 = False
    byte6_bit2 = False
    world = None

    crown = 2

    animations = SpriteAnimationCollection()
    eye_height = 17
    tower_entrance_horizontal_shift = 0
    alt_palette = None

    def __init__(self, world):
        self.world = world

    def is_equal(self, npc):
        return (
            npc.sprite_id == self.sprite_id
            and npc.show_shadow == self.show_shadow
            and npc.shadow_size == self.shadow_size
            and npc.acute_axis == self.acute_axis
            and npc.obtuse_axis == self.obtuse_axis
            and npc.height == self.height
            and npc.directions == self.directions
            and npc.min_vram_size == self.min_vram_size
            and npc.byte2_bit0 == self.byte2_bit0
            and npc.byte2_bit1 == self.byte2_bit1
            and npc.byte2_bit2 == self.byte2_bit2
            and npc.byte2_bit3 == self.byte2_bit3
            and npc.byte2_bit4 == self.byte2_bit4
            and npc.byte5_bit6 == self.byte5_bit6
            and npc.byte5_bit7 == self.byte5_bit7
            and npc.byte6_bit2 == self.byte6_bit2
        )


class Statue(NPC):
    details = StatueDetails()


class ItemNPC(NPC):
    chest_packet = 5
    chest_event = 883
    static_packet = 37
    falling_packet = 90
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    height = 7
    chest_70A7_upper = 0
    hover = False


class PartyNPC(NPC):
    minecart_shift = 0

    def __init__(self, world, sprite_id):
        super().__init__(world)
        self.sprite_id = sprite_id

        if sprite_id >= 7:
            self.directions = VramStore._00_SWSE_NWNE
        else:
            self.directions = VramStore._07_ALL_DIRECTIONS


class MimicFace(NPC):
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 3
    obtuse_axis = 3
    height = 3

    eye_height = 4

    crown = 1


class AreaNPC:
    occupant = None
    priority_0 = False
    priority_1 = False
    priority_2 = True
    _show_shadow = None
    _shadow_size = None
    _acute_axis = None
    _obtuse_axis = None
    _height = None
    _directions = None
    _vram_size = None
    cannot_clone = False
    _byte2_bit0 = None
    _byte2_bit1 = None
    _byte2_bit2 = None
    _byte2_bit3 = None
    _byte2_bit4 = None
    _byte5_bit6 = None
    _byte5_bit7 = None
    _byte6_bit2 = None
    _y_shift = None

    @property
    def show_shadow(self):
        if self._show_shadow is None:
            return self.occupant.show_shadow
        else:
            return self._show_shadow

    @property
    def shadow_size(self):
        if self._shadow_size is None:
            return self.occupant.shadow_size
        else:
            return self._shadow_size

    @property
    def acute_axis(self):
        if self._acute_axis is None:
            return self.occupant.acute_axis
        else:
            return self._acute_axis

    @property
    def obtuse_axis(self):
        if self._obtuse_axis is None:
            return self.occupant.obtuse_axis
        else:
            return self._obtuse_axis

    @property
    def directions(self):
        if self._directions is None:
            return self.occupant.directions
        else:
            return self._directions

    @property
    def vram_size(self):
        if self._vram_size is None:
            return self.occupant.min_vram_size
        else:
            return self._vram_size

    @property
    def height(self):
        if self._height is None:
            return self.occupant.height
        else:
            return self._height

    @property
    def byte2_bit0(self):
        if self._byte2_bit0 is None:
            return self.occupant.byte2_bit0
        else:
            return self._byte2_bit0

    @property
    def byte2_bit1(self):
        if self._byte2_bit1 is None:
            return self.occupant.byte2_bit1
        else:
            return self._byte2_bit1

    @property
    def byte2_bit2(self):
        if self._byte2_bit2 is None:
            return self.occupant.byte2_bit2
        else:
            return self._byte2_bit2

    @property
    def byte2_bit3(self):
        if self._byte2_bit3 is None:
            return self.occupant.byte2_bit3
        else:
            return self._byte2_bit3

    @property
    def byte2_bit4(self):
        if self._byte2_bit4 is None:
            return self.occupant.byte2_bit4
        else:
            return self._byte2_bit4

    @property
    def byte5_bit6(self):
        if self._byte5_bit6 is None:
            return self.occupant.byte5_bit6
        else:
            return self._byte5_bit6

    @property
    def byte5_bit7(self):
        if self._byte5_bit7 is None:
            return self.occupant.byte5_bit7
        else:
            return self._byte5_bit7

    @property
    def byte6_bit2(self):
        if self._byte6_bit2 is None:
            return self.occupant.byte6_bit2
        else:
            return self._byte6_bit2

    @property
    def y_shift(self):
        if self._y_shift is None:
            return self.occupant.y_shift
        else:
            return self._y_shift

    def is_equal(self, areaNPC):
        return (
            areaNPC.occupant.sprite_id == self.occupant.sprite_id
            and (
                (not areaNPC.show_shadow and not self.show_shadow)
                or (
                    areaNPC.show_shadow
                    and self.show_shadow
                    and areaNPC.occupant.shadow_size == self.shadow_size
                )
            )
            and areaNPC.priority_0 == self.priority_0
            and areaNPC.priority_1 == self.priority_1
            and areaNPC.priority_2 == self.priority_2
            and areaNPC.occupant.y_shift == self.occupant.y_shift
            and areaNPC.acute_axis == self.acute_axis
            and areaNPC.obtuse_axis == self.obtuse_axis
            and areaNPC.height == self.height
            and areaNPC.directions == self.directions
            and areaNPC.vram_size == self.vram_size
            and areaNPC.cannot_clone == self.cannot_clone
            and areaNPC.occupant.sprite_id == self.occupant.sprite_id
            and areaNPC.occupant.byte2_bit0 == self.occupant.byte2_bit0
            and areaNPC.occupant.byte2_bit1 == self.occupant.byte2_bit1
            and areaNPC.occupant.byte2_bit2 == self.occupant.byte2_bit2
            and areaNPC.occupant.byte2_bit3 == self.occupant.byte2_bit3
            and areaNPC.occupant.byte2_bit4 == self.occupant.byte2_bit4
            and areaNPC.occupant.byte5_bit6 == self.occupant.byte5_bit6
            and areaNPC.occupant.byte5_bit7 == self.occupant.byte5_bit7
            and areaNPC.occupant.byte6_bit2 == self.occupant.byte6_bit2
        )

    def __init__(
        self,
        occupant,
        priority_0=False,
        priority_1=False,
        priority_2=True,
        show_shadow=None,
        shadow_size=None,
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
        byte6_bit2=None):
        self.occupant = occupant
        self.priority_0 = priority_0
        self.priority_1 = priority_1
        self.priority_2 = priority_2
        self._show_shadow = show_shadow
        self._shadow_size = shadow_size
        self._y_shift = y_shift
        self._acute_axis = acute_axis
        self._obtuse_axis = obtuse_axis
        self._height = height
        self._directions = directions
        self._vram_size = vram_size
        self.cannot_clone = cannot_clone
        self._byte2_bit0 = byte2_bit0
        self._byte2_bit1 = byte2_bit1
        self._byte2_bit2 = byte2_bit2
        self._byte2_bit3 = byte2_bit3
        self._byte2_bit4 = byte2_bit4
        self._byte5_bit6 = byte5_bit6
        self._byte5_bit7 = byte5_bit7
        self._byte6_bit2 = byte6_bit2


class Mario(PartyNPC):
    sprite_id = 0
    y_shift = 1
    directions = VramStore._07_ALL_DIRECTIONS
    minecart_shift = 7


class Toadstool(PartyNPC):
    sprite_id = 7
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE
    minecart_shift = 6


class Bowser(PartyNPC):
    sprite_id = 13
    shadow_size = ShadowSize._02_OVAL_BIG
    acute_axis = 6
    obtuse_axis = 6
    height = 14
    y_shift = -2
    directions = VramStore._00_SWSE_NWNE


class Mallow(PartyNPC):
    sprite_id = 19
    height = 8
    directions = VramStore._00_SWSE_NWNE
    minecart_shift = 4


class Geno(PartyNPC):
    sprite_id = 25
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    directions = VramStore._00_SWSE_NWNE
    minecart_shift = 9


class YoshiNPC(NPC):
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1
    y_shift = 3


class YellowYoshi(YoshiNPC):
    sprite_id = 45
    byte2_bit0 = True
    byte2_bit3 = True


class PinkYoshi(YoshiNPC):
    sprite_id = 46


class Boshi(YoshiNPC):
    sprite_id = 47
    min_vram_size = 0


croco_bag_loop = SpriteAnimation(sequence_id=5, total_duration=104)
croco_bag_hit = SpriteAnimation(sequence_id=4, contact_frame=152, total_duration=158)
croco_bag_summon = SpriteAnimation(sequence_id=6, total_duration=136)
croco_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class CrocoBase(NPC):
    acute_axis = 5
    obtuse_axis = 5
    height = 10
    y_shift = 2
    directions = VramStore._00_SWSE_NWNE
    tower_entrance_horizontal_shift = 9

    eye_height = 16
    animations = SpriteAnimationCollection(
        recoil=croco_recoil,
        bandits_way_distracted=croco_bag_loop,
        mines_punch=croco_bag_hit,
        chapel_laugh=croco_bag_loop,
        dojo_challenge=croco_bag_summon,
        statue_flustered=croco_recoil,
        keep_challenge=croco_bag_summon,
        keep_summon=croco_bag_hit,
        chandelier_challenge=croco_bag_summon,
        endgame_challenge=croco_bag_summon)


class Croco(CrocoBase):
    sprite_id = 48


class RideYoshi(YoshiNPC):
    sprite_id = 49
    directions = VramStore._07_ALL_DIRECTIONS


booster_laugh = SpriteAnimation(sequence_id=2)
booster_punch = SpriteAnimation(
    sequence_id=3, contact_frame=74, total_duration=92, new_sprite_id=502
)
booster_jump = SpriteAnimation(sequence_id=4)
booster_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class Booster(NPC):
    sprite_id = 50
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 5
    obtuse_axis = 5
    y_shift = 2

    animations = SpriteAnimationCollection(
        recoil=booster_recoil,
        bandits_way_distracted=booster_laugh,
        mines_punch=booster_punch,
        chapel_laugh=booster_laugh,
        ship_beckon=booster_laugh,
        ship_chair=booster_laugh,
        dojo_challenge=booster_jump,
        statue_intro=booster_laugh,
        statue_flustered=booster_jump,
        keep_challenge=booster_jump,
        keep_summon=booster_laugh,
        chandelier_challenge=booster_punch,
        endgame_challenge=booster_punch)
    eye_height = 17


class GreenYoshi(YoshiNPC):
    sprite_id = 51
    min_vram_size = 0
    byte2_bit0 = True
    byte2_bit4 = True


class KingNimbus(NPC):
    sprite_id = 53
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 1


class QueenNimbus(NPC):
    sprite_id = 54
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 1


small_johnny_sit = SpriteAnimation(sequence_id=10)


class JohnnySmall(NPC):
    sprite_id = 55
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 2

    animations = SpriteAnimationCollection(
        bandits_way_distracted=small_johnny_sit,
        chapel_laugh=small_johnny_sit,
        ship_beckon=small_johnny_sit,
        ship_chair=small_johnny_sit,
        dojo_challenge=small_johnny_sit,
        keep_challenge=small_johnny_sit,
        chandelier_challenge=small_johnny_sit,
        endgame_challenge=small_johnny_sit)
    eye_height = 20


valentina_stand = SpriteAnimation(sequence_id=10)
valentina_laugh = SpriteAnimation(sequence_id=2)
valentina_hit = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=28)
valentina_taunt = SpriteAnimation(sequence_id=4, total_duration=58)
valentina_recoil = SpriteAnimation(sequence_id=2, total_duration=34)


class ValentinaSmall(NPC):
    sprite_id = 56
    directions = VramStore._00_SWSE_NWNE
    y_shift = 1

    eye_height = 16
    animations = SpriteAnimationCollection(
        bandits_way_distracted=valentina_stand,
        chapel_laugh=valentina_laugh,
        ship_beckon=valentina_laugh,
        ship_chair=valentina_stand,
        dojo_challenge=valentina_laugh,
        statue_intro=valentina_laugh,
        keep_challenge=valentina_laugh,
        keep_summon=valentina_laugh,
        chandelier_challenge=valentina_laugh,
        endgame_challenge=valentina_laugh)


small_magikoopa_hit = SpriteAnimation(
    sequence_id=10, contact_frame=44, total_duration=72
)


class SmallMagikoopa(NPC):
    directions = VramStore._00_SWSE_NWNE
    shadow_size = ShadowSize._00_OVAL_SMALL
    height = 10
    y_shift = 1

    animations = SpriteAnimationCollection(
        mines_punch=small_magikoopa_hit,
        ship_beckon=small_magikoopa_hit,
        dojo_challenge=small_magikoopa_hit,
        # statue_peck=small_magikoopa_hit,
        keep_challenge=small_magikoopa_hit,
        keep_summon=small_magikoopa_hit,
        chandelier_challenge=small_magikoopa_hit,
        endgame_challenge=small_magikoopa_hit)


class MagikoopaSmall(SmallMagikoopa):
    sprite_id = 57


class Frogfucius(NPC):
    sprite_id = 58
    directions = VramStore._00_SWSE_NWNE
    height = 11


class Tadpole(NPC):
    sprite_id = 59
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 4
    obtuse_axis = 4
    height = 5
    y_shift = 1


class Thwomp(NPC):
    sprite_id = 60
    acute_axis = 8
    obtuse_axis = 6
    height = 11
    shadow_size = ShadowSize._02_OVAL_BIG


class BigThwomp(NPC):
    sprite_id = 61
    acute_axis = 14
    obtuse_axis = 8
    height = 18
    shadow_size = ShadowSize._02_OVAL_BIG
    min_vram_size = 2


class NimbusLandStatue(NPC):
    sprite_id = 63
    show_shadow = False

    def __init__(self, world, occupant):
        super().__init__(world)
        self.acute_axis = occupant.acute_axis
        self.obtuse_axis = occupant.obtuse_axis
        self.height = occupant.height
        self.directions = occupant.directions
        self.min_vram_size = 0


class Villager(NPC):
    directions = VramStore._00_SWSE_NWNE
    byte5_bit7 = True


class SmallToad(Villager):
    height = 7
    y_shift = 2


class RedSmallToad(SmallToad):
    sprite_id = 64


class BigToad(Villager):
    acute_axis = 4
    obtuse_axis = 4
    height = 9
    y_shift = 1


class BlueToad(BigToad):
    sprite_id = 65


class PinkToad(BigToad):
    sprite_id = 66


class OldBlueToad(BigToad):
    sprite_id = 67


class OldRedToad(BigToad):
    sprite_id = 68


class GreenSmallToad(SmallToad):
    sprite_id = 69


class Chancellor(Villager):
    sprite_id = 70
    height = 9
    y_shift = 1


class PaMole(Villager):
    sprite_id = 71
    acute_axis = 4
    obtuse_axis = 4
    y_shift = 2


class MaMole(Villager):
    sprite_id = 72
    acute_axis = 4
    obtuse_axis = 4
    y_shift = 2


class PinkMole(Villager):
    sprite_id = 73
    height = 6
    y_shift = 1


class YellowMole(Villager):
    sprite_id = 74
    height = 6
    y_shift = 1


class BlueNimbite(Villager):
    sprite_id = 75
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 1


class RedNimbite(Villager):
    sprite_id = 76
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 1


class BrownNimbite(Villager):
    sprite_id = 77
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 1


class GreenNimbite(Villager):
    sprite_id = 78
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 1


class NimbusGuard(Villager):
    sprite_id = 79
    acute_axis = 4
    obtuse_axis = 4
    height = 11


class Toadofsky(NPC):
    sprite_id = 80
    acute_axis = 4
    obtuse_axis = 4
    height = 11


class MallowDoll(NPC):
    sprite_id = 81
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 3
    y_shift = 1


class StarPiece(NPC):
    acute_axis = 7
    obtuse_axis = 7
    height = 13
    y_shift = 1


class BlueStarPiece(StarPiece):
    sprite_id = 82


class PurpleStarPiece(StarPiece):
    sprite_id = 83


class RedStarPiece(StarPiece):
    sprite_id = 84


class OrangeStarPiece(StarPiece):
    sprite_id = 85


class GreenStarPiece(StarPiece):
    sprite_id = 86


class IndigoStarPiece(StarPiece):
    sprite_id = 87


class YellowStarPiece(StarPiece):
    sprite_id = 88


class BowserDoll(NPC):
    sprite_id = 90
    shadow_size = ShadowSize._00_OVAL_SMALL
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 1
    obtuse_axis = 1
    height = 3
    y_shift = 1


class ToadstoolDoll(NPC):
    sprite_id = 92
    shadow_size = ShadowSize._00_OVAL_SMALL
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 1
    obtuse_axis = 1
    height = 3
    y_shift = 1


class TreasureChest(NPC):
    sprite_id = 94
    shadow_size = ShadowSize._03_BLOCK
    y_shift = -2
    acute_axis = 7
    obtuse_axis = 7
    height = 8
    min_vram_size = 1


class MidasRiverMario(NPC):
    sprite_id = 96
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 2
    obtuse_axis = 2
    height = 5
    y_shift = 1


class Parachute(NPC):
    sprite_id = 97
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    sprite_id = 97
    acute_axis = 8
    obtuse_axis = 8
    y_shift = 1


class Barrel(NPC):
    sprite_id = 98
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 6
    obtuse_axis = 6
    height = 11


class Trampoline(NPC):
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 10
    min_vram_size = 1


class WarpTrampoline(Trampoline):
    sprite_id = 99


class JumpTrampoline(Trampoline):
    sprite_id = 100


class Seesaw(NPC):
    sprite_id = 101
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 14
    obtuse_axis = 5
    height = 5
    min_vram_size = 2


class SavePoint(NPC):
    sprite_id = 102
    y_shift = -2
    acute_axis = 7
    obtuse_axis = 7
    height = 7
    shadow_size = ShadowSize._03_BLOCK


class Corkpedite(NPC):
    sprite_id = 103
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 14
    obtuse_axis = 14
    height = 23
    min_vram_size = 3


class JBlock(NPC):
    sprite_id = 104
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 7
    shadow_size = ShadowSize._03_BLOCK
    show_shadow = False


class YellowPlatform(NPC):
    sprite_id = 105
    y_shift = -1
    acute_axis = 6
    obtuse_axis = 6
    height = 4
    shadow_size = ShadowSize._03_BLOCK


class WhirlpoolBubble(NPC):
    sprite_id = 106
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL


class Hinopio(NPC):
    sprite_id = 107
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    directions = VramStore._00_SWSE_NWNE


class FactoryNut(NPC):
    sprite_id = 108
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 2
    obtuse_axis = 2
    height = 11


class GreenSwitch(NPC):
    sprite_id = 109
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = -2
    acute_axis = 7
    obtuse_axis = 7
    height = 3


class RedToad(BigToad):
    sprite_id = 112


class GreenToad(BigToad):
    sprite_id = 113


class YellowToad(BigToad):
    sprite_id = 114


class TurquoiseToad(BigToad):
    sprite_id = 115


class PinkSmallToad(SmallToad):
    sprite_id = 116


class BlueSmallToad(SmallToad):
    sprite_id = 117


class OldBrownToad(BigToad):
    sprite_id = 118


class OldGreenToad(BigToad):
    sprite_id = 119


class OldDarkGreenToad(BigToad):
    sprite_id = 120


class OldPinkToad(BigToad):
    sprite_id = 121


class FatYoshi(NPC):
    sprite_id = 122
    acute_axis = 5
    obtuse_axis = 5


class PurpleSmallToad(SmallToad):
    sprite_id = 124


class FrogDisciple(NPC):
    sprite_id = 125
    y_shift = 1
    acute_axis = 4
    height = 10


class ChompBehind(NPC):
    sprite_id = 126
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 9
    obtuse_axis = 9
    height = 10
    min_vram_size = 2


class WigglerHead(NPC):
    sprite_id = 127
    directions = VramStore._00_SWSE_NWNE
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 4
    obtuse_axis = 4
    height = 9


class BlockShadow(NPC):
    sprite_id = 128
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = -7
    acute_axis = 1
    obtuse_axis = 1
    height = 0


class RedMagikoopa(SmallMagikoopa):
    sprite_id = 129

    eye_height = 12


class WigglerBody(NPC):
    sprite_id = 130
    directions = VramStore._00_SWSE_NWNE
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 4
    obtuse_axis = 4
    height = 7
    y_shift = 1


class ParsonDodo(NPC):
    sprite_id = 131
    shadow_size = ShadowSize._02_OVAL_BIG
    min_vram_size = 4
    acute_axis = 2
    obtuse_axis = 2
    height = 5


class KnifeGuySmall(NPC):
    sprite_id = 133
    min_vram_size = 2
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7


class KnifeGuySmall2(NPC):
    sprite_id = 134
    min_vram_size = 2
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7


class Minecart(NPC):
    sprite_id = 135
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 5
    acute_axis = 6
    obtuse_axis = 7
    height = 8


class FlatFireball(NPC):
    sprite_id = 137
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 5


class PipePiranhaPlant(NPC):
    sprite_id = 138
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1


class ThumpGoomba(NPC):
    sprite_id = 139
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 10


class BulletBill(NPC):
    sprite_id = 140
    directions = VramStore._00_SWSE_NWNE
    y_shift = 1
    acute_axis = 3
    obtuse_axis = 7
    height = 6


class GoldenBulletBill(NPC):
    sprite_id = 141
    directions = VramStore._00_SWSE_NWNE
    y_shift = 1
    acute_axis = 3
    obtuse_axis = 7
    height = 6


shovelknight_tile = SpriteAnimation(sequence_id=2)


class ShovelKnightBoss(NPC):
    directions = VramStore._00_SWSE_NWNE
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13

    animations = SpriteAnimationCollection(
        bandits_way_distracted=shovelknight_tile,
        chapel_laugh=shovelknight_tile,
        ship_chair=shovelknight_tile,
        dojo_challenge=shovelknight_tile,
        keep_challenge=shovelknight_tile,
        keep_summon=shovelknight_tile,
        chandelier_challenge=shovelknight_tile,
        endgame_challenge=shovelknight_tile)
    eye_height = 10
    statue = StatueDetails(
        [
            "F8E870",
            "F8E870",
            "E0C000",
            "D09020",
            "906010",
            "784818",
            "301830",
            "784818",
            "906010",
            "E0C000",
            "D09020",
            "906010",
            "482818",
            "301830",
            "181818",
        ],
        horizontal_pixel_shift=-3,
        north_facing_horizontal_pixel_shift=-5)


class ClerkSmall(ShovelKnightBoss):
    sprite_id = 142


class LandsEndCannon(NPC):
    sprite_id = 143
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 11


class BerryGridplane(ItemNPC):
    sprite_id = 144
    y_shift = 1


class CommanderTroopa(NPC):
    sprite_id = 146
    y_shift = -1
    acute_axis = 7
    obtuse_axis = 7
    height = 7
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1


belome_attack = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
belome_attack_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=SequenceSpeeds.FAST
)
belome_wiggle = SpriteAnimation(sequence_id=4, total_duration=66)
belome_recoil = SpriteAnimation(sequence_id=2, total_duration=14)


class BelomeStatue(NPC):
    sprite_id = 147
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 2
    acute_axis = 10
    obtuse_axis = 10
    height = 18
    min_vram_size = 5

    animations = SpriteAnimationCollection(
        mines_punch=belome_attack,
        statue_intro=belome_wiggle,
        statue_flustered=belome_recoil,
        statue_peck=belome_attack_fast,
        chandelier_challenge=belome_attack,
        endgame_challenge=belome_attack)


class ShyGuyClownCar(NPC):
    sprite_id = 149
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL


class MachineBowyer(NPC):
    sprite_id = 150
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 14
    obtuse_axis = 9
    height = 16
    min_vram_size = 3


class MachineYaridOverworld(NPC):
    sprite_id = 151
    y_shift = 1
    acute_axis = 6
    obtuse_axis = 6
    height = 15
    min_vram_size = 2


class GunyolkTop(NPC):
    sprite_id = 153
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


class GunyolkOuter(NPC):
    sprite_id = 154
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    min_vram_size = 1


class Crane(NPC):
    sprite_id = 155
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 8
    min_vram_size = 1


class SpinningStarPiece(NPC):
    sprite_id = 156
    show_shadow = False
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    y_shift = 1


class SmithyHammer(NPC):
    sprite_id = 157
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    y_shift = 1
    min_vram_size = 1


class SmithyBodyOverworld(NPC):
    sprite_id = 158
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    y_shift = 1


class PoisonGas(NPC):
    sprite_id = 159
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 0
    y_shift = 1
    min_vram_size = 3


class DynaMite(NPC):
    sprite_id = 161
    acute_axis = 5
    obtuse_axis = 5
    height = 8
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


class FakeToad(BigToad):
    sprite_id = 162


class FakeElder(BigToad):
    sprite_id = 163

    eye_height = 10


class Elder(BigToad):
    sprite_id = 164


class Monstromama(BigToad):
    sprite_id = 165
    byte5_bit7 = False


class NimbusGuardPurple(Villager):
    sprite_id = 166
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 0
    byte5_bit7 = False


class ManagerSmall(ShovelKnightBoss):
    sprite_id = 167


class DirectorSmall(ShovelKnightBoss):
    sprite_id = 168


boomer_alt_taunt = SpriteAnimation(sequence_id=1, total_duration=16)


class BoomerOverworld(NPC):
    sprite_id = 169
    acute_axis = 8
    obtuse_axis = 8
    height = 17
    y_shift = 1
    min_vram_size = 3

    animations = SpriteAnimationCollection(
        chandelier_challenge=boomer_alt_taunt, endgame_challenge=boomer_alt_taunt
    )


class DrTopper(NPC):
    sprite_id = 170
    acute_axis = 9
    obtuse_axis = 9
    height = 18
    y_shift = 1
    min_vram_size = 3


class StarPieceSparkle(NPC):
    sprite_id = 171
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    y_shift = 1


class GenoDoll(NPC):
    sprite_id = 172
    shadow_size = ShadowSize._00_OVAL_SMALL
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 1
    obtuse_axis = 1
    height = 3
    y_shift = 1


class SmelterSection(NPC):
    sprite_id = 173
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    y_shift = 1


class AeroShot(NPC):
    sprite_id = 174
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 3
    obtuse_axis = 3
    height = 13
    y_shift = 1


class GoldenChompBehind(NPC):
    sprite_id = 175
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 9
    obtuse_axis = 9
    height = 10
    min_vram_size = 2


class GrateGuySmall(NPC):
    sprite_id = 177
    directions = VramStore._00_SWSE_NWNE
    y_shift = 1

    eye_height = 16


class BlueStripedToad(BigToad):
    sprite_id = 178


class RedStripedToad(BigToad):
    sprite_id = 179


class PinkStripedToad(BigToad):
    sprite_id = 180


class YellowStripedToad(BigToad):
    sprite_id = 181


class OldBlueStripedToad(BigToad):
    sprite_id = 182


class OldRedStripedToad(BigToad):
    sprite_id = 183


class RedStripedSmallToad(SmallToad):
    sprite_id = 184


class PinkStripedSmallToad(SmallToad):
    sprite_id = 185


class Cannonball(NPC):
    sprite_id = 188
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 8


class Croco2(CrocoBase):
    sprite_id = 190
    alt_palette = [
        "B8D0C8",
        "88C090",
        "A090F8",
        "F8F8F8",
        "788080",
        "A070F8",
        "9048D0",
        "300000",
        "601000",
        "7030A8",
        "482880",
        "480800",
        "300060",
        "281000",
        "000000",
    ]


jinx_punch = SpriteAnimation(sequence_id=3, contact_frame=10, total_duration=18)
jinx_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class Jinx(NPC):
    acute_axis = 2
    obtuse_axis = 2
    height = 5
    directions = VramStore._00_SWSE_NWNE
    shadow_size = ShadowSize._00_OVAL_SMALL

    eye_height = 4
    crown = 1
    animations = SpriteAnimationCollection(
        recoil=jinx_recoil,
        mines_punch=jinx_punch,
        ship_beckon=jinx_punch,
        dojo_challenge=jinx_punch,
        statue_intro=jinx_punch,
        statue_peck=jinx_punch,
        keep_challenge=jinx_punch,
        keep_summon=jinx_punch,
        chandelier_challenge=jinx_punch,
        endgame_challenge=jinx_punch)


class Jinx2(Jinx):
    sprite_id = 191
    alt_palette = [
        "F8F8F8",
        "E0B068",
        "985040",
        "682848",
        "682848",
        "C00000",
        "C00000",
        "300000",
        "F8F800",
        "404040",
        "181818",
        "181818",
        "E0D8D8",
        "988888",
        "181818",
    ]


class Coin(ItemNPC):
    pass


class BigCoin(Coin):
    sprite_id = 192
    height = 6
    y_shift = 5
    min_vram_size = 1
    chest_packet = 16
    static_packet = 109
    falling_packet = 106


class SmallCoin(Coin):
    sprite_id = 193
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    y_shift = 1
    min_vram_size = 1
    chest_packet = 18
    static_packet = 110
    falling_packet = 107


class FrogCoin(Coin):
    sprite_id = 194
    height = 6
    y_shift = 5
    min_vram_size = 1
    chest_packet = 19
    static_packet = 111
    falling_packet = 108
    chest_70A7_upper = 3


class SlotFlower(NPC):
    sprite_id = 195
    acute_axis = 3
    obtuse_axis = 3
    height = 3
    y_shift = 1


class Ring(ItemNPC):
    sprite_id = 196
    chest_packet = 91
    static_packet = 93
    falling_packet = 92
    chest_event = 886


class SparkleSideways(NPC):
    sprite_id = 197
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


class SparkleDown(NPC):
    sprite_id = 198
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


class FryingPan(ItemNPC):
    sprite_id = 199
    chest_packet = 205
    chest_event = 921
    static_packet = 203
    falling_packet = 204


class Explosion(NPC):
    sprite_id = 200
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


class MokuraCloud(NPC):
    sprite_id = 201
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 3
    obtuse_axis = 3
    height = 3

    eye_height = 4
    crown = 1


class Shoes(ItemNPC):
    sprite_id = 202
    chest_packet = 99
    static_packet = 97
    falling_packet = 98
    chest_event = 888


class MicroBombItem(ItemNPC):
    sprite_id = 205
    y_shift = 1
    chest_packet = 114
    static_packet = 112
    falling_packet = 113
    chest_event = 891


class Card(ItemNPC):
    sprite_id = 206
    chest_packet = 126
    chest_event = 895
    static_packet = 124
    falling_packet = 125
    hover = True


class Brooch(ItemNPC):
    sprite_id = 207
    chest_packet = 96
    static_packet = 94
    falling_packet = 95
    chest_event = 887


class Hammer(ItemNPC):
    sprite_id = 208
    chest_packet = 208
    chest_event = 922
    static_packet = 206
    falling_packet = 207


class FroggieStick(ItemNPC):
    sprite_id = 209
    chest_packet = 211
    chest_event = 923
    static_packet = 209
    falling_packet = 210


class ChompItem(ItemNPC):
    sprite_id = 210
    chest_packet = 214
    chest_event = 924
    static_packet = 212
    falling_packet = 213


class Fan(ItemNPC):
    sprite_id = 211
    chest_packet = 217
    chest_event = 925
    static_packet = 215
    falling_packet = 216


class RedMushroom(ItemNPC):
    sprite_id = 212
    chest_packet = 196
    chest_event = 918
    static_packet = 194
    falling_packet = 195


class Teleport(NPC):
    sprite_id = 213
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 3


class GreenMushroom(ItemNPC):
    sprite_id = 214
    chest_packet = 199
    chest_event = 919
    static_packet = 197
    falling_packet = 198


class YellowMushroom(ItemNPC):
    sprite_id = 215
    chest_packet = 202
    chest_event = 920
    static_packet = 200
    falling_packet = 201


class Crown(ItemNPC):
    sprite_id = 216
    chest_packet = 103
    static_packet = 105
    falling_packet = 104
    chest_event = 890


class GreenCandy(ItemNPC):
    sprite_id = 217
    chest_packet = 175
    static_packet = 173
    falling_packet = 174
    chest_event = 911


class BlueCandy(ItemNPC):
    sprite_id = 218
    chest_packet = 178
    static_packet = 176
    falling_packet = 177
    chest_event = 912


class RedSyrup(ItemNPC):
    sprite_id = 219
    chest_packet = 132
    static_packet = 130
    falling_packet = 131
    chest_event = 897


class GreenSyrup(ItemNPC):
    sprite_id = 220
    chest_packet = 129
    static_packet = 127
    falling_packet = 128
    chest_event = 896


class YellowSyrup(ItemNPC):
    sprite_id = 221
    chest_packet = 138
    static_packet = 136
    falling_packet = 137
    chest_event = 899


class Banana(ItemNPC):
    sprite_id = 222
    chest_packet = 102
    static_packet = 100
    falling_packet = 101
    chest_event = 889


class BlueSyrup(ItemNPC):
    sprite_id = 223
    chest_packet = 135
    static_packet = 133
    falling_packet = 134
    chest_event = 898


class RedBomb(ItemNPC):
    sprite_id = 224
    chest_packet = 184
    static_packet = 182
    falling_packet = 183
    chest_event = 914


class TinyStar(ItemNPC):
    sprite_id = 226
    chest_packet = 81
    static_packet = 85
    falling_packet = 83
    chest_event = 885


class GreenBomb(ItemNPC):
    sprite_id = 233
    chest_packet = 181
    static_packet = 179
    falling_packet = 180
    chest_event = 913


class YellowBomb(ItemNPC):
    sprite_id = 234
    chest_packet = 190
    static_packet = 188
    falling_packet = 189
    chest_event = 916


class BlueBomb(ItemNPC):
    sprite_id = 235
    chest_packet = 187
    static_packet = 185
    falling_packet = 186
    chest_event = 915


class GreenJuice(ItemNPC):
    sprite_id = 236
    chest_packet = 141
    static_packet = 139
    falling_packet = 140
    chest_event = 900


class Egg(ItemNPC):
    sprite_id = 237
    chest_packet = 117
    static_packet = 115
    falling_packet = 116
    chest_event = 892


class RedJuice(ItemNPC):
    sprite_id = 238
    chest_packet = 144
    static_packet = 142
    falling_packet = 143
    chest_event = 901


class RDrink(ItemNPC):
    sprite_id = 239
    chest_packet = 165
    static_packet = 163
    falling_packet = 164
    chest_event = 908


class DDrink(ItemNPC):
    sprite_id = 240
    chest_packet = 148
    static_packet = 150
    falling_packet = 149
    chest_event = 903


class PDrink(ItemNPC):
    sprite_id = 241
    chest_packet = 147
    static_packet = 145
    falling_packet = 146
    chest_event = 902


class FrogDrink(ItemNPC):
    sprite_id = 244
    chest_packet = 157
    static_packet = 159
    falling_packet = 158
    chest_event = 906


class YellowMusicDrink(ItemNPC):
    sprite_id = 245
    chest_packet = 151
    static_packet = 153
    falling_packet = 152
    chest_event = 904


class BlueMusicDrink(ItemNPC):
    sprite_id = 246
    chest_packet = 154
    static_packet = 156
    falling_packet = 155
    chest_event = 905


class RedMusicDrink(ItemNPC):
    sprite_id = 247
    chest_packet = 160
    static_packet = 162
    falling_packet = 161
    chest_event = 907


class StarDrink(ItemNPC):
    sprite_id = 248
    chest_packet = 171
    static_packet = 169
    falling_packet = 170
    chest_event = 910


class RedShell(ItemNPC):
    sprite_id = 249
    chest_packet = 220
    static_packet = 218
    falling_packet = 219
    chest_event = 926
    acute_axis = 4
    obtuse_axis = 4
    height = 5


class GreenShell(ItemNPC):
    sprite_id = 250
    chest_packet = 223
    static_packet = 221
    falling_packet = 222
    chest_event = 927
    acute_axis = 4
    obtuse_axis = 4
    height = 5


class Parasol(ItemNPC):
    sprite_id = 251
    chest_packet = 226
    chest_event = 928
    static_packet = 224
    falling_packet = 225


class Feather(ItemNPC):
    sprite_id = 252
    chest_packet = 80
    chest_event = 884
    static_packet = 84
    falling_packet = 82


class Berry(ItemNPC):
    sprite_id = 253
    y_shift = 1
    chest_packet = 123
    chest_event = 894
    static_packet = 121
    falling_packet = 122


class Cookie(ItemNPC):
    sprite_id = 254
    chest_packet = 120
    chest_event = 893
    static_packet = 118
    falling_packet = 119


class Beetle(ItemNPC):
    sprite_id = 255
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    chest_packet = 193
    chest_event = 917
    static_packet = 191
    falling_packet = 192


jagger_recoil = SpriteAnimation(sequence_id=2, total_duration=18)
jagger_look = SpriteAnimation(sequence_id=8)
jagger_punch = SpriteAnimation(sequence_id=4, contact_frame=54, total_duration=74)
jagger_taunt = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=38)


class Terrapin(NPC):
    sprite_id = 256
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        bandits_way_distracted=jagger_look,
        mines_punch=jagger_punch,
        chapel_laugh=jagger_look,
        ship_beckon=jagger_taunt,
        dojo_challenge=jagger_punch,
        statue_intro=jagger_look,
        statue_peck=jagger_taunt,
        statue_flustered=jagger_recoil,
        keep_challenge=jagger_punch,
        keep_summon=jagger_punch,
        chandelier_challenge=jagger_punch,
        endgame_challenge=jagger_punch)


class Spikey(NPC):
    sprite_id = 257
    acute_axis = 5
    obtuse_axis = 5
    height = 9
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


class SkyTroopa(NPC):
    sprite_id = 258
    acute_axis = 6
    obtuse_axis = 6
    height = 10
    y_shift = 2
    directions = VramStore._00_SWSE_NWNE


hammer_hit = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=36)


class HammerNPC(NPC):
    acute_axis = 4
    obtuse_axis = 4
    height = 9
    y_shift = -1
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        tower_bullet=hammer_hit, kitchen_prep=hammer_hit, factory_pierce=hammer_hit
    )


class MadMallet(HammerNPC):
    sprite_id = 259


class Shaman(NPC):
    sprite_id = 260
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    y_shift = -1
    directions = VramStore._00_SWSE_NWNE


crook_scratch = SpriteAnimation(sequence_id=4, total_duration=20, contact_frame=10)


class Crook(NPC):
    sprite_id = 261
    acute_axis = 6
    obtuse_axis = 6
    height = 7
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1

    animations = SpriteAnimationCollection(
        tower_bullet=crook_scratch,
        kitchen_prep=crook_scratch,
        factory_pierce=crook_scratch)


class Goomba(NPC):
    sprite_id = 262
    acute_axis = 4
    obtuse_axis = 4
    height = 8
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


piranha_taunt = SpriteAnimation(sequence_id=4, total_duration=16)
piranha_bite = SpriteAnimation(sequence_id=3, contact_frame=20, total_duration=52)
piranha_recoil = SpriteAnimation(sequence_id=2, total_duration=20)


class PiranhaPlant(NPC):
    sprite_id = 263
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 1

    animations = SpriteAnimationCollection(
        recoil=piranha_recoil,
        bandits_way_distracted=piranha_taunt,
        mines_punch=piranha_bite,
        chapel_laugh=piranha_taunt,
        ship_beckon=piranha_taunt,
        dojo_challenge=piranha_bite,
        statue_intro=piranha_bite,
        statue_peck=piranha_bite,
        statue_flustered=piranha_recoil,
        keep_challenge=piranha_bite,
        keep_summon=piranha_bite,
        chandelier_challenge=piranha_bite,
        endgame_challenge=piranha_bite)
    eye_height = 14


class Amanita(NPC):
    sprite_id = 264
    acute_axis = 5
    obtuse_axis = 5
    height = 9
    y_shift = 1


class Goby(NPC):
    sprite_id = 265
    acute_axis = 6
    obtuse_axis = 6
    height = 9
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


squid_recoil = SpriteAnimation(sequence_id=2, total_duration=16)
squid_hit = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
squid_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=SequenceSpeeds.FAST
)


class Bloober(NPC):
    sprite_id = 266
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = -2

    animations = SpriteAnimationCollection(
        tower_bullet=squid_hit,
        recoil=squid_recoil,
        mines_punch=squid_hit,
        dojo_challenge=squid_hit,
        statue_peck=squid_hit_fast,
        statue_flustered=squid_recoil,
        keep_challenge=squid_hit,
        keep_summon=squid_hit,
        chandelier_challenge=squid_hit,
        endgame_challenge=squid_hit)
    eye_height = 10


bandana_attack = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=50)
bandana_taunt = SpriteAnimation(sequence_id=4, total_duration=36)


class BandanaRed(NPC):
    sprite_id = 267
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    y_shift = 2
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1

    animations = SpriteAnimationCollection(
        tower_bullet=bandana_taunt,
        kitchen_prep=bandana_attack,
        factory_pierce=bandana_attack)


class Lakitu(NPC):
    sprite_id = 268
    acute_axis = 7
    obtuse_axis = 7
    height = 11
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


bird_attack = SpriteAnimation(sequence_id=3, contact_frame=24, total_duration=36)


class ValentinaBird(NPC):
    acute_axis = 5
    obtuse_axis = 5
    height = 10
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        tower_bullet=bird_attack, kitchen_prep=bird_attack, factory_pierce=bird_attack
    )


class Birdy(ValentinaBird):
    sprite_id = 269


class Pinwheel(NPC):
    sprite_id = 270
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 4


class RatFunk(NPC):
    sprite_id = 271
    acute_axis = 4
    obtuse_axis = 4
    height = 9
    directions = VramStore._00_SWSE_NWNE


class K9(NPC):
    sprite_id = 272
    acute_axis = 6
    obtuse_axis = 6
    height = 11
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


class Magmite(NPC):
    sprite_id = 273
    acute_axis = 5
    obtuse_axis = 5
    height = 7
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


class BigBoo(NPC):
    sprite_id = 274
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    y_shift = 3
    directions = VramStore._00_SWSE_NWNE


class DryBones(NPC):
    sprite_id = 275
    acute_axis = 5
    obtuse_axis = 5
    y_shift = 1
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


class Greaper(NPC):
    sprite_id = 276
    acute_axis = 8
    obtuse_axis = 8
    height = 11
    y_shift = 3
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


fireball_spin = SpriteAnimation(sequence_id=3, contact_frame=40, total_duration=62)
fireball_recoil = SpriteAnimation(sequence_id=2, total_duration=12)
fireball_spin_fast = SpriteAnimation(
    sequence_id=3, contact_frame=20, total_duration=31, speed=SequenceSpeeds.FAST
)


class Fireball(NPC):
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 3

    animations = SpriteAnimationCollection(
        tower_bullet=fireball_spin,
        kitchen_prep=fireball_spin,
        factory_pierce=fireball_spin_fast)


class RedFireball(Fireball):
    sprite_id = 277


class Chomp(NPC):
    sprite_id = 278
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 9
    obtuse_axis = 9
    height = 9
    min_vram_size = 2


class MimicLarge(NPC):
    shadow_size = ShadowSize._03_BLOCK
    y_shift = 3
    acute_axis = 7
    obtuse_axis = 7
    height = 12
    min_vram_size = 1


pandorite_attack = SpriteAnimation(sequence_id=3, contact_frame=70, total_duration=80)
pandorite_short = SpriteAnimation(sequence_id=3, contact_frame=8, total_duration=80)
mimic_shake = SpriteAnimation(sequence_id=4, total_duration=58)
mimic_recoil = SpriteAnimation(sequence_id=2, total_duration=12)


class PandoriteLarge(MimicLarge):
    sprite_id = 279

    animations = SpriteAnimationCollection(
        mines_punch=pandorite_attack,
        statue_intro=mimic_shake,
        statue_peck=pandorite_short,
        statue_flustered=mimic_recoil,
        chandelier_challenge=pandorite_attack,
        endgame_challenge=pandorite_attack)


bomb_tick = SpriteAnimation(sequence_id=4)
bomb_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class BobOmb(NPC):
    sprite_id = 281
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        tower_bullet=bomb_tick, kitchen_prep=bomb_tick, factory_pierce=bomb_tick
    )


class Spookum(NPC):
    sprite_id = 282
    y_shift = 2
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    directions = VramStore._00_SWSE_NWNE


hammer_bro_bop = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
hammer_bro_bop_fast = SpriteAnimation(
    sequence_id=3, contact_frame=16, total_duration=21, speed=SequenceSpeeds.FAST
)
hammer_bro_taunt = SpriteAnimation(sequence_id=5, total_duration=20)
hammer_bro_recoil = SpriteAnimation(sequence_id=2, total_duration=12)


class HammerBroLarge(NPC):
    sprite_id = 283
    y_shift = 1
    acute_axis = 8
    obtuse_axis = 7
    height = 19
    min_vram_size = 3

    animations = SpriteAnimationCollection(
        mines_punch=hammer_bro_bop,
        statue_intro=hammer_bro_taunt,
        statue_peck=hammer_bro_bop_fast,
        statue_flustered=hammer_bro_recoil,
        chandelier_challenge=hammer_bro_taunt,
        endgame_challenge=hammer_bro_taunt)


class Buzzer(NPC):
    sprite_id = 284
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 2
    min_vram_size = 1


class Ameboid(NPC):
    sprite_id = 285
    acute_axis = 5
    obtuse_axis = 5
    height = 8
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


class Gecko(NPC):
    sprite_id = 286
    acute_axis = 7
    obtuse_axis = 7
    height = 5
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1


class Wiggler(NPC):
    sprite_id = 287
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 4
    obtuse_axis = 8
    height = 13
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 2


class Jawful(NPC):
    sprite_id = 291
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13
    min_vram_size = 3


class Guerrilla(NPC):
    sprite_id = 294
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = -1
    acute_axis = 13
    obtuse_axis = 13
    height = 19
    min_vram_size = 5


class Shogun(NPC):
    sprite_id = 298
    acute_axis = 7
    obtuse_axis = 7
    height = 10
    min_vram_size = 3


class HeavyTropa(NPC):
    sprite_id = 300
    shadow_size = ShadowSize._02_OVAL_BIG
    acute_axis = 10
    obtuse_axis = 13
    height = 15
    min_vram_size = 2


shovelknight_attack = SpriteAnimation(
    sequence_id=3, contact_frame=16, total_duration=22, speed=SequenceSpeeds.FAST
)
shovelknight_taunt = SpriteAnimation(sequence_id=4, total_duration=44)
shovelknight_recoil = SpriteAnimation(sequence_id=2, total_duration=24)
shovelknight_alt_taunt = SpriteAnimation(sequence_id=5)


class ShovelKnightBossLarge(NPC):
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = -1
    acute_axis = 7
    obtuse_axis = 7
    height = 13
    min_vram_size = 7

    animations = SpriteAnimationCollection(
        mines_punch=shovelknight_attack,
        statue_peck=shovelknight_attack,
        statue_intro=shovelknight_alt_taunt,
        statue_flustered=shovelknight_recoil,
        chandelier_challenge=shovelknight_taunt,
        endgame_challenge=shovelknight_taunt)


class ClerkLarge(ShovelKnightBossLarge):
    sprite_id = 702


boomer_hit = SpriteAnimation(sequence_id=3, contact_frame=42, total_duration=52)
boomer_taunt = SpriteAnimation(sequence_id=4, total_duration=48)
boomer_recoil = SpriteAnimation(sequence_id=2, total_duration=18)


class BoomerLarge(NPC):
    sprite_id = 701
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 2
    acute_axis = 9
    obtuse_axis = 9
    height = 22
    min_vram_size = 3

    animations = SpriteAnimationCollection(
        # mines_punch=boomer_hit, # vram issues
        statue_intro=boomer_taunt,
        # statue_peck=boomer_hit, # vram issues
        statue_flustered=boomer_recoil,
        chandelier_challenge=boomer_taunt,
        endgame_challenge=boomer_taunt)


dodo_peck = SpriteAnimation(sequence_id=3, contact_frame=16, total_duration=22)
dodo_taunt = SpriteAnimation(sequence_id=4, total_duration=66)


class DodoLarge(NPC):
    sprite_id = 695
    shadow_size = ShadowSize._02_OVAL_BIG
    acute_axis = 9
    obtuse_axis = 9
    height = 14
    min_vram_size = 3
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        mines_punch=dodo_peck,
        statue_intro=dodo_taunt,
        statue_flustered=dodo_taunt,
        statue_peck=dodo_peck,
        chandelier_challenge=dodo_taunt,
        endgame_challenge=dodo_taunt)


class TerraCotta(NPC):
    sprite_id = 320
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    y_shift = 1


class Spikester(NPC):
    sprite_id = 321
    acute_axis = 5
    obtuse_axis = 5
    height = 9
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


class Malakoopa(NPC):
    sprite_id = 322
    acute_axis = 6
    obtuse_axis = 6
    height = 10
    y_shift = 2
    directions = VramStore._00_SWSE_NWNE


class Pounder(HammerNPC):
    sprite_id = 323


class Poundette(HammerNPC):
    sprite_id = 324


class Sackit(NPC):
    sprite_id = 325
    acute_axis = 6
    obtuse_axis = 6
    height = 7
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1


class GuGoomba(NPC):
    sprite_id = 326
    acute_axis = 4
    obtuse_axis = 4
    height = 8
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


class Chewy(NPC):
    sprite_id = 327
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 1


class BlueFireball(Fireball):
    sprite_id = 328


class MrKipper(NPC):
    sprite_id = 329
    acute_axis = 6
    obtuse_axis = 6
    height = 9
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


ninja_hit = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=38)
ninja_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=13, total_duration=19)
ninja_taunt = SpriteAnimation(sequence_id=4, total_duration=54)
ninja_recoil = SpriteAnimation(sequence_id=2, total_duration=14)


class FactoryChief(NPC):
    sprite_id = 330
    acute_axis = 7
    obtuse_axis = 7
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE

    eye_height = 16
    animations = SpriteAnimationCollection(
        recoil=ninja_recoil,
        mines_punch=ninja_hit,
        chapel_laugh=ninja_taunt,
        ship_beckon=ninja_taunt,
        dojo_challenge=ninja_hit,
        statue_intro=ninja_taunt,
        statue_peck=ninja_hit_fast,
        statue_flustered=ninja_recoil,
        keep_challenge=ninja_hit,
        keep_summon=ninja_taunt,
        chandelier_challenge=ninja_hit,
        endgame_challenge=ninja_hit)


class BandanaBlue(NPC):
    sprite_id = 331
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    y_shift = 2
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1

    animations = SpriteAnimationCollection(
        tower_bullet=bandana_taunt,
        kitchen_prep=bandana_attack,
        factory_pierce=bandana_attack)


class ManagerLarge(ShovelKnightBossLarge):
    sprite_id = 703


class Bluebird(ValentinaBird):
    sprite_id = 333


class AlleyRat(NPC):
    sprite_id = 335
    acute_axis = 4
    obtuse_axis = 4
    height = 9
    directions = VramStore._00_SWSE_NWNE


class Chow(NPC):
    sprite_id = 336
    acute_axis = 6
    obtuse_axis = 6
    height = 11
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


class Magmus(NPC):
    sprite_id = 337
    acute_axis = 5
    obtuse_axis = 5
    height = 7
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


class LilBoo(NPC):
    sprite_id = 338
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    y_shift = 3
    directions = VramStore._00_SWSE_NWNE


class Vomer(NPC):
    sprite_id = 339
    acute_axis = 5
    obtuse_axis = 5
    y_shift = 1
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


class GlumReaper(NPC):
    sprite_id = 340
    acute_axis = 8
    obtuse_axis = 8
    height = 11
    y_shift = 3
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


hidon_attack = SpriteAnimation(sequence_id=3, contact_frame=60, total_duration=60)
hidon_attack_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=30, speed=SequenceSpeeds.FAST
)


class HidonLarge(MimicLarge):
    sprite_id = 343
    animations = SpriteAnimationCollection(
        mines_punch=hidon_attack,
        statue_flustered=mimic_recoil,
        statue_peck=hidon_attack_fast,
        statue_intro=mimic_shake,
        chandelier_challenge=hidon_attack,
        endgame_challenge=hidon_attack)


class SlingShy(NPC):
    sprite_id = 344
    y_shift = 1
    height = 7
    directions = VramStore._00_SWSE_NWNE


class RobOmb(NPC):
    sprite_id = 345
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 10
    min_vram_size = 1
    directions = VramStore._00_SWSE_NWNE


shyguy_spin = SpriteAnimation(sequence_id=5)
shyguy_hit = SpriteAnimation(sequence_id=3, contact_frame=32, total_duration=40)
shyguy_taunt = SpriteAnimation(sequence_id=4, total_duration=110)
shyguy_recoil = SpriteAnimation(sequence_id=2, total_duration=14)


class ShyGuy(NPC):
    sprite_id = 346
    y_shift = 1
    height = 7
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        tower_bullet=shyguy_hit, kitchen_prep=shyguy_taunt, factory_pierce=shyguy_hit
    )


class Ninja(NPC):
    sprite_id = 347
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 2
    directions = VramStore._00_SWSE_NWNE


class Stinger(NPC):
    sprite_id = 348
    acute_axis = 5
    obtuse_axis = 5
    height = 11
    y_shift = 2
    min_vram_size = 1


class Geckit(NPC):
    sprite_id = 350
    acute_axis = 7
    obtuse_axis = 7
    height = 5
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1


class Jabit(NPC):
    sprite_id = 351
    y_shift = 2
    height = 11
    directions = VramStore._00_SWSE_NWNE


big_magikoopa_hit = SpriteAnimation(sequence_id=3, contact_frame=38, total_duration=62)
big_magikoopa_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=14, total_duration=32, speed=SequenceSpeeds.VERY_FAST
)
big_magikoopa_taunt = SpriteAnimation(sequence_id=4, total_duration=60)
big_magikoopa_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class MagikoopaLarge(NPC):
    sprite_id = 353
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13
    min_vram_size = 2

    animations = SpriteAnimationCollection(
        mines_punch=big_magikoopa_hit,
        statue_intro=big_magikoopa_taunt,
        statue_peck=big_magikoopa_hit_fast,
        statue_flustered=big_magikoopa_recoil,
        chandelier_challenge=big_magikoopa_taunt,
        endgame_challenge=big_magikoopa_taunt)


class DirectorLarge(ShovelKnightBossLarge):
    sprite_id = 704


snifit_shoot = SpriteAnimation(sequence_id=4, total_duration=60)
snifit_taunt = SpriteAnimation(sequence_id=5, contact_frame=30, total_duration=46)
snifit_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class Apprentice(NPC):
    sprite_id = 384
    y_shift = 2
    acute_axis = 4
    obtuse_axis = 4
    height = 9
    directions = VramStore._00_SWSE_NWNE
    byte5_bit6 = True
    byte5_bit7 = True
    byte6_bit2 = True

    animations = SpriteAnimationCollection(
        tower_bullet=snifit_shoot,
        kitchen_prep=snifit_taunt,
        factory_pierce=snifit_taunt)


class GenoRedemption(NPC):
    sprite_id = 388
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    min_vram_size = 1


boxboy_attack = SpriteAnimation(sequence_id=3, contact_frame=76, total_duration=98)
boxboy_short = SpriteAnimation(sequence_id=3, contact_frame=8, total_duration=98)


class BoxBoyLarge(MimicLarge):
    sprite_id = 390

    animations = SpriteAnimationCollection(
        mines_punch=boxboy_attack,
        statue_intro=mimic_shake,
        statue_peck=boxboy_short,
        statue_flustered=mimic_recoil,
        chandelier_challenge=boxboy_attack,
        endgame_challenge=boxboy_attack)


class Oerlikon(NPC):
    sprite_id = 394
    acute_axis = 5
    obtuse_axis = 5
    height = 9
    y_shift = 1
    directions = VramStore._00_SWSE_NWNE


chester_attack = SpriteAnimation(sequence_id=3, contact_frame=50, total_duration=64)
chester_attack_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=26
)


class ChesterLarge(MimicLarge):
    sprite_id = 395

    animations = SpriteAnimationCollection(
        mines_punch=chester_attack,
        statue_intro=mimic_shake,
        statue_peck=chester_attack_fast,
        statue_flustered=mimic_recoil,
        chandelier_challenge=chester_attack,
        endgame_challenge=chester_attack)


torte_taunt = SpriteAnimation(sequence_id=3, total_duration=40)
torte_taunt_fast = SpriteAnimation(
    sequence_id=3, total_duration=20, speed=SequenceSpeeds.FAST
)


class Torte(NPC):
    sprite_id = 398
    acute_axis = 2
    obtuse_axis = 2
    height = 11
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        tower_bullet=torte_taunt,
        kitchen_prep=torte_taunt,
        factory_pierce=torte_taunt_fast)


class ShyAway(NPC):
    sprite_id = 399
    acute_axis = 6
    obtuse_axis = 6
    height = 10
    directions = VramStore._00_SWSE_NWNE
    min_vram_size = 1


class MachineShyster(NPC):
    sprite_id = 401
    y_shift = 1
    height = 11
    directions = VramStore._00_SWSE_NWNE
    shadow_size = ShadowSize._00_OVAL_SMALL


class MachineDrillBit(NPC):
    sprite_id = 402
    y_shift = 2
    height = 11
    directions = VramStore._00_SWSE_NWNE
    shadow_size = ShadowSize._00_OVAL_SMALL


class CloneNPC(NPC):
    directions = VramStore._00_SWSE_NWNE
    byte5_bit6 = True
    byte5_bit7 = True
    byte6_bit2 = True


marioclone_hit_fast = SpriteAnimation(
    sequence_id=0, contact_frame=8, total_duration=16, speed=SequenceSpeeds.FAST
)


class MarioClone(CloneNPC):
    sprite_id = 409
    y_shift = 1
    animations = SpriteAnimationCollection(
        kitchen_prep=marioclone_hit_fast, factory_pierce=marioclone_hit_fast
    )


peachclone_mad = SpriteAnimation(sequence_id=4, contact_frame=12, total_duration=24)


class PeachClone(CloneNPC):
    sprite_id = 410
    y_shift = 1

    animations = SpriteAnimationCollection(
        tower_bullet=peachclone_mad,
        kitchen_prep=peachclone_mad,
        factory_pierce=peachclone_mad)


bowserclone_laugh = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
bowserclone_mad = SpriteAnimation(sequence_id=4, contact_frame=12, total_duration=24)


class BowserClone(CloneNPC):
    sprite_id = 411
    shadow_size = ShadowSize._02_OVAL_BIG
    acute_axis = 6
    obtuse_axis = 6
    height = 14
    y_shift = -2

    animations = SpriteAnimationCollection(
        tower_bullet=bowserclone_laugh,
        kitchen_prep=bowserclone_mad,
        factory_pierce=bowserclone_mad)


genoclone_laugh = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
genoclone_mad = SpriteAnimation(sequence_id=4, contact_frame=6, total_duration=12)


class GenoClone(CloneNPC):
    sprite_id = 412
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4

    animations = SpriteAnimationCollection(
        tower_bullet=genoclone_laugh,
        kitchen_prep=genoclone_mad,
        factory_pierce=genoclone_mad)


mallowclone_laugh = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
mallowclone_mad = SpriteAnimation(sequence_id=4, contact_frame=8, total_duration=16)


class MallowClone(CloneNPC):
    sprite_id = 413
    height = 8

    animations = SpriteAnimationCollection(
        tower_bullet=mallowclone_laugh,
        kitchen_prep=mallowclone_mad,
        factory_pierce=mallowclone_mad)


shyster_taunt = SpriteAnimation(sequence_id=4, contact_frame=56, total_duration=56)
shyster_fast = SpriteAnimation(
    sequence_id=4, contact_frame=28, total_duration=28, speed=SequenceSpeeds.FAST
)
shyster_recoil = SpriteAnimation(sequence_id=2, total_duration=14)


class Shyster(NPC):
    sprite_id = 414
    y_shift = 1
    height = 11
    directions = VramStore._00_SWSE_NWNE
    shadow_size = ShadowSize._00_OVAL_SMALL

    animations = SpriteAnimationCollection(
        tower_bullet=shyster_taunt,
        kitchen_prep=shyster_taunt,
        factory_pierce=shyster_fast)


class HanginShy(NPC):
    sprite_id = 417
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    min_vram_size = 1


class MachineMack(NPC):
    sprite_id = 419
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 23
    min_vram_size = 3


axem_green_hit = SpriteAnimation(sequence_id=3, contact_frame=56, total_duration=84)
axem_green_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=28, total_duration=42, speed=SequenceSpeeds.FAST
)
axem_yellow_hit = SpriteAnimation(sequence_id=3, contact_frame=82, total_duration=108)
axem_yellow_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=41, total_duration=54, speed=SequenceSpeeds.FAST
)
axem_black_hit = SpriteAnimation(sequence_id=3, contact_frame=16, total_duration=64)
axem_pink_hit = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=58)
axem_red_hit = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=66)
axem_red_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=13, total_duration=33, speed=SequenceSpeeds.FAST
)
axem_red_taunt = SpriteAnimation(sequence_id=4, total_duration=120)
axem_red_recoil = SpriteAnimation(sequence_id=2, total_duration=22)


class MachineAxemPink(NPC):
    sprite_id = 422
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_pink_hit,
        kitchen_prep=axem_pink_hit,
        factory_pierce=axem_pink_hit)


class MachineAxemBlack(NPC):
    sprite_id = 423
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_black_hit,
        kitchen_prep=axem_black_hit,
        factory_pierce=axem_black_hit)


class MachineAxemRed(NPC):
    sprite_id = 424
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_red_hit,
        kitchen_prep=axem_red_hit,
        factory_pierce=axem_red_hit)


class MachineAxemYellow(NPC):
    sprite_id = 425
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_yellow_hit_fast, kitchen_prep=axem_yellow_hit
    )


class MachineAxemGreen(NPC):
    sprite_id = 426
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_green_hit,
        kitchen_prep=axem_green_hit,
        factory_pierce=axem_green_hit_fast)


class Starslap(NPC):
    sprite_id = 432
    y_shift = -4
    acute_axis = 6
    obtuse_axis = 6
    height = 6


class Mukumuku(NPC):
    sprite_id = 433
    y_shift = 3
    acute_axis = 4
    obtuse_axis = 4
    height = 9


class Zeostar(NPC):
    sprite_id = 434
    y_shift = -4
    acute_axis = 6
    obtuse_axis = 6
    height = 6


class Microbomb(NPC):
    sprite_id = 440
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 2
    obtuse_axis = 2
    height = 3

    animations = SpriteAnimationCollection(
        tower_bullet=bomb_tick, kitchen_prep=bomb_tick, factory_pierce=bomb_tick
    )


class Helio(NPC):
    sprite_id = 445
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False


class KnifeGuyLarge(NPC):
    sprite_id = 689
    min_vram_size = 3
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 11
    obtuse_axis = 11
    height = 13


grate_guy_hit = SpriteAnimation(sequence_id=4, contact_frame=52, total_duration=62)
grate_guy_hit_fast = SpriteAnimation(
    sequence_id=4, contact_frame=14, total_duration=17, speed=SequenceSpeeds.VERY_FAST
)
grate_guy_taunt = SpriteAnimation(sequence_id=3, total_duration=64)
grate_guy_recoil = SpriteAnimation(sequence_id=2, total_duration=20)


class GrateGuyLarge(NPC):
    sprite_id = 690
    min_vram_size = 3
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 11
    obtuse_axis = 11
    height = 13

    animations = SpriteAnimationCollection(
        mines_punch=grate_guy_hit,
        statue_intro=grate_guy_taunt,
        statue_peck=grate_guy_hit_fast,
        statue_flustered=grate_guy_recoil,
        chandelier_challenge=grate_guy_taunt,
        endgame_challenge=grate_guy_taunt)


bundt_recoil = SpriteAnimation(sequence_id=2, total_duration=30)
bundt_taunt = SpriteAnimation(sequence_id=4, contact_frame=74, total_duration=82)
bundt_short = SpriteAnimation(
    sequence_id=4, contact_frame=13, total_duration=16, speed=SequenceSpeeds.FASTEST
)


class BundtLarge(NPC):
    sprite_id = 450
    min_vram_size = 3
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 23

    animations = SpriteAnimationCollection(
        mines_punch=bundt_taunt,
        statue_intro=bundt_taunt,
        statue_flustered=bundt_recoil,
        chandelier_challenge=bundt_taunt,
        endgame_challenge=bundt_taunt)


class Belome1Large(NPC):
    sprite_id = 687
    min_vram_size = 5
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 2
    acute_axis = 10
    obtuse_axis = 10
    height = 18

    animations = SpriteAnimationCollection(
        mines_punch=belome_attack,
        statue_intro=belome_wiggle,
        statue_flustered=belome_recoil,
        statue_peck=belome_attack_fast,
        chandelier_challenge=belome_attack,
        endgame_challenge=belome_attack)


class Smilax(NPC):
    sprite_id = 458
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 7


class Thrax(NPC):
    sprite_id = 459
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 7


megasmilax_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
megasmilax_bite = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=28)
megasmilax_taunt = SpriteAnimation(sequence_id=4, total_duration=38)


class Megasmilax(NPC):
    sprite_id = 460
    min_vram_size = 3
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 11
    obtuse_axis = 11
    height = 13

    animations = SpriteAnimationCollection(
        mines_punch=megasmilax_bite,
        statue_flustered=megasmilax_recoil,
        statue_peck=megasmilax_bite,
        chandelier_challenge=megasmilax_taunt,
        endgame_challenge=megasmilax_taunt)


birdetta_attack = SpriteAnimation(sequence_id=3, contact_frame=40, total_duration=50)
birdetta_attack_fast = SpriteAnimation(
    sequence_id=3, contact_frame=14, total_duration=18, speed=SequenceSpeeds.FASTEST
)
birdetta_recoil = SpriteAnimation(sequence_id=2, total_duration=18)
birdetta_taunt = SpriteAnimation(sequence_id=4, total_duration=48)


class BirdettaLarge(NPC):
    sprite_id = 461
    shadow_size = ShadowSize._02_OVAL_BIG
    min_vram_size = 4
    y_shift = 1
    acute_axis = 9
    obtuse_axis = 11
    height = 23

    animations = SpriteAnimationCollection(
        mines_punch=birdetta_attack,
        statue_flustered=birdetta_recoil,
        statue_peck=birdetta_attack_fast,
        statue_intro=birdetta_taunt,
        chandelier_challenge=birdetta_attack,
        endgame_challenge=birdetta_attack)


eggbert_expand = SpriteAnimation(sequence_id=2, total_duration=32)


class Eggbert(NPC):
    sprite_id = 462
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    acute_axis = 2
    obtuse_axis = 2
    height = 5

    animations = SpriteAnimationCollection(
        tower_bullet=eggbert_expand,
        kitchen_prep=eggbert_expand,
        factory_pierce=eggbert_expand)


class AxemYellow(NPC):
    sprite_id = 463
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_yellow_hit_fast, kitchen_prep=axem_yellow_hit
    )


punchinello_hit = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=34)
punchinello_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=14, total_duration=24, speed=SequenceSpeeds.FAST
)
punchinello_taunt = SpriteAnimation(sequence_id=4, total_duration=54)
punchinello_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
punchinello_jump = SpriteAnimation(sequence_id=5, total_duration=34)


class PunchinelloLarge(NPC):
    sprite_id = 464
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 11
    obtuse_axis = 8
    height = 19
    min_vram_size = 2

    animations = SpriteAnimationCollection(
        mines_punch=punchinello_hit,
        statue_intro=punchinello_jump,
        statue_peck=punchinello_hit_fast,
        statue_flustered=punchinello_recoil,
        chandelier_challenge=punchinello_taunt,
        endgame_challenge=punchinello_taunt)


class AxemRed(NPC):
    sprite_id = 466
    acute_axis = 5
    obtuse_axis = 5

    eye_height = 15
    animations = SpriteAnimationCollection(
        bandits_way_distracted=axem_red_taunt,
        mines_punch=axem_red_hit,
        ship_beckon=axem_red_hit,
        dojo_challenge=axem_red_taunt,
        statue_intro=axem_red_taunt,
        statue_peck=axem_red_hit_fast,
        statue_flustered=axem_red_recoil,
        keep_challenge=axem_red_taunt,
        keep_summon=axem_red_hit,
        chandelier_challenge=axem_red_taunt,
        endgame_challenge=axem_red_taunt)


class AxemGreen(NPC):
    sprite_id = 467
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_green_hit,
        kitchen_prep=axem_green_hit,
        factory_pierce=axem_green_hit_fast)


class BundtSmall(NPC):
    sprite_id = 712
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 8

    eye_height = 8


czar_dragon_hit = SpriteAnimation(sequence_id=3, contact_frame=56, total_duration=66)
czar_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
czar_taunt = SpriteAnimation(sequence_id=5)


class CzarDragonLarge(NPC):
    sprite_id = 698
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 10
    obtuse_axis = 10
    height = 18
    min_vram_size = 3

    animations = SpriteAnimationCollection(
        mines_punch=czar_dragon_hit,
        statue_intro=czar_taunt,
        statue_flustered=czar_recoil)


cloaker_hit = SpriteAnimation(sequence_id=3, contact_frame=38, total_duration=50)
cloaker_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class CloakerLarge(NPC):
    sprite_id = 477
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 8
    obtuse_axis = 8
    height = 17
    min_vram_size = 3

    animations = SpriteAnimationCollection(
        # mines_punch=cloaker_hit, # breaks vram
        # statue_peck=cloaker_hit, # breaks vram
        statue_flustered=cloaker_recoil,
        # chandelier_challenge=cloaker_hit, # breaks vram
        # endgame_challenge=cloaker_hit # breaks vram
    )


class DominoLarge(NPC):
    sprite_id = 478
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 8
    obtuse_axis = 8
    height = 17
    min_vram_size = 3

    animations = SpriteAnimationCollection(statue_flustered=cloaker_recoil)


mack_hit = SpriteAnimation(sequence_id=4, contact_frame=22, total_duration=28)
mack_hit_fast = SpriteAnimation(
    sequence_id=4, contact_frame=13, total_duration=16, speed=SequenceSpeeds.FAST
)
mack_challenge = SpriteAnimation(sequence_id=2, total_duration=12)


class MackLarge(NPC):
    sprite_id = 686
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 23
    min_vram_size = 3

    animations = SpriteAnimationCollection(
        mines_punch=mack_hit,
        statue_peck=mack_hit_fast,
        statue_flustered=mack_challenge,
        chandelier_challenge=mack_challenge,
        endgame_challenge=mack_hit)


yaridovich_hit = SpriteAnimation(sequence_id=3, contact_frame=78, total_duration=84)
yaridovich_taunt = SpriteAnimation(sequence_id=4, total_duration=40)
yaridovich_taunt_fast = SpriteAnimation(
    sequence_id=4, total_duration=40, contact_frame=15, speed=SequenceSpeeds.FAST
)
yaridovich_alt_taunt = SpriteAnimation(sequence_id=1, total_duration=48)
yaridovich_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class YaridovichLarge(NPC):
    sprite_id = 692
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 23
    min_vram_size = 7

    animations = SpriteAnimationCollection(
        mines_punch=yaridovich_hit,
        statue_intro=yaridovich_taunt,
        statue_flustered=yaridovich_recoil,
        chandelier_challenge=yaridovich_taunt,
        endgame_challenge=yaridovich_taunt)


drillbit_hit = SpriteAnimation(sequence_id=3, contact_frame=54, total_duration=64)
drillbit_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=27, total_duration=32, speed=SequenceSpeeds.FAST
)
drillbit_taunt = SpriteAnimation(sequence_id=4, total_duration=56)
drillbit_recoil = SpriteAnimation(sequence_id=2, total_duration=14)


class DrillBit(NPC):
    sprite_id = 483
    y_shift = 2
    height = 11
    directions = VramStore._00_SWSE_NWNE
    shadow_size = ShadowSize._00_OVAL_SMALL

    animations = SpriteAnimationCollection(
        tower_bullet=drillbit_hit,
        kitchen_prep=drillbit_hit,
        factory_pierce=drillbit_hit_fast)


class AxemPink(NPC):
    sprite_id = 484
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_pink_hit,
        kitchen_prep=axem_pink_hit,
        factory_pierce=axem_pink_hit)


class AxemBlack(NPC):
    sprite_id = 485
    acute_axis = 5
    obtuse_axis = 5

    animations = SpriteAnimationCollection(
        tower_bullet=axem_black_hit,
        kitchen_prep=axem_black_hit,
        factory_pierce=axem_black_hit)


bowyer_hit = SpriteAnimation(sequence_id=3, contact_frame=76, total_duration=82)
bowyer_taunt = SpriteAnimation(sequence_id=4, total_duration=62)
bowyer_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class BowyerLarge(NPC):
    sprite_id = 688
    y_shift = 1
    acute_axis = 14
    obtuse_axis = 15
    height = 16
    min_vram_size = 5
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False

    animations = SpriteAnimationCollection(
        mines_punch=bowyer_hit,
        statue_intro=bowyer_taunt,
        statue_flustered=bowyer_recoil,
        chandelier_challenge=bowyer_taunt,
        endgame_challenge=bowyer_taunt)


class AeroUpright(NPC):
    sprite_id = 487
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 3
    obtuse_axis = 3
    height = 13
    y_shift = 1


class Snifit(NPC):
    sprite_id = 504
    y_shift = 2
    acute_axis = 4
    obtuse_axis = 4
    height = 9
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        tower_bullet=snifit_shoot,
        kitchen_prep=snifit_taunt,
        factory_pierce=snifit_taunt)


johnny_hit = SpriteAnimation(sequence_id=3, contact_frame=48, total_duration=84)
johnny_taunt = SpriteAnimation(sequence_id=4, total_duration=62)
johnny_recoil = SpriteAnimation(sequence_id=2, total_duration=16)


class JohnnyLarge(NPC):
    sprite_id = 691
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 23
    min_vram_size = 7

    animations = SpriteAnimationCollection(
        mines_punch=johnny_hit,
        chandelier_challenge=johnny_taunt,
        endgame_challenge=johnny_taunt)


class ValentinaLarge(NPC):
    sprite_id = 697
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 23
    min_vram_size = 5

    animations = SpriteAnimationCollection(
        # mines_punch=valentina_hit,
        statue_intro=valentina_taunt,
        # statue_peck=valentina_hit,
        statue_flustered=valentina_recoil,
        chandelier_challenge=valentina_taunt,
        endgame_challenge=valentina_taunt)


class CulexLarge(NPC):
    sprite_id = 694
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 31
    min_vram_size = 7


class CountDownGridplane(NPC):
    sprite_id = 572
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 11
    obtuse_axis = 11
    height = 13


class MokuraLarge(NPC):
    sprite_id = 573
    show_shadow = False
    y_shift = 2
    acute_axis = 10
    obtuse_axis = 10
    height = 18
    shadow_size = ShadowSize._00_OVAL_SMALL
    min_vram_size = 5


class PandoriteSmall(MimicFace):
    sprite_id = 583
    y_shift = 1

    alt_palette = [
        "F8F0D8",
        "F8F860",
        "F8E860",
        "00F8A8",
        "F8E800",
        "F8E0B0",
        "F0B888",
        "E0A030",
        "F8C048",
        "C87000",
        "E80000",
        "984000",
        "089000",
        "085800",
        "783800",
    ]


class HidonSmall(MimicFace):
    sprite_id = 584
    y_shift = 1
    alt_palette = [
        "F8F0D8",
        "F8F860",
        "F8E860",
        "00F8A8",
        "F8E800",
        "F8E0B0",
        "F0B888",
        "E0A030",
        "A0F800",
        "10A010",
        "E80000",
        "106800",
        "089000",
        "085800",
        "004000",
    ]


class ChesterSmall(MimicFace):
    sprite_id = 585
    y_shift = 1

    alt_palette = [
        "F8F0D8",
        "F8F860",
        "F8E860",
        "00F8A8",
        "F8E800",
        "F8E0B0",
        "F0B888",
        "E0A030",
        "C8A880",
        "A070B0",
        "E80000",
        "603068",
        "089000",
        "085800",
        "481040",
    ]


class BoxBoySmall(MimicFace):
    sprite_id = 586
    y_shift = 1

    alt_palette = [
        "F8F0D8",
        "F8F860",
        "F8E860",
        "00F8A8",
        "F8E800",
        "F8E0B0",
        "F0B888",
        "E0A030",
        "707870",
        "484040",
        "E80000",
        "384038",
        "089000",
        "085800",
        "181818",
    ]


class HammerBroSmall(NPC):
    sprite_id = 587
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13
    eye_height = 6


class MackSmall(NPC):
    sprite_id = 588
    y_shift = 1

    eye_height = 19


class Belome1Small(NPC):
    sprite_id = 589
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13


class Belome2Small(NPC):
    sprite_id = 590
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13
    alt_palette = [
        "F8D008",
        "F8A008",
        "F8F888",
        "984000",
        "F8F8F8",
        "181818",
        "F8B010",
        "401800",
        "F8D008",
        "F8F8B0",
        "582000",
        "C88008",
        "F8D060",
        "582000",
        "200000",
    ]


class BowyerSmall(NPC):
    sprite_id = 591
    y_shift = 1

    eye_height = 16


class PunchinelloSmall(NPC):
    sprite_id = 592
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13


class DodoSmall(NPC):
    sprite_id = 593
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13


class BirdettaSmall(NPC):
    sprite_id = 594
    y_shift = 1

    eye_height = 6


class CzarDragonSmall(NPC):
    sprite_id = 595
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13

    eye_height = 3


class BoomerSmall(NPC):
    sprite_id = 596
    y_shift = 1


class ExorSmall(NPC):
    sprite_id = 597
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13


class DominoSmall(NPC):
    sprite_id = 598
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13


class SmithySmall(NPC):
    sprite_id = 599
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 13


class MarioDoll(NPC):
    sprite_id = 600
    shadow_size = ShadowSize._00_OVAL_SMALL
    directions = VramStore._00_SWSE_NWNE
    acute_axis = 1
    obtuse_axis = 1
    height = 3
    y_shift = 1


class GoldGoomba(NPC):
    sprite_id = 602
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 10


class BigFlower(ItemNPC):
    sprite_id = 605
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    chest_packet = 0
    static_packet = 86
    falling_packet = 35
    chest_70A7_upper = 2


class SmallFrogCoin(Coin):
    sprite_id = 606
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    chest_packet = 19
    static_packet = 111
    falling_packet = 108
    chest_70A7_upper = 3
    acute_axis = 2
    obtuse_axis = 2
    height = 3
    min_vram_size = 1


class Jinx1(Jinx):
    sprite_id = 607


class Jinx3(Jinx):
    sprite_id = 608

    alt_palette = [
        "F8F8F8",
        "E0B068",
        "985040",
        "682848",
        "682848",
        "C00000",
        "C00000",
        "300000",
        "F8F800",
        "D0D0D0",
        "707070",
        "181818",
        "E0D8D8",
        "988888",
        "181818",
    ]


class TerrapinEnding(NPC):
    sprite_id = 609
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 11
    directions = VramStore._00_SWSE_NWNE


class StumpetHead(NPC):
    sprite_id = 610
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 10
    obtuse_axis = 10
    height = 18
    min_vram_size = 3


class StumpetRoot(NPC):
    sprite_id = 611
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 7
    obtuse_axis = 7
    height = 3


class CzarBody(NPC):
    sprite_id = 612
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 10
    obtuse_axis = 10
    height = 18
    min_vram_size = 3


class VineBeanstalk(NPC):
    sprite_id = 613
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 1
    obtuse_axis = 1
    height = 1
    min_vram_size = 3


class BrownBrick(NPC):
    sprite_id = 614
    show_shadow = False
    shadow_size = ShadowSize._03_BLOCK
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 7


class SandWhirlpool(NPC):
    sprite_id = 615
    y_shift = 1
    acute_axis = 9
    obtuse_axis = 9
    height = 0
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    min_vram_size = 1


class Letter(NPC):
    sprite_id = 616
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 4
    obtuse_axis = 4
    height = 7


class YaridOverworld(NPC):
    sprite_id = 617
    y_shift = 1
    acute_axis = 11
    obtuse_axis = 11
    height = 15
    min_vram_size = 2

    animations = SpriteAnimationCollection(
        chandelier_challenge=yaridovich_alt_taunt,
        endgame_challenge=yaridovich_alt_taunt)
    # may need adjusting


tentacle_beckon = SpriteAnimation(sequence_id=1, new_sprite_id=223)


class TentacleExtending(NPC):
    sprite_id = 618
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 2
    obtuse_axis = 9
    height = 5
    min_vram_size = 1

    animations = SpriteAnimationCollection(ship_beckon=tentacle_beckon)


class BackSnifit(NPC):
    sprite_id = 619
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5
    height = 11


class DonutLift(NPC):
    sprite_id = 620
    shadow_size = ShadowSize._03_BLOCK
    y_shift = -1
    acute_axis = 7
    obtuse_axis = 7
    height = 7


class NESProtagonist(NPC):
    sprite_id = 621
    height = 1


class SplashWaterDroplets(NPC):
    sprite_id = 623
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 2
    obtuse_axis = 2
    height = 3


class Fish(NPC):
    sprite_id = 624
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 2
    obtuse_axis = 2
    height = 3


class Geyser(NPC):
    sprite_id = 625
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


class BowyerOverworld(NPC):
    sprite_id = 626
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 6
    obtuse_axis = 8
    height = 16
    min_vram_size = 3


class MushroomLamp(NPC):
    sprite_id = 627
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5
    height = 3


class Link(NPC):
    sprite_id = 628
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5
    height = 2


class Samus(NPC):
    sprite_id = 629
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5
    height = 2


class GreyBlock(NPC):
    sprite_id = 630
    shadow_size = ShadowSize._03_BLOCK
    y_shift = -2
    acute_axis = 6
    obtuse_axis = 6
    height = 4


class PlaneModel(NPC):
    sprite_id = 631
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 3
    obtuse_axis = 3
    height = 6


class GreyBrick(NPC):
    sprite_id = 632
    shadow_size = ShadowSize._03_BLOCK
    y_shift = -3
    acute_axis = 7
    obtuse_axis = 7
    height = 7


class CulexSmall(NPC):
    sprite_id = 633
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7
    height = 11

    eye_height = 12


class CircularSparkle(NPC):
    sprite_id = 635
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


class Flower(ItemNPC):
    sprite_id = 636
    y_shift = 1
    chest_packet = 0
    static_packet = 86
    falling_packet = 35
    chest_70A7_upper = 2


class RecoveryMushroom(ItemNPC):
    sprite_id = 637
    y_shift = 1
    chest_packet = 1
    static_packet = 87
    falling_packet = 36


class Key(ItemNPC):
    sprite_id = 638
    y_shift = 1
    chest_packet = 2
    static_packet = 88
    falling_packet = 89
    chest_event = 882


class ItemBag(ItemNPC):
    sprite_id = 639
    y_shift = 1


class Music(ItemNPC):
    sprite_id = 640
    y_shift = 1
    chest_packet = 168
    static_packet = 166
    falling_packet = 167
    chest_event = 909


class TinyMushroom(NPC):
    sprite_id = 641
    shadow_size = ShadowSize._00_OVAL_SMALL


dingaling_attack = SpriteAnimation(sequence_id=4, contact_frame=32, total_duration=44)
dingaling_attack_fast = SpriteAnimation(
    sequence_id=4, contact_frame=16, total_duration=22, speed=SequenceSpeeds.FAST
)
dingaling_taunt = SpriteAnimation(sequence_id=7, total_duration=62)
dingaling_circle = SpriteAnimation(sequence_id=3, contact_frame=22, total_duration=34)
countdown_loop = SpriteAnimation(sequence_id=9, total_duration=32)


class DingalingGridplane(NPC):
    sprite_id = 642
    y_shift = -6
    acute_axis = 11
    obtuse_axis = 11
    height = 13


class EggbertGridplane(NPC):
    sprite_id = 643
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    acute_axis = 2
    obtuse_axis = 2
    height = 5

    animations = SpriteAnimationCollection(
        tower_bullet=eggbert_expand,
        kitchen_prep=eggbert_expand,
        factory_pierce=eggbert_expand)


class FireCrystal(NPC):
    sprite_id = 644
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5


class WaterCrystal(NPC):
    sprite_id = 645
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5


class EarthCrystal(NPC):
    sprite_id = 646
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5


class WindCrystal(NPC):
    sprite_id = 647
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 5
    obtuse_axis = 5


class GenoBullet(NPC):
    sprite_id = 648
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


class MackMedium(NPC):
    sprite_id = 649
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 1
    acute_axis = 13
    obtuse_axis = 13
    height = 23
    min_vram_size = 3


class KnifeGuyGridplane(NPC):
    sprite_id = 650
    min_vram_size = 0
    y_shift = 1
    acute_axis = 7
    obtuse_axis = 7


class TinyBloober(NPC):
    sprite_id = 651
    acute_axis = 2
    obtuse_axis = 2
    height = 7
    y_shift = 1


class MimicStatue(MimicFace, Statue):
    sprite_id = 652


class CrocoStatue(CrocoBase, Statue):
    sprite_id = 653
    details = StatueDetails(horizontal_pixel_shift=-3)


class BoosterStatue(Booster, Statue):
    sprite_id = 654


class JohnnyStatue(JohnnySmall, Statue):
    sprite_id = 655


class MagikoopaStatue(SmallMagikoopa, Statue):
    sprite_id = 656

    details = StatueDetails(
        horizontal_pixel_shift=2,
        north_facing_horizontal_pixel_shift=-4,
        north_facing_vertical_pixel_shift=-1)


class ShovelKnightStatue(ShovelKnightBoss, Statue):
    sprite_id = 657
    details = StatueDetails(
        horizontal_pixel_shift=-3,
        north_facing_horizontal_pixel_shift=-5)


class YaridovichStatue(FakeElder, Statue):
    sprite_id = 658


class GrateGuyStatue(GrateGuySmall, Statue):
    sprite_id = 659
    details = StatueDetails(
        horizontal_pixel_shift=-3,
        north_facing_horizontal_pixel_shift=-2)


class JinxStatue(Jinx, Statue):
    sprite_id = 660


class MokuraStatue(MokuraCloud, Statue):
    sprite_id = 661


class TerrapinStatue(Terrapin, Statue):
    sprite_id = 662


class PiranhaPlantStatue(PiranhaPlant, Statue):
    sprite_id = 663


class BlooberStatue(Bloober, Statue):
    sprite_id = 664


class FactoryChiefStatue(FactoryChief, Statue):
    sprite_id = 665
    details = StatueDetails(horizontal_pixel_shift=-1)


class AxemRedStatue(AxemRed, Statue):
    sprite_id = 666
    details = StatueDetails(horizontal_pixel_shift=-6)


class BundtStatue(BundtSmall, Statue):
    sprite_id = 667
    details = StatueDetails(horizontal_pixel_shift=-3)


class CountDownStatue(CountDownGridplane, Statue):
    sprite_id = 668
    details = StatueDetails(
        horizontal_pixel_shift=4,
        vertical_pixel_shift=-1)


class HammerBroStatue(HammerBroSmall, Statue):
    sprite_id = 669


class MackStatue(MackSmall, Statue):
    sprite_id = 670


class SmallBelomeStatue(Belome1Small, Statue):
    sprite_id = 671


class Belome2Large(NPC):
    sprite_id = 672
    min_vram_size = 5
    shadow_size = ShadowSize._02_OVAL_BIG
    y_shift = 2
    acute_axis = 10
    obtuse_axis = 10
    height = 18

    animations = SpriteAnimationCollection(
        mines_punch=belome_attack,
        statue_intro=belome_wiggle,
        statue_flustered=belome_recoil,
        statue_peck=belome_attack_fast,
        chandelier_challenge=belome_attack,
        endgame_challenge=belome_attack)

    alt_palette = [
        "F8F8D8",
        "F8F888",
        "F8D060",
        "F8D008",
        "F8B010",
        "F8F8B0",
        "F8D008",
        "F8A008",
        "C88008",
        "582000",
        "582000",
        "984000",
        "401800",
        "C85808",
        "181000",
    ]


class BowyerStatue(BowyerSmall, Statue):
    sprite_id = 673


class PunchinelloStatue(PunchinelloSmall, Statue):
    sprite_id = 674


class DodoStatue(DodoSmall, Statue):
    sprite_id = 675


class BirdettaStatue(BirdettaSmall, Statue):
    sprite_id = 676


class CzarStatue(CzarDragonSmall, Statue):
    sprite_id = 677


class BoomerStatue(BoomerSmall, Statue):
    sprite_id = 678


class ExorStatue(ExorSmall, Statue):
    sprite_id = 679


class DominoStatue(DominoSmall, Statue):
    sprite_id = 680


class SmithyStatue(SmithySmall, Statue):
    sprite_id = 681


class CulexStatue(CulexSmall, Statue):
    sprite_id = 682


class MallowStatue(NPC):
    sprite_id = 683
    height = 8


class Chompweed(NPC):
    sprite_id = 685
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    height = 6


class BeetleGridplane(ItemNPC):
    sprite_id = 706
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1


class BananaGridplane(ItemNPC):
    sprite_id = 707
    show_shadow = False
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1


class CrownGridplane(ItemNPC):
    sprite_id = 708


class BroochGridplane(ItemNPC):
    sprite_id = 709


class ShoesGridplane(ItemNPC):
    sprite_id = 710


class RingGridplane(ItemNPC):
    sprite_id = 711


class TinyBird(NPC):
    sprite_id = 777
    shadow_size = ShadowSize._00_OVAL_SMALL
    y_shift = 1
    acute_axis = 1
    obtuse_axis = 1
    height = 1


smithy_hit = SpriteAnimation(sequence_id=1, contact_frame=76, total_duration=122)
smithy_hit_fast = SpriteAnimation(
    sequence_id=1, contact_frame=14, total_duration=24, speed=SequenceSpeeds.FASTEST
)


class SmithyLarge(NPC):
    sprite_id = 959
    shadow_size = ShadowSize._03_BLOCK
    acute_axis = 12
    obtuse_axis = 15
    height = 13

    animations = SpriteAnimationCollection(
        mines_punch=smithy_hit,
        statue_peck=smithy_hit_fast,
        chandelier_challenge=smithy_hit,
        endgame_challenge=smithy_hit)


goombette_hit = SpriteAnimation(sequence_id=3, contact_frame=42, total_duration=52)
goombette_taunt = SpriteAnimation(sequence_id=2, total_duration=12)
goombette_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=21, total_duration=26, speed=SequenceSpeeds.FAST
)


class Goombette(NPC):
    sprite_id = 960
    shadow_size = ShadowSize._00_OVAL_SMALL
    acute_axis = 2
    obtuse_axis = 2
    height = 7
    directions = VramStore._00_SWSE_NWNE

    animations = SpriteAnimationCollection(
        tower_bullet=goombette_hit,
        kitchen_prep=goombette_taunt,
        factory_pierce=goombette_hit_fast)


class Empty(NPC):
    sprite_id = 1023
    shadow_size = ShadowSize._00_OVAL_SMALL
    show_shadow = False
    y_shift = 1
    acute_axis = 4
    obtuse_axis = 4
    height = 9


class TableNPC:
    sprite_id = 0
    priority_0 = False
    priority_1 = False
    priority_2 = True
    show_shadow = False
    shadow = ShadowSize._00_OVAL_SMALL
    y_shift = 0
    acute_axis = 3
    obtuse_axis = 3
    height = 12
    directions = VramStore._02_SWSE
    vram_size = 0
    cannot_clone = False
    byte2_bit0 = False
    byte2_bit1 = False
    byte2_bit2 = False
    byte2_bit3 = False
    byte2_bit4 = False
    byte5_bit6 = False
    byte5_bit7 = False
    byte6_bit2 = False

    def __init__(
        self,
        sprite_id,
        priority_0,
        priority_1,
        priority_2,
        show_shadow,
        shadow,
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
        byte6_bit2):
        self.sprite_id = sprite_id
        self.priority_0 = priority_0
        self.priority_1 = priority_1
        self.priority_2 = priority_2
        self.show_shadow = show_shadow
        self.shadow = shadow
        self.y_shift = y_shift
        self.acute_axis = acute_axis
        self.obtuse_axis = obtuse_axis
        self.height = height
        self.directions = directions
        self.vram_size = vram_size
        self.cannot_clone = cannot_clone
        self.byte2_bit0 = byte2_bit0
        self.byte2_bit1 = byte2_bit1
        self.byte2_bit2 = byte2_bit2
        self.byte2_bit3 = byte2_bit3
        self.byte2_bit4 = byte2_bit4
        self.byte5_bit6 = byte5_bit6
        self.byte5_bit7 = byte5_bit7
        self.byte6_bit2 = byte6_bit2
