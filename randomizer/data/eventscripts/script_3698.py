from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3698_start_battle_0',
        "command": 'start_battle',
        "args": [0x0060, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3698_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [1008],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3698_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3698_ret_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3698_stop_all_background_events_3',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3698_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3698_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 814],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3698_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]