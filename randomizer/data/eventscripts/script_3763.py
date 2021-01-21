from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3763_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3763_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3763_action_queue_async_1_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x00]
            },
            {
                "identifier": 'EVENT_3763_action_queue_async_1_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x701a, 0x0900]
            },
            {
                "identifier": 'EVENT_3763_action_queue_async_1_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_3763_action_queue_async_1_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3763_fade_in_from_black_sync_2',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3763_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3763_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3763_pause_3']
    },
    {
        "identifier": 'EVENT_3763_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 976]
    },
    {
        "identifier": 'EVENT_3763_pause_6',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_3763_ret_7',
        "command": 'ret'
    }
]
