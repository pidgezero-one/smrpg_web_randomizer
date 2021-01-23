from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1808_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 27, 'EVENT_1808_run_event_as_subroutine_9']
    },
    {
        "identifier": 'EVENT_1808_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 29, 'EVENT_1808_run_event_as_subroutine_4']
    },
    {
        "identifier": 'EVENT_1808_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_1808_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [1767]
    },
    {
        "identifier": 'EVENT_1808_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [34]
    },
    {
        "identifier": 'EVENT_1808_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1808_ret_8']
    },
    {
        "identifier": 'EVENT_1808_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1808_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [1767]
    },
    {
        "identifier": 'EVENT_1808_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1808_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_1808_set_10',
        "command": 'set',
        "args": [0x70a7, 109]
    },
    {
        "identifier": 'EVENT_1808_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1808_run_dialog_12',
        "command": 'run_dialog',
        "args": [1177, AreaObjects.MARIO, [_0x60Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_1808_put_inventory_13',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_1808_jmp_to_event_14',
        "command": 'jmp_to_event',
        "args": [1767]
    }
]
