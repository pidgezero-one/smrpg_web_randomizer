#A0499_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Db(bytearray(b' \x03')),
	Db(bytearray(b'$\xe0\x00\x90\xff')),
	Pause(4),
	Db(bytearray(b'$@\x00\xe0\xff')),
	Pause(2)
])
