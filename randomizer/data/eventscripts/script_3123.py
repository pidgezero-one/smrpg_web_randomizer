from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3123_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3123_set_bit_1',
        "command": 'set_bit',
        "args": [0x7055, 1]
    },
    {
        "identifier": 'EVENT_3123_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 56]
    },
    {
        "identifier": 'EVENT_3123_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3123_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3123_action_queue_sync_4_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3123_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3123_action_queue_sync_4_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3123_action_queue_sync_4_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3123_action_queue_sync_4_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3123_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._008_WATERFALL, 4]
    },
    {
        "identifier": 'EVENT_3123_run_dialog_6',
        "command": 'run_dialog',
        "args": [1585, AreaObjects.MARIO, []]
    },
    {
        "identifier": 'EVENT_3123_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3123_apply_solidity_mod_8',
        "command": 'apply_solidity_mod',
        "args": [Rooms._056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3123_apply_solidity_mod_9',
        "command": 'apply_solidity_mod',
        "args": [Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3123_apply_solidity_mod_10',
        "command": 'apply_solidity_mod',
        "args": [Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3123_apply_solidity_mod_11',
        "command": 'apply_solidity_mod',
        "args": [Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3123_apply_solidity_mod_12',
        "command": 'apply_solidity_mod',
        "args": [Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3123_ret_13',
        "command": 'ret'
    }
]
