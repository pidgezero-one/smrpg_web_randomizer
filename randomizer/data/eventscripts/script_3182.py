from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3182_set_0',
        "command": 'set',
        "args": [0x70df, 54]
    },
    {
        "identifier": 'EVENT_3182_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_3182_set_bit_3']
    },
    {
        "identifier": 'EVENT_3182_jmp_to_subroutine_2',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3183_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_3182_set_bit_3',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_3182_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3182_action_queue_sync_4_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3182_jmp_to_event_5',
        "command": 'jmp_to_event',
        "args": [15]
    }
]
