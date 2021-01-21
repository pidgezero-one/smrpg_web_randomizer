from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1732_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1732_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_1732_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1732_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 47]
    },
    {
        "identifier": 'EVENT_1732_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_1732_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_1732_pause_4']
    },
    {
        "identifier": 'EVENT_1732_jmp_if_present_in_current_level_6',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_12, 'EVENT_1732_set_object_memory_to_8']
    },
    {
        "identifier": 'EVENT_1732_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_1732_pause_4']
    },
    {
        "identifier": 'EVENT_1732_set_object_memory_to_8',
        "command": 'set_object_memory_to',
        "args": [0x702c]
    },
    {
        "identifier": 'EVENT_1732_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1732_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_12, 47]
    },
    {
        "identifier": 'EVENT_1732_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_1732_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_1732_pause_13']
    },
    {
        "identifier": 'EVENT_1732_jmp_if_present_in_current_level_15',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_13, 'EVENT_1732_set_object_memory_to_17']
    },
    {
        "identifier": 'EVENT_1732_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1732_pause_13']
    },
    {
        "identifier": 'EVENT_1732_set_object_memory_to_17',
        "command": 'set_object_memory_to',
        "args": [0x702c]
    },
    {
        "identifier": 'EVENT_1732_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_end_loop_19',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1732_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_13, 47]
    },
    {
        "identifier": 'EVENT_1732_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_1732_pause_22',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_1732_pause_22']
    },
    {
        "identifier": 'EVENT_1732_jmp_if_present_in_current_level_24',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_14, 'EVENT_1732_set_object_memory_to_26']
    },
    {
        "identifier": 'EVENT_1732_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_1732_pause_22']
    },
    {
        "identifier": 'EVENT_1732_set_object_memory_to_26',
        "command": 'set_object_memory_to',
        "args": [0x702c]
    },
    {
        "identifier": 'EVENT_1732_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_end_loop_28',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1732_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_14, 47]
    },
    {
        "identifier": 'EVENT_1732_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_1732_pause_31',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_jmp_if_bit_clear_32',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_1732_pause_31']
    },
    {
        "identifier": 'EVENT_1732_jmp_if_present_in_current_level_33',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_11, 'EVENT_1732_action_queue_async_35']
    },
    {
        "identifier": 'EVENT_1732_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_1732_pause_31']
    },
    {
        "identifier": 'EVENT_1732_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_1732_action_queue_async_35_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1732_clear_bit_36',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1732_set_object_memory_to_37',
        "command": 'set_object_memory_to',
        "args": [0x702c]
    },
    {
        "identifier": 'EVENT_1732_pause_38',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_end_loop_39',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1732_pause_40',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1732_pause_41',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1732_jmp_if_bit_set_42',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1732_pause_41']
    },
    {
        "identifier": 'EVENT_1732_jmp_43',
        "command": 'jmp',
        "args": ['EVENT_1732_set_bit_0']
    }
]
