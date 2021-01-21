from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3591_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": 'EVENT_3591_jmp_if_object_trigger_disabled_1',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_5, Rooms._087_ROSE_TOWN_ITEM_SHOP, 'EVENT_3591_fade_in_from_black_async_3']
    },
    {
        "identifier": 'EVENT_3591_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3591_action_queue_sync_2_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3591_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3591_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_3591_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3591_enable_controls_9']
    },
    {
        "identifier": 'EVENT_3591_jmp_if_object_trigger_disabled_6',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_5, Rooms._087_ROSE_TOWN_ITEM_SHOP, 'EVENT_3591_enable_controls_9']
    },
    {
        "identifier": 'EVENT_3591_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_3591_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_3591_enable_controls_9',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3591_ret_10',
        "command": 'ret'
    }
]
