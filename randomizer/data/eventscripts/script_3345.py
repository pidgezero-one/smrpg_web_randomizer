from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3345_remove_from_level_0',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_set_bit_4',
        "command": 'set_bit',
        "args": [0x707e, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_if_objects_less_than_xy_steps_apart_6',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_1, 0x00, 0x04, 'EVENT_3345_remove_from_current_level_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_3345_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_level_9',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_create_packet_at_object_coords_jmp_if_null_10',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_1, 'EVENT_3345_action_queue_sync_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_floating_off_4',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_jump_to_height_silent_8',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3345_pause_12',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_if_objects_less_than_xy_steps_apart_13',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_0, 0x00, 0x02, 'EVENT_3345_remove_from_current_level_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_3345_pause_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_current_level_15',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_level_16',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_create_packet_at_object_coords_jmp_if_null_17',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_0, 'EVENT_3345_pause_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_if_objects_less_than_xy_steps_apart_19',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_2, 0x00, 0x04, 'EVENT_3345_remove_from_current_level_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3345_pause_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_current_level_21',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_level_22',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_create_packet_at_object_coords_jmp_if_null_23',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_2, 'EVENT_3345_action_queue_sync_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3345_action_queue_sync_24_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x17]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_24_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_24_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3345_action_queue_sync_24_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3345_pause_25',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_if_objects_less_than_xy_steps_apart_26',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_3, 0x00, 0x04, 'EVENT_3345_remove_from_current_level_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3345_pause_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_current_level_28',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_remove_from_level_30',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._394_VOLCANO_POSTCD_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_create_packet_at_object_coords_jmp_if_null_31',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_3, 'EVENT_3345_create_packet_at_object_coords_jmp_if_null_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_create_packet_at_object_coords_jmp_if_null_32',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_0, 'EVENT_3345_ret_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3345_ret_33',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
