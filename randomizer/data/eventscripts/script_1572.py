from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1572_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1572_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1572_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 470]
    },
    {
        "identifier": 'EVENT_1572_add_short_3',
        "command": 'add_short',
        "args": [0x702a, 0x01]
    },
    {
        "identifier": 'EVENT_1572_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1572_ret_5',
        "command": 'ret'
    }
]
