from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3707_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_3707_jmp_if_object_trigger_disabled_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_set_bit_1',
        "command": 'set_bit',
        "args": [0x704c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_jmp_if_object_trigger_disabled_2',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, 'EVENT_3707_jmp_if_object_trigger_disabled_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3707_action_queue_async_3_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3707_jmp_if_object_trigger_disabled_4',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, 'EVENT_3707_apply_solidity_mod_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3707_action_queue_sync_5_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3707_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3707_action_queue_async_6_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3707_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_jmp_if_object_trigger_enabled_11',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, 'EVENT_3707_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_jmp_if_object_trigger_enabled_12',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, 'EVENT_3707_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3707_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
