from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3710_jmp_if_present_in_current_level_0',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3710_disable_trigger_in_level_1',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3710_set_2',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3710_add_3',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3710_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3710_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
