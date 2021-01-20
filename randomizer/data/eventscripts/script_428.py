from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_428_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x707c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_428_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_3, Rooms._127_PIPE_VAULT_AREA_02, 'EVENT_428_run_background_event_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_428_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._127_PIPE_VAULT_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_428_summon_to_current_level_3',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_428_run_background_event_4',
        "command": 'run_background_event',
        "args": [429, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_428_run_background_event_5',
        "command": 'run_background_event',
        "args": [505, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_428_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_428_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
