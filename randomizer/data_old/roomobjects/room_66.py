
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": None,
  "music": Music._13_ROAD_IS_FULL_OF_DANGERS,
  "entrance_event": 3917,
  "event_tiles": [
    {
      "event": 3154,
      "x": 27,
      "y": 74,
      "z": 1,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 7,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": True,
      "byte_8_bit_4": False,
    }
  ],
  "exit_fields": [
    {
      "x": 21,
      "y": 106,
      "z": 0,
      "f": Edge.SOUTHEAST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA,
      "show_message": False,
      "destination_props": {
        "x": 26,
        "y": 47,
        "z": 0,
        "z_half": False,
        "f": RadialDirection.NORTHWEST,
        "x_bit_7": False
      }
    }
  ],
  "objects": []
}
