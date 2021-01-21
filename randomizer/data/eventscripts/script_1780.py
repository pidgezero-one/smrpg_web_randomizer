from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1780_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 4, 'EVENT_1780_jmp_if_object_trigger_disabled_2']
    },
    {
        "identifier": 'EVENT_1780_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._317_LANDS_END_DESERT_AREA_01]
    },
    {
        "identifier": 'EVENT_1780_jmp_if_object_trigger_disabled_2',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_6, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS, 'EVENT_1780_run_event_as_subroutine_4']
    },
    {
        "identifier": 'EVENT_1780_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1780_action_queue_sync_3_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1780_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1780_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_1780_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1780_clear_bit_9']
    },
    {
        "identifier": 'EVENT_1780_jmp_if_object_trigger_disabled_7',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_6, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS, 'EVENT_1780_clear_bit_9']
    },
    {
        "identifier": 'EVENT_1780_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_1780_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_1780_ret_10',
        "command": 'ret'
    }
]
