
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": None,
  "music": Music._02_MUSHROOM_KINGDOM,
  "entrance_event": 15,
  "event_tiles": [],
  "exit_fields": [
    {
      "x": 27,
      "y": 30,
      "z": 0,
      "f": Edge.SOUTHEAST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
      "show_message": False,
      "destination_props": {
        "x": 4,
        "y": 23,
        "z": 2,
        "z_half": False,
        "f": RadialDirection.SOUTHEAST,
        "x_bit_7": False
      }
    },
    {
      "x": 26,
      "y": 19,
      "z": 3,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 2,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._032_MUSHROOM_KINGDOM_CASTLE_ENTRANCE_TO_TOADSTOOLS_ROOM,
      "show_message": False,
      "destination_props": {
        "x": 11,
        "y": 98,
        "z": 1,
        "z_half": False,
        "f": RadialDirection.NORTHEAST,
        "x_bit_7": False
      }
    }
  ],
  "objects": []
}
