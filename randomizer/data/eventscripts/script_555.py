from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_555_set_bit_0',
        "command": 'set_bit',
        "args": [0x7060, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_set_1',
        "command": 'set',
        "args": [0x70a7, 115],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_set_short_2',
        "command": 'set_short',
        "args": [0x7000, 0x020c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_pause_5',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_555_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_6_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_555_action_queue_async_6_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_555_action_queue_async_6_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_555_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._095_ROSE_TOWN_DURING_BOWYER_INN_2F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_run_dialog_10',
        "command": 'run_dialog',
        "args": [702, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_12',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_13',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_14',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_15',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_16',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_17',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_18',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_19',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_20',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_stop_sound_21',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_555_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
