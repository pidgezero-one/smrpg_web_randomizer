from __future__ import annotations
from randomizer.data.enemies.enemies import (GOOMBETTEEnemy, HIDONEnemy)
from randomizer.data.packs.pack_collection import (FORM0267_ONE_HIDON_FOUR_GOOMBETTE)
from randomizer.data.physical_objects.bosses import (HidonLargeObject, HidonSmallObject, MimicStatueObject)
from randomizer.data.physical_objects.henchmen import (GoombetteLowerHenchman)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1120_NIMBUS_BIRD_GUARD,
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
    DI1945_NIMBUS_GUARD,
    DI2023_SHIP_BOSS_2_DRINK,
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
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class HidonBossFight(BossFightPrize):
    _text = "Hidon"
    _formation = FORM0267_ONE_HIDON_FOUR_GOOMBETTE
    _members = [
        FormationMember(HIDONEnemy, 167, 119),
        FormationMember(GOOMBETTEEnemy, 135, 111, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 135, 135, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 167, 151, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 215, 151, hidden_at_start=True),
    ]
    _anchor_enemy = HIDONEnemy
    _hp_slice_excluded_enemies = [
        GOOMBETTEEnemy,
        GOOMBETTEEnemy,
        GOOMBETTEEnemy,
        GOOMBETTEEnemy,
    ]

    _seaside_letter_name_if_volcano_boss = "a green box sliding about"
    _seaside_letter_name_if_final_boss = "Hidon's monsters."
    _seaside_letter_name_if_final_boss_remake = "Whuhoh's Goombas."
    _remake_name = "Whuhoh"

    _npc_models = [HidonLargeObject, HidonSmallObject]
    _statue_npc = MimicStatueObject

    _gender = ("it", "it", "its", "its", "itself")

    _mook_henchmen = [
        BossFightHenchman(monster=GOOMBETTEEnemy, model=GoombetteLowerHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=GOOMBETTEEnemy, model=GoombetteLowerHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HIDON: No, I’m not gonna puke up\n another item for you! Go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Ugh... What a rude awakening!\n I’m going to make it a hassle for\n you to pass through here![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Hidon’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped HIDON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HIDON: Guess I’ll have to train the\n Goombettes harder.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HIDON: This is definitely an upgrade\n from my old post.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HIDON: Oh come on, you know I’m\n weak to jumps![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Goombettes! They’re after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Goombettes! They’re after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Listen up interloper![await][page]\n Good job getting rid of `SEASIDE_BOSS`! Now my naval dominance is complete![await]\n The Goombettes’ nest reported `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They sail under the flag of `FINAL_BOSS_NAME`[await]\n If you ever touch my box again, I’m taking a finger... at least.[await][page]\n\n                  Lots of Carni-kisses,\n                                    Hidon[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """GOOMBETTE: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI2061_HEAD_CHEF: """GOOMBETTE: Doesn’t this cake\n look just like Hidon?[await]""",
        DI2062_APPRENTICE_CHEF: """GOOMBETTE: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Hidon must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HIDON: ...I don’t know where the\n last [0x7024] item(s) are. Ask the\n Goombettes.[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """HIDON: ...You’re still missing a few\n things. They should be in this room.\n The Goombettes can help you.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Hidon is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Hidon.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nHIDON: Oh, it’s you.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hey! Why don’t you crash here for\n the night? It’s free! FREE![await]\n  [select] (Cool, thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Hidon’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hey! What are you doing in our\n town? Don’t go snooping around![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Why don’tcha mind your own\n beeswax?![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Don’t even THINK about going\n inside this house![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hey, buster![delay] You think you’re some\n kinda tough guy, tryin’ to step\n over us guards?![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HIDON: The dojo master’s pretty\n tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Ugh... What’d you wake me up for?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Ugh... What’d you wake me up for?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Treasure-this and Piranha-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HIDON: I bet this would be even\n harder to do in my box.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HIDON: I bet this would be even\n harder to do in my box.[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """WHUHOH: No, I’m not gonna puke up\n another item for you! Go away![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Whuhoh’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped WHUHOH!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """WHUHOH: Guess I’ll have to train\n the Mini Goombas harder.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """WHUHOH: This is definitely an\n upgrade from my old post.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """WHUHOH: Oh come on, you know I’m\n weak to jumps![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Mini Goombas! They’re after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Mini Goombas! They’re after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """MINI GOOMBA: Besides when he\n haphazardly throws us at enemies,\n Whuhoh is very good to us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Listen up interloper![await][page]\n Good job getting rid of `SEASIDE_BOSS`! Now my naval dominance is complete![await]\n The Mini Goombas’ nest reported `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They sail under the flag of `FINAL_BOSS_NAME`[await]\n If you ever touch my box again, I’m taking a finger... at least.[await][page]\n\n                  Lots of Carni-kisses,\n                                    Whuhoh[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """MINI GOOMBA: Hop on the\n trampoline in the next room. It’ll\n take you outside. Go on, try it![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """MINI GOOMBA: Besides when he\n haphazardly throws us at enemies,\n Whuhoh is very good to us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """MINI GOOMBA: Besides when he\n haphazardly throws us at enemies,\n Whuhoh is very good to us.[await]""",
        DI2061_HEAD_CHEF: """MINI GOOMBA: Doesn’t this cake\n look just like Whuhoh?[await]""",
        DI2062_APPRENTICE_CHEF: """MINI GOOMBA: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Whuhoh must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """WHUHOH: ...I don’t know where the\n last [0x7024] item(s) are. Ask the\n Mini Goombas.[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """WHUHOH: ...You’re still missing a\n few things. They should be in this\n room. The Mini Goombas can help.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Whuhoh is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Whuhoh.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nWHUHOH: Oh, it’s you.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Whuhoh’s\n house up on the hill yet?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """WHUHOH: The dojo master’s pretty\n tough.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """WHUHOH: I bet this would be even\n harder to do in my box.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """WHUHOH: I bet this would be even\n harder to do in my box.[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """MINI GOOMBA: Oh yeah? Think\n you’re tough, just ’cause you’re\n bigger than me?![await]""",
        DI1945_NIMBUS_GUARD: """MINI GOOMBA: I heard you laughing!\n Go on, laugh it up! At least I’m\n allowed in the castle![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """GOOMBETTE: You mighta’ won\n against us, but Hidon’s gonna\n beat you up![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """GOOMBETTE: You beat Hidon?![await]\n Oh, man...[await]""",
        DI2560_TOWER_HENCHMAN_1: """GOOMBETTE: I need a pen, but I\n can’t reach the top drawer of this\n desk. Can you help me out?[await][page]\n [delay]...What?[delay] “How are you going to\n use a pen when you don’t have any\n arms”?[await][pause] You makin’ fun of me?!\n [delay]That’s IT, buddy! Get down here![await]""",
        DI2572_TOWER_HENCHMAN_2: """GOOMBETTE: Hey! Hidon’s trying to\n stay in hidin’ over here![delay] Get lost![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """GOOMBETTE: (I’m too short to see\n out this window.)[await]""",
        DI3073_TOWER_HENCHMAN_3: """GOOMBETTE: Put up your dukes,\n tough guy![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """MINI GOOMBA: You mighta’ won\n against us, but Whuhoh’s gonna\n beat you up![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """MINI GOOMBA: You beat Whuhoh?![await]\n Oh, man...[await]""",
        DI2560_TOWER_HENCHMAN_1: """MINI GOOMBA: I need a pen, but I\n can’t reach the top drawer of this\n desk. Can you help me out?[await][page]\n [delay]...What?[delay] “How are you going to\n use a pen when you don’t have any\n arms”?[await][pause] You makin’ fun of me?!\n [delay]That’s IT, buddy! Get down here![await]""",
        DI2572_TOWER_HENCHMAN_2: """MINI GOOMBA: Hey! Whuhoh’s trying\n to stay in hidin’ over here![delay_30]\n Get lost![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """MINI GOOMBA: (I’m too short to\n see out this window.)[await]""",
        DI3073_TOWER_HENCHMAN_3: """MINI GOOMBA: Put up your dukes,\n tough guy![await]""",
    }


__all__ = ["HidonBossFight"]
