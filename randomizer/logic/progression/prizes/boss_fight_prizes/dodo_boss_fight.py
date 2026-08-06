from __future__ import annotations
from randomizer.data.enemies.enemies import (DODOEnemy, DODOEnemySolo)
from randomizer.data.packs.pack_collection import (FORM0315_ONE_DODOENEMYSOLO)
from randomizer.data.physical_objects.bosses import (DodoLargeObject, DodoSmallObject, DodoStatueObject)
from randomizer.data.physical_objects.henchmen import (FeatherHenchman)
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
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class DodoBossFight(BossFightPrize):
    _text = "Dodo"
    _formation = FORM0315_ONE_DODOENEMYSOLO
    _members = [
        FormationMember(DODOEnemySolo, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a large bird flapping about"
    _seaside_letter_name_if_final_boss = "Dodo's flock."

    _npc_models = [DodoLargeObject, DodoSmallObject]
    _statue_npc = DodoStatueObject

    _tiny_henchmen = [
        BossFightHenchman(monster=DODOEnemy, model=FeatherHenchman),
    ]

    _dialog_replacements = {
        # actually, don't use dialogs for dodo, just play sfx... how to handle this?
        # time this according to how long the feather sound effect is
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: "[center]\n••••••[await]",
        DI1660_SHIP_PASSWORD_COMPLETE: "[center]\n••••••[await]",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Dodo’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped DODO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: "[center]\n••••••[await]",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: "[center]\n••••••[await]",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: "[center]\n••••••[await]",
        DI1782_SHIP_BOSS_DRINK: """ (Dodo stares at a Hot Chocolate)[await]\n ...Please don’t tell Valentina.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ (Dodo stares at a Hot Chocolate)[await]\n ...Please don’t tell Valentina.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,[await][page] I saw your incredible battle with `SEASIDE_BOSS`![await]\n At the “Tanning Salon”, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n Valentina referred to them as `FINAL_BOSS_NAME`[await]\n Look, I actually think you’re cool, and I’m learning my Multistrike timing from our battles... [await]But...[delay] I can’t leave her. She needs me. I hope you understand.[await][page]\n\n                       Your biggest fan,\n                                      Dodo[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big bird! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """ (Dodo is a bird of few words.[await]\n You still have [0x7024] item(s) left\n to find.)[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """(Dodo won’t tell you this, but there\n are a few items lying around the\n room that you need to get.)[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Dodo’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Dodo.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: "[center]\n••••••[await]",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Dodo...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: "[center]\n••••••[await]",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """\n[center]••••••[delay_30][await]\n  [select] (I’m here for a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """\n[center]••••••[delay_30][await]\n  [select] (I’m here for a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n I never hear the guy next door.[await]\n Maybe he can’t talk.[await][page]\n I’d like to go over and introduce\n myself sometime, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: "[center]\n••••••[await]",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: "[center]\n••••••[await]",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Dodo’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Dodo.[await]""",
    }


__all__ = ["DodoBossFight"]
