from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1113_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7087, 7, 'EVENT_1113_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_1113_run_dialog_1',
        "command": 'run_dialog',
        "args": [2662, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_set_bit_2',
        "command": 'set_bit',
        "args": [0x7087, 7]
    },
    {
        "identifier": 'EVENT_1113_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 6, 'EVENT_1113_run_dialog_33']
    },
    {
        "identifier": 'EVENT_1113_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 5, 'EVENT_1113_jmp_if_bit_clear_13']
    },
    {
        "identifier": 'EVENT_1113_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7051, 4, 'EVENT_1113_jmp_if_bit_clear_9']
    },
    {
        "identifier": 'EVENT_1113_run_dialog_6',
        "command": 'run_dialog',
        "args": [2663, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_run_dialog_7',
        "command": 'run_dialog',
        "args": [2664, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1113_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 4, 'EVENT_1113_run_dialog_31']
    },
    {
        "identifier": 'EVENT_1113_run_dialog_10',
        "command": 'run_dialog',
        "args": [2663, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_run_dialog_11',
        "command": 'run_dialog',
        "args": [2665, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1113_jmp_if_bit_clear_13',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 0, 'EVENT_1113_run_dialog_31']
    },
    {
        "identifier": 'EVENT_1113_run_dialog_14',
        "command": 'run_dialog',
        "args": [2663, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_run_dialog_15',
        "command": 'run_dialog',
        "args": [2668, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_fade_out_music_to_volume_16',
        "command": 'fade_out_music_to_volume',
        "args": [1, 0]
    },
    {
        "identifier": 'EVENT_1113_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1113_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._038_TADPOLE_POND_STAFF_MI, 6]
    },
    {
        "identifier": 'EVENT_1113_pause_19',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1113_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._039_TADPOLE_POND_STAFF_FA, 6]
    },
    {
        "identifier": 'EVENT_1113_pause_21',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1113_play_sound_22',
        "command": 'play_sound',
        "args": [Sounds._040_TADPOLE_POND_STAFF_SO, 6]
    },
    {
        "identifier": 'EVENT_1113_pause_23',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1113_play_sound_24',
        "command": 'play_sound',
        "args": [Sounds._041_TADPOLE_POND_STAFF_LA, 6]
    },
    {
        "identifier": 'EVENT_1113_pause_25',
        "command": 'pause',
        "args": [75]
    },
    {
        "identifier": 'EVENT_1113_play_sound_26',
        "command": 'play_sound',
        "args": [Sounds._037_TADPOLE_POND_STAFF_RE, 6]
    },
    {
        "identifier": 'EVENT_1113_pause_27',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'EVENT_1113_run_dialog_28',
        "command": 'run_dialog',
        "args": [2673, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_fade_out_music_to_volume_29',
        "command": 'fade_out_music_to_volume',
        "args": [3, 100]
    },
    {
        "identifier": 'EVENT_1113_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1113_run_dialog_31',
        "command": 'run_dialog',
        "args": [2660, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1113_run_dialog_33',
        "command": 'run_dialog',
        "args": [2674, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1113_ret_34',
        "command": 'ret'
    }
]
