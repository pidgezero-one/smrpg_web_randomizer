from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3208_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._112_DRAINING_WATER, 4]
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xc8, 0x90]
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_run_away_shift_2',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_object_memory_modify_bits_4',
                "command": 'object_memory_modify_bits',
                "args": [0x0c, [4], [3, 5]]
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [39]
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_turn_clockwise_45_degrees_n_times_7',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_shift_z_down_pixels_8',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_floating_on_10',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3208_action_queue_async_0_SUBSCRIPT_set_solidity_bits_11',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3208_ret_1',
        "command": 'ret'
    }
]
