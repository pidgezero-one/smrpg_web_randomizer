from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1674_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 161],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._032_UNDERGROUND_WARP, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_start_embedded_action_script_async_2',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1674_start_embedded_action_script_async_2_SUBSCRIPT_end_loop_7',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1674_pixelate_layers_3',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 8, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, RadialDirections.NORTHWEST, 17, 103, 11, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x704e, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_set_bit_6',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_enable_controls_7',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_fade_in_from_black_sync_8',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1674_action_queue_sync_9_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
        ]
    },
    {
        "identifier": 'EVENT_1674_pause_script_until_effect_done_10',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1674_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_1676_jmp_if_object_trigger_disabled_1'],
        "subscript": []
    },
]
