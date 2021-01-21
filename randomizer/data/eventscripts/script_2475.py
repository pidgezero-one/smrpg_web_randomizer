from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2475_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._159_STAR_HILL_AREA_04, 'EVENT_2475_remove_from_level_2']
    },
    {
        "identifier": 'EVENT_2475_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2475_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._159_STAR_HILL_AREA_04]
    },
    {
        "identifier": 'EVENT_2475_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 756]
    },
    {
        "identifier": 'EVENT_2475_ret_4',
        "command": 'ret'
    }
]
