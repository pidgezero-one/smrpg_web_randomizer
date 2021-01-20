from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3342_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 5, 'EVENT_3342_run_event_as_subroutine_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3342_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3342_action_queue_sync_1_SUBSCRIPT_transfer_xyzf_steps_0',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 8, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3342_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3342_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 5, 'EVENT_3342_ret_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3342_run_background_event_4',
        "command": 'run_background_event',
        "args": [3345, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3342_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
