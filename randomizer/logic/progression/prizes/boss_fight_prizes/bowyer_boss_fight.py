from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (AEROEnemy, BOWYEREnemy)
from randomizer.data.packs.pack_collection import (FORM0291_ONE_BOWYER)
from randomizer.data.physical_objects.bosses import (BowyerLargeObject, BowyerOverworldObject, BowyerSmallObject, BowyerStatueObject)
from randomizer.data.physical_objects.henchmen import (AeroHenchman)
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
from randomizer.data.variables.variable_names import (MOLEVILLE_MINES_ENTRANCE_GATING, PIPE_VAULT_GATED)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (ClearBit)
from randomizer.types.flags import (Moleville1Gate, Moleville1Gating, PipeVaultGate, PipeVaultGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BowyerBossFight(BossFightPrize):
    _text = "Bowyer"
    _formation = FORM0291_ONE_BOWYER
    _members = [
        FormationMember(BOWYEREnemy, 183, 127),
    ]
    _force_start_event = BE0038_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT
    _additional_enemies_to_scale = [AEROEnemy]

    _seaside_letter_name_if_volcano_boss = "a longbow loosing arrows at"
    _seaside_letter_name_if_final_boss = "Bowyer's lackeys."

    _npc_models = [BowyerLargeObject, BowyerOverworldObject, BowyerSmallObject]
    _statue_npc = BowyerStatueObject

    _mook_henchmen = [BossFightHenchman(monster=AEROEnemy, model=AeroHenchman)]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOWYER: Disturb me you must not,\n nya!""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Nya, NYA?![delay_30] Cracked the code, you\n did! But fight you, I will, nya![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Bowyer’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BOWYER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOWYER: That was nyat fair!\n Scram you must, nya![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOWYER: Back again, you are,\n nya? I’m nyat as mad as before.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOWYER: Nya, NYA?! Stop this,\n you must![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Nya, Nya, NYA!  Make like Locke![await]\n Bring me more Strongbow Cider![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Nya, Nya, NYA!  Make like Locke![await]\n Bring me more Strongbow Cider![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we’re off the hook today.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Knock, knock, NYA!![await][page]\n Your battle is long and boring, even for `SEASIDE_BOSS`, nya![await]\n Aero #837 painted a target on `VOLCANO_BOSS_DESCRIPTION` near the volcano, nya!![await]\n 10,000 arrows will I fire at `FINAL_BOSS_NAME`[await]\n Follow me to the ship you will NOT![await][page]\n\n                                  NYA!!!![await]\n                                    Bowyer[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """FLUNKIE: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we’re off the hook today.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we’re off the hook today.[await]""",
        DI2061_HEAD_CHEF: """FLUNKIE: Doesn’t this cake\n look just like Bowyer?[await]""",
        DI2062_APPRENTICE_CHEF: """FLUNKIE: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bowyer must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOWYER: Nya, NYA!?[await][pause] Disturb me\n you must not, until [0x7024] more item(s)\n you find, nya![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BOWYER: Nya, NYA!?[await]\n Found all of `MARRYMORE_CHARACTER`’s belongings, you did![await]\n But clear out this room, you did NOT, nya!!![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Bowyer’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Bowyer.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\nBOWYER: Nya! Boring here, it is...[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Since I’m having a good day, you\n can stay here free of charge.\n [delay]How’s that sound?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Bowyer’s house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Don’t cause any trouble in our\n town! Stay away from the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I’m just a customer![delay] Let me shop\n in peace![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There’s a very uh... [delay]important\n meeting happening inside.\n [delay]You may not enter.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ What’s going on in here?[await][pause] None of\n your business, that’s what![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n BOWYER: Interesting, this will be![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Fight me, you will, nya?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Fight me, you will, nya?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Arrow-this and Target-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOWYER: 1000 jumps I must do,\n nya![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOWYER: 1000 jumps I must do,\n nya![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """FLUNKIE: Whoa! You sure showed\n us! Go on ahead to Bowyer’s\n place![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """FLUNKIE: Come back and visit\n us sometime. Bowyer won’t stay\n mad forever![await]""",
        DI2560_TOWER_HENCHMAN_1: """FLUNKIE: Hello.[await][pause] Bowyer is busy\n now, and he really hates to be\n interrupted.[await][page]\n[delay] ...If you’re not going to leave,\n I’ll have to kick you out myself![await]""",
        DI2572_TOWER_HENCHMAN_2: """FLUNKIE: I’m gonna have to ask you\n not to interrupt Bowyer’s target\n practice.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """FLUNKIE: ...sigh... [delay]Bowyer scolded me for interrupting his shooting practice.[await][pause] I was just trying to warn him that `MAIN_CHARACTER_NAME` is here![await]""",
        DI3073_TOWER_HENCHMAN_3: """FLUNKIE: You look like you’d make\n a good statue![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Bowyer’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Bowyer.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            PipeVaultGate, PipeVaultGating.BOWYER
        ):
            output.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        if world.settings.is_flag_value(
            Moleville1Gate, Moleville1Gating.BOWYER
        ):
            output.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        return EventScript(output)


__all__ = ["BowyerBossFight"]
