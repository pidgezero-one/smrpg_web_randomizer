from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3500_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3500_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3500_jmp_if_bit_clear_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3500_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3500_action_queue_sync_2_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [104]
            }
        ]
    },
    {
        "identifier": 'EVENT_3500_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3500_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3500_jmp_if_bit_clear_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3500_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3500_action_queue_sync_5_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [104]
            }
        ]
    },
    {
        "identifier": 'EVENT_3500_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3500_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_3500_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3500_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3500_action_queue_sync_8_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [104]
            }
        ]
    },
    {
        "identifier": 'EVENT_3500_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3500_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_3500_pause_0'],
        "subscript": []
    }
]
