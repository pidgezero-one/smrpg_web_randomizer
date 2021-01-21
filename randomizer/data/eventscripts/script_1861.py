from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1861_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1861_stop_all_background_events_1',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_1861_pause_2',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1861_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1861_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1861_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1861_action_queue_sync_3_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1861_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1861_action_queue_sync_3_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1861_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._119_CZAR_DRAGON_ROAR, 4]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1c, 0xb3]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_15',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1861_action_queue_async_4_SUBSCRIPT_visibility_off_16',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1861_ret_5',
        "command": 'ret'
    }
]
