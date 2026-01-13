"""Cosmetic settings that don't affect gameplay."""
from __future__ import annotations
import random
import datetime
from typing import TYPE_CHECKING, cast

from django.contrib.gis.measure import D

from randomizer.data.variables.dialog_names import DI1055_SEWER_GATING_TEXT, DI3072_TOWER_HENCHMAN_3_WINDOW, DI3073_TOWER_HENCHMAN_3
from randomizer.progression.prizelocations import BoosterTowerIndoorBossFight, FinalBossFight, MarrymoreCharacter, SeasideBeachBossFight, VolcanoExitBossFight
from randomizer.types.flags import BowsersKeepGate, BowsersKeepGating, FireworksOptions, FireworksSetting, KeepMinigameSpritesIntact, RangeFlag, SuperJump1Threshold, SuperJump2Threshold
from randomizer.types.prize import BossFightPrize, CharacterPrize
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands import (
    ScreenFlashWithDuration,
    AttackTimerBegins,
    DefineObjectQueue,
)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments import NO_COLOUR

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_cosmetic_settings(world: GameWorld) -> None:
    """Apply cosmetic settings that don't affect gameplay.

    This configures:
    - Canon names (Kamek, Birdetta)
    - Peach name
    - Remake names for enemies, items, spells, attacks
    - Remove screen flashes (accessibility)
    - Palette swaps for characters
    - Boss shuffle music
    - Random Star Hill wishes

    Note: Cosmetics are re-seeded with current timestamp so they vary
    between generations with the same seed.
    """
    from ...types.flags import (
        CanonNames, Peach, RemakeNames, RemoveFlashes, PaletteSwaps,
        ChangeNames, BossShuffleMusic, ShuffledMusic,
    )
    from ...data.enemies.enemies import (
        KAMEKEnemy, BIRDETTAEnemy,
        MARIOCLONEEnemy, MARIOCLONESEnemy,
        TOADSTOOL2Enemy, TOADSTOOL3Enemy,
        BOWSERCLONEEnemy, BOWSERCOPYSEnemy,
        GENOCLONEEnemy, GENOCLONESEnemy,
        MALLOWCLONEEnemy, MALLOWCOPYSEnemy,
    )
    from ...data.allies.palettes.mario import all_palettes as MARIO_PALETTES
    from ...data.allies.palettes.mallow import all_palettes as MALLOW_PALETTES
    from ...data.allies.palettes.geno import all_palettes as GENO_PALETTES
    from ...data.allies.palettes.toadstool import all_palettes as TOADSTOOL_PALETTES
    from ...data.allies.palettes.bowser import all_palettes as BOWSER_PALETTES
    from ...data.minigames.star_hill_wishes import WISH_POOL, WISH_DIALOG_IDS
    from ...data.variables.battle_effect_names import EF0025_PSYCH_BOMB_BG
    from ...types.enemy import Enemy
    from ...types.item import Item
    from ...types.spell import Spell
    from ...types.attack import EnemyAttack
    from ...types.prizelocation import BossFightLocation

    # Re-seed for cosmetics (so they vary between generations with same seed)
    random.seed(datetime.datetime.now().timestamp())

    # Canon names
    if world.settings.isflag_enabled(CanonNames):
        world.enemies.get_by_type(KAMEKEnemy).set_name("KAMEK")
        world.enemies.get_by_type(BIRDETTAEnemy).set_name("BIRDETTA")

    # Peach name
    if world.settings.isflag_enabled(Peach):
        world.allies._allies[1].name = "Peach"
        world.enemies.get_by_type(TOADSTOOL2Enemy).set_name("PEACH CLONE")
        world.enemies.get_by_type(TOADSTOOL3Enemy).set_name("PEACH CLONE S")

    # Remake names
    if world.settings.isflag_enabled(RemakeNames):
        for enemy in world.enemies.enemies:
            e = cast(Enemy, enemy)
            if e.remake_name is not None:
                enemy.set_name(e.remake_name)
        for item in world.items.items:
            it = cast(Item, item)
            if it.remake_name is not None:
                item.set_name(it.remake_name)
        for spell in world.spells.spells:
            sp = cast(Spell, spell)
            if sp.remake_name is not None:
                spell._title = sp.remake_name
        for attack in world.enemy_attacks.attacks:
            at = cast(EnemyAttack, attack)
            if at.remake_name is not None:
                attack.set_attack_name(at.remake_name)
        world.update_dialog(DI3072_TOWER_HENCHMAN_3_WINDOW, """SNIFSTER 3: Um...\n Nice weather we're having.[await]""")
        world.update_dialog(DI3073_TOWER_HENCHMAN_3, '''SNIFSTER 3: You wanna fight?[await]''')
        world.update_dialog(DI1055_SEWER_GATING_TEXT, " Oh, the sewers? I think they're\n closed for repairs.[await][pause] Honestly, I\n thought that finished ages ago.[await][page]\n I bet the guy working on it got\n distracted again when he heard\n Claymorton was around.[await]")
        world.overworld_dialogs.search_and_replace_in_all_dialogs("FROGFUCIUS", "FROG SAGE")

    for location in world.locations:
        if isinstance(location, BossFightLocation) and isinstance(location.prize, BossFightPrize):
            dialogs = location.prize.get_dialog_replacements(
                remake=world.settings.isflag_enabled(RemakeNames),
                canon=world.settings.isflag_enabled(CanonNames),
                mandatory_fights_changed=not world.settings.isflag_enabled(KeepMinigameSpritesIntact),
                peach=world.settings.isflag_enabled(Peach)
                )
            if dialogs:
                for dialog_id in location._dialogs_expecting_replacement:
                    if dialog_id in dialogs:
                        world.update_dialog(dialog_id, dialogs[dialog_id])
                        

    # Remove screen flashes (accessibility)
    if world.settings.isflag_enabled(RemoveFlashes):
        # Reduce flash intensity
        screenflashes = [
            "screen_flash_1",  # thunderbolt
            "screen_flash_2",
            "crusher_screenflash",  # crusher
            "darkstar_flash",  # dark star
            "spikedlink_flash_1",
            "spikedlink_flash_2",
            "spikedlink_flash_3",
        ]
        for identifier in screenflashes:
            world.battle_animations[0x35].get_command_by_name(identifier).set_colour(  # type: ignore
                NO_COLOUR
            )

        # Delete flash commands # 
        deletes = [
            "command_0x35BE52",  # geno flash
            "geno_blast_effect",  # geno blast
            "corona_flash",
            "shaker_delete_1",  # shaker / silver bullet
            "shaker_delete_2",
            "shaker_delete_3",
            "shaker_delete_4",
            "shaker_delete_5",
            "statice_delete_1",
            "statice_delete_2",
            "statice_delete_3",
            "statice_delete_4",
            "statice_delete_5",
            "meteorswarm_delete_maybe",
            "rockcandy_delete",
            "rockcandy_delete_2",
        ]
        for identifier in deletes:
            world.battle_animations[0x35].delete_command_by_name(identifier)
        # geno flash is a queue entry, move ptr to the command that comes after it
        doq = world.battle_animations[0x35].get_command_by_name("command_0x35BE06", DefineObjectQueue)
        doq.set_destinations([
            doq.destinations[0].label,
            "geno_flash_begins_if_accessibility_enabled",
            *[d.label for d in doq.destinations[2:]]
        ])

        deletes_3A = ["smithy_delete_1", "smithy_delete_2"]
        for identifier in deletes_3A:
            world.battle_animations[0x3A].delete_command_by_name(identifier)

        # Replace flash effects
        world.battle_animations[0x35].get_command_by_name(
            "bigbang_flash"
        ).set_effect(EF0025_PSYCH_BOMB_BG)  # type: ignore
        world.battle_animations[0x35].get_command_by_name(
            "firebomb_explosion"
        ).set_effect(EF0025_PSYCH_BOMB_BG)  # type: ignore
        world.battle_animations[0x35].replace_command_by_name(
            "icebomb_explosion", ScreenFlashWithDuration(NO_COLOUR, 1)
        )
        world.battle_animations[0x35].replace_command_by_name(
            "command_0x35358A",
            AttackTimerBegins(identifier="command_0x35358A"),  # shaker / silver bullet
        )
        world.battle_animations[0x35].replace_command_by_name(
            "statice_flash", ScreenFlashWithDuration(NO_COLOUR, 44)  # static e!
        )
        world.battle_animations[0x35].replace_command_by_name(
            "meteorswarm_replace",
            ScreenFlashWithDuration(NO_COLOUR, 16),  # meteor swarm
        )
        world.battle_animations[0x35].replace_command_by_name(
            "rockcandy_replace",
            ScreenFlashWithDuration(NO_COLOUR, 20),  # rock candy
        )
        world.battle_animations[0x35].replace_command_by_name(
            "meteorblast_replace",
            ScreenFlashWithDuration(NO_COLOUR, 20),  # meteor blast
        )
        world.battle_animations[0x3A].replace_command_by_name(
            "smithy_replace_1", ScreenFlashWithDuration(NO_COLOUR, 1)
        )
        world.battle_animations[0x3A].replace_command_by_name(
            "smithy_replace_2", ScreenFlashWithDuration(NO_COLOUR, 1)
        )

        for i in range(1, 11):
            flash_id = f"screenflash_{i}"
            world.event_scripts.delete_command_by_identifier(flash_id)

    # Palette swaps
    if world.settings.isflag_enabled(PaletteSwaps):
        world.mario_palette = random.choice(MARIO_PALETTES)
        world.mallow_palette = random.choice(MALLOW_PALETTES)
        world.geno_palette = random.choice(GENO_PALETTES)
        world.bowser_palette = random.choice(BOWSER_PALETTES)
        world.toadstool_palette = random.choice(TOADSTOOL_PALETTES)

        if world.settings.isflag_enabled(ChangeNames):
            world.allies._allies[0].name = world.mario_palette.name
            world.enemies.get_by_type(MARIOCLONEEnemy).set_name(
                world.mario_palette.clone_name
            )
            world.enemies.get_by_type(MARIOCLONESEnemy).set_name(
                world.mario_palette.strong_clone_name
            )
            world.allies._allies[1].name = world.toadstool_palette.name
            world.enemies.get_by_type(TOADSTOOL2Enemy).set_name(
                world.toadstool_palette.clone_name
            )
            world.enemies.get_by_type(TOADSTOOL3Enemy).set_name(
                world.toadstool_palette.strong_clone_name
            )
            world.allies._allies[2].name = world.bowser_palette.name
            world.enemies.get_by_type(BOWSERCLONEEnemy).set_name(
                world.bowser_palette.clone_name
            )
            world.enemies.get_by_type(BOWSERCOPYSEnemy).set_name(
                world.bowser_palette.strong_clone_name
            )
            world.allies._allies[3].name = world.geno_palette.name
            world.enemies.get_by_type(GENOCLONEEnemy).set_name(
                world.geno_palette.clone_name
            )
            world.enemies.get_by_type(GENOCLONESEnemy).set_name(
                world.geno_palette.strong_clone_name
            )
            world.allies._allies[4].name = world.mallow_palette.name
            world.enemies.get_by_type(MALLOWCLONEEnemy).set_name(
                world.mallow_palette.clone_name
            )
            world.enemies.get_by_type(MALLOWCOPYSEnemy).set_name(
                world.mallow_palette.strong_clone_name
            )
            world.overworld_dialogs.search_and_replace_in_all_dialogs("TOADSTOOL 2", world.toadstool_palette.clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("PEACH CLONE", world.toadstool_palette.clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("MALLOW CLONE", world.mallow_palette.clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("MARIO CLONE", world.mario_palette.clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("GENO CLONE", world.geno_palette.clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("BOWSER CLONE", world.bowser_palette.clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("TOADSTOOL 3", world.toadstool_palette.strong_clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("S PEACH CLONE", world.toadstool_palette.strong_clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("MALLOW COPY S", world.mallow_palette.strong_clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("BOWSER COPY S", world.bowser_palette.strong_clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("GENO CLONE S", world.geno_palette.strong_clone_name)
            world.overworld_dialogs.search_and_replace_in_all_dialogs("MARIO CLONE S", world.mario_palette.strong_clone_name)

    # Initialize selected music IDs
    world.selected_music_ids = []

    # Boss shuffle music
    if world.settings.isflag_enabled(BossShuffleMusic):
        from smrpgpatchbuilder.datatypes.battles.enums import BattleMusic

        # Get the enabled music tracks from user selection
        enabled_tracks = world.settings.get_flag(ShuffledMusic).enabled

        # Pick 8 random music IDs from the enabled tracks (with replacement if needed)
        if len(enabled_tracks) >= 8:
            selected_tracks = random.sample(enabled_tracks, 8)
        else:
            selected_tracks = random.choices(enabled_tracks, k=8)

        # Store the music IDs for patching in get_patch
        world.selected_music_ids = [track.music_id for track in selected_tracks]

        # The 8 battle music classes (pointers to the IDs we'll write at 0x029F51)
        music_classes = list(BattleMusic)

        for boss_fight in [
            l for l in world.locations if isinstance(l, BossFightLocation)
        ]:
            pack_id = cast(BossFightLocation, boss_fight).pack_id
            # Assign a random battle music class (0-7) to each boss fight
            battle_music = random.choice(music_classes)
            pack = world.get_battle_pack(pack_id)
            for f in pack.formations:
                f.set_music(battle_music)

    # Random Star Hill wishes (truly random, not tied to seed)
    wishes = zip(WISH_DIALOG_IDS, random.sample(WISH_POOL, len(WISH_DIALOG_IDS)))
    for dialog_id, wish in wishes:
        world.update_dialog(dialog_id, wish)

    # Room service and bomb shop dialog text (depends on RemakeNames setting)
    from ...data.variables.dialog_names import (
        DI3847_ROOM_SERVICE_MENU,
        DI1217_SWAP_SHOP_OVER_100_POINTS,
        DI1175_SWAP_SHOP_INSTRUCTIONS,
    )

    use_remake = world.settings.isflag_enabled(RemakeNames)

    # Room service menu dialog
    if world.room_service_items:
        low_item = cast(Item, world.get_item(world.room_service_items[0]))
        high_item = cast(Item, world.get_item(world.room_service_items[1]))
        world.update_dialog(
            DI3847_ROOM_SERVICE_MENU,
            f"[page]\n Here is the menu.[await]\n"
            f" [select]  {low_item.text_shop_menu(use_remake)}\n"
            f" [select]  {high_item.text_shop_menu(use_remake)})\n"
            f" [select]  (No thanks)[await]"
        )

    # Bomb trade shop dialogs
    if world.bomb_shop_items:
        bomb_items = [cast(Item, world.get_item(b)) for b in world.bomb_shop_items]
        bombs = [b.name for b in bomb_items]
        world.update_dialog(
            DI1217_SWAP_SHOP_OVER_100_POINTS,
            f" If we total that up, you've got\n [0x7000] points![await][page]\n"
            f" You have more than 100 points,\n so go ahead and choose an item.[await][page]\n"
            f"  [select]  ({bombs[0]})\n"
            f"  [select]  ({bombs[1]})\n"
            f"  [select]  ({bombs[2]})[await]"
        )
        world.update_dialog(
            DI1175_SWAP_SHOP_INSTRUCTIONS,
            f"\n  Bring your unwanted items here![await][page]\n"
            f"  We'll exchange your Mushrooms\n       and Syrups for points.[await]\n"
            f"        For every 100 points\n    you'll get an item in return![await][page]\n"
            f"           You can choose\n     one of the following gifts\n"
            f"       to take away with you.[await][page]\n"
            f"  1)\"{bombs[0]}\"\n"
            f"  2)\"{bombs[1]}\"\n"
            f"  3)\"{bombs[2]}\"[await]"
        )

    # Replace dialog placeholders
    # Character names and parts of speech
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MARIO_NAME`", world.allies._allies[0].name)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`PEACH_NAME`", world.allies._allies[1].name)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`BOWSER_NAME`", world.allies._allies[2].name)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`GENO_NAME`", world.allies._allies[3].name)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MALLOW_NAME`", world.allies._allies[4].name)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`PEACH_ARTICLE`", "n" if world.allies._allies[1].name[0].lower() in "aeiou" else "")
    oc = world.overworld_character.ally
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_NAME`", world.allies._allies[oc.index].name)
    nm = world.overworld_character.name_props
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_GENDER`", nm.gender)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_GENDER_CASUAL`", nm.gender_casual)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_HONORIFIC`", nm.honorific)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_HONORIFIC_CAP`", nm.honorific.capitalize())
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_TITLE`", nm.title)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_TITLE_SHORT`", nm.title_short)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_MOLE_GREETING`", nm.mole_greeting)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MAIN_CHARACTER_MBOY_GREETING`", nm.mboy_greeting)

    # Wedding courtyard dialogue
    towerboss = world.get_location(BoosterTowerIndoorBossFight).prize
    assert isinstance(towerboss, BossFightPrize)
    towerboss_name = towerboss.name(
        world.settings.isflag_enabled(RemakeNames),
        world.settings.isflag_enabled(CanonNames),
    )
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`TOWER_BOSS_1`", towerboss_name)
    chapelchar = world.get_location(MarrymoreCharacter).prize
    cc_name = world.allies._allies[chapelchar._ally.index].name if isinstance(chapelchar, CharacterPrize) else "Toad"
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`MARRYMORE_CHARACTER`", cc_name)
    cc_name_pool = [n for n in 
                    [*[world.allies._allies[i].name for i in range(len(world.allies._allies))], "Toad"]
        if n != cc_name
    ]
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`RANDOM_CHARACTER_NAME`", random.choice(cc_name_pool))
    bossfight_pool = [cast(BossFightPrize, l.prize) for l in world.locations.values() if isinstance(l, BossFightLocation) and isinstance(l.prize, BossFightPrize)]
    boss_pool = [x.name(
        world.settings.isflag_enabled(RemakeNames),
        world.settings.isflag_enabled(CanonNames),
    ) for x in bossfight_pool]
    random_boss_names = random.sample([n for n in boss_pool  if n != towerboss_name], k=3)
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`RANDOM_BOSS_NAME_1`", random_boss_names[0])
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`RANDOM_BOSS_NAME_2`", random_boss_names[1])
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`RANDOM_BOSS_NAME_3`", random_boss_names[2])

    # Other settings
    sjc1 = cast(RangeFlag, world.settings.get_flag(SuperJump1Threshold)).value
    sjc2 = cast(RangeFlag, world.settings.get_flag(SuperJump2Threshold)).value
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`SUPER_JUMP_PRIZE_1_CAP`", str(sjc1))
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`SUPER_JUMP_PRIZE_2_CAP`", str(sjc2))
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`FIREWORKS_CLAUSE`", "Aren't those in Moleville?" if world.settings.is_flag_value(FireworksSetting, FireworksOptions.VANILLA) else "I wonder where you could find one?")

    # Bowser's Keep access
    keep_cond = world.settings.get_flag(BowsersKeepGate).selected
    if keep_cond == BowsersKeepGating.AXEM:
        world.overworld_dialogs.search_and_replace_in_all_dialogs("`BOWSER_KEEP_CONDITION`", "with the Axem Rangers' permission.")
    elif keep_cond == BowsersKeepGating.OPEN:
        world.overworld_dialogs.search_and_replace_in_all_dialogs("`BOWSER_KEEP_CONDITION`", "on foot.")
    elif keep_cond == BowsersKeepGating.STAR_6:
        world.overworld_dialogs.search_and_replace_in_all_dialogs("`BOWSER_KEEP_CONDITION`", "with six Star Pieces.")
    else:
        world.overworld_dialogs.search_and_replace_in_all_dialogs("`BOWSER_KEEP_CONDITION`", "through the volcano.")

    # Seaside letter
    seasideboss = world.get_location(SeasideBeachBossFight).prize
    assert isinstance(seasideboss, BossFightPrize)
    seasideboss_name = seasideboss.seaside_letter_name_if_seaside_boss(
        world.settings.isflag_enabled(RemakeNames),
        world.settings.isflag_enabled(CanonNames),
    )
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`SEASIDE_BOSS`", seasideboss_name)

    volcanoboss = world.get_location(VolcanoExitBossFight).prize
    assert isinstance(volcanoboss, BossFightPrize)
    volcanoboss_name = volcanoboss.seaside_letter_name_if_seaside_boss(
        world.settings.isflag_enabled(RemakeNames),
        world.settings.isflag_enabled(CanonNames),
    )
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`VOLCANO_BOSS_DESCRIPTION`", volcanoboss_name)

    finalboss = world.get_location(FinalBossFight).prize
    assert isinstance(finalboss, BossFightPrize)
    finalboss_name = finalboss.seaside_letter_name_if_seaside_boss(
        world.settings.isflag_enabled(RemakeNames),
        world.settings.isflag_enabled(CanonNames),
    )
    world.overworld_dialogs.search_and_replace_in_all_dialogs("`FINAL_BOSS_NAME`", finalboss_name)



    

    # Restore seed for any further operations
    random.seed(world.seed)
