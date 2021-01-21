from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1743_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1743_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_1743_jmp_if_bit_clear_4']
    },
    {
        "identifier": 'EVENT_1743_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1743_action_queue_sync_2_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [104]
            }
        ]
    },
    {
        "identifier": 'EVENT_1743_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1743_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_1743_jmp_if_bit_clear_7']
    },
    {
        "identifier": 'EVENT_1743_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1743_action_queue_sync_5_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [104]
            }
        ]
    },
    {
        "identifier": 'EVENT_1743_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1743_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_1743_jmp_if_bit_clear_10']
    },
    {
        "identifier": 'EVENT_1743_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1743_action_queue_sync_8_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [104]
            }
        ]
    },
    {
        "identifier": 'EVENT_1743_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1743_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1743_pause_0']
    },
    {
        "identifier": 'EVENT_1743_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1743_action_queue_sync_11_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_1743_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1743_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_1743_pause_0']
    }
]
