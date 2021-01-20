from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3716_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_3716_set_bit_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [3716],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 6, 'EVENT_3716_set_action_script_sync_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_3716_pause_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 814],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3716_jmp_to_event_10',
        "command": 'jmp_to_event',
        "args": [3716],
        "subscript": []
    }
]
