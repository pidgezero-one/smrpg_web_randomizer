from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2403_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x708b, 3, 'EVENT_2403_ret_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 4, 'EVENT_2403_ret_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_stop_all_background_events_2',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_fade_out_music_3',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_set_bit_4',
        "command": 'set_bit',
        "args": [0x708b, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0xc0, 0xff]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [54]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_set_priority_9',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2403_pause_6',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_play_music_default_volume_7',
        "command": 'play_music_default_volume',
        "args": [Music._45_HEART_BEATING_A_LITTLE_FASTER_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_stop_embedded_action_script_8',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2403_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2403_action_queue_async_9_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2403_action_queue_async_9_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2403_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_fade_out_music_11',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_shadow_on_2',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2403_action_queue_sync_12_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2403_pause_13',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_play_music_default_volume_14',
        "command": 'play_music_default_volume',
        "args": [Music._46_HEART_BEATING_A_LITTLE_FASTER_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_stop_embedded_action_script_15',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_set_action_script_async_16',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_set_action_script_async_17',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_pause_18',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_play_music_default_volume_19',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_enable_controls_20',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2403_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
