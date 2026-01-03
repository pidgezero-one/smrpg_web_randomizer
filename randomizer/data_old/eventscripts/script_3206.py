
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3206_set_short_2',
        "command": "set_var_to_const",
        "args": [0x7016, 0x0004]
    },
    {
        "identifier": 'EVENT_3206_set_short_3',
        "command": "set_var_to_const",
        "args": [0x7018, 0x0026]
    },
    {
        "identifier": 'EVENT_3206_set_bit_40',
        "command": 'set_bit',
        "args": [0x7067, 5]
    },
    {
        "identifier": 'EVENT_3206_set_bit_40_',
        "command": 'set_bit',
        "args": [0x706F, 4]
    },
    {
        "identifier": 'EVENT_3206_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [66]
    },
    {
        "identifier": 'EVENT_3206_set_bit_5',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_3206_enable_controls_6',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3206_clear_bit_0',
        "command": 'set_bit',
        "args": [0x7087, 0]
    },
    {
        "identifier": 'EVENT_3206_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._160_SUNKEN_SHIP_AREA_01, RadialDirections.SOUTH, 4, 18, 8, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3206_action_queue_sync_8',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_3206_action_queue_sync_8_SUBSCRIPT_face_south_0',
                "command": 'face_south'
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
        "command": 'ret'
    }
]
