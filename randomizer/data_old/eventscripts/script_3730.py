
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3730_remove_from_level_0',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA]
    },
    {
        "identifier": 'EVENT_3730_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_14, Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA]
    },
    {
        "identifier": 'EVENT_3730_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, "EVENT_3730_sequence_setter_1"]
    },
    {
        "identifier": 'EVENT_3730_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 1, "EVENT_3730_sequence_setter_1"]
    },
    {
        "identifier": 'EVENT_3730_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 5, 'EVENT_3730_palette_set_6']
    },
    {
        "identifier": 'EVENT_3730_jmp_5',
        "command": 'jmp',
        "args": ["EVENT_3730_sequence_setter_1"]
    },
    {
        "identifier": 'EVENT_3730_palette_set_6',
        "command": 'palette_set',
        "args": [84, 1, [0, 1, 2, 3]]
    },
    {
        "identifier": 'EVENT_3730_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3730_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_3730_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3730_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA]
    },
    {
        "identifier": 'EVENT_3730_action_queue_sync_11',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": 'EVENT_3730_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [25, 21, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3730_action_queue_sync_11_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3730_action_queue_sync_12',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_5, True],
        "subscript": [
            {
                "identifier": 'EVENT_3730_action_queue_sync_12_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [26, 22, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3730_action_queue_sync_12_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3730_remember_last_object_13',
        "command": 'remember_last_object'
    },
    {
        "identifier": "EVENT_3730_sequence_setter_1",
        "command": "run_event_as_subroutine",
        "args": [824]
    },
    {
        "identifier": 'EVENT_3730_fade_in_from_black_async_14_',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3730_ret_15',
        "command": 'ret'
    }
]
