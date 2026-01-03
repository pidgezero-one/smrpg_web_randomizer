
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_1190_current_lvl",
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": "EVENT_1190_room_190_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 190, "EVENT_1190_room_190_logic"]
    },
    {
        "identifier": "EVENT_1190_cancel",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1190_room_190_logic',
        "command": 'start_battle',
        "args": [11, 28]
    },
    {
        "identifier": "EVENT_1190_end",
        "command": 'ret'
    },
]
