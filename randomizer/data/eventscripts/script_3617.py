from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3617_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 7, 'EVENT_3617_summon_to_current_level_3']
    },
    {
        "identifier": 'EVENT_3617_fade_in_from_black_async_1',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3617_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3617_summon_to_current_level_3',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3617_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3617_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3617_action_queue_async_4_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [250, 250, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3617_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._346_NIMBUS_LAND_INN_BEDROOM, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3617_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3617_ret_7',
        "command": 'ret'
    }
]
