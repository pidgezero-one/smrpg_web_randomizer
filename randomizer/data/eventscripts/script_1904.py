from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1904_set_short_0',
        "command": 'set_short',
        "args": [0x700e, 0x00d5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_start_battle_700E_1',
        "command": 'start_battle_700E',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1904_fade_in_from_black_sync_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1695_reset_and_choose_game_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 3, 'EVENT_1904_ret_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_pause_7',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_create_packet_at_object_coords_jmp_if_null_8',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, AreaObjects.NPC_0, 'EVENT_1904_pause_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_shift_south_steps_4',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1904_action_queue_async_11_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1904_set_bit_12',
        "command": 'set_bit',
        "args": [0x7096, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_apply_solidity_mod_13',
        "command": 'apply_solidity_mod',
        "args": [Rooms._474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_fade_in_from_black_sync_15',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_disable_trigger_16',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_resume_action_script_17',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1904_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
