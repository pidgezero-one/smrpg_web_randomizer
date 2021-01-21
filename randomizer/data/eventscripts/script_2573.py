from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2573_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2573_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2573_summon_to_current_level_2',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2573_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 14]
    },
    {
        "identifier": 'EVENT_2573_summon_to_current_level_4',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2573_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 398]
    },
    {
        "identifier": 'EVENT_2573_ret_6',
        "command": 'ret'
    }
]
