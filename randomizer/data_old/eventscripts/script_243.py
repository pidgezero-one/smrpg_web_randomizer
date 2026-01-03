
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_243_room_81_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 81, "EVENT_243_room_81_logic"]
    },
    {
        "identifier": "EVENT_243_room_144_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 144, "EVENT_243_room_144_446_logic"]
    },
    {
        "identifier": "EVENT_243_room_234_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 234, "EVENT_243_room_234_logic"]
    },
    {
        "identifier": "EVENT_243_room_446_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 446, "EVENT_243_room_144_446_logic"]
    },
    {
        "identifier": "EVENT_243_room_455_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 455, "EVENT_243_room_455_logic"]
    },
    {
        "identifier": "EVENT_243_room_457_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 457, "EVENT_243_room_457_logic"]
    },
    {
        "identifier": "EVENT_243_cancel",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_243_room_81_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_243_room_81_logic_2",
        "command": 'jmp_to_event',
        "args": [3404]
    },
    {
        "identifier": "EVENT_243_room_144_446_logic",
        "command": "set_var_to_const",
        "args": [0x70A7, 131]
    },
    {
        "identifier": "EVENT_243_room_144_446_logic_2",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_243_room_234_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_243_room_455_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_243_room_457_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
]
