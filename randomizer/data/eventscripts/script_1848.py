from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1848_jmp_if_316D_is_3_0',
        "command": 'jmp_if_316D_is_3',
        "args": ['EVENT_1848_enable_controls_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_freeze_all_npcs_until_return_1',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_enable_controls_2',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1848_action_queue_async_4_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._089_LIT_FUSE, 4]
            },
            {
                "identifier": 'EVENT_1848_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1848_action_queue_async_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1848_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_create_packet_at_object_coords_jmp_if_null_6',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, AreaObjects.NPC_2, 'EVENT_1848_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1847_action_queue_async_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_enable_controls_10',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_run_background_event_11',
        "command": 'run_background_event',
        "args": [1850, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1848_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
