from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1114_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 1, 'EVENT_1114_ret_4']
    },
    {
        "identifier": 'EVENT_1114_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1114_ret_4']
    },
    {
        "identifier": 'EVENT_1114_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 87]
    },
    {
        "identifier": 'EVENT_1114_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 88]
    },
    {
        "identifier": 'EVENT_1114_ret_4',
        "command": 'ret'
    }
]
