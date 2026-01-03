
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_937_action_queue_sync_185',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": 'EVENT_937_action_queue_sync_185_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_937_action_queue_sync_185_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_937_action_queue_sync_185_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_937_action_queue_sync_185_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_937_action_queue_sync_185_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_937_action_queue_sync_185_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_937_ret_291',
        "command": 'ret'
    }
]