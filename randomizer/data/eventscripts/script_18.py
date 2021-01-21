from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_18_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_18_disable_trigger_2']
    },
    {
        "identifier": 'EVENT_18_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [255]
    },
    {
        "identifier": 'EVENT_18_disable_trigger_2',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_18_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_18_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_18_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_18_start_battle_700E_6',
        "command": 'start_battle_700E'
    },
    {
        "identifier": 'EVENT_18_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [24]
    }
]
