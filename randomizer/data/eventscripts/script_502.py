from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_502_move_script_to_background_thread_2_0',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_502_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_502_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_502_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_502_set_short_4',
        "command": 'set_short',
        "args": [0x701c, 0x0018]
    },
    {
        "identifier": 'EVENT_502_run_background_event_with_pause_return_on_exit_5',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [509, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_502_move_script_to_main_thread_6',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_502_ret_7',
        "command": 'ret'
    }
]
