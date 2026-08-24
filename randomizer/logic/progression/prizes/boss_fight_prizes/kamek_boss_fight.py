from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (BAHAMUTTEnemy, BOBOMBEnemyHenchman, JINXCLONEEnemy, KAMEKEnemy, KINGBOMBEnemy, TERRAPINEnemy)
from randomizer.data.packs.pack_collection import (FORM0316_ONE_KAMEK_ONE_TERRAPIN)
from randomizer.data.physical_objects.bosses import (MagikoopaLargeObject, MagikoopaSmallObject, MagikoopaStatueObject)
from randomizer.data.physical_objects.henchmen import (JinxCloneHenchman, MicrobombHenchman)
from randomizer.data.rooms.npcs import (MAGIKOOPA_NPC_2)
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
from randomizer.data.variables.room_names import (R432_ENDING_CREDITS_JOHNNY_LOOKING_OUT_AT_SUNSET_ON_BEACH_SHORE, R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, R505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI, R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_10, NPC_6, NPC_9)

if TYPE_CHECKING:
    from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC)
    from randomizer.types.physical_objects import (BossNPC)
    from smrpgpatchbuilder.datatypes.levels.classes import (NPC as NPCBase)


class KamekBossFight(BossFightPrize):
    _text = "Magikoopa"
    _formation = FORM0316_ONE_KAMEK_ONE_TERRAPIN
    _members = [
        FormationMember(KAMEKEnemy, 215, 111),
        FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
    ]
    _anchor_enemy = KAMEKEnemy
    _scaling_excluded_enemies = [TERRAPINEnemy]
    _hp_slice_excluded_enemies = [TERRAPINEnemy]
    _additional_enemies_to_scale = [JINXCLONEEnemy, KINGBOMBEnemy, BAHAMUTTEnemy]

    _seaside_letter_name_if_volcano_boss = "a hooded sorceror flying"
    _seaside_letter_name_if_final_boss = "Magikoopa's guys."
    _seaside_letter_name_if_final_boss_remake = "Wizakoopa's guys."
    _remake_name = "Wizakoopa"

    # _mook_henchmen = [
    #     BossFightHenchman(monster=JINXCLONEEnemy, model=JinxCloneHenchman),
    #     BossFightHenchman(monster=KINGBOMBEnemy, model=BobOmbHenchman),
    # ]
    _tiny_henchmen = [
        BossFightHenchman(monster=JINXCLONEEnemy, model=JinxCloneHenchman),
        BossFightHenchman(monster=BOBOMBEnemyHenchman, model=MicrobombHenchman),
    ]

    _npc_models = [MagikoopaLargeObject, MagikoopaSmallObject]
    _statue_npc = MagikoopaStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MAGIKOOPA: Normally,[delay] when I\n summon an egg,[delay] it doesn’t\n encapsulate me...[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ This..is..my ship!\n Come in..if you dare![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Magikoopa’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n MAGIKOOPA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n  MAGIKOOPA: Huh? ...Where am I?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MAGIKOOPA: Oh, yes, I have seen\n `MARIO_NAME`’s brother before.\n I can’t recall where, though...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MAGIKOOPA: `MAIN_CHARACTER_NAME`,\n why did you do this???[await]""",
        DI1782_SHIP_BOSS_DRINK: """ There’s Magic Hat in my magic hat,[await]\n but we’re not handing it over to[await]\n the likes of you![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ There’s Magic Hat in my magic hat,[await]\n but we’re not handing it over to[await]\n the likes of you![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`![await][page]\n Before I could cast a spell, you defeated `SEASIDE_BOSS`![await]\n Earlier while flying around seeking vengeance, I saw `VOLCANO_BOSS_DESCRIPTION` by the volcano.[await]\n I remember them being one of `FINAL_BOSS_NAME`.[await]\n I’d better get back to the ship in case Yoshi falls into one of the pits.[await][page]\n\n     Now you see me, now you don’t![await]\n                              Magikoopa""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big wizard! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Magikoopa must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MAGIKOOPA: You..need..[0x7024] more\n item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """MAGIKOOPA: You’re still missing...\n some things...in this room![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Magikoopa’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Magikoopa.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """MAGIKOOPA:\n[center]There’s nothing..to see..here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Magikoopa...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """[center]\nMAGIKOOPA: OH, MY!![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ MAGIKOOPA: Yes?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ MAGIKOOPA: Yes?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Yoshi-this and Bowser-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MAGIKOOPA:\n[center]Oh, dear... What to do...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MAGIKOOPA:\n[center]Oh, dear... What to do...[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """WIZAKOOPA: Normally,[delay] when I\n summon an egg,[delay] it doesn’t\n encapsulate me...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Wizakoopa’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n WIZAKOOPA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n  WIZAKOOPA: Huh? ...Where am I?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """WIZAKOOPA: Oh, yes, I have seen\n `MARIO_NAME`’s brother before.\n I can’t recall where, though...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """WIZAKOOPA: `MAIN_CHARACTER_NAME`,\n why did you do this???[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`![await][page]\n Before I could cast a spell, you defeated `SEASIDE_BOSS`![await]\n Earlier while flying around seeking vengeance, I saw `VOLCANO_BOSS_DESCRIPTION` by the volcano.[await]\n I remember them being one of `FINAL_BOSS_NAME`.[await]\n I’d better get back to the ship in case Yoshi falls into one of the pits.[await][page]\n\n     Now you see me, now you don’t![await]\n                              Wizakoopa""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """WIZAKOOPA: You..need..[0x7024] more\n item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """WIZAKOOPA: You’re still missing...\n some things...in this room![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Wizakoopa’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Wizakoopa.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """WIZAKOOPA:\n[center]There’s nothing..to see..here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Wizakoopa...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """[center]\nWIZAKOOPA: OH, MY!![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ WIZAKOOPA: Yes?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ WIZAKOOPA: Yes?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """WIZAKOOPA:\n[center]Oh, dear... What to do...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """WIZAKOOPA:\n[center]Oh, dear... What to do...[await]""",
    }
    _dialog_replacements_canon = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """KAMEK: Normally,[delay] when I\n summon an egg,[delay] it doesn’t\n encapsulate me...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Kamek’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n KAMEK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nKAMEK: Huh? ...Where am I?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """KAMEK: Oh, yes, I have seen\n `MARIO_NAME`’s brother before.\n I can’t recall where, though...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """KAMEK: `MAIN_CHARACTER_NAME`,\n why did you do this???[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`![await][page]\n Before I could cast a spell, you defeated `SEASIDE_BOSS`![await]\n Earlier while flying around seeking vengeance, I saw `VOLCANO_BOSS_DESCRIPTION` by the volcano.[await]\n I remember them being one of `FINAL_BOSS_NAME`.[await]\n I’d better get back to the ship in case Yoshi falls into one of the pits.[await][page]\n\n     Now you see me, now you don’t![await]\n                                    Kamek""",
        DI2180_CHAPEL_NPC: """ Reverend Kamek must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """KAMEK: You..need..[0x7024] more\n item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """KAMEK: You’re still missing...\n some things...in this room![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Kamek’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Kamek.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """KAMEK:\n[center]There’s nothing..to see..here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Kamek... in his house.\n He is...the most respected person\n here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """[center]\nKAMEK: OH, MY!![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ KAMEK: Yes?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ KAMEK: Yes?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """[center]\nKAMEK: Oh, dear... What to do...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """[center]\nKAMEK: Oh, dear... What to do...[await]""",
    }
    _dialog_replacements_canon_and_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Kamek’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Kamek.[await]""",
    }

    def get_forced_npc_model_for_location(
        self, location: "BossFightLocation"
    ) -> type[BossNPC] | None:
        from randomizer.logic.progression.prizelocations import (InnerMinesBossFight)

        if isinstance(location, InnerMinesBossFight):
            return MagikoopaSmallObject
        return None

    def get_slot_base_override(
        self,
        location: "BossFightLocation",
        slot: "BossFightLocationNPC",
        chosen_model: type["BossNPC"],
    ) -> "NPCBase | None":
        """Return an override NPC base to apply to a specific slot, or None.

        Kamek reuses the shared MagikoopaSmallObject/MagikoopaLargeObject models,
        but a handful of ending-credits and vanilla slots need dedicated NPC
        bases (MAGIKOOPA_NPC_2 / MAGIKOOPA_NPC_3) with their own sprite
        configurations. Overriding obj._npc at the slot level keeps the shared
        model classes unmutated so other rooms that rely on the original bases
        keep working.
        """
        from randomizer.logic.progression.prizelocations import (BanditsWayBossFight, BoosterTowerIndoorBossFight, KeepAfterObstaclesBossFight, NimbusFinalBossFight, ShipFinalBossFight)

        small_slot_overrides: list[tuple[type, int, int]] = [
            (
                BanditsWayBossFight,
                R505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI,
                NPC_10,
            ),
            (
                BoosterTowerIndoorBossFight,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                NPC_10,
            ),
            (
                NimbusFinalBossFight,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                NPC_9,
            ),
            (
                ShipFinalBossFight,
                R432_ENDING_CREDITS_JOHNNY_LOOKING_OUT_AT_SUNSET_ON_BEACH_SHORE,
                NPC_0,
            ),
            (
                KeepAfterObstaclesBossFight,
                R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR,
                NPC_6,
            ),
        ]
        for loc_cls, room_id, npc_id in small_slot_overrides:
            if (
                isinstance(location, loc_cls)
                and slot.room_id == room_id
                and slot.npc_id == npc_id
            ):
                return MAGIKOOPA_NPC_2

        #if isinstance(location, StatueRoomBossFight) and chosen_model is MagikoopaLargeObject:
        #    return MAGIKOOPA_NPC_3

        return None


__all__ = ["KamekBossFight"]
