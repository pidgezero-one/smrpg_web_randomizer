# pylint: disable=C0301,C0103

"""referenced by ,weapons SonicCymbal,weapons Accessory,behaviour_32_0x350C14,weapons SuperHammer,weapons StickyGlove,weapons FroggieStick,weapons SlapGlove,behaviour_23_0x350A55,weapons Armor,behaviour_8_0x3507A2,weapons Hammer,behaviour_51_0x350F56,weapons HandGun,weapons PunchGlove,weapons TroopaShell,weapons WarFan,behaviour_43_0x350E38,behaviour_24_0x350A9C,weapons SuperSlap,behaviour_33_0x350C5B,behaviour_52_0x350F6B,weapons Parasol,weapons MegaGlove,weapons StarGun,weapons NokNokShell,weapons SpikedLink,weapons WhompGlove,weapons Chomp,weapons LuckyHammer,behaviour_42_0x350DED,weapons DoublePunch,weapons FingerShot,weapons HurlyGloves,weapons Masher,behaviour_41_0x350DAF,weapons Weapon,weapons Cymbals,weapons RibbitStick,weapons UltraHammer,weapons ChompShell,weapons HandCannon,weapons DrillClaw,weapons FryingPan,weapons Space,ally_spells Sleepy Time,behaviour_34_0x350C9E,behaviour_16_0x350928,weapons LazyShellWeapon,behaviour_9_0x3507E9"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=18,
    script=[
        ClearAMEM8Bit(0x6F, identifier="command_0x35f112"),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x35F137),
        Pause1Frame(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0002_MARIO_WALKING_UP_RIGHT, sequence=10, store_to_vram=True
        ),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        PauseScriptUntilSpriteSequenceDone(),
        ReturnSubroutine(),
    ],
)
