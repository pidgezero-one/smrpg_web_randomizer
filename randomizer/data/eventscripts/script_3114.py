from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3114_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3114_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3114_run_dialog_2',
        "command": 'run_dialog',
        "args": [1576, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3114_jmp_if_dialog_option_b_3',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3088_pause_action_script_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3114_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [3864],
        "subscript": []
    },
]
