# referenced by ,items KerokeroCola,items MapleSyrup,items Megalixir,items 79,items BadMushroom,items RoyalSyrup,items SleepyBomb,items AbleJuice,items Bracer,items MukuCookie,items RockCandy,items PureWater,items Elixir,items IceBomb,items YoshiAde,items HoneySyrup,items MidMushroom,items RedEssence,items FireBomb,items Mushroom,items RottenMush,items FroggieDrink,items PickMeUp,items Energizer,items MysteryEgg,items WiltShroom,items MaxMushroom

# classes
from randomizer.types.battle_animation_scripts.commands import *
from randomizer.types.battle_animation_scripts.classes import (
    AnimationScript,
    BattleAnimationScript,
    SubroutineOrBanklessScript,
)

# ids
from randomizer.types.battle_animation_scripts.constants.origins import *
from randomizer.types.battle_animation_scripts.constants.pause_until import *
from randomizer.types.battle_animation_scripts.constants.shift_type import *
from randomizer.types.battle_animation_scripts.constants.message_type import *
from randomizer.types.battle_animation_scripts.constants.effects import *
from randomizer.types.battle_animation_scripts.constants.layer_priority_type import *
from randomizer.types.battle_animation_scripts.constants.flash_colours import *
from randomizer.types.battle_animation_scripts.constants.bonus_messages import *
from randomizer.types.battle_animation_scripts.constants.screen_effects import *
from randomizer.types.battle_animation_scripts.constants.sounds import *
from randomizer.types.battle_animation_scripts.constants.music import *
from randomizer.types.battle_animation_scripts.constants.battle_targets import *
from randomizer.types.battle_animation_scripts.constants.script_ids.battle_events import *
from randomizer.types.sprites.constants.sprite_ids import *
from randomizer.entities.items.items import *
from randomizer.entities.enemies.enemies import *

# types
# entities

script = SubroutineOrBanklessScript(
    expected_size=42,
    script=[
        SetAMEMToRandom(amem=0x6E, upper_bound=100, identifier="command_0x35c968"),
        JmpIfAMEM8BitGreaterOrEqualThanConst(0x6E, 26, ["command_0x35c974"]),
        RunSubroutine(["command_0x35c982"]),
        ReturnSubroutine(identifier="command_0x35c974"),
        SetAMEMToRandom(amem=0x6E, upper_bound=100, identifier="command_0x35c975"),
        JmpIfAMEM8BitGreaterOrEqualThanConst(0x6E, 13, ["command_0x35c981"]),
        RunSubroutine(["command_0x35c982"]),
        ReturnSubroutine(identifier="command_0x35c981"),
        PlaySound(sound=S0006_BONUS_FLOWER_STATUS_UP, identifier="command_0x35c982"),
        DisplayMessage(BATTLE_MESSAGE, 8),
        PauseScriptUntilDialogueClosed(),
        SetAMEM16BitTo7E1x(0x60, 0x7EE022),
        IncAMEM16BitByConst(0x60, 96),
        StoreOMEM60ToItemInventory(),
        ReturnSubroutine(),
    ],
)
