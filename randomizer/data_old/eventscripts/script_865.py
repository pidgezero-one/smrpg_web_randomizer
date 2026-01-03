
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_865_action_queue_async_12',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, False],
        "subscript": [
            {
                "identifier": 'EVENT_865_action_queue_async_12_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_865_action_queue_sync_43_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_865_action_queue_sync_43_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_865_action_queue_sync_43_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_865_action_queue_sync_43_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_865_action_queue_sync_43_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_865_action_queue_sync_43_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [18]
            }
        ]
    },
    {
        "identifier": "EVENT_865_ret",
        "command": "ret"
    }
]
