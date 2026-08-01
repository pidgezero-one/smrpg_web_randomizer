from __future__ import annotations
from randomizer.data.enemies.enemies import (JOHNNYEnemy2, WATERCRYSTALEnemy)
from randomizer.data.packs.pack_collection import (FORM0216_ONE_JOHNNYENEMY2)
from randomizer.data.physical_objects.bosses import (Johnny2LargeObject, Johnny2SmallObject, JohnnyStatueObject)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1660_SHIP_PASSWORD_COMPLETE,
    DI1786_LETTER_FROM_SHIP_BOSS,
    DI2061_HEAD_CHEF,
    DI2180_CHAPEL_NPC,
    DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
    DI2560_TOWER_HENCHMAN_1,
    DI2572_TOWER_HENCHMAN_2,
    DI2830_SEASIDE_BOSS_WELCOMES_YOU,
    DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
    DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
    DI3057_MONSTRO_SUPERBOSS_PROMPT,
    DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT,
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class Johnny2Fight(BossFightPrize):
    _text = "Johnny 2"
    _formation = FORM0216_ONE_JOHNNYENEMY2
    _members = [
        FormationMember(JOHNNYEnemy2, 165, 121),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ]
    _name = "Johnny"
    _seaside_letter_name_if_volcano_boss = "a shark prowling around"
    _seaside_letter_name_if_final_boss = "Johnny's crew."
    _seaside_letter_name_if_sunken_ship_boss = "Jonathan “Johnny” Jones"

    _npc_models = [Johnny2LargeObject, Johnny2SmallObject]
    _statue_npc = JohnnyStatueObject
    _scaling_excluded_enemies = [WATERCRYSTALEnemy, WATERCRYSTALEnemy]
    _hp_slice_excluded_enemies = [WATERCRYSTALEnemy, WATERCRYSTALEnemy]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JOHNNY: Matey, it’d be mighty fun\n to spar again, but I’m tryin’ to\n sleep now.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Good job, matey... But ye gotta\n fight me first if ye wanna be let\n through![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,[await][page]\n Knowin’ you, it must’ve been a breeze knockin’ down `SEASIDE_BOSS`, eh?[await]\n By the way, my pirates say they say `VOLCANO_BOSS_DESCRIPTION` across the sky.[await]\n It’s probably one of `FINAL_BOSS_NAME`[await]\n Well, my gills are failing on me, so I’ll be heading back down. Drop in when you have time, okay?[await][page]\n\n                         Your true mate,\n             Jonathan “Johnny” Jones[await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like shark! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jones must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JOHNNY: Found [0x7000] item(s, eh? Arr,\n harr, harr...! You gotta find [0x7024]\n more, matey![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """JOHNNY: Look alive, sea slug!!!\n How’d ye manage to find all this\n gear, but not the junk in here?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Johnny is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Johnny.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nJOHNNY: Ahoy, matey![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Johnny...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JOHNNY: Good luck, matey. The\n dojo master’s mighty tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Arr-this and Matey-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JOHNNY: Matey, I’ve got lots o’\n training to do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JOHNNY: Matey, I’ve got lots o’\n training to do![await]""",
    }


__all__ = ["Johnny2Fight"]
