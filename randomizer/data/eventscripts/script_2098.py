from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2098_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_2098_ret_6']
    },
    {
        "identifier": 'EVENT_2098_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_2098_set_action_script_sync_4']
    },
    {
        "identifier": 'EVENT_2098_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 864]
    },
    {
        "identifier": 'EVENT_2098_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2098_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 869]
    },
    {
        "identifier": 'EVENT_2098_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2098_ret_6',
        "command": 'ret'
    }
]
