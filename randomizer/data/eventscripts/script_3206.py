from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3206_set_bit_0',
        "command": 'set_bit',
        "args": [0x7067, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_set_bit_1',
        "command": 'set_bit',
        "args": [0x706f, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_set_short_2',
        "command": 'set_short',
        "args": [0x7016, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_set_short_3',
        "command": 'set_short',
        "args": [0x7018, 0x0026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_set_bit_5',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_enable_controls_6',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._160_SUNKEN_SHIP_AREA_01, RadialDirections.SOUTH, 4, 18, 8, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3206_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3206_action_queue_sync_8_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3206_action_queue_sync_8_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3206_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
