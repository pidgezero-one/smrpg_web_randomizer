from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1897_set_bit_0',
        "command": 'set_bit',
        "args": [0x7095, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 3, 'EVENT_1897_action_queue_sync_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_apply_solidity_mod_2',
        "command": 'apply_solidity_mod',
        "args": [Rooms._474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1897_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1897_action_queue_sync_3_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1897_action_queue_sync_3_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1897_action_queue_sync_3_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1897_action_queue_sync_3_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1897_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 1, 'EVENT_1897_fade_in_from_black_sync_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_fade_in_from_black_sync_7',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_transfer_xyzf_steps_2',
                "command": 'transfer_xyzf_steps',
                "args": [0, 255, 30, RadialDirections.NORTHEAST]
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_walk_1_step_south_4',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1897_action_queue_async_8_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_1897_action_queue_async_8_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1897_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7096, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1897_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
