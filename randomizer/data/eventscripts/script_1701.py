from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1701_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1701_ret_19']
    },
    {
        "identifier": 'EVENT_1701_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_1701_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1701_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1701_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1701_pause_action_script_9']
    },
    {
        "identifier": 'EVENT_1701_set_bit_5',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1701_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1701_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1701_run_background_event_8',
        "command": 'run_background_event',
        "args": [1705, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1701_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1701_set_7000_to_7000_short_mem_10',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_1701_mem_compare_val_11',
        "command": 'mem_compare_val',
        "args": [27]
    },
    {
        "identifier": 'EVENT_1701_jmp_if_loaded_memory_is_not_0_12',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_1701_set_14']
    },
    {
        "identifier": 'EVENT_1701_add_short_13',
        "command": 'add_short',
        "args": [0x7024, 0x0080]
    },
    {
        "identifier": 'EVENT_1701_set_14',
        "command": 'set',
        "args": [0x70a9, 27]
    },
    {
        "identifier": 'EVENT_1701_set_short_15',
        "command": 'set_short',
        "args": [0x703e, 0x001b]
    },
    {
        "identifier": 'EVENT_1701_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 478]
    },
    {
        "identifier": 'EVENT_1701_pause_17',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'EVENT_1701_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 477]
    },
    {
        "identifier": 'EVENT_1701_ret_19',
        "command": 'ret'
    }
]
