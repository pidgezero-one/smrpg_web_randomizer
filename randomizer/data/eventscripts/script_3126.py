from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3126_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 7, 'EVENT_3126_jmp_to_event_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_set_short_1',
        "command": 'set_short',
        "args": [0x700e, 0x009d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [35],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7064, 5, 'EVENT_3126_ret_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_set_bit_4',
        "command": 'set_bit',
        "args": [0x7057, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_set_short_6',
        "command": 'set_short',
        "args": [0x700a, 0x00d4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_stop_sound_8',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_stop_sound_9',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3126_jmp_to_event_11',
        "command": 'jmp_to_event',
        "args": [34],
        "subscript": []
    }
]
