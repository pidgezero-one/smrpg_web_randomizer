from __future__ import annotations
from randomizer.data.enemies.enemies import (CROCO2Enemy, CROOKEnemyHenchman)
from randomizer.data.packs.pack_collection import (FORM0274_ONE_CROCO2)
from randomizer.data.physical_objects.bosses import (Croco2Object, CrocoStatueObject)
from randomizer.data.physical_objects.henchmen import (CrookHenchman)
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


class Croco2BossFight(BossFightPrize):
    _text = "Croco 2"
    _formation = FORM0274_ONE_CROCO2
    _members = [
        FormationMember(CROCO2Enemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a thieving dinosaur dashing"
    _seaside_letter_name_if_final_boss = "Croco's accomplices."
    _name = "Croco"
    _additional_enemies_to_scale = [CROOKEnemyHenchman]

    _npc_models = [Croco2Object]
    _statue_npc = CrocoStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=CROOKEnemyHenchman, model=CrookHenchman),
        BossFightHenchman(monster=CROOKEnemyHenchman, model=CrookHenchman),
        BossFightHenchman(monster=CROOKEnemyHenchman, model=CrookHenchman),
    ]
    _mook_henchmen = [
        BossFightHenchman(monster=CROOKEnemyHenchman, model=CrookHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """[center]\nCROCO: Get the heck outta here![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Alright, alright, so ya figured out\n my password! But I ain’t goin’\n down without a fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Croco’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped CROCO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CROCO: Enough already, get outta\n here![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CROCO: Back already? How ’bout a\n drink?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """[center]\nCROCO: ’Dis some kinda joke?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I tapped Canada’s Maple Syrup[await]\n Reserve. They’ll NEVER catch me!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ I tapped Canada’s Maple Syrup[await]\n Reserve. They’ll NEVER catch me!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FLUNKIE: To be honest, Croco’s not\n really a bad guy.[await][pause] I guess that’s why\n we follow him.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """FLUNKIE: To be honest, Croco’s not\n really a bad guy.[await][pause] I guess that’s why\n we follow him.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n ’Sup Half-Wits?![await][page]\n Did it take you 500 years to beat `SEASIDE_BOSS`?[await]\n While chasing my next heist, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano. Seems... nice.[await]\n I better get a crew together with `FINAL_BOSS_NAME`[await]\n I’m telling you this because I want it to be a challenge this time.[await]\n I bet this bazooka that I lifted from that toad “guard” will be useful![await][page]\n\n                                    Seeya!\n                                     Croco[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """FLUNKIE: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """FLUNKIE: To be honest, Croco’s not\n really a bad guy.[await][pause] I guess that’s why\n we follow him.[await]""",
        DI2061_HEAD_CHEF: """FLUNKIE: Doesn’t this cake\n look just like Croco?[await]""",
        DI2062_APPRENTICE_CHEF: """FLUNKIE: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Croco must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CROCO: What’s this?[await][pause] You fools’re\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """CROCO: What’s this? You found all of `MARRYMORE_CHARACTER`’s things?[await]\n You’re missing a few things in this room, though. Don’t take another 50 years to find them.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Croco’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Croco.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CROCO: Whaddya doin’ hangin\n ’round here?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ You tired? You can stay here\n for free.[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Croco’s house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ You better not be snooping around\n the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Huh?[delay] What am I doing here?[delay] None\n of your business, that’s what![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nNothin’ to see here.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Nope, nothing suspicious going on\n in this house![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CROCO: Think ya can beat the dojo\n master, chump? I’d like to see ya\n try![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """FLUNKIE: (Sob, sob...)[delay_30]\n You’re pretty tough. I guess I’ll let\n you through to Croco’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """FLUNKIE: You beat Croco!?[delay_30]\n We’ll getcha for this![await][page]\n Maybe not today, maybe not\n tomorrow, but someday...[await]""",
        DI2560_TOWER_HENCHMAN_1: """FLUNKIE: Croco’s busy! Scram![await]\n[delay_60] ...Not leaving, huh?\n[delay] Alright buddy, you asked for it![await]""",
        DI2572_TOWER_HENCHMAN_2: """FLUNKIE: Where d’ya think YOU’RE\n going?![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """[center]\nFLUNKIE: I could use a stepstool.[await]""",
        DI3073_TOWER_HENCHMAN_3: """[center]\nFLUNKIE: A tough guy, eh?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Croco’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Croco.[await]""",
    }


__all__ = ["Croco2BossFight"]
