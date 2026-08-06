from __future__ import annotations
from randomizer.data.enemies.enemies import (BIRDETTAEnemy, EGGBERTEnemy, SHELLYEnemy)
from randomizer.data.packs.pack_collection import (FORM0285_ONE_BIRDETTA_ONE_SHELLY_FOUR_EGGBERT)
from randomizer.data.physical_objects.bosses import (BirdettaLargeObject, BirdettaSmallObject, BirdettaStatueObject)
from randomizer.data.physical_objects.henchmen import (EggbertHenchman)
from randomizer.data.variables.battlefield_names import (BF23_NIMBUS_CASTLE_BIRDOS_ROOM)
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


class BirdettaBossFight(BossFightPrize):
    _text = "Birdo"
    _formation = FORM0285_ONE_BIRDETTA_ONE_SHELLY_FOUR_EGGBERT
    _members = [
        FormationMember(BIRDETTAEnemy, 167, 118, hidden_at_start=True),
        FormationMember(SHELLYEnemy, 171, 103),
        FormationMember(EGGBERTEnemy, 135, 119, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 135, 135, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 167, 151, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 199, 151, hidden_at_start=True),
    ]
    _anchor_enemy = BIRDETTAEnemy
    _hp_slice_excluded_enemies = [
        EGGBERTEnemy,
        EGGBERTEnemy,
        EGGBERTEnemy,
        EGGBERTEnemy,
    ]
    _force_battlefield = BF23_NIMBUS_CASTLE_BIRDOS_ROOM
    _seaside_letter_name_if_volcano_boss = "a giant egg rolling"
    _seaside_letter_name_if_final_boss = "Birdo's bad eggs."
    _seaside_letter_name_if_seaside_boss_canon = "Birdetta's bad eggs."

    _npc_models = [BirdettaLargeObject, BirdettaSmallObject]
    _statue_npc = BirdettaStatueObject

    _gender = ("she", "her", "her", "hers", "herself")

    _mook_henchmen = [
        BossFightHenchman(monster=EGGBERTEnemy, model=EggbertHenchman),
    ]

    _tiny_henchmen = [
        BossFightHenchman(monster=EGGBERTEnemy, model=EggbertHenchman),
    ]

    _dialog_replacements = {
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, yay, you’ve come to play!\n Come on in~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Birdo’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n BIRDO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BIRDO: Tee hee! Let’s play\n again sometime![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BIRDO: Oh, you didn’t forget\n about me! You’re so sweet![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BIRDO: This isn’t what I had in\n mind when I said I wanted to play![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Thanks for playing with me~![await]\n I lost, but I made Yoshi’s Eggnog![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Thanks for playing with me~![await]\n I lost, but I made Yoshi’s Eggnog![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """EGGBERT: You visiting us has\n really made Birdo happy.\n Thank you![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """EGGBERT: You visiting us has\n really made Birdo happy.\n Thank you![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hi `MAIN_CHARACTER_NAME`♥![await][page]\n Did `SEASIDE_BOSS` submit to the power of HUGS?!♥[await]\n While doing some incubating, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n My eggies♥ think they scramble with `FINAL_BOSS_NAME`[await]\n My lovelies♪ and I have to get back to the ship, and the bouyant forces of seawater aren’t helping.[await]\n Stop by again soon♥! [await][page]\n\n                           ♥XO♥XO♥XO♥\n                                     Birdo[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EGGBERT: You visiting us has\n really made Birdo happy.\n Thank you![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """EGGBERT: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """EGGBERT: We’re making this cake\n look just like Birdo![await]""",
        DI2062_APPRENTICE_CHEF: """EGGBERT: No eggs were harmed\n in the making of this cake.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Birdo must have gotten\n lost on her way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BIRDO: Hello![await]\n ...Oh, no, you’re still missing\n [0x7024] item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BIRDO: Oh, hooray!\n You found all the wedding\n decorations![await]\n Don’t forget to clean out this room\n so we can get the fun started♥![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nBIRDO: Hello![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello! You’ve been chosen to stay\n here in our lovely inn for FREE!\n Aren’t you lucky?[await]\n Will you stay with us?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Birdo’s busy right now, so she\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Birdo.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Birdo’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hi![delay] Welcome to our town![delay]\n Stay away from our shed, OK~?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Do you think they sell frying pans\n here?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ It’s perfectly normal for two eggs\n to stand outside a locked house![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There’s nothing weird going on\n here![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BIRDO: Ooh, are you gonna play\n with the dojo master?![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello! Did you come to play?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello! Did you come to play?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She’s always mumbling about\n Egg-this and Playtime-that.[await][page]\n Sometimes I’d like to ask her what\n she’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BIRDO: Thanks for playing with\n me~![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BIRDO: Thanks for playing with\n me~![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Birdo’s busy right now, so she\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Birdo.[await]""",
    }
    _dialog_replacements_canon = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n[center]BIRDETTA: Don’t forget about me![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Birdetta’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n BIRDETTA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BIRDETTA: Tee hee! Let’s play\n again sometime![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BIRDETTA: Oh, you didn’t forget\n about me! You’re so sweet![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BIRDETTA: This isn’t what I had in\n mind when I said I wanted to play![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hi `MAIN_CHARACTER_NAME`♥![await][page]\n Did `SEASIDE_BOSS` submit to the power of HUGS?!♥[await]\n While doing some incubating, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n My eggies♥ think they scramble with `FINAL_BOSS_NAME`[await]\n My lovelies♪ and I have to get back to the ship, and the bouyant forces of seawater aren’t helping.[await]\n Stop by again soon♥! [await][page]\n\n                           ♥XO♥XO♥XO♥\n                                  Birdetta[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI2061_HEAD_CHEF: """EGGBERT: We’re making this cake\n look just like Birdetta![await]""",
        DI2062_APPRENTICE_CHEF: """EGGBERT: No eggs were harmed\n in the making of this cake.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Birdetta must have\n gotten lost on her way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BIRDETTA: Hello![await]\n ...Oh, no, you’re still missing\n [0x7024] item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BIRDETTA: Oh, hooray!\n You found all the wedding\n decorations![await]\n Don’t forget to clean out this room\n so we can get the fun started♥![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Birdetta’s busy right now, so she\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Birdetta.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nBIRDETTA: Hello![await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Birdetta’s\n house up on the hill yet?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BIRDETTA: Ooh, are you gonna play\n with the dojo master?![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She’s always mumbling about\n Egg-this and Playtime-that.[await][page]\n Sometimes I’d like to ask her what\n she’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BIRDETTA: Thanks for playing with\n me~![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BIRDETTA: Thanks for playing with\n me~![await]""",
    }
    _dialog_replacements_canon_and_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Birdetta’s busy right now, so she\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Birdetta.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """EGGBERT: Wow, you sure showed\n us! Don’t disappoint Birdo![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """EGGBERT: Thanks for playing\n with us today![await]""",
        DI2560_TOWER_HENCHMAN_1: """EGGBERT: Birdo’s feeling lonely\n today, so feel free to pay her a\n visit upstairs.[await][pause] I’m sure she’d love\n the company.[await][page]\n Just, let me make sure you’ll be\n nice, first![await]""",
        DI2572_TOWER_HENCHMAN_2: """EGGBERT: Pardon me, Birdo’s\n not back here. Please refrain from\n snooping around.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EGGBERT: What did Birdo want\n me to do here, again? I’m just an\n egg![await]""",
        DI3073_TOWER_HENCHMAN_3: """EGGBERT: You’re making me so\n mad, I could explode![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_canon = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """EGGBERT: Wow, you sure showed\n us! Don’t disappoint Birdetta![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """EGGBERT: Thanks for playing\n with us today![await]""",
        DI2560_TOWER_HENCHMAN_1: """EGGBERT: Birdetta’s feeling lonely\n today, so feel free to pay her a\n visit upstairs.[await][pause] I’m sure she’d love\n the company.[await][page]\n Just, let me make sure you’ll be\n nice, first![await]""",
        DI2572_TOWER_HENCHMAN_2: """EGGBERT: Pardon me, Birdetta’s\n not back here. Please refrain from\n snooping around.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EGGBERT: What did Birdetta want\n me to do here, again? I’m just an\n egg![await]""",
    }


__all__ = ["BirdettaBossFight"]
