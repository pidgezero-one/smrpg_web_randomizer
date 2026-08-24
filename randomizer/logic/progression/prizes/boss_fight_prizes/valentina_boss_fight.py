from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (BIRDYEnemyHenchman, BLUEBIRDEnemyHenchman, DODOEnemy, VALENTINAEnemy)
from randomizer.data.packs.pack_collection import (FORM0281_ONE_VALENTINA_ONE_DODO)
from randomizer.data.physical_objects.bosses import (NimbusLandStatueObject, ValentinaLargeObject, ValentinaSmallObject)
from randomizer.data.physical_objects.henchmen import (BirdyHenchman, BluebirdHenchman)
from randomizer.data.variables.battle_event_names import (BE0038_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT)
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
from randomizer.data.variables.variable_names import (MAP_BARREL_VOLCANO, MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (SetBit)
from randomizer.types.flags import (BarrelVolcanoGate, BarrelVolcanoGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)


class ValentinaBossFight(BossFightPrize):
    _text = "Valentina"
    _formation = FORM0281_ONE_VALENTINA_ONE_DODO
    _members = [
        FormationMember(VALENTINAEnemy, 183, 127),
        FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a bossy lady being carried"
    _seaside_letter_name_if_final_boss = "Valentina's little birds."
    _anchor_enemy = VALENTINAEnemy
    _additional_enemies_to_scale = [BLUEBIRDEnemyHenchman, BIRDYEnemyHenchman]
    # Dodo contributes 40% of his HP to the pie total, but gets 2.5x his calculated slice
    _hp_pie_contribution_multipliers = {DODOEnemy: 0.4}
    _hp_slice_multipliers = {DODOEnemy: 2.5}
    _force_start_event = BE0038_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT

    _npc_models = [ValentinaLargeObject, ValentinaSmallObject]
    _statue_npc = NimbusLandStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=BLUEBIRDEnemyHenchman, model=BluebirdHenchman),
        BossFightHenchman(monster=BIRDYEnemyHenchman, model=BirdyHenchman),
    ]

    _gender = ("she", "her", "her", "hers", "herself")

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """VALENTINA: ...What? You’re STILL\n here?! Go AWAY!!![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ ALRIGHT, already![delay_30] If you’re going\n to annoy me like this, get in here\n and finish the job![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Valentina’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n VALENTINA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """VALENTINA: If you don’t stop\n bothering me, I’m going to turn\n your mustache into a\n vegetable scrubber![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """VALENTINA: YOU again?! You better\n have brought some margaritas![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """VALENTINA: Get OFF of my head\n before I take your shoes and throw\n them in the ocean!!![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Pfffft!  You call THIS a Martini?[await]\n MAKE IT AGAIN, and I MIGHT tip!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Pfffft!  You call THIS a Martini?[await]\n MAKE IT AGAIN, and I MIGHT tip!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Valentina’s grumpy. Booster got\n her a gold beetle for their\n anniversary.[await][pause] She wanted a ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Valentina’s grumpy. Booster got\n her a gold beetle for their\n anniversary.[await][pause] She wanted a ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To whom it may concern,[await][page]\n Make sure that pesky `SEASIDE_BOSS` is gone by the time I get back.[await]\n A little birdy told me they saw `VOLCANO_BOSS_DESCRIPTION` near the volcano. Gross.[await]\n I cannot abide any more of `FINAL_BOSS_NAME` They’re all beneath me. Literally.[await]\n Well, I’ve got a ship full of idiots to command. Don’t call, I have a boyfriend. His name is...Booster.[await][page]\n\n                       NOT yours,\n                         Valentina[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Valentina’s grumpy. Booster got\n her a gold beetle for their\n anniversary.[await][pause] She wanted a ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """ Why are we making a cake that\n looks like Valentina, again?[await]""",
        DI2062_APPRENTICE_CHEF: """ We’re making a cake that looks like\n Valentina.[await][pause] What else would we\n do on our day off?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Valentina must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """VALENTINA: STOP BOTHERING ME![await]\n If you need something to do, go\n look for [0x7024] more item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """VALENTINA: You’re STILL missing a\n few things in this room!\n USELESS!!![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Valentina’s busy right now, so she\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Valentina.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nVALENTINA: I’m SO frustrated![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome![delay] I’ll let you stay here for\n free, but don’t tell Valentina.[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Valentina’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hmm...[delay] What’re you loitering\n around here for?[delay] Uh...[delay] Stay away\n from the shed, OK?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ ...I’m on my break. [delay]Just let me\n shop in peace, OK?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nYou can’t just barge in here![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nHey! Who’re YOU?!...[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """VALENTINA: You? Fighting the dojo\n master? Good luck, chump![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What? What do you want?![await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What? What do you want?![await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She’s always mumbling about\n Queen-this and Dodo-that.[await][page]\n Sometimes I’d like to ask her what\n she’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """VALENTINA: Is this REALLY going to make me powerful enough to take ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit to Nimbus Land?![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """VALENTINA: Is this REALLY going to make me powerful enough to take ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit to Nimbus Land?![await]""",
    }
    _dialog_replacements_canon_and_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Valentina’s busy right now, so she\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Valentina.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """ Whatever, go on and fight\n Valentina. She doesn’t pay us\n enough to keep you out.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """ Oh, you won?[await]\n [delay_30](...[delay_30]It’s about time!)[await]""",
        DI2560_TOWER_HENCHMAN_1: """ I hate being a secretary! And...\n [delay_30]I’m going to make this your\n problem![await]""",
        DI2572_TOWER_HENCHMAN_2: """Whaddya want?[await][pause] You better not be\n trying to bother Valentina, [delay]or I’ll\n be in trouble![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """Valentina only gives us the most\n boring jobs to do...[await]""",
        DI3073_TOWER_HENCHMAN_3: """[center]\nI’m bored. Entertain me![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA
        ):
            output.extend(
                [
                    SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                    SetBit(MAP_BARREL_VOLCANO),
                ]
            )
        return EventScript(output)


__all__ = ["ValentinaBossFight"]
