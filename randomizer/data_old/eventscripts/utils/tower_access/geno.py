
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    # tower's already been opened
    {
        "identifier": 'EVENT_1331_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 6, 'EVENT_1331_ret']
    },

    # don't have the right character yet
    {
        "identifier": 'EVENT_1331_jmp_if_bit_set_0_',
        "command": 'jmp_if_bit_clear',
        "args": [0x7053, 7, 'EVENT_1331_ret']
    },

    # do have the right character
    {
        "identifier": 'EVENT_1331_remove_from_current_level_3_',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },


    {
        "identifier": 'EVENT_1331_action_queue_async_10',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [4, 114]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_face_east_3',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": "EVENT_1331_pause_1",
        "command": "pause",
        "args": [25]
    },
    {
        "identifier": "EVENT_1331_summon_partner",
        "command": "summon_to_current_level_at_marios_coords",
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_11',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, False],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [5, 115]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'face_northeast'
            },
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_sync_11_________',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, True],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_face_east_3',
                "command": 'visibility_off'
            },
        ]
    },
    {
        "identifier": 'EVENT_1331_pause_13________',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_11____',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, False],
        "subscript": [
            {
                "identifier": 'ACTION_830_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_face_east_3',
                "command": 'visibility_on'
            }
        ]
    },
    
    {
        "identifier": 'EVENT_1331_pause_13_',
        "command": 'pause',
        "args": [21]
    },
    {
        "identifier": 'EVENT_1331_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._075_ROCKETING_BLAST, 6]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_11___',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": 'ACTION_830_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_north_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_west_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_face_east_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_face_east_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_shift_northeast_steps_17',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
        ]
    },

    {
        "identifier": 'EVENT_1331_pause_13__',
        "command": 'pause',
        "args": [22]
    },

    {
        "identifier": 'EVENT_1331_apply_solidity_mod_14',
        "command": 'apply_solidity_mod',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1331_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1331_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1331_remove_from_level_18',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._202_BOOSTER_TOWER_ENTRANCE]
    },
    {
        "identifier": 'EVENT_1331_remove_from_current_level_17_',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1331_summon_current_level_17_',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1331_pause_19',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1331_remove_from_current_level_17__',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_133',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, False],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_133_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_133_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'pause_132',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2496_____action_queue_async_250_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'face_southwest',
            },
        ]
    },
    
    {
        "identifier": 'EVENT_1331_pause_19__________________',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_10__',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, True],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [5, 116]
            },
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_10_',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, False],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [5, 116]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_face_east_3',
                "command": 'face_northeast'
            },
        ]
    },
    {
        "identifier": 'EVENT_1331_remove_from_current_level_3__',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },

    {
        "identifier": 'EVENT_1331_set_bit',
        "command": 'set_bit',
        "args": [0x7053, 6]
    },
    {
        "identifier": 'EVENT_1331_ret',
        "command": 'ret'
    }
]
