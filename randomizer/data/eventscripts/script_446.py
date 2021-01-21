from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_446_dec_short_0',
        "command": 'dec_short',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_446_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 10, 'EVENT_446_set_short_mem_23']
    },
    {
        "identifier": 'EVENT_446_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 0, 'EVENT_446_run_dialog_6']
    },
    {
        "identifier": 'EVENT_446_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_446_run_dialog_4',
        "command": 'run_dialog',
        "args": [835, AreaObjects.MARIO, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_446_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_446_set_short_20']
    },
    {
        "identifier": 'EVENT_446_run_dialog_6',
        "command": 'run_dialog',
        "args": [866, AreaObjects.MARIO, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_446_stop_all_background_events_7',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_446_db_8',
        "command": 'db',
        "args": [0xfd, 0x44]
    },
    {
        "identifier": 'EVENT_446_unfreeze_camera_9',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_446_fade_out_music_to_volume_10',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_446_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_446_set_bit_12',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_446_enable_controls_13',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_446_set_bit_14',
        "command": 'set_bit',
        "args": [0x7083, 7]
    },
    {
        "identifier": 'EVENT_446_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_446_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_446_jmp_if_mario_in_air_17',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_446_pause_16']
    },
    {
        "identifier": 'EVENT_446_play_music_default_volume_18',
        "command": 'play_music_default_volume',
        "args": [Music._07_PIPE_VAULT]
    },
    {
        "identifier": 'EVENT_446_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_446_set_short_20',
        "command": 'set_short',
        "args": [0x701c, 0x0050]
    },
    {
        "identifier": 'EVENT_446_run_background_event_with_pause_return_on_exit_21',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [446, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_446_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_446_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_446_mem_compare_24',
        "command": 'mem_compare',
        "args": [0x7000, 20]
    },
    {
        "identifier": 'EVENT_446_jmp_if_comparison_result_is_greater_or_equal_25',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_446_set_bit_27']
    },
    {
        "identifier": 'EVENT_446_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_446_jmp_if_var_equals_short_2']
    },
    {
        "identifier": 'EVENT_446_set_bit_27',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_446_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_446_jmp_if_var_equals_short_2']
    }
]
