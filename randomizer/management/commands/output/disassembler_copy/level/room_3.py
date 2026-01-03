
from randomizer.data.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": None,
  "music": Music._11_BOWSERS_CASTLE_1ST_TIME,
  "entrance_event": 15,
  "event_tiles": [],
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
      "destination": Rooms._004_BOWSERS_KEEP_1ST_TIME_AREA_02,
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
