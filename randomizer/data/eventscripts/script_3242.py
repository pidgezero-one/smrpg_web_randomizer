from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3242_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3242_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 340]
    },
    {
        "identifier": 'EVENT_3242_run_dialog_2',
        "command": 'run_dialog',
        "args": [1666, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3242_run_background_event_3',
        "command": 'run_background_event',
        "args": [3212, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3242_run_dialog_4',
        "command": 'run_dialog',
        "args": [1657, AreaObjects.BOWSER, []]
    },
    {
        "identifier": 'EVENT_3242_ret_5',
        "command": 'ret'
    }
]
