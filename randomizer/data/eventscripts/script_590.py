from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_590_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_590_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_590_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._105_SURPRISE, 6]
    },
    {
        "identifier": 'EVENT_590_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 210]
    },
    {
        "identifier": 'EVENT_590_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_12, 426]
    },
    {
        "identifier": 'EVENT_590_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_590_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_590_dec_short_7',
        "command": 'dec_short',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_590_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_590_run_dialog_9',
        "command": 'run_dialog',
        "args": [835, AreaObjects.MARIO, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_590_ret_10',
        "command": 'ret'
    }
]
