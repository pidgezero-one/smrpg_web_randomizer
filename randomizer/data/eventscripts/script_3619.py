from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3619_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3619_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3619_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3619_action_queue_async_2_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._090_CURTAIN, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3619_set_7000_to_current_level_3',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3619_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 416, 'EVENT_3619_apply_tile_mod_8']
    },
    {
        "identifier": 'EVENT_3619_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 438, 'EVENT_3619_apply_tile_mod_10']
    },
    {
        "identifier": 'EVENT_3619_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._061_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA_RIGHT_BEFORE_FIGHT, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3619_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3619_apply_tile_mod_8',
        "command": 'apply_tile_mod',
        "args": [Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3619_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3619_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3619_ret_11',
        "command": 'ret'
    }
]
