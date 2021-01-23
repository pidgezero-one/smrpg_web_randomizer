from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_603_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_603_run_dialog_42']
    },
    {
        "identifier": 'EVENT_603_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 5, 'EVENT_603_run_dialog_6']
    },
    {
        "identifier": 'EVENT_603_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_603_run_dialog_44']
    },
    {
        "identifier": 'EVENT_603_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_321_inc_0']
    },
    {
        "identifier": 'EVENT_603_run_dialog_4',
        "command": 'run_dialog',
        "args": [979, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_603_run_dialog_6',
        "command": 'run_dialog',
        "args": [992, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_603_pause_35']
    },
    {
        "identifier": 'EVENT_603_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_603_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_603_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_603_run_dialog_11',
        "command": 'run_dialog',
        "args": [994, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 7, 'EVENT_603_run_dialog_17']
    },
    {
        "identifier": 'EVENT_603_run_dialog_13',
        "command": 'run_dialog',
        "args": [996, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_603_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 322]
    },
    {
        "identifier": 'EVENT_603_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_603_run_dialog_17',
        "command": 'run_dialog',
        "args": [995, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_603_jmp_if_random_above_66_19',
        "command": 'jmp_if_random_above_66',
        "args": [0x7175, 0x7180]
    },
    {
        "identifier": 'EVENT_603_set_20',
        "command": 'set',
        "args": [0x70a7, 97]
    },
    {
        "identifier": 'EVENT_603_jmp_to_subroutine_21',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_603_play_sound_32']
    },
    {
        "identifier": 'EVENT_603_put_inventory_22',
        "command": 'put_inventory',
        "args": [items.MidMushroom]
    },
    {
        "identifier": 'EVENT_603_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_603_set_bit_39']
    },
    {
        "identifier": 'EVENT_603_set_24',
        "command": 'set',
        "args": [0x70a7, 98]
    },
    {
        "identifier": 'EVENT_603_jmp_to_subroutine_25',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_603_play_sound_32']
    },
    {
        "identifier": 'EVENT_603_put_inventory_26',
        "command": 'put_inventory',
        "args": [items.MaxMushroom]
    },
    {
        "identifier": 'EVENT_603_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_603_set_bit_39']
    },
    {
        "identifier": 'EVENT_603_set_28',
        "command": 'set',
        "args": [0x70a7, 102]
    },
    {
        "identifier": 'EVENT_603_jmp_to_subroutine_29',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_603_play_sound_32']
    },
    {
        "identifier": 'EVENT_603_put_inventory_30',
        "command": 'put_inventory',
        "args": [items.PickMeUp]
    },
    {
        "identifier": 'EVENT_603_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_603_set_bit_39']
    },
    {
        "identifier": 'EVENT_603_play_sound_32',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_603_run_dialog_33',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_603_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_603_pause_35',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_603_set_action_script_async_36',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_603_pause_37',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_603_run_dialog_38',
        "command": 'run_dialog',
        "args": [993, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_set_bit_39',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_603_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 322]
    },
    {
        "identifier": 'EVENT_603_ret_41',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_603_run_dialog_42',
        "command": 'run_dialog',
        "args": [1006, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_603_run_dialog_44',
        "command": 'run_dialog',
        "args": [969, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_603_ret_45',
        "command": 'ret'
    }
]
