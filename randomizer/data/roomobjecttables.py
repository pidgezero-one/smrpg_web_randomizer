from types import SimpleNamespace

object_type = {
    0: 'OBJECT',
    1: 'CHEST',
    2: 'BATTLE'
}

ObjectType = SimpleNamespace()
for i in object_type:
    setattr(ObjectType, object_type[i], i)

event_initiator = {
    0x0: 'NONE',
    0x1: 'PRESS_A_FROM_ANY_SIDE',
    0x2: 'PRESS_A_FROM_FRONT',
    0x3: 'ANYTHING_EXCEPT_TOUCH_SIDE',
    0x4: 'PRESS_A_OR_TOUCH_ANY_SIDE',
    0x5: 'PRESS_A_OR_TOUCH_FRONT',
    0x6: 'DO_ANYTHING',
    0x7: 'HIT_FROM_BELOW',
    0x8: 'JUMP_ON',
    0x9: 'JUMP_ON_OR_HIT_FROM_BELOW',
    0xA: 'TOUCH_ANY_SIDE',
    0xB: 'TOUCH_FROM_FRONT',
    0xC: 'ANYTHING_EXCEPT_PRESS_A',
}

Initiator = SimpleNamespace()
for i in event_initiator:
    setattr(Initiator, event_initiator[i], i)

post_battle_behaviour = {
    0x0: 'REMOVE_PERMANENTLY',
    0x1: 'REMOVE_UNTIL_RELOAD',
    0x2: 'DO_NOT_REMOVE',
    0x3: 'REMOVE_PERMANENTLY_NO_IFRAME_COLLISION',
    0x4: 'REMOVE_UNTIL_RELOAD_NO_IFRAME_COLLISION',
}

PostBattle = SimpleNamespace()
for i in post_battle_behaviour:
    setattr(PostBattle, post_battle_behaviour[i], i)

radial_direction_table = {
    0x0: 'EAST',
    0x1: 'SOUTHEAST',
    0x2: 'SOUTH',
    0x3: 'SOUTHWEST',
    0x4: 'WEST',
    0x5: 'NORTHWEST',
    0x6: 'NORTH',
    0x7: 'NORTHEAST'
}

RadialDirection = SimpleNamespace()
for i in radial_direction_table:
    setattr(RadialDirection, radial_direction_table[i], i)
