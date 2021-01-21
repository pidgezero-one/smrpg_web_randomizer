from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_500_move_script_to_background_thread_2_0',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_500_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_500_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_500_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_500_set_7000_to_tapped_button_4',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_500_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_500_ret_14']
    },
    {
        "identifier": 'EVENT_500_jmp_if_7000_any_bits_set_6',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_500_jmp_if_present_in_current_level_9']
    },
    {
        "identifier": 'EVENT_500_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_500_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_500_set_7000_to_tapped_button_4']
    },
    {
        "identifier": 'EVENT_500_jmp_if_present_in_current_level_9',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_7, 'EVENT_500_play_sound_11']
    },
    {
        "identifier": 'EVENT_500_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_500_summon_to_current_level_12']
    },
    {
        "identifier": 'EVENT_500_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_500_summon_to_current_level_12',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_500_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_500_ret_14',
        "command": 'ret'
    }
]
