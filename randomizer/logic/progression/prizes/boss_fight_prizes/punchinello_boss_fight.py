from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (BOBOMBEnemyHenchman, MEZZOBOMBEnemy, MICROBOMBEnemy, PUNCHINELLOEnemy)
from randomizer.data.packs.pack_collection import (FORM0251_ONE_PUNCHINELLO_FOUR_MICROBOMB)
from randomizer.data.physical_objects.bosses import (PunchinelloLargeObject, PunchinelloSmallObject, PunchinelloStatueObject)
from randomizer.data.physical_objects.henchmen import (BobOmbHenchman, MicrobombHenchman)
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
from randomizer.data.variables.room_names import (R202_BOOSTER_TOWER_ENTRANCE)
from randomizer.data.variables.variable_names import (TOWER_OPENED)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (ApplySolidityModToLevel, ApplyTileModToLevel, SetBit)
from randomizer.types.flags import (BoosterTowerGate, BoosterTowerGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class PunchinelloBossFight(BossFightPrize):
    _text = "Punchinello 1"
    _formation = FORM0251_ONE_PUNCHINELLO_FOUR_MICROBOMB
    _members = [
        FormationMember(PUNCHINELLOEnemy, 199, 119),
        FormationMember(MICROBOMBEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 151, 135, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 183, 151, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 215, 159, hidden_at_start=True),
    ]
    _anchor_enemy = PUNCHINELLOEnemy
    _hp_slice_excluded_enemies = [MICROBOMBEnemy]
    _additional_enemies_to_scale = [BOBOMBEnemyHenchman, MEZZOBOMBEnemy]

    _name = "Punchinello"
    _seaside_letter_name_if_seaside_boss = "Hothead"
    _seaside_letter_name_if_volcano_boss = "a demolitionist stomping"
    _seaside_letter_name_if_final_boss = "Punchinello's demo team."

    _npc_models = [PunchinelloLargeObject, PunchinelloSmallObject]
    _statue_npc = PunchinelloStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=BOBOMBEnemyHenchman, model=BobOmbHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=BOBOMBEnemyHenchman, model=MicrobombHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PUNCHINELLO: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So... You figured out my\n password.[await]\n If you’re not here for an\n autograph, I’ll have to test you\n once more to let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Punchinello’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n PUNCHINELLO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PUNCHINELLO: Grrr... I’ll never get famous at this rate![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PUNCHINELLO: You’ve come back to\n visit? I truly must be famous![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PUNCHINELLO: They say I’m a hot\n head, so it’s a bad idea to stand\n on my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ WATCH ME DRINK THIS TOBASCO![await]\n I’m gonna be youtube-famous![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ WATCH ME DRINK THIS TOBASCO![await]\n I’m gonna be youtube-famous![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """[center]\nBOB-OMB: I need a break.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n WHAT’S UP CHAT?![await][page]\n I just watched a HYPE fight versus `SEASIDE_BOSS`.  Oh.  Em.  Gee.[await]\n My Bob-omb army told me about `VOLCANO_BOSS_DESCRIPTION` near the volcano. Fuse is LIT!![await]\n I smell a collab video with `FINAL_BOSS_NAME`[await]\n Don’t forget to tune in for my 100 follower special, where I’ll play Bob-omb roulette with watermelons![await][page]\n\n           Like, Share, and Subscribe!\n                              Punchinello[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """BOB-OMB: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """[center]\nBOB-OMB: I need a break.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """[center]\nBOB-OMB: I need a break.[await]""",
        DI2061_HEAD_CHEF: """BOB-OMB: Doesn’t this cake\n look just like Punchinello?[await]""",
        DI2062_APPRENTICE_CHEF: """BOB-OMB: We’ve gotten quite\n good with fondant.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Punchinello must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PUNCHINELLO: Huh?[delay_30] What the hay?[await]\n Where are the other [0x7024] item(s)?[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """PUNCHINELLO: Huh?[delay_30] You’ve got all the stuff we need\n for the ceremony?[await]\n Great.[delay] But aren’t there a few more\n things to grab in this room?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Punchinello’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Punchinello.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PUNCHINELLO: Hmmm... [delay]Huh?\n [delay]A visitor? [delay]Well, there’s not much\n to do around here.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello there.[await][pause] Today, we’ve got an\n explosively good deal for you![delay] All\n inn expenses are free of charge.[await]\n Would you like to stay?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Punchinello’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hello there.[delay] Welcome to our humble\n town. We have the least suspicious\n shed in all the land.[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I know how this must look, but I’m\n just here to browse the perfectly\n legal goods they’re selling.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hello there.[delay] Sorry, but I can’t let\n you through this door today.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ You wouldn’t wanna enter this\n house, oh no.[delay] We’ll make sure you\n don’t enter by accident.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PUNCHINELLO: A challenge from\n the dojo master, eh? Let’s see\n where this goes.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I’m here to fight you)\n  [select] (Sorry, wrong number)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I’m here to fight you)\n  [select] (Sorry, wrong number)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Bomb-this and Famous-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Punchinello’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Punchinello.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BOB-OMB: I guess I was a little\n hot-headed, thinking I could win.\n Go on in to Punchinello’s room.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BOB-OMB: Wow, you beat\n Punchinello! He’s not very happy\n about that.[await]""",
        DI2560_TOWER_HENCHMAN_1: """BOB-OMB: Hello there.[await][pause] If you’ve\n come for Punchinello’s autograph,\n please allow me to buzz you up...[await][page]\n [delay]...You’re not here for that?[await]\n [delay]Uh oh, he’ll be pretty mad!\n [delay]I’d better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """BOB-OMB: There’s nothing to see\n back here...[await][pause] I mean that.[await]\n You don’t believe me?[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """BOB-OMB: I don’t look like the\n other bob-ombs here. [delay]That’s weird.[await]""",
        DI3073_TOWER_HENCHMAN_3: """BOB-OMB: You don’t think it makes\n sense for a bob-omb to be shooting\n bullets?[await][pause] ...Fight me about it![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            BoosterTowerGate, BoosterTowerGating.PUNCHINELLO
        ):
            output.extend(
                [
                    ApplySolidityModToLevel(
                        permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
                    ),
                    ApplyTileModToLevel(
                        use_alternate=True,
                        room_id=R202_BOOSTER_TOWER_ENTRANCE,
                        mod_id=32,
                    ),
                    SetBit(TOWER_OPENED),
                ]
            )
        return EventScript(output)


__all__ = ["PunchinelloBossFight"]
