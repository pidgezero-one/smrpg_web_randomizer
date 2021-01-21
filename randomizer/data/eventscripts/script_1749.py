from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1749_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1749_action_queue_sync_0_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_1749_set_short_1',
        "command": 'set_short',
        "args": [0x701e, 0x001d]
    },
    {
        "identifier": 'EVENT_1749_run_background_event_with_pause_return_on_exit_2',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1748, 0x701e, [12, 13]]
    },
    {
        "identifier": 'EVENT_1749_ret_3',
        "command": 'ret'
    }
]
