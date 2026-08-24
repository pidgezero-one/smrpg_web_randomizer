from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (EXOREnemy, LEFTEYEEnemy, NEOSQUIDEnemy, RIGHTEYEEnemy)
from randomizer.data.packs.pack_collection import (FORM0296_ONE_EXOR_ONE_NEOSQUID_ONE_RIGHTEYE_ONE_LEFTEYE)
from randomizer.data.physical_objects.bosses import (ExorSmallObject, ExorStatueObject)
from randomizer.data.variables.battle_event_names import (BE0080_EXOR_FIGHT_BEGINS)
from randomizer.data.variables.battlefield_names import (BF16_BOWSERS_KEEP_TURRET_EXOR)
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
from randomizer.data.variables.variable_names import (MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, MAP_GATE)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (SetBit)
from randomizer.types.flags import (FactoryGate, FactoryGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)


class ExorBossFight(BossFightPrize):
    _text = "Exor"
    _formation = FORM0296_ONE_EXOR_ONE_NEOSQUID_ONE_RIGHTEYE_ONE_LEFTEYE
    _members = [
        FormationMember(EXOREnemy, 193, 64),
        FormationMember(NEOSQUIDEnemy, 187, 136),
        FormationMember(RIGHTEYEEnemy, 174, 145, hidden_at_start=True),
        FormationMember(LEFTEYEEnemy, 203, 157, hidden_at_start=True),
    ]
    _force_start_event = BE0080_EXOR_FIGHT_BEGINS
    _force_battlefield = BF16_BOWSERS_KEEP_TURRET_EXOR
    _seaside_letter_name_if_volcano_boss = "a massive sword falling"
    _seaside_letter_name_if_final_boss = "Exor's sellswords."
    _hp_slice_excluded_enemies = [
        RIGHTEYEEnemy,
        NEOSQUIDEnemy,
    ]  # exor and left eye are minimum required to defeat so only they count
    _anchor_enemy = [RIGHTEYEEnemy, LEFTEYEEnemy, NEOSQUIDEnemy]

    _npc_models = [ExorSmallObject]
    _statue_npc = ExorStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """EXOR: What do you want? Get\n lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Halt! This ship belongs to ME!\n If you want to get through...\n bring it on![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Exor’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped EXOR!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """EXOR: If it weren’t for nosey\n characters like you, I could live in\n this ship undisturbed![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """EXOR: Halt! Don’t even THINK\n about leaving until you’ve had\n some of this juice![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """EXOR: Look, if you really want to humiliate me, why not use Geno Whirl too, while you’re at it?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ You think I was MADE this HUGE?![await]\n No, I drank my Milk EVERY DAY!!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ You think I was MADE this HUGE?![await]\n No, I drank my Milk EVERY DAY!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n HEY![await][page]\n What did you do to `SEASIDE_BOSS`?![await]\n Let’s see you deal with `VOLCANO_BOSS_DESCRIPTION` at the volcano![await]\n You are no match for us, `FINAL_BOSS_NAME`[await]\n Trespass on my ship at your own peril![await]\n I will devour you and expel your corporeal form in the dimension of bombs and sledges![await]\n Mind your place, Tiny.[await][page]\n\n                                      Exor[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big sword! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Exor must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """EXOR: Halt![await][pause] What do you have\n here?[delay] [0x7000] item(s)?[await]\n No, this won’t do.[await][pause] Find [0x7024] more,\n[delay] or I won’t let you through![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """EXOR: Halt! You found the gear,\n but there are still items in this\n room![await]\n Pick them up NOW![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Exor’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Exor.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """EXOR: There isn’t much to see in\n this town. Especially not in\n the shed.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Exor...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """EXOR: Think you’re gonna beat the\n dojo master? Now this I GOTTA\n see![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Halt! What do you want?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Halt! What do you want?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Nosey-this and Trespasser-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """[center]\nEXOR: How humiliating![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """[center]\nEXOR: How humiliating![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Exor’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Exor.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(FactoryGate, FactoryGating.EXOR):
            output.extend(
                [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
            )

        return EventScript(output)


__all__ = ["ExorBossFight"]
