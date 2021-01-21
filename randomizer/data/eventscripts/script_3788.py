from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3788_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3788_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3788_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3788_set_7010_to_object_xyz_3',
        "command": 'set_7010_to_object_xyz',
        "args": [0x80]
    },
    {
        "identifier": 'EVENT_3788_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7014, 40, 'EVENT_3788_pause_6']
    },
    {
        "identifier": 'EVENT_3788_jmp_to_event_5',
        "command": 'jmp_to_event',
        "args": [3584]
    },
    {
        "identifier": 'EVENT_3788_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3788_set_7000_to_tapped_button_7',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_3788_jmp_if_7000_any_bits_set_8',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 1, 2, 3], 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3788_jmp_if_7000_any_bits_set_9',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3788_set_7000_to_pressed_button_11']
    },
    {
        "identifier": 'EVENT_3788_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_3788_pause_6']
    },
    {
        "identifier": 'EVENT_3788_set_7000_to_pressed_button_11',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3788_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 1, 2, 3], 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3788_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3788_summon_to_current_level_14',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_3788_summon_to_level_15',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    },
    {
        "identifier": 'EVENT_3788_ret_16',
        "command": 'ret'
    }
]
