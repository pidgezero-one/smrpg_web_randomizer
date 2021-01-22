from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1585_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1585_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1585_pause_0']
    },
    {
        "identifier": 'EVENT_1585_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1585_set_7']
    },
    {
        "identifier": 'EVENT_1585_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_1585_set_22']
    },
    {
        "identifier": 'EVENT_1585_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1585_set_37']
    },
    {
        "identifier": 'EVENT_1585_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_1585_set_52']
    },
    {
        "identifier": 'EVENT_1585_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_1585_pause_0']
    },
    {
        "identifier": 'EVENT_1585_set_7',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_1585_set_short_8',
        "command": 'set_short',
        "args": [0x7016, 0x071c]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_9',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_10',
        "command": 'set_short',
        "args": [0x7016, 0x0520]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_11',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_12',
        "command": 'set_short',
        "args": [0x7016, 0x0622]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_14',
        "command": 'set_short',
        "args": [0x7016, 0x0426]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_15',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_16',
        "command": 'set_short',
        "args": [0x7016, 0x022a]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_18',
        "command": 'set_short',
        "args": [0x7016, 0x002e]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_19',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1585_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_1585_pause_0']
    },
    {
        "identifier": 'EVENT_1585_set_22',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_1585_set_short_23',
        "command": 'set_short',
        "args": [0x7016, 0x183a]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_24',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_25',
        "command": 'set_short',
        "args": [0x7016, 0x193c]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_26',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_27',
        "command": 'set_short',
        "args": [0x7016, 0x1740]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_28',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_29',
        "command": 'set_short',
        "args": [0x7016, 0x1544]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_30',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_31',
        "command": 'set_short',
        "args": [0x7016, 0x1246]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_32',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_33',
        "command": 'set_short',
        "args": [0x7016, 0x1348]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_34',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_clear_bit_35',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1585_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_1585_pause_0']
    },
    {
        "identifier": 'EVENT_1585_set_37',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_1585_set_short_38',
        "command": 'set_short',
        "args": [0x7016, 0x0a56]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_39',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_40',
        "command": 'set_short',
        "args": [0x7016, 0x0b58]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_41',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_42',
        "command": 'set_short',
        "args": [0x7016, 0x095c]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_43',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_44',
        "command": 'set_short',
        "args": [0x7016, 0x065e]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_45',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_46',
        "command": 'set_short',
        "args": [0x7016, 0x0760]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_47',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_48',
        "command": 'set_short',
        "args": [0x7016, 0x0564]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_49',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_clear_bit_50',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1585_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_1585_pause_0']
    },
    {
        "identifier": 'EVENT_1585_set_52',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_1585_set_short_53',
        "command": 'set_short',
        "args": [0x7016, 0x1b74]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_54',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_55',
        "command": 'set_short',
        "args": [0x7016, 0x1c76]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_56',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_57',
        "command": 'set_short',
        "args": [0x7016, 0x1978]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_58',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_59',
        "command": 'set_short',
        "args": [0x7016, 0x1a7a]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_60',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_61',
        "command": 'set_short',
        "args": [0x7016, 0x177c]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_62',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_set_short_63',
        "command": 'set_short',
        "args": [0x7016, 0x1580]
    },
    {
        "identifier": 'EVENT_1585_jmp_to_subroutine_64',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1585_set_short_mem_67']
    },
    {
        "identifier": 'EVENT_1585_clear_bit_65',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1585_jmp_66',
        "command": 'jmp',
        "args": ['EVENT_1585_pause_0']
    },
    {
        "identifier": 'EVENT_1585_set_short_mem_67',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7018]
    },
    {
        "identifier": 'EVENT_1585_mem_7000_shift_left_68',
        "command": 'mem_7000_shift_left',
        "args": [0x7016, 8]
    },
    {
        "identifier": 'EVENT_1585_set_short_69',
        "command": 'set_short',
        "args": [0x701a, 0x000a]
    },
    {
        "identifier": 'EVENT_1585_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_1585_action_queue_async_70_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x9a]
            },
            {
                "identifier": 'EVENT_1585_action_queue_async_70_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1585_action_queue_async_70_SUBSCRIPT_object_memory_clear_bit_2',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1585_set_action_script_sync_71',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 163]
    },
    {
        "identifier": 'EVENT_1585_add_72',
        "command": 'add',
        "args": [0x70ab, 0x01]
    },
    {
        "identifier": 'EVENT_1585_pause_73',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1585_ret_74',
        "command": 'ret'
    }
]
