from __future__ import annotations
from randomizer.data.enemies.enemies import (BLOOBEREnemyHenchman, KINGCALAMARIEnemy, TENTACLESEnemy, TENTACLESEnemy2)
from randomizer.data.packs.pack_collection import (FORM0277_ONE_KINGCALAMARI_TWO_TENTACLESENEMY2_THREE_TENTACLES)
from randomizer.data.physical_objects.bosses import (BlooberObject, BlooberStatueObject)
from randomizer.data.physical_objects.henchmen import (BlooberHenchman, TinyBlooberHenchman)
from randomizer.data.variables.battle_event_names import (BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES)
from randomizer.data.variables.battlefield_names import (BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
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


class KingCalamariBossFight(BossFightPrize):
    _text = "King Calamari"
    _formation = FORM0277_ONE_KINGCALAMARI_TWO_TENTACLESENEMY2_THREE_TENTACLES
    _members = [
        FormationMember(KINGCALAMARIEnemy, 222, 94, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 136, 115, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 112, 127, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 193, 143, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 168, 156, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 135, 143, hidden_at_start=True),
    ]
    _extra_hp_enemies = [TENTACLESEnemy2, TENTACLESEnemy2, TENTACLESEnemy]
    _anchor_enemy = KINGCALAMARIEnemy
    _additional_enemies_to_scale = [BLOOBEREnemyHenchman]

    _force_start_event = BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES
    _force_battlefield = BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR
    _seaside_letter_name_if_seaside_boss = "the Squid"
    _seaside_letter_name_if_volcano_boss = "a giant squid lurking"
    _seaside_letter_name_if_final_boss = "King Calamari's hands."

    _npc_models = [BlooberObject]
    _statue_npc = BlooberStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=BLOOBEREnemyHenchman, model=BlooberHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=BLOOBEREnemyHenchman, model=TinyBlooberHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """KING CALAMARI: When I was born, I\n hatched from an egg that was only\n three times as large as this one.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to King Calamari’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n KING CALAMARI!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """KING CALAMARI: I can’t believe I\n was defeated in the ship I sunk\n myself...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """KING CALAMARI: Win or lose, I’m\n still king of this ship.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """KING CALAMARI: I’m pretty slimy,\n so this seems like a bad idea.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I’ve found booty in the hold![await]\n Vats of Pearlescent Oyster Juice![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ I’ve found booty in the hold![await]\n Vats of Pearlescent Oyster Juice![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n There’s a wet parchment with ink:[await][page]\n There’s a surpringly great picture of your battle with `SEASIDE_BOSS`.[await][page]\n On the back is an image of\n `VOLCANO_BOSS_DESCRIPTION` near a volcano, looks like.[await]\n Then a bunch of ?’s next to `FINAL_BOSS_NAME`[await]\n Finally, there’s a picture of a squid with X’s for eyes falling towards the shipwreck.[await]\n This drawing raises more questions than it answers.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: "[center]\n••••••[await]",
        DI2062_APPRENTICE_CHEF: "[center]\n••••••[await]",
        DI2180_CHAPEL_NPC: """ Reverend Calamari must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """KING CALAMARI: Sorry, I don’t\n have any hint memos for where you\n can find the last [0x7024] item(s).[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """KING CALAMARI: Great job. You\n found all the gear. But you’re\n missing some things in this room.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n King Calamari is busy right now, so\n he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering King Calamari.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """KING CALAMARI: It’s not so weird\n for a squid to run a town.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ (Stay in the inn for free?)[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: "[center]\n••••••[await]",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: "[center]\n••••••[await]",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: "[center]\n••••••[await]",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: "[center]\n••••••[await]",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: "[center]\n••••••[await]",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: "[center]\n••••••[await]",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: "[center]\n••••••[await]",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """KING CALAMARI: Think you can beat\n the dojo master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What do you want?[await]\n  [select] (Let’s fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What do you want?[await]\n  [select] (Let’s fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Ship-this and Tentacle-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """KING CALAMARI: My tentacles\n shouldn’t be able to do this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """KING CALAMARI: My tentacles\n shouldn’t be able to do this.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI2560_TOWER_HENCHMAN_1: """ Hello there. Welcome to our\n first-ever above-ground treasure\n hoard.[await][page]\n [delay].[delay].[delay].[delay]You’re not here to see that?[delay_30]\n Well,[delay] then you must be an intruder!""",
        DI2572_TOWER_HENCHMAN_2: """ There’s nothing back here!\n I mean it![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """ You’ve made your point, we’ll step\n aside. But you haven’t seen\n anything yet![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """ You beat King Calamari?[await][pause] I guess\n that’s why this is a Mario game and\n not a Squid Game.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """ I’d just like to go back to\n shooting ink, not bullets...[await]""",
        DI3073_TOWER_HENCHMAN_3: """[center]\nYou looking for a fight?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n King Calamari is busy right now, so\n he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering King Calamari.[await]""",
    }


__all__ = ["KingCalamariBossFight"]
