
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1931_start_battle_350',
        "command": 'start_battle',
        "args": [0x009e, 21]
    },
    {
        "identifier": 'EVENT_1931_jmp_if_bit_set_351',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1931_reset_and_choose_game_366']
    },
    {
        "identifier": 'EVENT_1931_ret_',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1931_reset_and_choose_game_366',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1931_ret',
        "command": 'ret'
    },
]
