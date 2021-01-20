from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2585_disable_event_trigger_for_object_at_70A8_0',
        "command": 'disable_event_trigger_for_object_at_70A8',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2585_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [2644],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2585_run_dialog_2',
        "command": 'run_dialog',
        "args": [3155, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2585_put_inventory_3',
        "command": 'put_inventory',
        "args": [items.KerokeroCola],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2585_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
