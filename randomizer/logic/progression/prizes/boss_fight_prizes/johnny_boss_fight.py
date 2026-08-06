from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (BANDANABLUEEnemy, BANDANAREDEnemyHenchman, JOHNNYEnemy, WATERCRYSTALEnemy)
from randomizer.data.packs.pack_collection import (FORM0276_ONE_JOHNNY_FOUR_BANDANABLUE_TWO_WATERCRYSTAL)
from randomizer.data.physical_objects.bosses import (JohnnyLargeObject, JohnnySmallObject, JohnnyStatueObject)
from randomizer.data.physical_objects.henchmen import (BandanaBlueHenchman, BandanaRedHenchman)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1120_NIMBUS_BIRD_GUARD,
    DI1660_SHIP_PASSWORD_COMPLETE,
    DI1786_LETTER_FROM_SHIP_BOSS,
    DI1945_NIMBUS_GUARD,
    DI2061_HEAD_CHEF,
    DI2062_APPRENTICE_CHEF,
    DI2180_CHAPEL_NPC,
    DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
    DI2560_TOWER_HENCHMAN_1,
    DI2572_TOWER_HENCHMAN_2,
    DI2830_SEASIDE_BOSS_WELCOMES_YOU,
    DI2832_OCCUPIED_SEASIDE_INNKEEPER,
    DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING,
    DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED,
    DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
    DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED,
    DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER,
    DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
    DI3057_MONSTRO_SUPERBOSS_PROMPT,
    DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT,
    DI3072_TOWER_HENCHMAN_3_WINDOW,
    DI3073_TOWER_HENCHMAN_3,
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.data.variables.variable_names import (SEASIDE_BOSS_AVAILABLE)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (SetBit)
from randomizer.types.flags import (YaridovichGate, YaridovichGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class JohnnyBossFight(BossFightPrize):
    _text = "Johnny 1"
    _formation = FORM0276_ONE_JOHNNY_FOUR_BANDANABLUE_TWO_WATERCRYSTAL
    _members = [
        FormationMember(JOHNNYEnemy, 183, 127),
        FormationMember(BANDANABLUEEnemy, 135, 111),
        FormationMember(BANDANABLUEEnemy, 135, 135),
        FormationMember(BANDANABLUEEnemy, 183, 159),
        FormationMember(BANDANABLUEEnemy, 215, 151),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ]
    _name = "Johnny"
    _seaside_letter_name_if_volcano_boss = "a shark prowling around"
    _seaside_letter_name_if_final_boss = "Johnny's crew."
    _seaside_letter_name_if_sunken_ship_boss = "Jonathan “Johnny” Jones"
    _anchor_enemy = JOHNNYEnemy
    _hp_slice_excluded_enemies = [
        BANDANABLUEEnemy,
        BANDANABLUEEnemy,
        BANDANABLUEEnemy,
        BANDANABLUEEnemy,
        WATERCRYSTALEnemy,
        WATERCRYSTALEnemy,
    ]
    _scaling_excluded_enemies = [WATERCRYSTALEnemy, WATERCRYSTALEnemy]
    # Red-shark mook henchman (swapped into PACK068/PACK069). Registering it here
    # scales it with Johnny (matching Croco2/Booster/Punchinello) AND adds it to
    # the shuffler's boss_enemy_types so its henchman formations aren't reshuffled.
    _additional_enemies_to_scale = [BANDANAREDEnemyHenchman]

    _npc_models = [JohnnyLargeObject, JohnnySmallObject]
    _statue_npc = JohnnyStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
    ]
    _mook_henchmen = [
        BossFightHenchman(monster=BANDANAREDEnemyHenchman, model=BandanaRedHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JOHNNY: Matey, it’d be mighty fun\n to spar again, but I’m tryin’ to\n sleep now.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Good job, matey... But ye gotta\n fight me first if ye wanna be let\n through![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,[await][page]\n Knowin’ you, it must’ve been a breeze knockin’ down `SEASIDE_BOSS`, eh?[await]\n By the way, my pirates say they say `VOLCANO_BOSS_DESCRIPTION` across the sky.[await]\n It’s probably one of `FINAL_BOSS_NAME`[await]\n Well, my gills are failing on me, so I’ll be heading back down. Drop in when you have time, okay?[await][page]\n\n                         Your true mate,\n             Jonathan “Johnny” Jones[await]""",
        DI2061_HEAD_CHEF: """PIRATE: Y’arr, don’t ye think\n this cake here be lookin’ just like\n Johnny?[await]""",
        DI2062_APPRENTICE_CHEF: """PIRATE: Us pirates are pretty\n good with food, arr harr![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jones must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JOHNNY: Found [0x7000] item(s), eh?\n Arr, harr, harr...! Ya gotta find\n [0x7024] more, matey![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """JOHNNY: Look alive, sea slug!!!\n How’d ye manage to find all this\n gear, but not the junk in here?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Johnny is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Johnny.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nJOHNNY: Ahoy, matey![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome, matey! How’d ya like to\n stay here tonight, on the house?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two fellas o’er in the left\n building have been actin’ weird.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ It ain’t always easy gettin’ into\n the Sea.[await][pause] Ya might need to do\n somethin’ else, first![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have ye been to visit Johnny up\n on the hill yet, matey?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Arr, what ye be doin’ in our town?\n Just stay away from the shed,\n ya hear?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Out in yonder Sunken Ship, there\n be a... er...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ A treasure chest, behind a big\n stack o’ boxes! Don’t forget about\n it, matey![await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ If ye can tough it out through the\n ship, you can come back here for\n some... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Come back here for some FUN,\n arr harr! Ya got that, matey?![await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """[center]\nI just be shoppin’, matey.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Read my lips... WE AIN’T LETTIN’\n YA THROUGH![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n You ain’t gettin in here! It’s ours![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JOHNNY: Good luck, matey. The\n dojo master’s mighty tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Arr-this and Matey-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JOHNNY: Matey, I’ve got lots o’\n training to do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JOHNNY: Matey, I’ve got lots o’\n training to do![await]""",
        DI1120_NIMBUS_BIRD_GUARD: """ Read my lips... WE AIN’T LETTIN’\n YA THROUGH![await]""",
        DI1945_NIMBUS_GUARD: """ Arr, they won’t even let us go for\n a dip in the springs! We’re FISH![await]\n ...Time to unionize, arr harr![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Johnny is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Johnny.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI2560_TOWER_HENCHMAN_1: """PIRATE: Welcome, matey![await][pause] Here to\n spar with Johnny, are ye?[await][page]\n Arr, good fun! Let’s have a\n warm-up round![await]""",
        DI2572_TOWER_HENCHMAN_2: """PIRATE: This ain’t the corner you\n want, matey![await][pause] But while you’re here,\n let’s have a spar, arr harr![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """PIRATE: I know there be some fine\n loot in this tower, but it’s too far\n ’bove sea level for my liking![await]""",
        DI3073_TOWER_HENCHMAN_3: """PIRATE: I’ll make ya see stars,\n arr harr![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            YaridovichGate, YaridovichGating.JOHNNY
        ):
            output.extend([SetBit(SEASIDE_BOSS_AVAILABLE)])
        return EventScript(output)


__all__ = ["JohnnyBossFight"]
