from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3325_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 1023]
    },
    {
        "identifier": 'EVENT_3325_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 1023]
    },
    {
        "identifier": 'EVENT_3325_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 1023]
    },
    {
        "identifier": 'EVENT_3325_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 1023]
    },
    {
        "identifier": 'EVENT_3325_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3325_set_7000_to_current_level_5',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3325_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_7000_equals_short',
        "args": [390, 'EVENT_3325_jmp_if_object_not_in_level_9']
    },
    {
        "identifier": 'EVENT_3325_jmp_if_object_not_in_level_7',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET, 'EVENT_3325_ret_11']
    },
    {
        "identifier": 'EVENT_3325_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3325_run_background_event_10']
    },
    {
        "identifier": 'EVENT_3325_jmp_if_object_not_in_level_9',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET, 'EVENT_3325_ret_11']
    },
    {
        "identifier": 'EVENT_3325_run_background_event_10',
        "command": 'run_background_event',
        "args": [3326, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3325_ret_11',
        "command": 'ret'
    }
]
