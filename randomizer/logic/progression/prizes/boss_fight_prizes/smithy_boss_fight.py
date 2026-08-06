from __future__ import annotations
from randomizer.data.enemies.enemies import (MACHINEMADEBodyguardEnemy, SMELTEREnemy, SMITHY1Enemy, SMITHY2Enemy, SMITHYBodyEnemy, SMITHYChestEnemy, SMITHYMageEnemy, SMITHYSafeEnemy2, SMITHYTankEnemy)
from randomizer.data.packs.pack_collection import (FORM0295_ONE_SMITHY1_ONE_SMELTER_TWO_MACHINEMADEBODYGUARD)
from randomizer.data.physical_objects.bosses import (SmithyLargeObject, SmithySmallObject, SmithyStatueObject)
from randomizer.data.variables.battlefield_names import (BF44_FACTORY_GROUNDS_SMITHYS_PAD)
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


class SmithyBossFight(BossFightPrize):
    _text = "Smithy"
    _formation = FORM0295_ONE_SMITHY1_ONE_SMELTER_TWO_MACHINEMADEBODYGUARD
    _members = [
        FormationMember(SMITHY1Enemy, 199, 127),
        FormationMember(SMELTEREnemy, 87, 87),
        FormationMember(MACHINEMADEBodyguardEnemy, 135, 127, hidden_at_start=True),
        FormationMember(MACHINEMADEBodyguardEnemy, 199, 159, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a furious weaponsmith thundering"
    _seaside_letter_name_if_final_boss = "Smithy's gang."
    _hp_slice_excluded_enemies = [
        MACHINEMADEBodyguardEnemy,
        MACHINEMADEBodyguardEnemy,
        SMELTEREnemy,
    ]
    _extra_hp_enemies = [SMITHY2Enemy]
    _additional_enemies_to_scale = [
        SMITHYBodyEnemy,
        SMITHYChestEnemy,
        SMITHYMageEnemy,
        SMITHYSafeEnemy2,
        SMITHYTankEnemy,
    ]

    _npc_models = [SmithyLargeObject, SmithySmallObject]
    _statue_npc = SmithyStatueObject
    
    _force_battlefield = BF44_FACTORY_GROUNDS_SMITHYS_PAD

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """SMITHY: How utterly annoying!\n Leave me alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Gufaw, haw, haw![delay_30] You really think\n I’m going to let you through with\n just a password?![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Smithy’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n SMITHY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """SMITHY: How utterly annoying!\n Get out of here before I crush\n you all![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """SMITHY: Gufaw, haw, haw...\n Not quite as impressive as my\n factory, eh?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """SMITHY: Never have I been so\n wronged![await]""",
        DI1782_SHIP_BOSS_DRINK: """ This isn’t even my final form![await]\n Barkeep!  Bring me more Ale!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ This isn’t even my final form![await]\n Barkeep!  Bring me more Ale!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Weakling,[await][page]\n I’ll bet you had trouble with `SEASIDE_BOSS`. Pathetic.[await]\n A Drill Bit screamed about `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I expected better from `FINAL_BOSS_NAME`[await]\n The Shyper is complaining about my blood pressure again. I have a sledge for problems like these.[await][page]\n\n You haven’t seen my final form yet,\n                                    Smithy[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like blacksmith! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Smithy must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """SMITHY: How utterly annoying![await]\n Give me [0x7024] more item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """SMITHY: How utterly annoying![await]\n You found all the gear, but there\n are still items in this room![await]\n Pick them up before I crush you![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Smithy’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Smithy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """SMITHY: So, it’s YOU![await]\n Unfortunately for you, there’s\n nothing evil in this town that\n demands your attention.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Smithy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """[center]\nSMITHY: Grr... Leave me alone![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Grr... What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Grr... What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Factory-this and Weapon-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """SMITHY: Grr... [delay]You’re stronger\n than I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """SMITHY: Grr... [delay]You’re stronger\n than I thought...[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Smithy’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Smithy.[await]""",
    }


__all__ = ["SmithyBossFight"]
