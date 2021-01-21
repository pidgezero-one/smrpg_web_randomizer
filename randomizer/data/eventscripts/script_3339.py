from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3339_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 2, 'EVENT_3339_run_event_as_subroutine_42']
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_1_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_1_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3339_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_async_3_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_4_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_set_2',
                "command": 'set',
                "args": [0x70af, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_3',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._041_AXEM_BLACK, AreaObjects.NPC_6, 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_clear_bit_7',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_9',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_walk_1_step_northeast_10',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_off_11',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_5_SUBSCRIPT_set_bit_12',
                "command": 'set_bit',
                "args": [0x7044, 7]
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_run_dialog_6',
        "command": 'run_dialog',
        "args": [1814, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_jmp_if_bit_clear_3',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 7, 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_pause_2']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_clear_bit_4',
                "command": 'clear_bit',
                "args": [0x7044, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_set_5',
                "command": 'set',
                "args": [0x70af, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_6',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._042_AXEM_PINK, AreaObjects.NPC_5, 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_clear_bit_10',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_visibility_on_11',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_on_12',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_walk_1_step_northeast_13',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_off_14',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_7_SUBSCRIPT_set_bit_15',
                "command": 'set_bit',
                "args": [0x7044, 7]
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_run_dialog_8',
        "command": 'run_dialog',
        "args": [1815, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_9_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_jmp_if_bit_clear_3',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 7, 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_pause_2']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_clear_bit_4',
                "command": 'clear_bit',
                "args": [0x7044, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_set_5',
                "command": 'set',
                "args": [0x70af, 135]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_6',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._043_AXEM_YELLOW, AreaObjects.NPC_4, 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_clear_bit_10',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_visibility_on_11',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_on_12',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_walk_1_step_northwest_13',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_off_14',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_10_SUBSCRIPT_set_bit_15',
                "command": 'set_bit',
                "args": [0x7044, 7]
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_run_dialog_11',
        "command": 'run_dialog',
        "args": [1816, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_jmp_if_bit_clear_4',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 7, 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_clear_bit_5',
                "command": 'clear_bit',
                "args": [0x7044, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_set_6',
                "command": 'set',
                "args": [0x70af, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_7',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._044_AXEM_GREEN, AreaObjects.NPC_3, 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_pause_8']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_clear_bit_11',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_visibility_on_12',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_fixed_f_coord_on_15',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_walk_1_step_northwest_16',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_fixed_f_coord_off_17',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_face_southeast_18',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_12_SUBSCRIPT_set_bit_20',
                "command": 'set_bit',
                "args": [0x7044, 7]
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_run_dialog_13',
        "command": 'run_dialog',
        "args": [1817, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3339_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_jmp_if_bit_clear_7',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 7, 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_clear_bit_8',
                "command": 'clear_bit',
                "args": [0x7044, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_set_9',
                "command": 'set',
                "args": [0x70af, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_10',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._040_AXEM_RED, AreaObjects.NPC_2, 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_pause_11']
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_visibility_off_12',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_clear_bit_14',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_set_bit_16',
                "command": 'set_bit',
                "args": [0x7044, 7]
            },
            {
                "identifier": 'EVENT_3339_action_queue_sync_14_SUBSCRIPT_set_bit_17',
                "command": 'set_bit',
                "args": [0x7043, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_run_dialog_15',
        "command": 'run_dialog',
        "args": [1818, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3339_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3339_jmp_if_bit_clear_17',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'EVENT_3339_pause_16']
    },
    {
        "identifier": 'EVENT_3339_pause_18',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3339_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_3339_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3339_action_queue_async_20_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3339_action_queue_async_20_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3339_remove_from_current_level_21',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3339_remove_from_current_level_22',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3339_create_packet_at_object_coords_jmp_if_null_23',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_2, 'EVENT_3339_create_packet_at_object_coords_jmp_if_null_24']
    },
    {
        "identifier": 'EVENT_3339_create_packet_at_object_coords_jmp_if_null_24',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_1, 'EVENT_3339_pause_25']
    },
    {
        "identifier": 'EVENT_3339_pause_25',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3339_remove_from_current_level_26',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_3339_create_packet_at_object_coords_jmp_if_null_27',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_6, 'EVENT_3339_pause_28']
    },
    {
        "identifier": 'EVENT_3339_pause_28',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3339_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3339_create_packet_at_object_coords_jmp_if_null_30',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_4, 'EVENT_3339_pause_31']
    },
    {
        "identifier": 'EVENT_3339_pause_31',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3339_remove_from_current_level_32',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_3339_create_packet_at_object_coords_jmp_if_null_33',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_5, 'EVENT_3339_pause_34']
    },
    {
        "identifier": 'EVENT_3339_pause_34',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3339_remove_from_current_level_35',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_3339_create_packet_at_object_coords_jmp_if_null_36',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_3, 'EVENT_3339_pause_37']
    },
    {
        "identifier": 'EVENT_3339_pause_37',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3339_set_bit_38',
        "command": 'set_bit',
        "args": [0x707e, 2]
    },
    {
        "identifier": 'EVENT_3339_pause_39',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3339_play_music_default_volume_40',
        "command": 'play_music_default_volume',
        "args": [Music._63_AXEM_RANGERS_DROP_IN]
    },
    {
        "identifier": 'EVENT_3339_ret_41',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3339_run_event_as_subroutine_42',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3339_ret_43',
        "command": 'ret'
    }
]
