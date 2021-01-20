from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1734_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_1734_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_set_2',
        "command": 'set',
        "args": [0x70ab, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_jmp_if_present_in_current_level_4',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70AB, 'EVENT_1734_set_action_script_sync_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_resume_action_script_5',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70AB],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_1734_add_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 770],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_add_8',
        "command": 'add',
        "args": [0x70ab, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_end_loop_9',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_pause_10',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1734_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_1734_set_2'],
        "subscript": []
    }
]
