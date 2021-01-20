from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_430_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_430_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_430_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_jmp_if_bit_clear_4',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 4, 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_6']
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_430_action_queue_async_2_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [25, 28, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_vram_priority_11',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_12',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_13',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_floating_off_14',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_transfer_xyzf_pixels_17',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 19, RadialDirections.NORTHEAST]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_shift_z_down_pixels_18',
                "command": 'shift_z_down_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_shift_southwest_pixels_20',
                "command": 'shift_southwest_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_end_loop_21',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_face_northeast_23',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_solidity_bits_24',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_solidity_bits_25',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_floating_on_26',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_430_action_queue_async_2_SUBSCRIPT_shadow_on_28',
                "command": 'shadow_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_430_freeze_all_npcs_until_return_3',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_430_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [276],
        "subscript": []
    },
    {
        "identifier": 'EVENT_430_unfreeze_all_npcs_5',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_430_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_430_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_430_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
