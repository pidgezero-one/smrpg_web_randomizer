"""Enemy and combat-related tweaks and settings."""
from __future__ import annotations
import random
from typing import TYPE_CHECKING

from randomizer.data.spells.spells import CakerBeamSpell
from smrpgpatchbuilder.datatypes.monster_scripts.commands import (
    CastSpell,
    ClearVar,
    IfTargetedByItem,
    SetUntargetable,
    SetTargetable
)
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import MONSTER_1_SET
from smrpgpatchbuilder.datatypes.spells.enums import Status
from ...data.variables.pack_names import *
from ...data.enemies.enemies import (
    BODYGUARDEnemy,
    GOOMBETTEEnemy,
    FAUTSOEnemy,
    BAHAMUTTEnemy,
    BAHAMUTTEnemy2,
    KINGBOMBEnemy,
    JINXCLONEEnemy,
    MARIOCLONEEnemy,
    MARIOCLONESEnemy,
    MALLOWCLONEEnemy,
    MALLOWCOPYSEnemy,
    GENOCLONEEnemy,
    GENOCLONESEnemy,
    BOWSERCLONEEnemy,
    BOWSERCOPYSEnemy,
    TOADSTOOL2Enemy,
    TOADSTOOL3Enemy,
    TENTACLESEnemy,
    TENTACLESEnemy2,
    BOBOMBEnemyHenchman,
    MICROBOMBEnemy,
    MEZZOBOMBEnemy,
    STRONGBOBOMB1Enemy,
    STRONGBOBOMB2Enemy,
    STRONGBOBOMB3Enemy,
    STRONGBOBOMB4Enemy,
    SNIFITEnemyHenchman,
    SNIFIT2Enemy,
    BANDANABLUEEnemy,
    TORTE2Enemy,
    TORTEEnemy,
    SMILAXEnemy,
    EGGBERTEnemy,
    DINGALINGEnemy,
    FIRECRYS3DEnemy,
    FIRECRYSTALEnemy,
    WINDCRYS3DEnemy,
    WATERCRYS3DEnemy,
    WATERCRYSTALEnemy,
    EARTHCRYS3DEnemy,
    EARTHCRYSTALEnemy,
    MADMALLETEnemyHenchman,
    POUNDEREnemyHenchman,
    POUNDETTEEnemyHenchman,
    HELIOEnemy,
    SHYPEREnemy,
    HAMMERBROEnemy,
    CROCO1Enemy,
    MACKEnemy,
    BELOME1Enemy,
    BOWYEREnemy,
    CROCO2Enemy,
    PUNCHINELLOEnemy,
    PUNCHINELLO2Enemy,
    BOOSTEREnemy,
    BOOSTEREnemy2,
    KNIFEGUYEnemy,
    GRATEGUYEnemy,
    BUNDTEnemy,
    BUNDT2Enemy,
    PANDORITEEnemy,
    HIDONEnemy,
    BOXBOYEnemy,
    CHESTEREnemy,
    KINGCALAMARIEnemy,
    JOHNNYEnemy,
    JOHNNYEnemy2,
    YARIDOVICHEnemy,
    YARIDOVICHMirageEnemy,
    BELOME2Enemy,
    BELOMEEnemy3,
    MOKURAEnemy,
    FORMLESSEnemy,
    JAGGEREnemy,
    JINX1Enemy,
    JINX2Enemy,
    JINX3Enemy,
    JINXEnemy4,
    CULEXEnemy,
    CULEX3DEnemy,
    MEGASMILAXEnemy,
    DODOEnemySolo,
    BIRDETTAEnemy,
    DODOEnemy,
    VALENTINAEnemy,
    CZARDRAGONEnemy,
    ZOMBONEEnemy,
    AXEMREDEnemy,
    AXEMPINKEnemy,
    AXEMBLACKEnemy,
    AXEMYELLOWEnemy,
    AXEMGREENEnemy,
    AXEMRANGERSEnemy,
    KAMEKEnemy,
    BOOMEREnemy,
    EXOREnemy,
    RIGHTEYEEnemy,
    LEFTEYEEnemy,
    NEOSQUIDEnemy,
    COUNTDOWNEnemy,
    CLOAKEREnemy,
    CLOAKEREnemy2,
    MADADDEREnemy,
    EARTHLINKEnemy,
    CLERKEnemy,
    MANAGEREnemy,
    DIRECTOREnemy,
    GUNYOLKEnemy,
    FACTORYCHIEFEnemy,
    SMITHY1Enemy,
    SMITHY2Enemy,
    SMITHYBodyEnemy,
    SMITHYChestEnemy,
    SMITHYMageEnemy,
    SMITHYSafeEnemy2,
    SMITHYTankEnemy,
    SMELTEREnemy,
)
from ...types.flags import (
        PoisonMushroom, UncapSuperJumps, NoGenoWhirlExor, FixMagikoopa,
        NoOHKO, EnemySpells, Punchinello2BobombDifficulty,
        Punchinello2BobombDifficultyOptions,
    )
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.commands import (
        JmpIfAMEM8BitLessThanConst,
    )
