from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (BUNDTEnemy, RASPBERRYEnemy, TORTEEnemy)
from randomizer.data.packs.pack_collection import (FORM0286_ONE_BUNDT_ONE_RASPBERRY_TWO_TORTE)
from randomizer.data.physical_objects.bosses import (BundtLargeObject, BundtSmallObject, BundtStatueObject)
from randomizer.data.physical_objects.henchmen import (TorteHenchman)
from randomizer.data.variables.battle_event_names import (BE0038_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT)
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
    DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
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
from randomizer.data.variables.variable_names import (MAP_DIRECTIONAL_SEASIDE_DOWN_SEA, MAP_SEA)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (SetBit)
from randomizer.types.flags import (SeaGate, SeaGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)


class BundtBossFight(BossFightPrize):
    _text = "Bundt 1"
    _formation = FORM0286_ONE_BUNDT_ONE_RASPBERRY_TWO_TORTE
    _members = [
        FormationMember(BUNDTEnemy, 199, 127),
        FormationMember(RASPBERRYEnemy, 199, 119),
        FormationMember(TORTEEnemy, 199, 151),
        FormationMember(TORTEEnemy, 135, 119),
    ]
    _anchor_enemy = [BUNDTEnemy, RASPBERRYEnemy]
    _hp_slice_excluded_enemies = [TORTEEnemy, TORTEEnemy]
    _seaside_letter_name_if_seaside_boss = "the Cake"
    _seaside_letter_name_if_volcano_boss = "a possessed cake walking"
    _seaside_letter_name_if_final_boss = "Bundt's dinner guests."
    _name = "Bundt"
    _force_start_event = BE0038_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT

    _npc_models = [BundtLargeObject, BundtSmallObject]
    _statue_npc = BundtStatueObject

    _gender = ("it", "it", "its", "its", "itself")

    _mook_henchmen = [
        BossFightHenchman(monster=TORTEEnemy, model=TorteHenchman),
    ]
    _character_henchmen = [
        BossFightHenchman(monster=TORTEEnemy, model=TorteHenchman),
        BossFightHenchman(monster=TORTEEnemy, model=TorteHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n[center]BUNDT: La la la la la la la la la~[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ What a surprise! [delay_30]Welcome![await]\n Let me warm up for the feast![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Bundt’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BUNDT!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BUNDT: Oh...! My beautiful body![await][pause]\n Please go away while I recover![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BUNDT: Come back to celebrate a\n wedding? At least try and eat me\n this time...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """[center]\nBUNDT: OH! MY CANDLES![await]""",
        DI1782_SHIP_BOSS_DRINK: """ I’ve got my own frosting, thanks.[await]\n “Happy” Frogs taste best, though![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ I’ve got my own frosting, thanks.[await]\n “Happy” Frogs taste best, though![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings and Salutations![await][page]\n I can’t get over how quickly you dispatched `SEASIDE_BOSS`![await]\n My dinner guests informed me of `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I heard they’re having a reunion with `FINAL_BOSS_NAME`[await]\n I’ve gotten hungry aboard this ship. You wouldn’t believe how much you can miss your chefs and creams. [await]\n Come visit and have a slice![await][page]\n\n       Frosting my way to victory,\n                                     Bundt[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: This masterpiece is\n our latest creation... wait...[await]""",
        DI2062_APPRENTICE_CHEF: """APPRENTICE: Chef Torte! [delay]Why\n did we make another Bundt?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bundt must have gotten\n lost on its way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BUNDT: Hmm?[delay] You look like you\n could use a break![await][pause] Come back with\n the other [0x7024] item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BUNDT: You found all the wedding\n gear, but you’re missing a few\n things in this room.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Bundt is busy right now, so it\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Bundt.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BUNDT: Greetings and salutations!\n Welcome to our quiet little town![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Bundt...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BUNDT: What a fierce battle![await][pause] That\n was nothing compared to the dojo\n master, you know.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What’s this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What’s this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Candle-this and Frosting-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
        DI1120_NIMBUS_BIRD_GUARD: """CHEF TORTE: Is dinner time.[await]\n Ze guests are enjoyeeng zeir\n dinner, so ve cannot let you in.[await]""",
        DI1945_NIMBUS_GUARD: """APPRENTICE: Oh, yeah, I’m sure\n they’re loving the food. Nice of\n them to invite us in for some...[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Bundt is busy right now, so it\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Bundt.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """APPRENTICE: Fine, go on ahead.\n I’ll warn you, though, some idiot\n stepped on the cake, so be careful.await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """APPRENTICE: Wow, you ate the\n whole thing? [delay_30]...[delay_30]How was it?[await]""",
        DI2560_TOWER_HENCHMAN_1: """CHEF TORTE: ’Allo. Ze dessert ees\n not ready yet. Please come back\n later, yes?[await][page]\n [delay]...[delay]Escuse me, sir, I said to please\n come back... LATER![await][page]\n[delay]\n   (He von’t leave... [delay]Vat to do?)[await][page]\n\n                YOU FOOLS!![await]""",
        DI2572_TOWER_HENCHMAN_2: """APPRENTICE: Hey, genius, this way\n is the kitchen. Stay out![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """APPRENTICE: Why did Chef Torte\n tell me to stay up here? This is\n nowhere near the kitchen...[await]""",
        DI3073_TOWER_HENCHMAN_3: """APPRENTICE: I’m so bored! The\n other chefs won’t let me into the\n kitchen![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(SeaGate, SeaGating.BUNDT):
            output.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        return EventScript(output)


__all__ = ["BundtBossFight"]
