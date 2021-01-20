from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_20_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_20_disable_trigger_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_20_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [255],
        "subscript": []
    },
    {
        "identifier": 'EVENT_20_disable_trigger_2',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_20_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_20_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x707c, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_20_set_bit_5',
        "command": 'set_bit',
        "args": [0x707c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_20_start_battle_700E_6',
        "command": 'start_battle_700E',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_20_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [25],
        "subscript": []
    },
]
