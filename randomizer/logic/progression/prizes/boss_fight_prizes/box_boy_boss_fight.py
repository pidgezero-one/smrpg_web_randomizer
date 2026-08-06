from __future__ import annotations
from randomizer.data.enemies.enemies import (BOXBOYEnemy, FAUTSOEnemy)
from randomizer.data.packs.pack_collection import (FORM0268_ONE_BOXBOY_ONE_FAUTSO)
from randomizer.data.physical_objects.bosses import (BoxBoyLargeObject, BoxBoySmallObject, MimicStatueObject)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1660_SHIP_PASSWORD_COMPLETE,
    DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
    DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
    DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
    DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
    DI1781_SHIP_BOSS_JUMP_ON_HEAD,
    DI1782_SHIP_BOSS_DRINK,
    DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
    DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1,
    DI1786_LETTER_FROM_SHIP_BOSS,
    DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
    DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4,
    DI2023_SHIP_BOSS_2_DRINK,
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


class BoxBoyBossFight(BossFightPrize):
    _text = "Box Boy"
    _formation = FORM0268_ONE_BOXBOY_ONE_FAUTSO
    _members = [
        FormationMember(BOXBOYEnemy, 183, 127),
        FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a grey box sliding about"
    _seaside_letter_name_if_final_boss = "Box Boy's monsters."
    _seaside_letter_name_if_final_boss_remake = "Pleaseno's monsters."
    _remake_name = "Pleaseno"
    _hp_slice_excluded_enemies = [FAUTSOEnemy]
    _anchor_enemy = BOXBOYEnemy

    _npc_models = [BoxBoyLargeObject, BoxBoySmallObject]
    _statue_npc = MimicStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOX BOY: How many times are you\n gonna wake me up? Get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, you’re gonna PAY for waking\n me up like this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Box Boy’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BOX BOY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nBOX BOY: You just got lucky![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """[center]\nBOX BOY: This place is boring.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOX BOY: You sure you wanna jump\n on me? I counter special attacks.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ You don’t even deserve to LOOK at[await]\n My 1990 Comanee-Ronti Pinot Noir![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ You don’t even deserve to LOOK at[await]\n My 1990 Comanee-Ronti Pinot Noir![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Trespassers BEWARE:[await][page]\n Loitering Prohibited (yes, you too `SEASIDE_BOSS`!)[await]\n Don’t think I didn’t see `VOLCANO_BOSS_DESCRIPTION` either, keep to your volcano.[await]\n And there will be no exceptions made for `FINAL_BOSS_NAME`[await]\n Also, I expect SILENCE. No spells. Casting a spell is a good way to get blasted.  You’ve been warned.[await][page]\n\n             Now, GET OFF MY LAWN!!\n                                  Box Boy[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Boy must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOX BOY: Still missing [0x7024] item(s)?\n Pathetic![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BOX BOY: Hey, loser! You found all\n this gear, but missed the junk in\n here? Pathetic!""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Box Boy’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Box Boy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BOX BOY:\n[center]What’d you come here for?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Box Boy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOX BOY: The dojo master’s gonna\n kick your butt![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ This’d BETTER be important![await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ This’d BETTER be important![await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOX BOY:\n[center]Ahh, you’re not so tough![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOX BOY:\n[center]Ahh, you’re not so tough![await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PLEASENO: How many times are you\n gonna wake me up? Get lost![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Pleaseno’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped PLEASENO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nPLEASENO: You just got lucky![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """[center]\nPLEASENO: This place is boring.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PLEASENO: You sure you wanna\n jump on me? I counter special\n attacks.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n  Trespassers BEWARE:[await][page]\n Loitering Prohibited (yes, you too `SEASIDE_BOSS`!)[await]\n Don’t think I didn’t see `VOLCANO_BOSS_DESCRIPTION` either, keep to your volcano.[await]\n And there will be no exceptions made for `FINAL_BOSS_NAME`[await]\n Also, I expect SILENCE. No spells. Casting a spell is a good way to get blasted.  You’ve been warned.[await][page]\n\n             Now, GET OFF MY LAWN!!\n                                  Pleaseno[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Pleaseno must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PLEASENO: Still missing [0x7024] item(s)?\n Pathetic![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """PLEASENO: Hey, loser! You found\n all this gear, but missed the junk\n in here? Pathetic![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Pleaseno’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Pleaseno.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PLEASENO:\n[center]What’d you come here for?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Pleaseno...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PLEASENO: The dojo master’s gonna\n kick your butt![await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PLEASENO:\n[center]Ahh, you’re not so tough![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PLEASENO:\n[center]Ahh, you’re not so tough![await]""",
    }


__all__ = ["BoxBoyBossFight"]