from ...data.items.items import MushroomItem2, CarboCookieItem
from ...data.enemies.enemies import KINGBOMBEnemy
from ...data.variables.battle_variable_names import BV7EE000
from ...data.spells.spells import (
        DrainSpell, LightningOrbSpell, FlameSpell, BoltSpell, CrystalSpell,
        FlameStoneSpell, MegaDrainSpell, WillyWispSpell, DiamondSawSpell,
        ElectroshockSpell, BlastSpell, StormSpell, IceRockSpell,
        DarkStarSpell, RecoverSpell, MegaRecoverSpell, FlameWallSpell,
        StaticESpell, SandStormSpell, BlizzardSpell, DrainBeamSpell,
        MeteorBlastSpell, LightBeamSpell, WaterBlastSpell, SolidifySpell,
        PetalBlastSpell, AuroraFlashSpell, BoulderSpell, CoronaSpell,
        MeteorSwarmSpell, WeirdMushroomSpell, BreakerBeamSpell, ShredderSpell,
        SledgeSpell, SwordRainSpell, SpearRainSpell, ArrowRainSpell, BigBangSpell,
        EnemySpell, EscapeSpell, Engine023Spell
    )
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import (
        DoNothing,
    )

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


# Enemy type lists for OHKO immunity and experience settings
SIDEKICK_ENEMIES: list[type] = []
BOSS_ENEMIES: list[type] = []


