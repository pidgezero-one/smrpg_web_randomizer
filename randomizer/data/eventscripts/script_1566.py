from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1566_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1566_ret_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 818],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_pause_2',
        "command": 'pause',
        "args": [9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 818],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_pause_4',
        "command": 'pause',
        "args": [9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 818],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_pause_7',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_1566_pause_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_pause_9',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1566_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
