from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1676_fade_in_from_black_async_0',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_jmp_if_object_trigger_disabled_1',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_6, Rooms._270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, 'EVENT_1676_run_event_as_subroutine_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1676_action_queue_sync_2_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1676_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1676_clear_bit_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_jmp_if_object_trigger_disabled_5',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_6, Rooms._270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, 'EVENT_1676_clear_bit_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_set_8',
        "command": 'set',
        "args": [0x70df, 37],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x708c, 4, 'EVENT_1676_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_set_10',
        "command": 'set',
        "args": [0x70df, 43],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1676_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
