from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_330_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_330_jmp_if_var_equals_byte_10']
    },
    {
        "identifier": 'EVENT_330_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 3, 'EVENT_330_jmp_to_event_20']
    },
    {
        "identifier": 'EVENT_330_inc_2',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'EVENT_330_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'EVENT_330_action_queue_async_6']
    },
    {
        "identifier": 'EVENT_330_run_dialog_4',
        "command": 'run_dialog',
        "args": [568, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_330_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_330_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_330_action_queue_async_6_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_330_run_dialog_7',
        "command": 'run_dialog',
        "args": [569, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_330_set_8',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'EVENT_330_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_330_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 1, 'EVENT_330_run_dialog_4']
    },
    {
        "identifier": 'EVENT_330_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 2, 'EVENT_330_run_dialog_4']
    },
    {
        "identifier": 'EVENT_330_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'EVENT_330_action_queue_async_6']
    },
    {
        "identifier": 'EVENT_330_set_7000_to_object_coord_13',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.F, []]
    },
    {
        "identifier": 'EVENT_330_set_7000_short_mem_to_7000_14',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_330_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_330_action_queue_async_15_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_330_action_queue_async_15_SUBSCRIPT_face_mario_1',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_330_inc_16',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'EVENT_330_run_dialog_17',
        "command": 'run_dialog',
        "args": [568, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_330_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_330_action_queue_async_18_SUBSCRIPT_set_700C_to_7000_short_mem_0',
                "command": 'set_700C_to_7000_short_mem',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_330_action_queue_async_18_SUBSCRIPT_face_east_7C_1',
                "command": 'face_east_7C'
            }
        ]
    },
    {
        "identifier": 'EVENT_330_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_330_jmp_to_event_20',
        "command": 'jmp_to_event',
        "args": [3598]
    }
]
