from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3288_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 0, 'EVENT_3289_ret_6']
    },
    {
        "identifier": 'EVENT_3288_set_bit_1',
        "command": 'set_bit',
        "args": [0x707d, 0]
    },
    {
        "identifier": 'EVENT_3288_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3288_action_queue_sync_2_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3288_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3288_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3288_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3288_action_queue_sync_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3288_action_queue_sync_2_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3288_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3288_restore_all_hp_4',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3288_restore_all_fp_5',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3288_set_short_6',
        "command": 'set_short',
        "args": [0x7022, 0x0008]
    },
    {
        "identifier": 'EVENT_3288_run_background_event_with_pause_7',
        "command": 'run_background_event_with_pause',
        "args": [3075, 0x7022, [12, 13]]
    },
    {
        "identifier": 'EVENT_3288_ret_8',
        "command": 'ret'
    }
]
