from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_723_set_bit_7_offset_0',
        "command": 'set_bit_7_offset',
        "args": [0x0158, []]
    },
    {
        "identifier": 'EVENT_723_set_1',
        "command": 'set',
        "args": [0x70df, 10]
    },
    {
        "identifier": 'EVENT_723_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x709c, 1, 'EVENT_723_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_723_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_723_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 4, 'EVENT_723_jmp_if_bit_set_6']
    },
    {
        "identifier": 'EVENT_723_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL]
    },
    {
        "identifier": 'EVENT_723_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_723_jmp_8']
    },
    {
        "identifier": 'EVENT_723_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [262]
    },
    {
        "identifier": 'EVENT_723_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_723_jmp_if_bit_set_12']
    },
    {
        "identifier": 'EVENT_723_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_723_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_723_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_723_action_queue_async_10_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_723_action_queue_async_10_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_723_jmp_to_event_11',
        "command": 'jmp_to_event',
        "args": [262]
    },
    {
        "identifier": 'EVENT_723_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_262_jmp_if_bit_clear_0']
    },
    {
        "identifier": 'EVENT_723_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_723_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 84, 12, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_723_action_queue_async_13_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 8, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_723_action_queue_async_13_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_723_action_queue_async_13_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_723_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 978]
    },
    {
        "identifier": 'EVENT_723_jmp_to_event_15',
        "command": 'jmp_to_event',
        "args": [262]
    },
    {
        "identifier": 'EVENT_723_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_723_summon_to_level_17',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_723_summon_to_level_18',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_723_remove_from_level_19',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_723_remove_from_level_20',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_723_remove_from_level_21',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_723_remove_from_level_22',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    }
]
