from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_80_pause_script_if_menu_open_0',
        "command": 'pause_script_if_menu_open'
    },
    {
        "identifier": 'EVENT_80_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_81_ret_9']
    },
    {
        "identifier": 'EVENT_80_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_80_set_bit_3',
        "command": 'set_bit',
        "args": [0x7052, 7]
    },
    {
        "identifier": 'EVENT_80_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_80_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x70c6, 0x7000]
    },
    {
        "identifier": 'EVENT_80_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_80_freeze_camera_7',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_80_unfreeze_all_npcs_8',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_80_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._150_EXIT_TO_WORLD_MAP, 6]
    },
    {
        "identifier": 'EVENT_80_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 408]
    },
    {
        "identifier": 'EVENT_80_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_shift_z_up_steps_5',
                "command": 'shift_z_up_steps',
                "args": [14]
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_set_short_mem_6',
                "command": 'set_short_mem',
                "args": [0x700c, 0x70c6]
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_set_short_mem_7',
                "command": 'set_short_mem',
                "args": [0x70a9, 0x700c]
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0xc8, 0x91]
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_run_away_transfer_8A_9',
                "command": 'run_away_transfer_8A'
            },
            {
                "identifier": 'EVENT_80_action_queue_async_11_SUBSCRIPT_ret_10',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_80_fade_out_to_black_async_12',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_80_open_save_menu_13',
        "command": 'open_save_menu'
    }
]
