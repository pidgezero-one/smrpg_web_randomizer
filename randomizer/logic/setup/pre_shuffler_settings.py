"""Progression gating and startup event setup."""

from __future__ import annotations
from typing import TYPE_CHECKING

from ...data.items import MarioDollItem
from ...data.variables.event_script_names import (
    E0182_NPC_QUEST_5_CONTAINER,
    E0241_FREESTANDING_1_GRANT,
    E0464_YOSHI_RACE_COOKIE_GRANTER_SUBROUTINE,
    E1357_USE_MARIO_DOLL,
    E1928_BALCONY_IS_LOCKED,
    E2191_MARIO_DOLL_ERROR_MSG,
)
from ...data.variables.overworld_sfx_names import SO063_YOSHI_TALK
from ...data.variables.room_names import (
    R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
)
from ...data.variables.variable_names import (
    COMPLETED_MUSHROOM_DERBY,
    ITEM_ID,
    MAP_CASINO,
    MAP_DIRECTIONAL_BEAN_VALLEY_CASINO,
    MAP_DIRECTIONAL_PIPE_VAULT_YOSTER_ISLE,
    MAP_YOSTER_ISLE,
    PRIMARY_TEMP_7000,
    RETURNED_MARIO_DOLL,
    YOSHI_ITEM_GRANTED,
    BANDITS_WAY_LIBERATED
)
from ...data.variables.dialog_names import (
    DI1051_MOLEVILLE_CLOSED,
    DI1052_PIPE_VAULT_HINT,
    DI1053_BANDITS_WAY_HINT,
    DI1054_SUNKEN_SHIP_HINT,
    DI1055_SEWER_GATING_TEXT,
    DI2474_NIMBUS_NPC,
    DI3726_KEEP_ACCESS_HINT,
    DI4058_SHUFFLE_COOKIES_1,
    DI4059_SHUFFLE_COOKIES_2,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    DisableObjectTrigger,
    RunEventAsSubroutine,
    SetBit,
    ClearBit,
    ApplySolidityModToLevel,
    ApplyTileModToLevel,
    SetVarToConst,
    SummonObjectToSpecificLevel,
    RemoveObjectFromSpecificLevel,
    JmpIfBitClear,
    JmpIfBitSet,
    JmpIfVarEqualsConst,
    PlaySound,
    RemoveOneOfItemFromInventory,
    Return,
    ReturnAll,
    StoreItemAmountTo7000,
    Pause,
    RunDialog,
    JmpToEvent,
    Jmp
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import (
    MEM_70A8,
    NPC_0,
    NPC_1,
    NPC_2,
    NPC_3,
    NPC_5,
)
from smrpgpatchbuilder.datatypes.levels.classes import EventInitiator

from ...types.flags import BossScaleOptions, BossShuffleScaleStats, EnemySpells, ShuffleCookies, ShuffleMarioDoll

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_shuffler_independent_settings(world: GameWorld) -> None:
    """Apply settings to the world that don't require any input from the shuffler results."""
    from ...types.flags import (
        WinCondition,
        WinConditions,
        FastTravel,
        CasinoWarp,
        BucketWarp,
        ShuffleWeddingGear,
        EXPChallenge,
        EXPChallengeOptions,
        SkipBossFights,
        BanditsWayGate,
        BanditsWayGating,
        KeroSewersGate,
        KeroSewersGating,
        ForestMazeGate,
        ForestMazeGating,
        PipeVaultGate,
        PipeVaultGating,
        Moleville1Gate,
        Moleville1Gating,
        BoosterHillGate,
        BoosterHillGating,
        BoosterTowerGate,
        BoosterTowerGating,
        MarrymoreGate,
        MarrymoreGating,
        SeaGate,
        SeaGating,
        YaridovichGate,
        YaridovichGating,
        LandsEndGate,
        LandsEndGating,
        BelomeTempleGate,
        BelomeTempleGating,
        MonstroTownGate,
        MonstroTownGating,
        NimbusGate,
        NimbusGating,
        BarrelVolcanoGate,
        BarrelVolcanoGating,
        BowsersKeepGate,
        BowsersKeepGating,
        FactoryGate,
        FactoryGating,
    )
    from ...data.variables.variable_names import (
        SMITHY_BOSS_HUNT_WIN_CONDITION,
        WIN_CONDITION_STAR_PIECES,
        WIN_CONDITION_MONSTRO_DOOR,
        FAST_TRAVEL_ENABLED,
        CASINO_WARP_ENABLED,
        BUCKET_WARP_ENABLED,
        CHAPEL_ITEMS_ANYWHERE_ENABLED,
        PROGRESSIVE_STAR_EXP_ENABLED,
        PROGRESSIVE_BOSS_EXP_ENABLED,
        ALTERNATE_STAR_PIECE_WIN_CONDITION,
        MAP_BANDITS_WAY,
        MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY,
        SEWERS_CLOSED,
        MAP_FOREST_MAZE,
        MAP_DIRECTIONAL_ROSE_TOWN_FOREST_MAZE,
        PIPE_VAULT_GATED,
        MOLEVILLE_MINES_ENTRANCE_GATING,
        BOOSTER_HILL_CLOSED,
        TOWER_OPENED,
        MARRYMORE_BACKDOOR_OPEN,
        SEA_GATED_BY_STAR_PIECES,
        MAP_SEA,
        MAP_DIRECTIONAL_SEA_SUNKEN_SHIP,
        MAP_SUNKEN_SHIP,
        MAP_DIRECTIONAL_SEASIDE_DOWN_SEA,
        SEASIDE_BOSS_AVAILABLE,
        LANDS_END_GATED,
        LANDS_END_GATED_BY_STAR_PIECES,
        TEMPLE_BOSS_GATED,
        MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN,
        MAP_MONSTRO_TOWN,
        NIMBUS_MAINLAND_UNLOCKED,
        MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO,
        MAP_BARREL_VOLCANO,
        MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL,
        KEEP_GATED_BY_STAR_PIECES,
        FACTORY_MATCHES_KEEP,
        MAP_VISTA_HILL,
        MAP_GATE,
        MAP_DIRECTIONAL_BOWSERS_KEEP_GATE,
        FACTORY_GATED_BY_STAR_PIECES,
        PAINT_GATING,
    )
    from ...data.variables.room_names import (
        R333_KERO_SEWERS_ENTRANCE,
        R202_BOOSTER_TOWER_ENTRANCE,
        R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN,
        R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE,
    )
    from ...data.variables.event_script_names import (
        E1254_UNLOCK_SEWER_BY_RFC,
        E1255_UNLOCK_FOREST_BY_PIE,
        E1256_UNLOCK_MOLEVILLE_IF_GATED_BY_BOSHI,
        E1329_HILL_UNLOCKS,
        E1169_OPEN_LANDS_END_IF_GATED_BY_ELDER,
    )

    world.event_2496_startup += [SetBit(MAP_CASINO)]
    world.event_2496_startup += [SetBit(MAP_DIRECTIONAL_BEAN_VALLEY_CASINO)]
    world.event_2496_startup += [SetBit(MAP_YOSTER_ISLE)]
    world.event_2496_startup += [SetBit(MAP_DIRECTIONAL_PIPE_VAULT_YOSTER_ISLE)]

    # Win conditions
    if world.settings.is_flag_value(WinCondition, WinConditions.SMITHY):
        world.event_2496_startup += [SetBit(SMITHY_BOSS_HUNT_WIN_CONDITION)]
    elif world.settings.is_flag_value(WinCondition, WinConditions.STARS):
        world.event_2496_startup += [SetBit(WIN_CONDITION_STAR_PIECES)]
    elif world.settings.is_flag_value(WinCondition, WinConditions.SEALED):
        world.event_2496_startup += [SetBit(WIN_CONDITION_MONSTRO_DOOR)]

    # Travel and warp settings
    if world.settings.isflag_enabled(FastTravel):
        world.event_2496_startup += [SetBit(FAST_TRAVEL_ENABLED)]
    if world.settings.isflag_enabled(CasinoWarp):
        world.event_2496_startup += [SetBit(CASINO_WARP_ENABLED)]
    if world.settings.isflag_enabled(BucketWarp):
        world.event_2496_startup += [SetBit(BUCKET_WARP_ENABLED)]
    if world.settings.isflag_enabled(ShuffleWeddingGear):
        world.event_2496_startup += [SetBit(CHAPEL_ITEMS_ANYWHERE_ENABLED)]

    # EXP challenge settings
    if world.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.NONE) or world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE) or world.settings.debug_mode:
        world.event_scripts.replace_command_by_identifier("inc_exp_by_packet", Jmp(["EVENT_255_ret_13"]))
        world.event_scripts.get_command_by_identifier("EVENT_3072_set_var_to_const_60", SetVarToConst).set_value_and_address(ITEM_ID, 0)
        world.event_scripts.get_command_by_identifier("EVENT_3072_set_var_to_const_63", SetVarToConst).set_value_and_address(ITEM_ID, 0)
        world.event_scripts.get_command_by_identifier("EVENT_3072_set_var_to_const_66", SetVarToConst).set_value_and_address(ITEM_ID, 0)
        world.event_scripts.get_command_by_identifier("EVENT_3072_set_var_to_const_69", SetVarToConst).set_value_and_address(ITEM_ID, 0)
        world.event_scripts.get_command_by_identifier("EVENT_3072_set_var_to_const_72", SetVarToConst).set_value_and_address(ITEM_ID, 0)
        world.event_scripts.get_command_by_identifier("EVENT_3072_set_var_to_const_75", SetVarToConst).set_value_and_address(ITEM_ID, 0)
        world.event_scripts.get_command_by_identifier("EVENT_3072_set_var_to_const_78", SetVarToConst).set_value_and_address(ITEM_ID, 0)
    elif world.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.STARS):
        world.event_2496_startup += [SetBit(PROGRESSIVE_STAR_EXP_ENABLED)]
    elif world.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.BOSSES):
        world.event_2496_startup += [SetBit(PROGRESSIVE_BOSS_EXP_ENABLED)]

    if world.settings.isflag_enabled(SkipBossFights):
        world.event_2496_startup += [SetBit(ALTERNATE_STAR_PIECE_WIN_CONDITION)]

    # Area gates

    # Bandits Way
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.OPEN):
        world.event_2496_startup += [
            SetBit(MAP_BANDITS_WAY),
            SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
        ]
    elif world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.HAMMER_BRO):
        world.update_dialog(
            DI1053_BANDITS_WAY_HINT,
            """ Have you been to Bandit's Way?[await] I got lost on my way over there. I heard only the Hammer Bros know where the entrance is.[await]""",
        )
    elif world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MALLOW):
        world.update_dialog(
            DI1053_BANDITS_WAY_HINT,
            """ Have you been to Bandit's Way?[await] I got lost on my way over there. I heard only `MALLOW_NAME` knows where the entrance is.[await]""",
        )
    elif world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MUSHROOM_WAY):
        world.update_dialog(
            DI1053_BANDITS_WAY_HINT,
            """ Have you been to Bandit's Way?[await] I couldn't figure out how to get in. I heard you need to go through Mushroom Way. Is that true?[await]""",
        )

    # Kero Sewers
    if not world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.OPEN):
        world.event_2496_startup += [SetBit(SEWERS_CLOSED)]

        if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.RFC):
            world.event_scripts.get_script_by_id(
                E1254_UNLOCK_SEWER_BY_RFC
            ).insert_before_nth_command(0, ClearBit(SEWERS_CLOSED))
            world.event_scripts.get_script_by_id(
                E1254_UNLOCK_SEWER_BY_RFC
            ).insert_before_nth_command(
                0, RemoveObjectFromSpecificLevel(NPC_0, R333_KERO_SEWERS_ENTRANCE)
            )
            world.event_scripts.get_script_by_id(
                E1254_UNLOCK_SEWER_BY_RFC
            ).insert_before_nth_command(
                0, RemoveObjectFromSpecificLevel(NPC_1, R333_KERO_SEWERS_ENTRANCE)
            )
            world.update_dialog(
                DI1055_SEWER_GATING_TEXT,
                " Oh, the sewers? I think they're\n closed for repairs.[await][pause] Honestly, I\n thought that finished ages ago.[await][page]\n I think the guy who was working on\n it is waiting for payment, but our\n shop guy is out of RareFrogCoins.[await]",
            )

        elif world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MALLOW):
            world.update_dialog(
                DI1055_SEWER_GATING_TEXT,
                " Oh, the sewers? I think they're\n closed for repairs.[await][pause] Honestly, I\n thought that finished ages ago.[await][page]\n I think the guy who was working on it needs help from `MALLOW_NAME`, but nobody knows where he is.[await]",
            )
        if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.KINGDOM):
            world.update_dialog(
                DI1055_SEWER_GATING_TEXT,
                " Oh, the sewers? I think they're\n closed for repairs.[await][pause] Honestly, I\n thought that finished ages ago.[await][page]\n I bet some bigger changes will\n happen to this town before that\n ever gets finished.[await]",
            )
        if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MACK):
            world.update_dialog(
                DI1055_SEWER_GATING_TEXT,
                " Oh, the sewers? I think they're\n closed for repairs.[await][pause] Honestly, I\n thought that finished ages ago.[await][page]\n I bet the guy working on it got\n distracted again when he heard\n Mack was around.[await]",
            )
    else:
        world.event_2496_startup += [
            ClearBit(SEWERS_CLOSED),
            RemoveObjectFromSpecificLevel(NPC_0, R333_KERO_SEWERS_ENTRANCE),
            RemoveObjectFromSpecificLevel(NPC_1, R333_KERO_SEWERS_ENTRANCE),
        ]

    # Forest Maze
    if world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.OPEN):
        world.event_2496_startup += [
            SetBit(MAP_FOREST_MAZE),
            SetBit(MAP_DIRECTIONAL_ROSE_TOWN_FOREST_MAZE),
        ]
    elif world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
        e = world.event_scripts.get_script_by_id(E1255_UNLOCK_FOREST_BY_PIE)
        e.insert_before_nth_command(0, SetBit(MAP_FOREST_MAZE))
        e.insert_before_nth_command(0, SetBit(MAP_DIRECTIONAL_ROSE_TOWN_FOREST_MAZE))

    # Pipe Vault
    if not world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.OPEN):
        world.event_2496_startup += [SetBit(PIPE_VAULT_GATED)]
        if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.BOWYER):
            world.update_dialog(
                DI1052_PIPE_VAULT_HINT,
                """ There's a pipe in the road a bit\n west of here. I wonder what's\n down there?[await][page]\n It might be closed, though. [await]\n The guy working on it was mumbling\n something about the jerk who was\n shooting arrows into town.[await]""",
            )
        if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.GENO):
            world.update_dialog(
                DI1052_PIPE_VAULT_HINT,
                """ There's a pipe in the road a bit\n west of here. I wonder what's\n down there?[await][page]\n It might be closed, though. [await]\n The guy working on it was talking\n to someone named `GENO_NAME`.[await] If you find him, he might know how to get in.[await]""",
            )
        if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
            world.update_dialog(
                DI1052_PIPE_VAULT_HINT,
                """ There's a pipe in the road a bit\n west of here. I wonder what's\n down there?[await][page]\n It might be closed, though. [await]\n The guy working on it ran off to\n get something from the forest.[await]""",
            )

    # Moleville Mines
    if not world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.OPEN):
        world.event_2496_startup += [SetBit(MOLEVILLE_MINES_ENTRANCE_GATING)]
        if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOSHI):
            world.event_scripts.get_script_by_id(
                E1256_UNLOCK_MOLEVILLE_IF_GATED_BY_BOSHI
            ).insert_before_nth_command(0, ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING))
            world.update_dialog(
                DI1051_MOLEVILLE_CLOSED,
                """ The menfolk'll help you get inside\n once they come back to town.[await][pause] They\n went off to the racetrack.[await]""",
            )
        elif world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOWYER):
            world.update_dialog(
                DI1051_MOLEVILLE_CLOSED,
                """ The menfolk'll help you get inside\n once they come back to town.[await][pause] They\n left to go hunt down some fella\n named “Bowyer”, or somethin'.[await]""",
            )
        elif world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
            world.update_dialog(
                DI1051_MOLEVILLE_CLOSED,
                """ The menfolk'll help you get inside\n once they come back to town.[await][pause] They\n left to go get firewood from\n the forest.[await]""",
            )
        elif world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.GENO):
            world.update_dialog(
                DI1051_MOLEVILLE_CLOSED,
                """ The menfolk'll help you get inside\n once they come back to town.[await][pause] They\n went lookin' for some fella\n named `GENO_NAME`.[await]""",
            )

    # Booster Hill
    if not world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.OPEN):
        world.event_2496_startup += [SetBit(BOOSTER_HILL_CLOSED)]

    # Booster Tower
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.OPEN):
        world.event_2496_startup += [
            ApplySolidityModToLevel(
                permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
            ),
            ApplyTileModToLevel(
                use_alternate=True,
                room_id=R202_BOOSTER_TOWER_ENTRANCE,
                mod_id=32,
            ),
            SetBit(TOWER_OPENED),
        ]

    # Marrymore
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.OPEN):
        world.event_2496_startup += [SetBit(MARRYMORE_BACKDOOR_OPEN)]
    elif world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.HILL):
        world.event_scripts.get_script_by_id(
            E1329_HILL_UNLOCKS
        ).insert_before_nth_command(0, SetBit(MARRYMORE_BACKDOOR_OPEN))

    # Sea
    if world.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        world.event_2496_startup += [SetBit(SEA_GATED_BY_STAR_PIECES)]
        world.update_dialog(
            DI1054_SUNKEN_SHIP_HINT,
            """ Did you know there's a shipwreck\n off the beach to the south?[await]\n It will be pretty easy to find if you\n have four stars to guide you.[await]""",
        )
    elif world.settings.is_flag_value(SeaGate, SeaGating.OPEN):
        world.event_2496_startup += [
            SetBit(MAP_SEA),
            SetBit(MAP_DIRECTIONAL_SEA_SUNKEN_SHIP),
            SetBit(MAP_SUNKEN_SHIP),
            SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
        ]
    elif world.settings.is_flag_value(SeaGate, SeaGating.TOADSTOOL):
        world.update_dialog(
            DI1054_SUNKEN_SHIP_HINT,
            """ Did you know there's a shipwreck\n off the beach to the south?[await] `PEACH_NAME` can help you get there.[await]""",
        )
    elif world.settings.is_flag_value(SeaGate, SeaGating.BUNDT):
        world.update_dialog(
            DI1054_SUNKEN_SHIP_HINT,
            """ Did you know there's a shipwreck\n off the beach to the south?[await]\n You'll need to vanquish a large\n cake in order to make it more\n visible.[await]""",
        )
    elif world.settings.is_flag_value(SeaGate, SeaGating.MARRYMORE):
        world.update_dialog(
            DI1054_SUNKEN_SHIP_HINT,
            """ Did you know there's a shipwreck\n off the beach to the south?[await]\n I heard you can only get there\n through Marrymore, somehow.[await]""",
        )

    # Yaridovich
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.OPEN):
        world.event_2496_startup += [SetBit(SEASIDE_BOSS_AVAILABLE)]

    # Land's End
    if not world.settings.is_flag_value(LandsEndGate, LandsEndGating.OPEN):
        world.event_2496_startup += [SetBit(LANDS_END_GATED)]

        if world.settings.is_flag_value(LandsEndGate, LandsEndGating.ELDER):
            world.event_scripts.get_script_by_id(
                E1169_OPEN_LANDS_END_IF_GATED_BY_ELDER
            ).insert_before_nth_command(0, ClearBit(LANDS_END_GATED))
        if world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
            world.event_2496_startup += [SetBit(LANDS_END_GATED_BY_STAR_PIECES)]

    # Belome Temple
    if world.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.KEY):
        world.event_2496_startup += [SetBit(TEMPLE_BOSS_GATED)]

    # Monstro Town
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.BELOME_2):
        world.event_2496_startup += [
            SummonObjectToSpecificLevel(
                NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
            )
        ]
    elif world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
        world.event_2496_startup += [
            RemoveObjectFromSpecificLevel(
                NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
            ),
            SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
            SetBit(MAP_MONSTRO_TOWN),
        ]

    # Nimbus Land
    if world.settings.is_flag_value(
        NimbusGate, NimbusGating.OPEN
    ) or world.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
        world.event_2496_startup += [
            SetBit(NIMBUS_MAINLAND_UNLOCKED),
            RemoveObjectFromSpecificLevel(
                NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
            ),
        ]
    if world.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
        world.event_2496_startup += [
            SetBit(PAINT_GATING),
        ]

    # Barrel Volcano
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.OPEN):
        world.event_2496_startup += [
            SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
            SetBit(MAP_BARREL_VOLCANO),
        ]
    elif world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
        world.update_dialog(
            DI2474_NIMBUS_NPC,
            """ Oh, hello there! Are you visiting?[await]\n We don't get tourists here very\n often. I guess our town is a little\n bit out of the way.[await][page]\n If you're looking for something fun\n to do, you should visit our\n volcano![await][pause] You might need to clear\n out the castle first, though.[await]""",
        )
    elif world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA):
        world.update_dialog(
            DI2474_NIMBUS_NPC,
            """ Oh, hello there! Are you visiting?[await]\n We don't get tourists here very\n often. I guess our town is a little\n bit out of the way.[await][page]\n If you're looking for something fun\n to do, you should visit our\n volcano![await][pause] You might need\n Valentina's permission to enter,\n though.[await]""",
        )

    # Bowser's Keep
    if not world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.OPEN):
        world.event_2496_startup += [SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL)]
        if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
            world.event_2496_startup += [SetBit(KEEP_GATED_BY_STAR_PIECES)]
            if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                world.event_2496_startup += [SetBit(FACTORY_MATCHES_KEEP)]
    else:
        world.event_2496_startup += [
            SetBit(MAP_VISTA_HILL),
            ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
        ]
        if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
            world.event_2496_startup += [
                SetBit(MAP_GATE),
                SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
            ]

    # Factory
    if world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        world.event_2496_startup += [SetBit(FACTORY_GATED_BY_STAR_PIECES)]
        world.update_dialog(
            DI3726_KEEP_ACCESS_HINT,
            """ I heard there was a big factory\n behind it. Is that true?[await][pause] I wish I had\n 6 Star Pieces, so I could find out.[await]""",
        )
    elif world.settings.is_flag_value(FactoryGate, FactoryGating.EXOR):
        world.update_dialog(
            DI3726_KEEP_ACCESS_HINT,
            """ I heard there was a big factory\n behind it. Is that true?[await][pause] I bet Exor\n would know, if you run into him![await]""",
        )

    # Settings that aren't dependent on shuffler contents
    if world.settings.isflag_enabled(ShuffleCookies):
        world.event_scripts.get_script_by_id(
            E0464_YOSHI_RACE_COOKIE_GRANTER_SUBROUTINE
        ).set_contents(
            [
                Pause(10),
                PlaySound(sound=SO063_YOSHI_TALK, channel=6),
                JmpIfBitClear(YOSHI_ITEM_GRANTED, ["EVENT_464_pause_11"]),
                JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_464_pause_10"]),
                RunDialog(
                    dialog_id=DI4058_SHUFFLE_COOKIES_1,
                    above_object=MEM_70A8,
                    closable=True,
                    sync=False,
                    multiline=True,
                    use_background=True,
                    identifier="EVENT_464_pause_11",
                ),
                JmpIfBitSet(YOSHI_ITEM_GRANTED, ["EVENT_464_pause_10"]),
                SetBit(YOSHI_ITEM_GRANTED),
                RunDialog(
                    dialog_id=DI4059_SHUFFLE_COOKIES_2,
                    above_object=MEM_70A8,
                    closable=True,
                    sync=False,
                    multiline=True,
                    use_background=True,
                ),
                JmpToEvent(E0182_NPC_QUEST_5_CONTAINER),
                Return(identifier="EVENT_464_pause_10"),
            ]
        )
    if world.settings.isflag_enabled(ShuffleMarioDoll):
        world.event_scripts.get_script_by_id(E1357_USE_MARIO_DOLL).set_contents(
            [
                JmpIfBitSet(RETURNED_MARIO_DOLL, ["EVENT_1357_pause_10"]),
                StoreItemAmountTo7000(MarioDollItem),
                JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1357_pause_12"]),
                SetBit(RETURNED_MARIO_DOLL),
                DisableObjectTrigger(NPC_5),
                RemoveOneOfItemFromInventory(MarioDollItem),
                Return(identifier="EVENT_1357_pause_10"),
                ReturnAll(identifier="EVENT_1357_pause_12"),
            ]
        )
        bdoor_e = world.event_scripts.get_script_by_id(E1928_BALCONY_IS_LOCKED)
        bdoor_e.set_contents([
            RunEventAsSubroutine(E2191_MARIO_DOLL_ERROR_MSG),
            *bdoor_e.contents,
        ])
        _curtain_npc = world.get_room(
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM
        ).get_npc_by_target_id(NPC_5)
        _curtain_npc.set_event_script(E0241_FREESTANDING_1_GRANT)
        _curtain_npc.set_initiator(EventInitiator.ANYTHING_EXCEPT_PRESS_A)

    # For safety, delete Breaker Beam caster animations in case an enemy uses it that doesn't have a sequence 3

    # Apply debug starting items if debug mode is enabled
    from .debug import apply_debug_start_items

    apply_debug_start_items(world)
