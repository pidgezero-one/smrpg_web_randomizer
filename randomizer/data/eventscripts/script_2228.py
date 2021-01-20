from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2228_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM, 'EVENT_2228_db_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 1010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_db_2',
        "command": 'db',
        "args": [0xfd, 0x8f, 0x02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_priority_set_3',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_3], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.BACKGROUND, _0x81Flags.HALF_INTENSITY]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2228_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2228_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2228_action_queue_sync_5_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2228_action_queue_sync_5_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2228_action_queue_sync_5_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2228_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2228_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2228_action_queue_sync_6_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2228_action_queue_sync_6_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2228_action_queue_sync_6_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2228_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2228_action_queue_async_7_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2228_action_queue_async_7_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2228_action_queue_async_7_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2228_set_7000_to_object_coord_8',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_jmp_if_var_not_equals_short_9',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 27, 'EVENT_2228_fade_in_from_black_async_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_set_bit_12',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_set_bit_13',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2228_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
