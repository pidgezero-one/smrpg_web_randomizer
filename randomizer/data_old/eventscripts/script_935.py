
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_935_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 'EVENT_935_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_935_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_935_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_935_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_935_ret_11',
        "command": 'ret'
    }
]
