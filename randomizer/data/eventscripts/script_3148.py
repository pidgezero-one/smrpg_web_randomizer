from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3148_set_bit_0',
        "command": 'set_bit',
        "args": [0x707c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._082_ROSE_WAY_WINDING_PATH_WCROOKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._082_ROSE_WAY_WINDING_PATH_WCROOKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._082_ROSE_WAY_WINDING_PATH_WCROOKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._082_ROSE_WAY_WINDING_PATH_WCROOKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_set_short_5',
        "command": 'set_short',
        "args": [0x7038, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_set_short_6',
        "command": 'set_short',
        "args": [0x703a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_set_short_7',
        "command": 'set_short',
        "args": [0x703c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_set_short_8',
        "command": 'set_short',
        "args": [0x703e, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_jmp_if_object_not_in_level_9',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_7, Rooms._079_ROSE_WAY_MAIN_AREA, 'EVENT_3148_jmp_if_object_not_in_level_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3148_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3148_jmp_if_object_not_in_level_11',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_8, Rooms._079_ROSE_WAY_MAIN_AREA, 'EVENT_3148_jmp_to_event_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3148_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3148_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3148_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    }
]
