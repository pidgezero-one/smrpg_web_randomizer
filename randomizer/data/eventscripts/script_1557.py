from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1557_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7047, 0, 'EVENT_1557_jmp_if_bit_clear_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1557_action_queue_async_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1557_freeze_all_npcs_until_return_2',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_freeze_camera_4',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 482],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_unfreeze_camera_7',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_unfreeze_all_npcs_8',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x707a, 2, 'EVENT_1557_set_action_script_sync_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 36],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 36],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 36],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 36],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_pause_17',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_fade_in_from_black_sync_18',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1557_action_queue_async_19_SUBSCRIPT_walk_1_step_west_0',
                "command": 'walk_1_step_west',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1557_set_bit_20',
        "command": 'set_bit',
        "args": [0x707a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1557_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
