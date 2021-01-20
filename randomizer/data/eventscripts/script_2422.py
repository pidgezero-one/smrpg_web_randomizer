from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2422_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_2422_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2422_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2422_action_queue_async_1_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_1_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_1_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_1_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_1_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_1_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2422_set_action_script_async_2',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 408],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2422_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2422_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2422_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2422_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [23, 53]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0x24, 0xc0, 0xff, 0x80, 0xfe]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0x25, 0x00, 0x09, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_bpl_26_27_28_11',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2422_action_queue_async_6_SUBSCRIPT_set_solidity_bits_12',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2422_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2422_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
