from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3077_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3077_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3077_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3077_move_script_to_background_thread_2_3',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_3077_enable_controls_until_return_4',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3077_restore_all_hp_5',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3077_restore_all_fp_6',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3077_tint_layers_7',
        "command": 'tint_layers',
        "args": [0x40, 0xa0, 0x40, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3077_tint_layers_8',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3077_reset_priority_set_9',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_3077_move_script_to_main_thread_10',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_3077_ret_11',
        "command": 'ret'
    }
]
