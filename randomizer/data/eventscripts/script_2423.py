from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2423_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_2423_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_2423_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2423_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2423_action_queue_async_2_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2423_action_queue_async_2_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2423_action_queue_async_2_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2423_action_queue_async_2_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2423_action_queue_async_2_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2423_action_queue_async_2_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2423_set_action_script_async_3',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 408]
    },
    {
        "identifier": 'EVENT_2423_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 6]
    },
    {
        "identifier": 'EVENT_2423_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0x30, 0x02, 0xe0, 0xfe]
            },
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x09, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2423_action_queue_sync_5_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2423_pause_6',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2423_freeze_camera_7',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2423_pause_8',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2423_fade_out_to_black_async_duration_9',
        "command": 'fade_out_to_black_async_duration',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2423_stop_embedded_action_script_10',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2423_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x708f, 7, 'EVENT_2423_enter_area_14']
    },
    {
        "identifier": 'EVENT_2423_enter_area_12',
        "command": 'enter_area',
        "args": [Rooms._223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM, RadialDirections.SOUTH, 4, 113, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2423_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2423_enter_area_14',
        "command": 'enter_area',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, RadialDirections.SOUTH, 15, 10, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2423_ret_15',
        "command": 'ret'
    }
]
