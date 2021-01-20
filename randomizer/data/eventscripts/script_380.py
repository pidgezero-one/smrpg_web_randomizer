from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_380_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_380_set_1',
        "command": 'set',
        "args": [0x70a9, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_380_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [278],
        "subscript": []
    },
    {
        "identifier": 'EVENT_380_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_380_run_dialog_4',
        "command": 'run_dialog',
        "args": [656, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_380_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
