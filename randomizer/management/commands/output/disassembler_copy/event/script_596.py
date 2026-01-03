
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_596_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_596_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_596_pause_22']
    },
    {
        "identifier": 'EVENT_596_jmp_if_present_in_current_level_2',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_596_set_action_script_sync_4']
    },
    {
        "identifier": 'EVENT_596_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_596_pause_0']
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 298]
    },
    {
        "identifier": 'EVENT_596_pause_5',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 299]
    },
    {
        "identifier": 'EVENT_596_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_596_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_596_pause_25']
    },
    {
        "identifier": 'EVENT_596_jmp_if_present_in_current_level_9',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_4, 'EVENT_596_set_action_script_sync_11']
    },
    {
        "identifier": 'EVENT_596_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_596_pause_7']
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 298]
    },
    {
        "identifier": 'EVENT_596_pause_12',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 299]
    },
    {
        "identifier": 'EVENT_596_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_596_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_596_pause_28']
    },
    {
        "identifier": 'EVENT_596_jmp_if_present_in_current_level_16',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_596_set_action_script_sync_18']
    },
    {
        "identifier": 'EVENT_596_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_596_pause_14']
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 298]
    },
    {
        "identifier": 'EVENT_596_pause_19',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 299]
    },
    {
        "identifier": 'EVENT_596_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_596_pause_0']
    },
    {
        "identifier": 'EVENT_596_pause_22',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_596_create_packet_at_object_coords_jmp_if_null_23',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._033_BOMB_EXPLOSION, AreaObjects.NPC_3, 'EVENT_596_pause_22']
    },
    {
        "identifier": 'EVENT_596_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_596_pause_7']
    },
    {
        "identifier": 'EVENT_596_pause_25',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_596_create_packet_at_object_coords_jmp_if_null_26',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._033_BOMB_EXPLOSION, AreaObjects.NPC_4, 'EVENT_596_pause_25']
    },
    {
        "identifier": 'EVENT_596_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_596_pause_14']
    },
    {
        "identifier": 'EVENT_596_pause_28',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_596_create_packet_at_object_coords_jmp_if_null_29',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._033_BOMB_EXPLOSION, AreaObjects.NPC_2, 'EVENT_596_pause_28']
    },
    {
        "identifier": 'EVENT_596_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_596_pause_0']
    }
]
