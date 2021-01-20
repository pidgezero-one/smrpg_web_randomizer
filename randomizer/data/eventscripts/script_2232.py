from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2232_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2232_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2232_pause_2',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2232_priority_set_3',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_3], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.BACKGROUND, _0x81Flags.HALF_INTENSITY]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2232_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
