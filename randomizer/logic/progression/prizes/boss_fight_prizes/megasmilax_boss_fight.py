from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (MEGASMILAXEnemy, PIRANHAPLANTEnemyHenchman, SMILAXEnemy)
from randomizer.data.overworld_scripts.event.scripts.script_3645 import (NPC_2)
from randomizer.data.packs.pack_collection import (FORM0283_FIVE_SMILAX_ONE_MEGASMILAX)
from randomizer.data.physical_objects.bosses import (MegasmilaxLargeObject, PiranhaPlantObject, PiranhaPlantStatueObject)
from randomizer.data.physical_objects.henchmen import (PiranhaPlantHenchman)
from randomizer.data.variables.battle_event_names import (BE0058_THRAX_IS_THERE)
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
from randomizer.data.variables.room_names import (R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE)
from randomizer.data.variables.variable_names import (NIMBUS_MAINLAND_UNLOCKED)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (RemoveObjectFromSpecificLevel, SetBit)
from randomizer.types.flags import (NimbusGate, NimbusGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)


class MegasmilaxBossFight(BossFightPrize):
    _text = "Megasmilax"
    _formation = FORM0283_FIVE_SMILAX_ONE_MEGASMILAX
    _members = [
        FormationMember(SMILAXEnemy, 180, 157),
        FormationMember(SMILAXEnemy, 164, 175, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 143, 119, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 207, 151, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 191, 127, hidden_at_start=True),
        FormationMember(MEGASMILAXEnemy, 175, 111, hidden_at_start=True),
    ]
    _force_start_event = BE0058_THRAX_IS_THERE
    _seaside_letter_name_if_seaside_boss = "the Plant"
    _seaside_letter_name_if_volcano_boss = "an invasive plant spreading"
    _seaside_letter_name_if_final_boss = "Megasmilax's seedlings."
    _anchor_enemy = MEGASMILAXEnemy
    _extra_hp_enemies = [SMILAXEnemy, SMILAXEnemy, SMILAXEnemy]
    _additional_enemies_to_scale = [PIRANHAPLANTEnemyHenchman]

    _npc_models = [MegasmilaxLargeObject, PiranhaPlantObject]
    _statue_npc = PiranhaPlantStatueObject

    _gender = ("she", "her", "her", "hers", "herself")

    _mook_henchmen = [
        BossFightHenchman(
            monster=PIRANHAPLANTEnemyHenchman, model=PiranhaPlantHenchman
        ),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MEGASMILAX: I’m thirsty.[await][pause] Can you\n ask Shy Away to come back here,[delay]\n please?[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Hm?[delay_30] Not often we get visitors\n down here.[delay_30] Come in...[delay_60]\n at your own risk, that is![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Megasmilax’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n MEGASMILAX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nMEGASMILAX: I’m thirsty.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MEGASMILAX: You’d think it\n wouldn’t be so difficult to get\n watered around here.[await][pause] We’re\n literally underwater.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MEGASMILAX: Careful. I have sharp\n teeth.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Go ahead, just add Water![await]\n Cha-Cha-Cha-Chia!  La Dee Dah~![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Go ahead, just add Water![await]\n Cha-Cha-Cha-Chia!  La Dee Dah~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """SMILAX: I guess salt water\n wouldn’t be very good for us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,[await][page]\n I’m still salivating over your battle with `SEASIDE_BOSS`.[await]\n I must taste its umami someday...[await]\n I’ve heard through the vine about `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They must be part of the underground network of `FINAL_BOSS_NAME`[await]\n My offer to have you for dinner stands. I must return to my roots.[await][page]\n\n                             Stay hungry,\n                              Megasmilax[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """SMILAX: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """SMILAX: I guess salt water\n wouldn’t be very good for us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """SMILAX: I guess salt water\n wouldn’t be very good for us.[await]""",
        DI2061_HEAD_CHEF: """SMILAX: We’re making this cake\n in honour of Megasmilax.[await]""",
        DI2062_APPRENTICE_CHEF: """SMILAX: I hope the wedding party\n likes it. If they don’t...[delay] well,[delay]\n why hire PLANTS to bake a cake?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Megasmilax must have\n gotten lost on her way here.""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Megasmilax is busy right now, so\n she can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Megasmilax.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MEGASMILAX: Hm?[await]\n [0x7024] more item(s)?[await]\n Don’t ask me.[delay] I’m just a plant.[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """MEGASMILAX: There are a few more\n items planted in this room. You\n should find them.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nMEGASMILAX: Hmm...[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello there. Are you tired?\n We don’t charge any fees here,\n if you’d like to stay.[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Megasmilax’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Welcome to our humble little town.\n You’re welcome to stick around,\n but keep away from the shed, OK?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I’m shopping for some fertilizer.[await]\n [delay]...Don’t give me that look!\n [delay]I’m just a plant![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There’s nothing suspicious going on\n in here.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ We’re just two plants growing in\n front of an abandoned door. ...But\n we’re not letting you in.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MEGASMILAX: I would love to\n watch your match with the dojo\n master.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You don’t look like the gardener...[await]\n  [select] (I’m here to fight you)\n  [select] (Oops, my mistake)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You don’t look like the gardener...[await]\n  [select] (I’m here to fight you)\n  [select] (Oops, my mistake)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the lady next door.[await][page]\n She’s always mumbling about\n Water-this and Fertilizer-that.[await]\n ...[delay]Actually, [delay]that doesn’t sound\n so bad![await][page]\n Sometimes I’d like to ask her what\n she’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MEGASMILAX: This is harder than it\n looks. I’m a plant.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MEGASMILAX: This is harder than it\n looks. I’m a plant.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Megasmilax is busy right now, so\n she can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Megasmilax.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """SMILAX: Go on ahead to visit\n Megasmilax. But be warned, she’s\n pretty tough when she’s hydrated.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """SMILAX: Wow, you won![await][pause] Shy Away\n must have watered you more than\n he watered Megasmilax.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SMILAX: Hello there. Are you the\n gardener?[await][page]\n No?[await][pause] Well, [delay]we didn’t call for a\n plumber today... [await][pause]]I better get you\n outta here![await]""",
        DI2572_TOWER_HENCHMAN_2: """SMILAX: If you didn’t come back\n here to water us, you’d better get\n outta here.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """[center]\nSMILAX: I’m thirsty.[await]""",
        DI3073_TOWER_HENCHMAN_3: """[center]\nSMILAX: Careful, I bite.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            NimbusGate, NimbusGating.MEGASMILAX
        ):
            output.extend(
                [
                    SetBit(NIMBUS_MAINLAND_UNLOCKED),
                    RemoveObjectFromSpecificLevel(
                        NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                    ),
                ]
            )
        return EventScript(output)


__all__ = ["MegasmilaxBossFight"]
