
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": None,
  "music": Music._27_DUNGEON_IS_FULL_OF_MONSTERS,
  "entrance_event": 1778,
  "event_tiles": [
    {
      "event": 1680,
      "x": 20,
      "y": 74,
      "z": 1,
      "f": Edge.SOUTHEAST,
      "length": 1,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "byte_8_bit_4": False,
    }
  ],
  "exit_fields": [
    {
      "x": 12,
      "y": 81,
      "z": 1,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
      "show_message": False,
      "destination_props": {
        "x": 12,
        "y": 21,
        "z": 9,
        "z_half": False,
        "f": RadialDirection.SOUTHWEST,
        "x_bit_7": False
      }
    }
  ],
  "objects": []
}
