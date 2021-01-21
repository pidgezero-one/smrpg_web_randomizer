from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1777_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06]
    },
    {
        "identifier": 'EVENT_1777_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._402_LANDS_END_DESERT_AREA_03]
    },
    {
        "identifier": 'EVENT_1777_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._403_LANDS_END_DESERT_AREA_05]
    },
    {
        "identifier": 'EVENT_1777_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._404_LANDS_END_DESERT_AREA_04]
    },
    {
        "identifier": 'EVENT_1777_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02]
    },
    {
        "identifier": 'EVENT_1777_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1777_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 0, 'EVENT_1777_ret_32']
    },
    {
        "identifier": 'EVENT_1777_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._123_CHAIN_RUMBLING_NOISE, 6]
    },
    {
        "identifier": 'EVENT_1777_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1777_fade_out_sound_to_volume_9',
        "command": 'fade_out_sound_to_volume',
        "args": [8, 0]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_10_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_10_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [22]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_5',
                "command": 'transfer_to_xyzf',
                "args": [24, 113, 24, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_bounce_to_xy_with_height_6',
                "command": 'bounce_to_xy_with_height',
                "args": [24, 113, 44]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_11_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [21, 107, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [21, 107, 14]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [23, 110, 18, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [23, 110, 18]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_13_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [26, 116, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [26, 116, 20]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_14_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [24, 113, 24, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [24, 113, 24]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_15_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [22, 108, 24, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [22, 108, 24]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_16_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [20, 105, 28, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [20, 105, 28]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_17_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [21, 107, 31, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [21, 107, 36]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_sync_18_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [23, 111, 30, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [23, 111, 30]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_19_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_set_20',
        "command": 'set',
        "args": [0x70ab, 21]
    },
    {
        "identifier": 'EVENT_1777_run_event_as_subroutine_21',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1777_set_bit_22',
        "command": 'set_bit',
        "args": [0x7094, 4]
    },
    {
        "identifier": 'EVENT_1777_set_23',
        "command": 'set',
        "args": [0x70ab, 29]
    },
    {
        "identifier": 'EVENT_1777_start_loop_n_times_24',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'EVENT_1777_run_event_as_subroutine_25',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1777_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_set_short_0',
                "command": 'set_short',
                "args": [0x7034, 0xffff]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xc7, 0x13]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_add_short_2',
                "command": 'add_short',
                "args": [0x7010, 0x0050]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_add_short_3',
                "command": 'add_short',
                "args": [0x7014, 0x0080]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_create_packet_at_7010_coords_jmp_if_null_5',
                "command": 'create_packet_at_7010_coords_jmp_if_null',
                "args": [NPCPackets._032_BLUE_CLOUD]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._134_SWIPE, 4]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_fixed_f_coord_on_10',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_shift_northwest_pixels_11',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_shift_southeast_pixels_12',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1777_action_queue_async_26_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1777_dec_27',
        "command": 'dec',
        "args": [0x70ab]
    },
    {
        "identifier": 'EVENT_1777_end_loop_28',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1777_set_29',
        "command": 'set',
        "args": [0x70ab, 0]
    },
    {
        "identifier": 'EVENT_1777_run_event_as_subroutine_30',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1777_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x7094, 4]
    },
    {
        "identifier": 'EVENT_1777_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1777_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1777_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1777_ret_35',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1777_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1777_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1777_ret_38',
        "command": 'ret'
    }
]
