
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_379_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 0, 'EVENT_379_run_dialog_16']
    },
    {
        "identifier": 'EVENT_379_set_bit_1',
        "command": 'set_bit',
        "args": [0x7083, 0]
    },
    {
        "identifier": 'EVENT_379_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_3_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_3_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_379_action_queue_async_4_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [27, 49]
            },
            {
                "identifier": 'EVENT_379_action_queue_async_4_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_4_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_run_dialog_5',
        "command": 'run_dialog',
        "args": [2559, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_6_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_7_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_7_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_8_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_379_run_dialog_9',
        "command": 'run_dialog',
        "args": [654, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_379_set_10',
        "command": 'set',
        "args": [0x70a7, 85]
    },
    {
        "identifier": 'EVENT_379_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_379_run_dialog_12',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_379_put_inventory_13',
        "command": 'put_inventory',
        "args": [items.WakeUpPin]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_14_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_379_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_379_run_dialog_16',
        "command": 'run_dialog',
        "args": [655, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_379_ret_17',
        "command": 'ret'
    }
]
