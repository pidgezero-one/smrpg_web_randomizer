from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3512_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3512_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3512_set_action_script_async_2',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 365]
    },
    {
        "identifier": 'EVENT_3512_set_3',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3512_add_max_FP_7000_4',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_3512_inc_5',
        "command": 'inc',
        "args": [0x70b1]
    },
    {
        "identifier": 'EVENT_3512_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3512_set_bit_7',
        "command": 'set_bit',
        "args": [0x704e, 2]
    },
    {
        "identifier": 'EVENT_3512_ret_8',
        "command": 'ret'
    }
]
