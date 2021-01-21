from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3705_start_battle_0',
        "command": 'start_battle',
        "args": [0x0063, 22]
    },
    {
        "identifier": 'EVENT_3705_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3705_set_temp_action_script_sync_7']
    },
    {
        "identifier": 'EVENT_3705_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3705_jmp_to_event_18']
    },
    {
        "identifier": 'EVENT_3705_remove_object_at_70A8_from_current_level_3',
        "command": 'remove_object_at_70A8_from_current_level'
    },
    {
        "identifier": 'EVENT_3705_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3705_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3705_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3705_set_temp_action_script_sync_7',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2]
    },
    {
        "identifier": 'EVENT_3705_set_7000_to_current_level_8',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3705_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 410, 'EVENT_3705_set_temp_action_script_sync_14']
    },
    {
        "identifier": 'EVENT_3705_set_temp_action_script_sync_10',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_5, 2]
    },
    {
        "identifier": 'EVENT_3705_set_temp_action_script_sync_11',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_6, 2]
    },
    {
        "identifier": 'EVENT_3705_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3705_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3705_set_temp_action_script_sync_14',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_6, 2]
    },
    {
        "identifier": 'EVENT_3705_set_temp_action_script_sync_15',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_7, 2]
    },
    {
        "identifier": 'EVENT_3705_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3705_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3705_jmp_to_event_18',
        "command": 'jmp_to_event',
        "args": [287]
    }
]
