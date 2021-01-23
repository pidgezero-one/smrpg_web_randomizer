from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1719_set_0',
        "command": 'set',
        "args": [0x70ab, 24]
    },
    {
        "identifier": 'EVENT_1719_set_1',
        "command": 'set',
        "args": [0x70a9, 20]
    },
    {
        "identifier": 'EVENT_1719_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1719_summon_to_current_level_3',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MEM_70A9]
    },
    {
        "identifier": 'EVENT_1719_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 366]
    },
    {
        "identifier": 'EVENT_1719_inc_5',
        "command": 'inc',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_1719_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1719_run_background_event_7',
        "command": 'run_background_event',
        "args": [1721, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1719_ret_8',
        "command": 'ret'
    }
]
