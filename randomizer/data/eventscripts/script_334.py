from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_334_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 1, 'EVENT_334_summon_to_current_level_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 5, 'EVENT_261_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_summon_to_current_level_2',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_summon_to_current_level_3',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_jmp_to_event_6',
        "command": 'jmp_to_event',
        "args": [261],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_summon_to_current_level_7',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_334_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [261],
        "subscript": []
    }
]
