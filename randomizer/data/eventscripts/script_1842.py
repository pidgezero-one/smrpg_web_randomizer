from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1842_priority_set_0',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_3], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.HALF_INTENSITY]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1842_set_short_1',
        "command": 'set_short',
        "args": [0x701e, 0x0008],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1842_run_background_event_with_pause_return_on_exit_2',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1843, 0x701e, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1842_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [1838],
        "subscript": []
    },
]
