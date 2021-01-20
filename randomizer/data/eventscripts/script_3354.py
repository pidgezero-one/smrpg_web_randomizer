from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3354_set_0',
        "command": 'set',
        "args": [0x70a8, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3354_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3354_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3354_add_3',
        "command": 'add',
        "args": [0x70a8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3354_end_loop_4',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3354_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3354_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3354_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3354_action_queue_async_6_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [6, 49]
            },
            {
                "identifier": 'EVENT_3354_action_queue_async_6_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3354_run_event_at_return_7',
        "command": 'run_event_at_return',
        "args": [3355],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3354_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
