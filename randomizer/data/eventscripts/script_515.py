from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_515_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 0, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_bit_1',
        "command": 'set_bit',
        "args": [0x7066, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_bit_2',
        "command": 'set_bit',
        "args": [0x706e, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_bit_3',
        "command": 'set_bit',
        "args": [0x7060, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_move_script_to_background_thread_2_4',
        "command": 'move_script_to_background_thread_2',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_bit_5',
        "command": 'set_bit',
        "args": [0x7085, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_515_action_queue_sync_7_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[1]]
            }
        ]
    },
    {
        "identifier": 'EVENT_515_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_515_action_queue_async_8_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[1]]
            }
        ]
    },
    {
        "identifier": 'EVENT_515_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_515_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_515_action_queue_sync_9_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_515_action_queue_sync_9_SUBSCRIPT_face_west_2',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_515_action_queue_sync_9_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_515_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_run_dialog_11',
        "command": 'run_dialog',
        "args": [769, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_remember_last_object_12',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_enable_controls_until_return_13',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_pause_14',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_async_15',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 624],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_async_16',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 625],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_pause_17',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_run_dialog_18',
        "command": 'run_dialog',
        "args": [770, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_pause_19',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_async_20',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_run_dialog_21',
        "command": 'run_dialog',
        "args": [771, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_pause_22',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 625],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_run_dialog_24',
        "command": 'run_dialog',
        "args": [772, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_async_25',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 627],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_run_dialog_27',
        "command": 'run_dialog',
        "args": [773, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_bit_28',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 629],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_pause_30',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_run_dialog_32',
        "command": 'run_dialog',
        "args": [774, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_remember_last_object_33',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 630],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 631],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_pause_36',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_run_dialog_37',
        "command": 'run_dialog',
        "args": [775, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_move_script_to_main_thread_38',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_515_ret_39',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
