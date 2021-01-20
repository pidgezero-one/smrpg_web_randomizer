from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_683_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_end_loop_8',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_683_action_queue_async_0_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_683_run_dialog_1',
        "command": 'run_dialog',
        "args": [2200, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_683_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_683_action_queue_async_2_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_683_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
