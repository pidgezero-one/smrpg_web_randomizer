
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3685_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3685_set_1',
        "command": 'set',
        "args": [0x70a7, 93]
    },
    {
        "identifier": 'EVENT_3685_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3685_set_bit_3',
        "command": 'set_bit',
        "args": [0x704b, 6]
    },
    {
        "identifier": 'EVENT_3685_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 510]
    },
    {
        "identifier": 'EVENT_3685_run_dialog_5',
        "command": 'run_dialog',
        "args": [3826, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3685_unsync_action_script_6',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3685_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3685_action_queue_async_7_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3685_put_inventory_8',
        "command": 'put_inventory',
        "args": [items.SignalRing]
    },
    {
        "identifier": 'EVENT_3685_ret_9',
        "command": 'ret'
    }
]
