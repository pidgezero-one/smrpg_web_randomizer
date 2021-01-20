from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1539_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_freeze_all_npcs_until_return_3',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_resume_action_script_4',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_resume_action_script_5',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 470],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_pause_8',
        "command": 'pause',
        "args": [7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_move_script_to_background_thread_2_9',
        "command": 'move_script_to_background_thread_2',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_10',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_add_coins_11',
        "command": 'add_coins',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_pause_12',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_unfreeze_all_npcs_13',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_move_script_to_main_thread_14',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_jmp_if_var_not_equals_short_16',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 23, 'EVENT_1539_jmp_if_var_not_equals_short_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 468],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_bit_18',
        "command": 'set_bit',
        "args": [0x7077, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_jmp_if_var_not_equals_short_19',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 24, 'EVENT_1539_ret_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 468],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_set_bit_21',
        "command": 'set_bit',
        "args": [0x7077, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1539_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
