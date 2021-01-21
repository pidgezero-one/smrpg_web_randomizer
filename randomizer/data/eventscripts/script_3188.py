from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3188_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3188_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3188_action_queue_sync_1_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_3188_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_transfer_to_object_xy_3',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MEM_70A8]
            },
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 26, RadialDirections.NORTHEAST]
            },
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_sequence_playback_off_6',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3188_action_queue_async_2_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3188_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_embedded_animation_routine_4',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_embedded_animation_routine_5',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._048_MINECART_START, 4]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_3_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [200]
            }
        ]
    },
    {
        "identifier": 'EVENT_3188_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_embedded_animation_routine_3',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_embedded_animation_routine_4',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_embedded_animation_routine_5',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [200]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_set_bit_7',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3188_action_queue_sync_4_SUBSCRIPT_object_memory_clear_bit_8',
                "command": 'object_memory_clear_bit',
                "args": [0x0b, [3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3188_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3188_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3188_pause_5']
    },
    {
        "identifier": 'EVENT_3188_fade_out_to_black_async_7',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_3188_store_7000_minecart_timer_8',
        "command": 'store_7000_minecart_timer'
    },
    {
        "identifier": 'EVENT_3188_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x702e, 0x7000]
    },
    {
        "identifier": 'EVENT_3188_run_moleville_mountain_sequence_10',
        "command": 'run_moleville_mountain_sequence'
    },
    {
        "identifier": 'EVENT_3188_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, RadialDirections.SOUTH, 0, 0, 0, []]
    },
    {
        "identifier": 'EVENT_3188_set_bit_12',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_3188_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [1648]
    }
]
