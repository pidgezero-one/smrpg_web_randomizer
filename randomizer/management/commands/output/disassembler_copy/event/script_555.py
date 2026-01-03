
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_555_set_bit_0',
        "command": 'set_bit',
        "args": [0x7060, 3]
    },
    {
        "identifier": 'EVENT_555_run_dialog_1',
        "command": 'run_dialog',
        "args": [819, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_555_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_555_set_3',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_555_run_dialog_4',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_555_put_inventory_5',
        "command": 'put_inventory',
        "args": [items.FlowerTab]
    },
    {
        "identifier": 'EVENT_555_pause_6',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_555_run_dialog_7',
        "command": 'run_dialog',
        "args": [832, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_555_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 636]
    },
    {
        "identifier": 'EVENT_555_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_555_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_555_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_10_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_10_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_555_action_queue_async_10_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_555_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_555_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._095_ROSE_TOWN_DURING_BOWYER_INN_2F]
    },
    {
        "identifier": 'EVENT_555_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_555_run_dialog_14',
        "command": 'run_dialog',
        "args": [702, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_555_ret_15',
        "command": 'ret'
    }
]
