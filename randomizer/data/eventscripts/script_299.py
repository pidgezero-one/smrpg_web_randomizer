from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_299_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_299_set_bit_1',
        "command": 'set_bit',
        "args": [0x7081, 4]
    },
    {
        "identifier": 'EVENT_299_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_299_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_299_action_queue_async_3_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_299_run_dialog_4',
        "command": 'run_dialog',
        "args": [535, AreaObjects.NPC_4, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_299_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_299_action_queue_async_5_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_299_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_299_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [286]
    },
    {
        "identifier": 'EVENT_299_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_299_action_queue_async_7_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_299_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_299_action_queue_async_7_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_298_action_queue_async_8_SUBSCRIPT_pause_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_299_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_299_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_299_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_299_action_queue_async_9_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_299_action_queue_async_9_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_299_action_queue_async_9_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_299_run_dialog_10',
        "command": 'run_dialog',
        "args": [536, AreaObjects.NPC_4, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_299_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_299_action_queue_async_11_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_299_ret_12',
        "command": 'ret'
    }
]
