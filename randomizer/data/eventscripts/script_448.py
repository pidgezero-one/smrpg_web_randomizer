from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_448_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_448_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_448_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._066_KICK_BALL_SHELL, 6]
    },
    {
        "identifier": 'EVENT_448_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 210]
    },
    {
        "identifier": 'EVENT_448_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 420]
    },
    {
        "identifier": 'EVENT_448_inc_short_5',
        "command": 'inc_short',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_448_set_7000_to_7000_short_mem_6',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_448_run_dialog_7',
        "command": 'run_dialog',
        "args": [835, AreaObjects.MARIO, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_448_ret_8',
        "command": 'ret'
    }
]
