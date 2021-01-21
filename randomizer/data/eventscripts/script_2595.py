from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2595_set_0',
        "command": 'set',
        "args": [0x70c0, 237]
    },
    {
        "identifier": 'EVENT_2595_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 4, 'EVENT_2595_jmp_if_bit_clear_3']
    },
    {
        "identifier": 'EVENT_2595_set_action_script_async_2',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 690]
    },
    {
        "identifier": 'EVENT_2595_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_2595_fade_in_from_black_async_6']
    },
    {
        "identifier": 'EVENT_2595_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_2595_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2595_run_event_as_subroutine_7']
    },
    {
        "identifier": 'EVENT_2595_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2595_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_2595_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2595_clear_bit_12']
    },
    {
        "identifier": 'EVENT_2595_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x708f, 4, 'EVENT_2595_clear_bit_12']
    },
    {
        "identifier": 'EVENT_2595_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2595_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2595_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2595_ret_13',
        "command": 'ret'
    }
]
