from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1542_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1542_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1542_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 4, 'EVENT_1542_end_all_6']
    },
    {
        "identifier": 'EVENT_1542_set_7000_to_pressed_button_3',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1542_jmp_if_var_not_equals_short_4',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 4, 'EVENT_1542_end_all_6']
    },
    {
        "identifier": 'EVENT_1542_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1542_end_all_6',
        "command": 'end_all'
    }
]
