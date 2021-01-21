from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3624_jmp_if_object_trigger_disabled_0',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._344_NIMBUS_LAND_ITEM_SHOP, 'EVENT_3624_fade_in_from_black_async_2']
    },
    {
        "identifier": 'EVENT_3624_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3624_action_queue_async_1_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3624_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3624_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_3624_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3624_jmp_if_object_trigger_disabled_5',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._344_NIMBUS_LAND_ITEM_SHOP, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3624_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_3624_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_3624_ret_8',
        "command": 'ret'
    }
]