def _get_enemy_lists():
    """Lazily initialize enemy type lists."""
    global SIDEKICK_ENEMIES, BOSS_ENEMIES

    if SIDEKICK_ENEMIES:
        return SIDEKICK_ENEMIES, BOSS_ENEMIES


    SIDEKICK_ENEMIES = [
        BODYGUARDEnemy, GOOMBETTEEnemy, FAUTSOEnemy, BAHAMUTTEnemy, BAHAMUTTEnemy2,
        KINGBOMBEnemy, JINXCLONEEnemy, MARIOCLONEEnemy, MARIOCLONESEnemy,
        MALLOWCLONEEnemy, MALLOWCOPYSEnemy, GENOCLONEEnemy, GENOCLONESEnemy,
        BOWSERCLONEEnemy, BOWSERCOPYSEnemy, TOADSTOOL2Enemy, TOADSTOOL3Enemy,
        TENTACLESEnemy, TENTACLESEnemy2, BOBOMBEnemyHenchman, MICROBOMBEnemy,
        MEZZOBOMBEnemy, STRONGBOBOMB1Enemy, STRONGBOBOMB2Enemy, STRONGBOBOMB3Enemy,
        STRONGBOBOMB4Enemy, SNIFITEnemyHenchman, SNIFIT2Enemy, BANDANABLUEEnemy,
        TORTE2Enemy, TORTEEnemy, SMILAXEnemy, EGGBERTEnemy, DINGALINGEnemy,
        FIRECRYS3DEnemy, FIRECRYSTALEnemy, WINDCRYS3DEnemy, WINDCRYS3DEnemy,
        WATERCRYS3DEnemy, WATERCRYSTALEnemy, EARTHCRYS3DEnemy, EARTHCRYSTALEnemy,
        MADMALLETEnemyHenchman, POUNDEREnemyHenchman, POUNDETTEEnemyHenchman,
        HELIOEnemy, SHYPEREnemy,
    ]

    BOSS_ENEMIES = [
        HAMMERBROEnemy, CROCO1Enemy, MACKEnemy, BELOME1Enemy, BOWYEREnemy,
        CROCO2Enemy, PUNCHINELLOEnemy, PUNCHINELLO2Enemy, BOOSTEREnemy,
        BOOSTEREnemy2, KNIFEGUYEnemy, GRATEGUYEnemy, BUNDTEnemy, BUNDT2Enemy,
        PANDORITEEnemy, HIDONEnemy, BOXBOYEnemy, CHESTEREnemy, KINGCALAMARIEnemy,
        JOHNNYEnemy, JOHNNYEnemy2, YARIDOVICHEnemy, YARIDOVICHMirageEnemy,
        BELOME2Enemy, BELOMEEnemy3, MOKURAEnemy, FORMLESSEnemy, JAGGEREnemy,
        JINX1Enemy, JINX2Enemy, JINX3Enemy, JINXEnemy4, CULEXEnemy, CULEX3DEnemy,
        MEGASMILAXEnemy, DODOEnemySolo, BIRDETTAEnemy, DODOEnemy, VALENTINAEnemy,
        CZARDRAGONEnemy, ZOMBONEEnemy, AXEMREDEnemy, AXEMPINKEnemy, AXEMBLACKEnemy,
        AXEMYELLOWEnemy, AXEMGREENEnemy, AXEMRANGERSEnemy, KAMEKEnemy, BOOMEREnemy,
        EXOREnemy, RIGHTEYEEnemy, LEFTEYEEnemy, NEOSQUIDEnemy, COUNTDOWNEnemy,
        CLOAKEREnemy, CLOAKEREnemy2, MADADDEREnemy, EARTHLINKEnemy, CLERKEnemy,
        MANAGEREnemy, DIRECTOREnemy, GUNYOLKEnemy, FACTORYCHIEFEnemy, SMITHY1Enemy,
        SMITHY2Enemy, SMITHYBodyEnemy, SMITHYChestEnemy, SMITHYMageEnemy,
        SMITHYSafeEnemy2, SMITHYTankEnemy, SMELTEREnemy,
    ]

    return SIDEKICK_ENEMIES, BOSS_ENEMIES


