from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_636_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_636_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_636_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_636_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_636_set_short_4',
        "command": 'set_short',
        "args": [0x701c, 0x0014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_636_run_background_event_with_pause_return_on_exit_5',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [637, 0x701c, [13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_636_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
