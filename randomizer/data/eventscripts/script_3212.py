from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3212_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3212_action_queue_sync_3_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_3212_action_queue_sync_3_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_3212_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_set_7000_to_pressed_button_5',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_jmp_if_7000_all_bits_clear_6',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[4], 'EVENT_3212_pause_action_script_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_enable_controls_until_return_7',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 351],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3212_action_queue_sync_9_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3212_action_queue_sync_9_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3212_pause_10',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_jmp_if_mario_in_air_11',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3212_pause_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_set_7000_to_object_coord_12',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_mem_7000_shift_left_13',
        "command": 'mem_7000_shift_left',
        "args": [0x7006, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_close_dialog_14',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_run_dialog_15',
        "command": 'run_dialog',
        "args": [1658, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_jmp_if_dialog_option_b_16',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3212_pause_action_script_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_run_dialog_17',
        "command": 'run_dialog',
        "args": [1657, AreaObjects.BOWSER, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3212_pause_action_script_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_pause_action_script_19',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3212_action_queue_sync_21_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_3212_action_queue_sync_21_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_3212_enter_area_22',
        "command": 'enter_area',
        "args": [Rooms._168_SUNKEN_SHIP_PUZZLE_ROOM_3, RadialDirections.NORTHWEST, 31, 116, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3212_ret_23',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
