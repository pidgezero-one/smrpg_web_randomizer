from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3680_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 5, 'EVENT_3680_run_dialog_35']
    },
    {
        "identifier": 'EVENT_3680_start_battle_1',
        "command": 'start_battle',
        "args": [0x00af, 23]
    },
    {
        "identifier": 'EVENT_3680_set_bit_2',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_3680_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [1011]
    },
    {
        "identifier": 'EVENT_3680_set_bit_4',
        "command": 'set_bit',
        "args": [0x705f, 5]
    },
    {
        "identifier": 'EVENT_3680_restore_all_hp_5',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3680_restore_all_fp_6',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3680_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3680_set_short_8',
        "command": 'set_short',
        "args": [0x700a, 0x00dc]
    },
    {
        "identifier": 'EVENT_3680_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [720]
    },
    {
        "identifier": 'EVENT_3680_jmp_to_event_10',
        "command": 'jmp_to_event',
        "args": [560]
    },
    {
        "identifier": 'EVENT_3680_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3680_run_dialog_12',
        "command": 'run_dialog',
        "args": [50, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3680_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_17',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_22',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_28',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3680_run_dialog_35',
        "command": 'run_dialog',
        "args": [49, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3680_ret_36',
        "command": 'ret'
    }
]
