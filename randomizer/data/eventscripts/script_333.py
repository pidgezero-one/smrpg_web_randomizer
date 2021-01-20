from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_333_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 5, 'EVENT_265_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_333_summon_to_current_level_1',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_333_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_333_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [265],
        "subscript": []
    },
]
