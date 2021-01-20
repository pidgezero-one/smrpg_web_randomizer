from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2090_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7093, 3, 'EVENT_2090_action_queue_sync_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_set_action_script_async_1',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_2, 690],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2090_action_queue_sync_2_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2090_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2090_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2090_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2090_action_queue_sync_3_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2090_action_queue_sync_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_2090_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2090_action_queue_async_4_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2090_action_queue_async_4_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2090_action_queue_async_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_2090_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7093, 3, 'EVENT_2090_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2090_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2090_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
