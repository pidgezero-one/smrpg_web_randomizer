from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3592_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3592_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3592_action_queue_async_1_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3592_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 1, 'EVENT_3592_set_action_script_async_5']
    },
    {
        "identifier": 'EVENT_3592_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._026_LAUGHING_BOWSER, 6]
    },
    {
        "identifier": 'EVENT_3592_pause_4',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3592_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MEM_70A8, 636]
    },
    {
        "identifier": 'EVENT_3592_run_dialog_6',
        "command": 'run_dialog',
        "args": [539, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3592_set_7000_to_current_level_7',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3592_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 51, 'EVENT_3592_action_queue_async_28']
    },
    {
        "identifier": 'EVENT_3592_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 495, 'EVENT_3592_action_queue_async_28']
    },
    {
        "identifier": 'EVENT_3592_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3592_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_10_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_10_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [12, 117]
            }
        ]
    },
    {
        "identifier": 'EVENT_3592_pause_11',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3592_set_7000_to_current_level_12',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3592_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 191, 'EVENT_3592_apply_tile_mod_16']
    },
    {
        "identifier": 'EVENT_3592_apply_tile_mod_14',
        "command": 'apply_tile_mod',
        "args": [Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3592_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3592_play_sound_17']
    },
    {
        "identifier": 'EVENT_3592_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3592_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3592_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3592_action_queue_async_18_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_18_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3592_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3592_set_7000_to_current_level_20',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3592_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 191, 'EVENT_3592_apply_tile_mod_24']
    },
    {
        "identifier": 'EVENT_3592_apply_tile_mod_22',
        "command": 'apply_tile_mod',
        "args": [Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, 0, []]
    },
    {
        "identifier": 'EVENT_3592_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_3592_play_sound_25']
    },
    {
        "identifier": 'EVENT_3592_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, 0, []]
    },
    {
        "identifier": 'EVENT_3592_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3592_set_bit_26',
        "command": 'set_bit',
        "args": [0x709c, 1]
    },
    {
        "identifier": 'EVENT_3592_ret_27',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3592_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3592_action_queue_async_28_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_28_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_28_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_28_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3592_action_queue_async_28_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3592_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3592_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x709c, 1]
    },
    {
        "identifier": 'EVENT_3592_ret_31',
        "command": 'ret'
    }
]
