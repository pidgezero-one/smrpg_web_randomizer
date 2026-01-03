
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_555_rlo__0',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_555_set_bit_0',
        "command": 'set_bit',
        "args": [0x7060, 3]
    },
    {
        "identifier": 'EVENT_555_grant',
        "command": 'run_event_as_subroutine',
        "args": [178]
    },
    {
        "identifier": 'EVENT_555_set_action_script_async_4',
        "command": 'set_action_script',
        'args': [AreaObjects.MEM_70A8, False, 636]
    },
    {
        "identifier": 'EVENT_555_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_555_action_queue_async_6',
        "command": 'action_queue',
        'args': [AreaObjects.MEM_70A8, False],
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
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_555_action_queue_async_6_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_555_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_555_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._095_ROSE_TOWN_DURING_BOWYER_INN_2F]
    },
    {
        "identifier": 'EVENT_555_remove_from_level_8_',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._096_ROSE_TOWN_INN_2F]
    },
    {
        "identifier": 'EVENT_555_ret_9',
        "command": 'ret'
    }
]
