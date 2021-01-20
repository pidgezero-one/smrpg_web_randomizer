from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2617_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7091, 3, 'EVENT_2617_fade_in_from_black_async_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2617_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2617_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_1_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_1_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_1_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_1_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2617_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2617_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_2_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_2_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_2_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2617_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2617_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_3_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_3_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2617_action_queue_sync_3_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2617_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2617_action_queue_async_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2617_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2617_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2617_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
