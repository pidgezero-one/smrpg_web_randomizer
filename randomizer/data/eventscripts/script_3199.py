from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3199_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 6, 'EVENT_3199_ret_5']
    },
    {
        "identifier": 'EVENT_3199_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_3199_add_frog_coins_2',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3199_set_bit_3',
        "command": 'set_bit',
        "args": [0x7057, 6]
    },
    {
        "identifier": 'EVENT_3199_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3199_action_queue_sync_4_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3199_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3199_action_queue_sync_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3199_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3199_action_queue_sync_4_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3199_action_queue_sync_4_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3199_action_queue_sync_4_SUBSCRIPT_ret_6',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3199_ret_5',
        "command": 'ret'
    }
]
