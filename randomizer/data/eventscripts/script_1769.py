from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1769_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704f, 3, 'EVENT_1769_ret_6']
    },
    {
        "identifier": 'EVENT_1769_set_bit_1',
        "command": 'set_bit',
        "args": [0x704f, 3]
    },
    {
        "identifier": 'EVENT_1769_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1769_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1769_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1769_action_queue_sync_2_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1769_action_queue_sync_2_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1769_apply_solidity_mod_3',
        "command": 'apply_solidity_mod',
        "args": [Rooms._268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1769_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._017_OPEN_FRONT_GATE, 6]
    },
    {
        "identifier": 'EVENT_1769_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_1769_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1769_action_queue_async_5_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1769_action_queue_async_5_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1769_ret_6',
        "command": 'ret'
    }
]
