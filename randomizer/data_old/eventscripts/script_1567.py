
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1567_set_bit_0',
        "command": 'set_bit',
        "args": [0x7042, 3]
    },
    {
        "identifier": 'EVENT_1567_action_queue_sync_1',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": 'EVENT_1567_action_queue_sync_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1567_action_queue_sync_1_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1567_action_queue_sync_1_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1567_action_queue_async_2',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, False],
        "subscript": [
            {
                "identifier": 'EVENT_1567_action_queue_async_2_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1567_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1567_action_queue_async_2_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1567_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1567_ret_11',
        "command": 'ret'
    }
]
