from __future__ import annotations
from randomizer.data.enemies.enemies import (BELOMEEnemy3, BOWSERCOPYSEnemy, GENOCLONESEnemy, MALLOWCOPYSEnemy, MARIOCLONESEnemy, TOADSTOOL3Enemy)
from randomizer.data.packs.pack_collection import (FORM0055_ONE_BELOMEENEMY3_ONE_MARIOCLONES_ONE_TOADSTOOL3)
from randomizer.data.physical_objects.bosses import (Belome3LargeObject, Belome3SmallObject, BelomeSmallStatueObject)
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


class Belome3Fight(BossFightPrize):
    _text = "Belome 3"
    _formation = FORM0055_ONE_BELOMEENEMY3_ONE_MARIOCLONES_ONE_TOADSTOOL3
    _members = [
        FormationMember(BELOMEEnemy3, 183, 127),
        FormationMember(MARIOCLONESEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL3Enemy, 215, 159, hidden_at_start=True),
    ]
    _additional_enemies_to_scale = [BOWSERCOPYSEnemy, GENOCLONESEnemy, MALLOWCOPYSEnemy]
    _anchor_enemy = BELOMEEnemy3
    _hp_slice_excluded_enemies = [MARIOCLONESEnemy, TOADSTOOL3Enemy]

    _seaside_letter_name_if_volcano_boss = "a hungry dog walking"
    _seaside_letter_name_if_final_boss = "Belome's clones."
    _name = "Belome"

    _npc_models = [Belome3LargeObject, Belome3SmallObject]
    _statue_npc = BelomeSmallStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """[center]\nBELOME: Good night~![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Belome’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BELOME!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BELOME: Oh, you’re back![await]\n Did you bring any food?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BELOME: Say, it’s past my bedtime.\n Can you get off of my head?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ (It’s a damp, slimy looking note. Did Belome LICK this?[await][page]\n A paw print and a crudely drawn image of `VOLCANO_BOSS_DESCRIPTION` are etched on the paper.[await]\n This is probably one of `FINAL_BOSS_NAME`[await]\n Belome likely headed down to find more snacks, so it’s time to move on.)[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Belome must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BELOME: Oh, no, you’re still\n missing [0x7024] item(s).[await][pause] I can’t wait any\n longer to see what today’s cake\n will be.[await][pause] I’m STARVING![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BELOME: Mmm, you’ve found all of `MARRYMORE_CHARACTER`’s things![await]\n But they won’t bring the cake in here until we AERO_NPclean the place up.[await]\n Go Cgrab the leftover items, please.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Belome’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Belome.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BELOME: It’s dreadfully boring\n around here~![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I’m here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I’m here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Belome’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Belome.[await]""",
    }


__all__ = ["Belome3Fight"]
