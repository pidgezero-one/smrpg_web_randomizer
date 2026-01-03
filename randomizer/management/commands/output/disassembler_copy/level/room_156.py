
from randomizer.data.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": None,
  "music": Music._39_MARRYMORE,
  "entrance_event": 261,
  "event_tiles": [
    {
      "event": 671,
      "x": 6,
      "y": 87,
      "z": 2,
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
      "x": 2,
      "y": 92,
      "z": 0,
      "f": Edge.SOUTHEAST,
      "length": 1,
      "height": 1,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": True,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._155_MARRYMORE_CHAPEL_KITCHEN,
      "show_message": False,
      "destination_props": {
        "x": 9,
        "y": 16,
        "z": 0,
        "z_half": True,
        "f": RadialDirection.SOUTHWEST,
        "x_bit_7": False
      }
    }
  ],
  "objects": []
}
