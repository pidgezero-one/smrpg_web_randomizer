from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1394_jmp_if_var_equals_short_0',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71f0, 200, 'EVENT_1394_set_short_mem_6']
    },
    {
        "identifier": 'EVENT_1394_store_coin_amount_7000_1',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1394_dec_coins_2',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1394_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x700a, 0x7000]
    },
    {
        "identifier": 'EVENT_1394_set_short_4',
        "command": 'set_short',
        "args": [0x71f0, 0x00c8]
    },
    {
        "identifier": 'EVENT_1394_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1394_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x700a]
    },
    {
        "identifier": 'EVENT_1394_add_coins_7',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1394_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_17',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_22',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1394_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1394_pause_25',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1394_pause_script_resume_on_next_dialog_page_a_FD61_26',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1394_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1394_action_queue_async_27_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_27_SUBSCRIPT_face_southwest_7D_1',
                "command": 'face_southwest_7D',
                "args": [0x00]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_27_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_1394_pause_script_resume_on_next_dialog_page_a_FD61_28',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1394_unsync_dialog_29',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1394_close_dialog_30',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1394_reset_coords_31',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1394_pause_32',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1394_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 146]
    },
    {
        "identifier": 'EVENT_1394_set_bit_34',
        "command": 'set_bit',
        "args": [0x7053, 0]
    },
    {
        "identifier": 'EVENT_1394_set_bit_35',
        "command": 'set_bit',
        "args": [0x7065, 0]
    },
    {
        "identifier": 'EVENT_1394_set_bit_36',
        "command": 'set_bit',
        "args": [0x706d, 1]
    },
    {
        "identifier": 'EVENT_1394_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1394_run_dialog_38',
        "command": 'run_dialog',
        "args": [2762, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1394_ret_39',
        "command": 'ret'
    }
]
