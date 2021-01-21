from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1855_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1855_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._105_SURPRISE, 4]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_walk_1_step_south_7',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_set_700C_to_object_coord_8',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_jmp_if_var_not_equals_short_9',
                "command": 'jmp_if_var_not_equals_short',
                "args": [0x700c, 0, 'EVENT_1855_action_queue_async_1_SUBSCRIPT_walk_1_step_south_7']
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_jump_to_height_silent_12',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1855_action_queue_async_1_SUBSCRIPT_jmp_if_mario_in_air_14',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1855_action_queue_async_1_SUBSCRIPT_pause_13']
            }
        ]
    },
    {
        "identifier": 'EVENT_1855_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1830_store_coin_amount_7000_10']
    }
]
