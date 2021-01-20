from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1673_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1673_ret_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1673_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1673_set_7000_to_tapped_button_2',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1673_jmp_if_7000_all_bits_clear_3',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_1673_ret_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1673_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1673_action_queue_sync_4_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1673_action_queue_sync_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_1673_action_queue_sync_4_SUBSCRIPT_jmp_if_bit_set_2',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 2, 'EVENT_1673_ret_5']
            },
            {
                "identifier": 'EVENT_1673_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1673_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
