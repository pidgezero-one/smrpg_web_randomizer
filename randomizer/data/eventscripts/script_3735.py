from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3735_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3735_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3735_apply_tile_mod_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3735_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [3735],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3735_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3735_apply_solidity_mod_4',
        "command": 'apply_solidity_mod',
        "args": [Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3735_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
