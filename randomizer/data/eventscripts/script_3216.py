from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3216_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_3216_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3216_disable_trigger_2',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3216_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3216_action_queue_sync_3_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3216_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3216_action_queue_sync_3_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3216_action_queue_sync_3_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3216_add_4',
        "command": 'add',
        "args": [0x70af, 0x01]
    },
    {
        "identifier": 'EVENT_3216_jmp_if_var_equals_byte_5',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 16, 'EVENT_3216_set_action_script_sync_7']
    },
    {
        "identifier": 'EVENT_3216_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3216_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_17, 338]
    },
    {
        "identifier": 'EVENT_3216_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 3, 'EVENT_3216_ret_15']
    },
    {
        "identifier": 'EVENT_3216_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3216_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_3216_add_coins_11',
        "command": 'add_coins',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3216_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3216_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3216_set_bit_14',
        "command": 'set_bit',
        "args": [0x707d, 3]
    },
    {
        "identifier": 'EVENT_3216_ret_15',
        "command": 'ret'
    }
]
