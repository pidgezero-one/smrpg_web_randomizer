from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2542_set_bit_0',
        "command": 'set_bit',
        "args": [0x7047, 0]
    },
    {
        "identifier": 'EVENT_2542_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2542_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2542_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2542_action_queue_async_2_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2542_action_queue_async_2_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2542_action_queue_async_2_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2542_action_queue_async_2_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2542_action_queue_async_2_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2542_action_queue_async_2_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2542_set_action_script_async_3',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 408]
    },
    {
        "identifier": 'EVENT_2542_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 6]
    },
    {
        "identifier": 'EVENT_2542_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2542_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2542_action_queue_sync_5_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2542_action_queue_sync_5_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x00, 0x0f, 0xf0, 0xff]
            },
            {
                "identifier": 'EVENT_2542_action_queue_sync_5_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2542_action_queue_sync_5_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2542_pause_6',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2542_fade_out_to_black_async_duration_7',
        "command": 'fade_out_to_black_async_duration',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2542_stop_embedded_action_script_8',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2542_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, RadialDirections.SOUTH, 7, 34, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2542_ret_10',
        "command": 'ret'
    }
]
