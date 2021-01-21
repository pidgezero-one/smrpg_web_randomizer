from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1741_set_0',
        "command": 'set',
        "args": [0x70ae, 3]
    },
    {
        "identifier": 'EVENT_1741_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1741_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_1741_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 774]
    },
    {
        "identifier": 'EVENT_1741_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_1741_pause_5',
        "command": 'pause',
        "args": [170]
    },
    {
        "identifier": 'EVENT_1741_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_1741_set_bit_1']
    }
]
