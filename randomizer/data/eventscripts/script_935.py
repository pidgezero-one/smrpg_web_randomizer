from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_935_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 'EVENT_935_jmp_if_object_trigger_disabled_2']
    },
    {
        "identifier": 'EVENT_935_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_935_jmp_if_object_trigger_disabled_2',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 'EVENT_935_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_935_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_935_action_queue_async_3_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_935_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_935_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_935_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_935_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_935_jmp_if_object_trigger_disabled_8',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_935_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_935_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_935_ret_11',
        "command": 'ret'
    }
]
