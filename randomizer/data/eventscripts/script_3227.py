from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3227_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, 'EVENT_3227_jmp_if_object_trigger_enabled_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 16, 'EVENT_3227_run_background_event_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3227_action_queue_async_3_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [19, 117]
            },
        ]
    },
    {
        "identifier": 'EVENT_3227_run_background_event_4',
        "command": 'run_background_event',
        "args": [3228, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_jmp_if_object_trigger_enabled_5',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_2, Rooms._179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, 'EVENT_3227_run_event_as_subroutine_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3227_action_queue_async_6_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3227_action_queue_async_6_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3227_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3227_clear_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_jmp_if_object_trigger_disabled_10',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, 'EVENT_3227_clear_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3227_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
