from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1811_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x704f, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_jmp_if_object_trigger_disabled_1',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, 'EVENT_1811_jmp_if_object_trigger_disabled_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1811_action_queue_async_2_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1811_jmp_if_object_trigger_disabled_3',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_3, Rooms._425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, 'EVENT_1811_run_event_as_subroutine_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1811_action_queue_async_4_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1811_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [1844],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1811_clear_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_jmp_if_object_trigger_enabled_9',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_2, Rooms._425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, 'EVENT_1811_play_sound_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_jmp_if_object_trigger_disabled_10',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_3, Rooms._425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, 'EVENT_1811_clear_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1811_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
