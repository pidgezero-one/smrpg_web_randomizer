from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3299_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_set_700C_to_object_coord_3',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_mem_compare_4',
                "command": 'mem_compare',
                "args": [0x700c, 1280]
            },
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_jmp_if_loaded_memory_is_above_or_equal_0_5',
                "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
                "args": ['EVENT_3299_action_queue_async_0_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1']
            },
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3299_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_7',
                "command": 'object_memory_set_bit',
                "args": [0x0c, [3, 4, 5]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3299_ret_1',
        "command": 'ret'
    }
]
