from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.datatypes.spells.enums import (
    SpellType,
    EffectType,
    Element,
    Status,
    InflictFunction,
    TempStatBuff,
)
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    BUTTON_MASH,
    CHARGE_ONLY,
    MULTIPLE_BUTTON_PRESSES,
    ONE_PLUS_MORE_TARGETS_WITH_PRESSES,
    ONE_TIMING_FOR_125_DMG_ONLY,
    ONE_TIMING_FOR_125_OR_15X_DMG,
    ROTATE_1_TARGET_IF_TIMED_ALL,
    ROTATE_ONLY,
    TIMED_FOR_9999_SET_ENEMY_HP_0,
    TIMED_GIVES_TARGET_DEFENSE_UP_BUFF,
    TIMED_HEALS_ALL_HP_TO_FIRST_TARGET,
    TIMED_JUMPS,
    TIME_TO_ACTIVATE_HP_READ,
)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    NO_MODIFIERS,
    X00625_MODIFIER,
    X00625_MODIFIER_WITH_MULTI_TARGETING,
    X0125_MODIFIER_WITH_MULTI_TARGETING,
    X05_MODIFIER,
)
from ...types.spell import CharacterSpell, EnemySpell, palette_to_bytes
from .ally_spells import *
from .enemy_spells import *

ALL_SPELLS = SpellCollection(
    [
        JumpSpell(),  # index: 0
        FireOrbSpell(),  # index: 1
        SuperJumpSpell(),  # index: 2
        SuperFlameSpell(),  # index: 3
        UltraJumpSpell(),  # index: 4
        UltraFlameSpell(),  # index: 5
        TherapySpell(),  # index: 6
        GroupHugSpell(),  # index: 7
        SleepyTimeSpell(),  # index: 8
        ComeBackSpell(),  # index: 9
        MuteSpell(),  # index: 10
        PsychBombSpell(),  # index: 11
        TerrorizeSpell(),  # index: 12
        PoisonGasSpell(),  # index: 13
        CrusherSpell(),  # index: 14
        BowserCrushSpell(),  # index: 15
        GenoBeamSpell(),  # index: 16
        GenoBoostSpell(),  # index: 17
        GenoWhirlSpell(),  # index: 18
        GenoBlastSpell(),  # index: 19
        GenoFlashSpell(),  # index: 20
        ThunderboltSpell(),  # index: 21
        HPRainSpell(),  # index: 22
        PsychopathSpell(),  # index: 23
        ShockerSpell(),  # index: 24
        SnowySpell(),  # index: 25
        StarRainSpell(),  # index: 26
        DrainSpell(),  # index: 64
        LightningOrbSpell(),  # index: 65
        FlameSpell(),  # index: 66
        BoltSpell(),  # index: 67
        CrystalSpell(),  # index: 68
        FlameStoneSpell(),  # index: 69
        MegaDrainSpell(),  # index: 70
        WillyWispSpell(),  # index: 71
        DiamondSawSpell(),  # index: 72
        ElectroshockSpell(),  # index: 73
        BlastSpell(),  # index: 74
        StormSpell(),  # index: 75
        IceRockSpell(),  # index: 76
        EscapeSpell(),  # index: 77
        DarkStarSpell(),  # index: 78
        RecoverSpell(),  # index: 79
        MegaRecoverSpell(),  # index: 80
        FlameWallSpell(),  # index: 81
        StaticESpell(),  # index: 82
        SandStormSpell(),  # index: 83
        BlizzardSpell(),  # index: 84
        DrainBeamSpell(),  # index: 85
        MeteorBlastSpell(),  # index: 86
        LightBeamSpell(),  # index: 87
        WaterBlastSpell(),  # index: 88
        SolidifySpell(),  # index: 89
        PetalBlastSpell(),  # index: 90
        AuroraFlashSpell(),  # index: 91
        BoulderSpell(),  # index: 92
        CoronaSpell(),  # index: 93
        MeteorSwarmSpell(),  # index: 94
        Engine023Spell(),  # index: 95
        WeirdMushroomSpell(),  # index: 96
        BreakerBeamSpell(),  # index: 97
        ShredderSpell(),  # index: 98
        SledgeSpell(),  # index: 99
        SwordRainSpell(),  # index: 100
        SpearRainSpell(),  # index: 101
        ArrowRainSpell(),  # index: 102
        BigBangSpell(),  # index: 103
        CakerBeamSpell(),  # index: 108
    ],
    additional_desc_ranges=[(0x3A1EA0, 0x3A20F0)]
)
