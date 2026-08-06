from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (BELOME2Enemy, BOWSERCLONEEnemy, GENOCLONEEnemy, MALLOWCLONEEnemy, MARIOCLONEEnemy, TOADSTOOL2Enemy)
from randomizer.data.packs.pack_collection import (FORM0279_ONE_BELOME2_ONE_MARIOCLONE_ONE_TOADSTOOL2)
from randomizer.data.physical_objects.bosses import (Belome2LargeObject, Belome2SmallObject, BelomeSmallStatueObject)
from randomizer.data.physical_objects.henchmen import (BowsercloneHenchman_2, GenocloneHenchman, MallowcloneHenchman, MariocloneHenchman, PeachcloneHenchman)
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
    DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
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
from randomizer.data.variables.room_names import (R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN)
from randomizer.data.variables.variable_names import (MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN, MAP_MONSTRO_TOWN)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_3)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (RemoveObjectFromSpecificLevel, SetBit)
from randomizer.types.flags import (MonstroTownGate, MonstroTownGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Belome2BossFight(BossFightPrize):
    _text = "Belome 2"
    _formation = FORM0279_ONE_BELOME2_ONE_MARIOCLONE_ONE_TOADSTOOL2
    _members = [
        FormationMember(BELOME2Enemy, 183, 127),
        FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a hungry dog walking"
    _seaside_letter_name_if_final_boss = "Belome's clones."
    _name = "Belome"

    _anchor_enemy = BELOME2Enemy
    _hp_slice_excluded_enemies = [MARIOCLONEEnemy, TOADSTOOL2Enemy]
    _additional_enemies_to_scale = [MALLOWCLONEEnemy, GENOCLONEEnemy, BOWSERCLONEEnemy]
    _character_henchmen = [
        BossFightHenchman(monster=MARIOCLONEEnemy, model=MariocloneHenchman),
        BossFightHenchman(monster=TOADSTOOL2Enemy, model=PeachcloneHenchman),
        BossFightHenchman(monster=GENOCLONEEnemy, model=GenocloneHenchman),
        BossFightHenchman(monster=MALLOWCLONEEnemy, model=MallowcloneHenchman),
    ]

    _mook_henchmen = [
        BossFightHenchman(monster=MARIOCLONEEnemy, model=MariocloneHenchman),
        BossFightHenchman(monster=TOADSTOOL2Enemy, model=PeachcloneHenchman),
        BossFightHenchman(monster=GENOCLONEEnemy, model=GenocloneHenchman),
        BossFightHenchman(monster=MALLOWCLONEEnemy, model=MallowcloneHenchman),
        BossFightHenchman(monster=BOWSERCLONEEnemy, model=BowsercloneHenchman_2),
    ]

    _npc_models = [Belome2LargeObject, Belome2SmallObject]
    _statue_npc = BelomeSmallStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """[center]\nBELOME: Good night~![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Belome’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BELOME!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BELOME: Oh, you’re back![await]\n Did you bring any food?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BELOME: Say, it’s past my bedtime.\n Can you get off of my head?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """MARIO CLONE:\n[center]••••••[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """MALLOW CLONE: Hey `MAIN_CHARACTER_TITLE`, have you seen my parents?[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ (It’s a damp, slimy looking note. Did Belome LICK this?[await][page]\n A paw print and a crudely drawn image of `VOLCANO_BOSS_DESCRIPTION` are etched on the paper.[await]\n This is probably one of `FINAL_BOSS_NAME`[await]\n Belome likely headed down to find more snacks, so it’s time to move on.)[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """GENO CLONE: If you find any Star Pieces, think you could hand them over to me?[await][page] No? [delay]...Oh well, I tried.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """TOADSTOOL 2: Take the trampoline in the next room. Go on, get outta here![await]""",
        DI2061_HEAD_CHEF: """MARIO CLONE:\n[center]••••••[await]""",
        DI2062_APPRENTICE_CHEF: "TOADSTOOL 2: I’ve baked a cake for you.[await][pause] It just happens to look like a dog.[await]",
        DI2180_CHAPEL_NPC: """ Reverend Belome must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BELOME: Oh, no, you’re still\n missing [0x7024] item(s).[await][pause] I can’t wait any\n longer to see what today’s cake\n will be.[await][pause] I’m STARVING![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BELOME: Mmm, you’ve found all of `MARRYMORE_CHARACTER`’s things![await]\n But they won’t bring the cake in here until we AERO_NPclean the place up.[await]\n Go Cgrab the leftover items, please.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Belome’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Belome.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BELOME: It’s dreadfully boring\n around here~![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you the pizza delivery `MAIN_CHARACTER_GENDER_CASUAL`?[await]\n  [select] (I’m here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Are you the pizza delivery `MAIN_CHARACTER_GENDER_CASUAL`?[await]\n  [select] (I’m here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """MARIO CLONE:\n[center]••••••[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """TOADSTOOL 2: Yuck, I don’t want to play ANYTHING with you![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """GENO CLONE: Need a nap? You can stay here for free.[await][pause] No dolls will wander around overnight, I swear.[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI1945_NIMBUS_GUARD: """MARIO CLONE:\n[center]••••••[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """TOADSTOOL 2: There’s nothing illegal going on here.[await][pause] But it should be a crime to be so beautiful.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """[center]\n••••••[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """[center]\n••••••[await]""",
        DI2560_TOWER_HENCHMAN_1: """MARIO CLONE:\n[center]••••••[await]""",
        DI2572_TOWER_HENCHMAN_2: """TOADSTOOL 2: If you aren’t here to tell us about a good cake recipe, then shoo![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """GENO CLONE: (What do Star Pieces even look like...?)[await]""",
        DI3073_TOWER_HENCHMAN_3: """GENO CLONE: I serve...a higher authority...[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            MonstroTownGate, MonstroTownGating.BELOME_2
        ):
            output.extend(
                [
                    RemoveObjectFromSpecificLevel(
                        NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
                    ),
                    SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
                    SetBit(MAP_MONSTRO_TOWN),
                ]
            )
        return EventScript(output)


__all__ = ["Belome2BossFight"]
