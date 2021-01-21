from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1689_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x1d10]
    },
    {
        "identifier": 'EVENT_1689_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [66]
    },
    {
        "identifier": 'EVENT_1689_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, RadialDirections.SOUTH, 4, 43, 9, []]
    },
    {
        "identifier": 'EVENT_1689_set_bit_3',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_1689_enable_controls_4',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1689_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1689_action_queue_sync_5_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1689_jmp_to_event_6',
        "command": 'jmp_to_event',
        "args": [1771]
    }
]
