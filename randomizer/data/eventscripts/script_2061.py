from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2061_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_2061_pause_1',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2061_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._038_TADPOLE_POND_STAFF_MI, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_shift_southeast_pixels_12',
                "command": 'shift_southeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._039_TADPOLE_POND_STAFF_FA, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_shift_northwest_pixels_20',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_21',
                "command": 'play_sound',
                "args": [Sounds._040_TADPOLE_POND_STAFF_SO, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_shift_southeast_pixels_25',
                "command": 'shift_southeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_26',
                "command": 'play_sound',
                "args": [Sounds._041_TADPOLE_POND_STAFF_LA, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_28',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_29',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_31',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_32',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_33',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_jump_to_height_34',
                "command": 'jump_to_height',
                "args": [37]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_35',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_36',
                "command": 'play_sound',
                "args": [Sounds._037_TADPOLE_POND_STAFF_RE, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_38',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_39',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_40',
                "command": 'play_sound',
                "args": [Sounds._040_TADPOLE_POND_STAFF_SO, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_41',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_42',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_43',
                "command": 'play_sound',
                "args": [Sounds._041_TADPOLE_POND_STAFF_LA, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_44',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_45',
                "command": 'set_sprite_sequence',
                "args": [20, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_46',
                "command": 'play_sound',
                "args": [Sounds._042_TADPOLE_POND_STAFF_TI, 6]
            },
            {
                "identifier": 'EVENT_2061_action_queue_async_2_SUBSCRIPT_pause_47',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2061_set_bit_3',
        "command": 'set_bit',
        "args": [0x7089, 0]
    },
    {
        "identifier": 'EVENT_2061_fade_out_music_to_volume_4',
        "command": 'fade_out_music_to_volume',
        "args": [5, 100]
    },
    {
        "identifier": 'EVENT_2061_ret_5',
        "command": 'ret'
    }
]
