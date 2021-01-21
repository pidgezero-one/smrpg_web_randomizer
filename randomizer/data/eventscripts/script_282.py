from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_282_set_bit_0',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_282_move_script_to_background_thread_2_1',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_282_enable_controls_2',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_282_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_282_action_queue_async_3_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x00]
            },
            {
                "identifier": 'EVENT_282_action_queue_async_3_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x701a, 0x0900]
            },
            {
                "identifier": 'EVENT_282_action_queue_async_3_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_282_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_282_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 3, 'EVENT_282_clear_bit_6']
    },
    {
        "identifier": 'EVENT_282_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_282_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x709c, 3]
    },
    {
        "identifier": 'EVENT_282_ret_7',
        "command": 'ret'
    }
]
