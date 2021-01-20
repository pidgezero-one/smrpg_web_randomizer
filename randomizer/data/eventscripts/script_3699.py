from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3699_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3699_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3699_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3699_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 814],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3699_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]