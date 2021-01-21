from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1866_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7095, 3, 'EVENT_1866_ret_11']
    },
    {
        "identifier": 'EVENT_1866_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7095, 2, 'EVENT_1866_ret_11']
    },
    {
        "identifier": 'EVENT_1866_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1866_action_queue_async_2_SUBSCRIPT_shift_f_direction_pixels_0',
                "command": 'shift_f_direction_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1866_action_queue_async_2_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1866_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1866_action_queue_async_3_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1866_action_queue_async_3_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1866_action_queue_async_3_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1866_action_queue_async_3_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1866_action_queue_async_3_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1866_pause_4',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1866_run_dialog_5',
        "command": 'run_dialog',
        "args": [1281, AreaObjects.BOWSER, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1866_pause_6',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'EVENT_1866_close_dialog_7',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1866_fade_out_to_black_async_duration_8',
        "command": 'fade_out_to_black_async_duration',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1866_set_bit_9',
        "command": 'set_bit',
        "args": [0x7095, 3]
    },
    {
        "identifier": 'EVENT_1866_enter_area_10',
        "command": 'enter_area',
        "args": [Rooms._266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, RadialDirections.SOUTHWEST, 25, 95, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1866_ret_11',
        "command": 'ret'
    }
]
