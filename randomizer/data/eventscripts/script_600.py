from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_600_set_bit_7_offset_0',
        "command": 'set_bit_7_offset',
        "args": [0x015e]
    },
    {
        "identifier": 'EVENT_600_set_bit_7_offset_1',
        "command": 'set_bit_7_offset',
        "args": [0x0160]
    },
    {
        "identifier": 'EVENT_600_set_bit_7_offset_2',
        "command": 'set_bit_7_offset',
        "args": [0x0162]
    },
    {
        "identifier": 'EVENT_600_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_600_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_14, Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_600_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14]
    },
    {
        "identifier": 'EVENT_600_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_600_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_6_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_6_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_600_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_600_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_7_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_7_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_600_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_600_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_8_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_8_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_600_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_600_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_9_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_600_action_queue_sync_9_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_600_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_600_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_600_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_600_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_600_ret_12',
        "command": 'ret'
    }
]