def apply_enemy_tweaks(world: GameWorld) -> None:
    """Apply enemy and combat-related tweaks.

    This configures:
    - Poison mushroom random status effect
    - Uncapped super jumps
    - Geno Whirl Exor immunity
    - Magikoopa fix
    - OHKO immunity for sidekicks
    - Enemy spell randomization

    Note: Experience zero settings are handled separately by apply_experience_zero_settings()
    which must run after all enemy stat randomization.
    """

    sidekicks, _ = _get_enemy_lists()

    # Poison Mushroom random status effect
    if world.settings.isflag_enabled(PoisonMushroom):
        chosen_status = random.choice([
            Status.MUTE,
            Status.SLEEP,
            Status.POISON,
            Status.FEAR,
            Status.BERSERK,
            Status.MUSHROOM,
            Status.SCARECROW,
            Status.INVINCIBLE,
        ])
        world.items.get_by_type(MushroomItem2).set_status_immunities([chosen_status])
        world.poison_mushroom_status = chosen_status.name

    # Uncap super jumps
    if world.settings.isflag_enabled(UncapSuperJumps):
        world.battle_animations[0x35].delete_command_by_name("super_jump_cap_1")
        world.battle_animations[0x35].delete_command_by_name("super_jump_cap_2")

    # No Geno Whirl Exor
    if world.settings.isflag_enabled(NoGenoWhirlExor):
        world.monster_scripts.replace_command_by_identifier(
            "exor_vulnerability_1", [SetTargetable(MONSTER_1_SET)]
        )
        world.monster_scripts.replace_command_by_identifier(
            "exor_vulnerability_2", [SetTargetable(MONSTER_1_SET)]
        )
        world.monster_scripts.replace_command_by_identifier(
            "exor_vulnerability_3", [SetUntargetable(MONSTER_1_SET)]
        )

    # Fix Magikoopa
    if world.settings.isflag_enabled(FixMagikoopa):
        world.monster_scripts.scripts[
            KINGBOMBEnemy._monster_id
        ].insert_after_nth_command(0, ClearVar(BV7EE000))

    # OHKO immunity for sidekicks
    if world.settings.isflag_enabled(NoOHKO):
        for enemy_type in sidekicks:
            enemy = world.enemies.get_by_type(enemy_type)
            enemy.set_ohko_immune(True)
            enemy.set_morph_chance(0)
            for cmd in world.monster_scripts.scripts[enemy.monster_id].contents:
                if isinstance(cmd, IfTargetedByItem):
                    cmd.set_commands([CarboCookieItem])

    # Enemy spell randomization
    if world.settings.isflag_enabled(EnemySpells):
        # Breaker Beam's animation code includes forcing the caster to run sprite seq 3 
        # which not all monsters actually have. delete it if this flag is turned on
        world.battle_animations[0x35].delete_command_by_name("breaker_beam_sequence_1")
        world.battle_animations[0x35].delete_command_by_name("breaker_beam_sequence_2")

        spell_pool: list[type[EnemySpell]] = [
            DrainSpell, LightningOrbSpell, FlameSpell, BoltSpell, CrystalSpell,
            FlameStoneSpell, MegaDrainSpell, WillyWispSpell, DiamondSawSpell,
            ElectroshockSpell, BlastSpell, StormSpell, IceRockSpell,
            DarkStarSpell, FlameWallSpell,
            StaticESpell, SandStormSpell, BlizzardSpell, DrainBeamSpell,
            MeteorBlastSpell, LightBeamSpell, WaterBlastSpell, SolidifySpell,
            PetalBlastSpell, AuroraFlashSpell, BoulderSpell, CoronaSpell,
            MeteorSwarmSpell, ShredderSpell, BreakerBeamSpell,
            SledgeSpell, SwordRainSpell, SpearRainSpell, ArrowRainSpell,
        ]
        for script in world.monster_scripts.scripts:
            for cmd in script.contents:
                if isinstance(cmd, CastSpell):
                    # Skip special spells - spell slots contain types, not instances
                    excluded_spells = (DoNothing, EscapeSpell, BigBangSpell, Engine023Spell, RecoverSpell, MegaRecoverSpell, CakerBeamSpell, WeirdMushroomSpell)
                    if cmd.spell_1 is not None and cmd.spell_1 not in excluded_spells:
                        cmd.set_spell_1(random.choice(spell_pool))
                    if cmd.spell_2 is not None and cmd.spell_2 not in excluded_spells:
                        cmd.set_spell_2(random.choice(spell_pool))
                    if cmd.spell_3 is not None and cmd.spell_3 not in excluded_spells:
                        cmd.set_spell_3(random.choice(spell_pool))

    # Punchinello 2 Strong Bob-Omb facing-direction likelihood
    p2bobomb_value_map = {
        Punchinello2BobombDifficultyOptions.PERCENT_0: 0,
        Punchinello2BobombDifficultyOptions.PERCENT_25: 1,
        Punchinello2BobombDifficultyOptions.PERCENT_50: 2,
        Punchinello2BobombDifficultyOptions.PERCENT_75: 3,
        Punchinello2BobombDifficultyOptions.PERCENT_100: 4,
    }
    for option, value in p2bobomb_value_map.items():
        if world.settings.is_flag_value(Punchinello2BobombDifficulty, option):
            for identifier in (
                "bobomb_roll_output_1",
                "bobomb_roll_output_2",
                "bobomb_roll_output_3",
                "bobomb_roll_output_4",
            ):
                world.battle_animations[0x3A].get_command_by_name(
                    identifier, JmpIfAMEM8BitLessThanConst
                ).set_value(value)
            break