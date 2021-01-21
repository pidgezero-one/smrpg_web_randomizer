from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_278_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x11, 0x56]
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_set_short_mem_5',
                "command": 'set_short_mem',
                "args": [0x700c, 0x70a9]
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_278_ret_1']
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_floating_off_7',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_278_action_queue_async_0_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_278_ret_1',
        "command": 'ret'
    }
]
