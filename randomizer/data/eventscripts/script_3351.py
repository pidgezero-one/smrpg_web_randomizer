from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3351_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, RadialDirections.SOUTHWEST, 7, 33, 0, []]
    },
    {
        "identifier": 'EVENT_3351_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b7]
    },
    {
        "identifier": 'EVENT_3351_mem_7000_shift_left_2',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3351_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7000]
    },
    {
        "identifier": 'EVENT_3351_add_short_4',
        "command": 'add_short',
        "args": [0x7016, 0x0003]
    },
    {
        "identifier": 'EVENT_3351_mem_7000_shift_left_5',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 255]
    },
    {
        "identifier": 'EVENT_3351_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7018, 0x7000]
    },
    {
        "identifier": 'EVENT_3351_add_short_7',
        "command": 'add_short',
        "args": [0x7018, 0x0019]
    },
    {
        "identifier": 'EVENT_3351_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3351_action_queue_sync_8_SUBSCRIPT_run_away_transfer_0',
                "command": 'run_away_transfer'
            }
        ]
    },
    {
        "identifier": 'EVENT_3351_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [3376]
    }
]
