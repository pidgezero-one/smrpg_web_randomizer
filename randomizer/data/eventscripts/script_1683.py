from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1683_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x704f, 1, 'EVENT_1682_set_short_mem_0']
    },
    {
        "identifier": 'EVENT_1683_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_1583_action_queue_sync_6']
    },
    {
        "identifier": 'EVENT_1683_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_1683_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._319_LANDS_END_DESERT_AREA_06, RadialDirections.NORTH, 7, 118, 0, []]
    },
    {
        "identifier": 'EVENT_1683_fade_in_from_black_sync_4',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1683_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_walk_1_step_north_3',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_floating_on_5',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1683_action_queue_sync_5_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_1683_action_queue_sync_5_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1683_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1683_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [1783]
    }
]
