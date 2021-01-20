from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_701_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_701_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_701_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_701_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_701_action_queue_async_2_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_701_action_queue_async_2_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [23, 70, 2]
            },
            {
                "identifier": 'EVENT_701_action_queue_async_2_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_701_action_queue_async_2_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_701_action_queue_async_2_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_701_set_action_script_async_3',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_701_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_701_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_701_action_queue_async_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_701_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_701_action_queue_async_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_701_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_701_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
