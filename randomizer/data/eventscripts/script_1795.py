from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1795_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x704f, 7, 'EVENT_1795_jmp_if_bit_clear_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_summon_to_current_level_4',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_18, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 1, 'EVENT_1795_run_event_as_subroutine_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_summon_to_current_level_8',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_19, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1795_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
