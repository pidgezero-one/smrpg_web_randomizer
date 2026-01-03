
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": None,
  "music": Music._66_BOWSERS_CASTLE_2ND_TIME,
  "entrance_event": 2233,
  "event_tiles": [
    {
      "event": 2149,
      "x": 4,
      "y": 38,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "byte_8_bit_4": False,
    }
  ],
  "exit_fields": [
    {
      "x": 11,
      "y": 21,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._477_BOWSERS_KEEP_2ND_TIME_AREA_02,
      "show_message": False,
      "destination_props": {
        "x": 4,
        "y": 95,
        "z": 0,
        "z_half": False,
        "f": RadialDirection.NORTHEAST,
        "x_bit_7": False
      }
    }
  ],
  "objects": []
}
