from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3149_remove_object_at_70A8_from_current_level_0',
        "command": 'remove_object_at_70A8_from_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 28, 'EVENT_3149_disable_trigger_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_disable_trigger_2',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3149_action_queue_sync_5_SUBSCRIPT_shift_z_up_steps_0',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3149_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3149_action_queue_sync_5_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3149_action_queue_sync_5_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3149_set_6',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_add_max_FP_7000_7',
        "command": 'add_max_FP_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_disable_trigger_9',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_move_script_to_background_thread_2_12',
        "command": 'move_script_to_background_thread_2',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_enable_controls_until_return_13',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_restore_all_hp_14',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_restore_all_fp_15',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_tint_layers_16',
        "command": 'tint_layers',
        "args": [0x40, 0xa0, 0x40, 3, [_0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_tint_layers_17',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 3, [_0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_reset_priority_set_18',
        "command": 'reset_priority_set',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_move_script_to_main_thread_19',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3149_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
