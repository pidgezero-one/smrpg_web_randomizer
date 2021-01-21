from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2339_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 7, 'EVENT_2339_ret_6']
    },
    {
        "identifier": 'EVENT_2339_set_bit_1',
        "command": 'set_bit',
        "args": [0x7047, 7]
    },
    {
        "identifier": 'EVENT_2339_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    },
    {
        "identifier": 'EVENT_2339_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    },
    {
        "identifier": 'EVENT_2339_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    },
    {
        "identifier": 'EVENT_2339_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 702]
    },
    {
        "identifier": 'EVENT_2339_ret_6',
        "command": 'ret'
    }
]
