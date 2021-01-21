from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_255_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_255_start_embedded_action_script_async_1',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_255_start_embedded_action_script_async_1_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [0, 1]]
            },
            {
                "identifier": 'EVENT_255_start_embedded_action_script_async_1_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_255_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 1022]
    },
    {
        "identifier": 'EVENT_255_inc_exp_by_packet_3',
        "command": 'inc_exp_by_packet'
    },
    {
        "identifier": 'EVENT_255_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_255_ret_13']
    },
    {
        "identifier": 'EVENT_255_set_bit_5',
        "command": 'set_bit',
        "args": [0x7064, 4]
    },
    {
        "identifier": 'EVENT_255_set_bit_6',
        "command": 'set_bit',
        "args": [0x707c, 3]
    },
    {
        "identifier": 'EVENT_255_unfreeze_all_npcs_7',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_255_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_255_create_packet_at_object_coords_jmp_if_null_9',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._031_LEVELUP_TEXT, AreaObjects.MARIO, 'EVENT_255_set_bit_5']
    },
    {
        "identifier": 'EVENT_255_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._095_LEVEL_UP_WITH_STAR, 6]
    },
    {
        "identifier": 'EVENT_255_set_short_11',
        "command": 'set_short',
        "args": [0x701e, 0x0040]
    },
    {
        "identifier": 'EVENT_255_run_background_event_with_pause_return_on_exit_12',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [254, 0x701e, [12, 13]]
    },
    {
        "identifier": 'EVENT_255_ret_13',
        "command": 'ret'
    }
]
