from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_377_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 108]
    },
    {
        "identifier": 'EVENT_377_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_377_start_embedded_action_script_async_F1_2',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_377_start_embedded_action_script_async_F1_2_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_377_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 110]
    },
    {
        "identifier": 'EVENT_377_pause_4',
        "command": 'pause',
        "args": [150]
    },
    {
        "identifier": 'EVENT_377_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_377_start_embedded_action_script_async_F1_6',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_377_start_embedded_action_script_async_F1_6_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_377_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 110]
    },
    {
        "identifier": 'EVENT_377_pause_8',
        "command": 'pause',
        "args": [150]
    },
    {
        "identifier": 'EVENT_377_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_377_pause_action_script_1']
    }
]
