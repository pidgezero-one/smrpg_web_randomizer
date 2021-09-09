# Common utilities for outputting binary data for the patches, and shuffling stat values.

import inspect
import random
import re
import enum
import copy
import uuid
from randomizer.data.objectsequencetables import _0x08Flags
from randomizer.data.eventtables import AreaObjects
from randomizer.data.helpers import SequenceType

# Amount to boost very small values when shuffling to give a bit more range for very small values.
SMALL_BOOST_AMOUNT = 2.0


def isclass_or_instance(obj_or_cls, classinfo):
    """Helper function to check if an object is an instance of a class, or the class itself."""
    return isinstance(obj_or_cls, classinfo) or (inspect.isclass(obj_or_cls) and issubclass(obj_or_cls, classinfo))


class BitMapSet(set):
    """A class representing a bitmap of a certain length using the set built-in type to track which bits are set."""

    def __init__(self, num_bytes=1, *args, **kwargs):
        """
        :type num_bytes: int
        """
        super().__init__(*args, **kwargs)
        self._num_bytes = num_bytes

    def as_bytes(self):
        """Return bitmap in little endian byte format for ROM patching.

        :rtype: bytearray
        """
        result = 0
        for value in self:
            result |= (1 << value)
        return result.to_bytes(self._num_bytes, 'little')

    def __str__(self):
        return "BitMapSet({})".format(super().__str__())


class ByteField:
    """Base class for an integer value field spanning one or more bytes."""

    def __init__(self, value, num_bytes=1):
        """
        :type value: int
        :type num_bytes: int
        """
        self._value = value
        self._num_bytes = num_bytes

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = int(value)

    def as_bytes(self):
        """Return current value of this stat as a little-endian byte array for the patch.  If the value is less than
        zero, convert this to a signed int in byte format.

        :rtype: bytearray
        """
        if self._value < 0:
            val = self._value + (2 ** (self._num_bytes * 8))
        else:
            val = self._value
        return val.to_bytes(self._num_bytes, 'little')

    def __str__(self):
        return "ByteField(current value: {}, number of bytes: {}".format(self.value, self._num_bytes)


class Mutator:
    """Mutator class that shuffles stat attributes based on min/max values and a difficulty setting."""

    def __init__(self, difficulty=None):
        # Placeholder for future difficulty option.
        self.difficulty = difficulty

    def mutate_normal(self, value, minimum=0, maximum=0xff):
        """Mutate a value with a given range.
        This is roughly simulating a normal distribution with mean <value>, std deviation approx 1/5 <value>.
        """
        # The actual value we're shuffling is the difference between the default value and the minimum or maximum,
        # whichever is smaller.  Shuffle this distance value, then recompute the new actual value below.
        value = max(minimum, min(value, maximum))
        if value > (minimum + maximum) / 2:
            reverse = True
        else:
            reverse = False

        if reverse:
            value = maximum - value
        else:
            value = value - minimum

        # For very small values, give a small boost amount to allow for a bit more variance.  Subtract this later.
        boosted = False
        if value < SMALL_BOOST_AMOUNT:
            value += SMALL_BOOST_AMOUNT
            if value > 0:
                boosted = True
            else:
                value = 0

        # Make new random value.
        if value > 0:
            half = value / 2.0
            a, b = random.random(), random.random()
            value = half + (half * a) + (half * b)

        # If we boosted the value, bring it back down now.
        if boosted:
            value -= SMALL_BOOST_AMOUNT

        # Compute actual final value with new distance from minimum/maximum.
        if reverse:
            value = maximum - value
        else:
            value = value + minimum

        # 1/10 chance to chain mutate for more variance.
        if random.randint(1, 10) == 10:
            return self.mutate_normal(value, minimum=minimum, maximum=maximum)
        else:
            value = max(minimum, min(value, maximum))
            value = int(round(value))
            return value


class _GlobalMutator:
    """Container class for the global mutator instance so we can control the difficulty."""
    mutator = Mutator()

    @classmethod
    def get_mutator(cls):
        return cls.mutator

    @classmethod
    def set_difficulty(cls, difficulty):
        cls.mutator.difficulty = difficulty


def mutate_normal(value, minimum=0, maximum=0xff):
    """Mutate a stat value using the global mutator."""
    return _GlobalMutator.get_mutator().mutate_normal(value, minimum, maximum)


def set_difficulty(difficulty):
    """Set the difficulty level for the global mutator that shuffles stats."""
    _GlobalMutator.set_difficulty(difficulty)


def coin_flip(odds=0.5):
    """Weighted coin flip with odds."""
    return random.random() < odds


def add_desc_fields(fields):
    d = ''
    for chars, flag, attr in fields:
        if isinstance(attr, (list, tuple)):
            if flag in attr:
                d += chars
        elif isinstance(attr, bool):
            if attr:
                d += chars
    return d


def split_camel_case(string):
    """

    Args:
        string: String to split.

    Returns:
        str: Camel case string split out with spaces in between words.

    """
    return re.sub(r'(?!^)([A-Z0-9][a-z]*)', r' \1', string)


def allocate_string(string_length, free_list):
    for base in sorted(free_list, key=lambda x: free_list[x]):
        if free_list[base] >= string_length:
            size = free_list[base]
            del free_list[base]
            free_list[base+string_length] = size - string_length
            return base

    # If we get this far, we couldn't find space for the string.
    return None

# animation utils

class CommandTypes(enum.Enum):
    Action = enum.auto()
    Event = enum.auto()


def new_animation(event_id, command, npc_id, subscript):
    cmd = new_command(event_id, command, [npc_id + 0x14])
    cmd["subscript"] = subscript
    return cmd


def new_command(event_id, command, args=None, t=CommandTypes.Event):
    if t == CommandTypes.Action:
        cmdType = "ACTION"
    else:
        cmdType = "EVENT"
    cmd = {
        "identifier": "%s_%i_%s" % (cmdType, event_id, str(uuid.uuid4())),
        "command": command
    }
    if args is not None:
        cmd["args"] = args
    return cmd


def is_animation_header(command, npc_id):
    return command["command"] in ['action_queue_async', 'action_queue_sync', 'start_embedded_action_script_async_F0', 'start_embedded_action_script_async_F1', 'start_embedded_action_script_sync_F0', 'start_embedded_action_script_sync_F1'] and command["args"][0] == npc_id + 0x14


def remove_sequence_changes_from_action_script(script):
    #if NPC is supposed to keep a certain mold/sequence, make sure it never resets
    return [a for a in script if a["command"] != 'set_sprite_sequence' and a["command"] != "reset_properties"]

def fix_directions_for_sequenced_sprite(script, sequence_type=SequenceType.Sequence, sequence_id=0, sprite_offset=0):
    # specific sequence sprites: face left or right depending on intent of script
    output = []
    flags = []
    if sequence_type==SequenceType.Sequence:
        flags.append(_0x08Flags.READ_AS_SEQUENCE)
    else:
        flags.append(_0x08Flags.READ_AS_MOLD)
    for command in script:
        if command["command"] in ["face_southeast", "face_northeast"]:
            output.append({
                "identifier": 'dummy',
                "command": 'set_sprite_sequence',
                "args": [sequence_id, sprite_offset, [*flags, _0x08Flags.MIRROR_SPRITE]]
            })
        elif command["command"] in ["face_southwest", "face_northwest"]:
            output.append({
                "identifier": 'dummy',
                "command": 'set_sprite_sequence',
                "args": [sequence_id, sprite_offset, flags]
            })
        elif command["command"] in ["walk_1_step_east", "walk_1_step_northeast", "shift_east_steps", "shift_northeast_steps", "shift_east_pixels", "shift_northeast_pixels", "walk_1_step_southeast", "shift_southeast_steps", "shift_southeast_pixels", "walk_1_step_south", "shift_south_steps", "shift_south_pixels"]:
            c = {
                "identifier": 'dummy',
                "command": 'set_sprite_sequence',
                "args": [sequence_id, sprite_offset, [*flags, _0x08Flags.MIRROR_SPRITE]]
            }
            output.append(c)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_west", "walk_1_step_southwest", "shift_west_steps", "shift_southwest_steps", "shift_west_pixels", "shift_southwest_pixels", "walk_1_step_north", "walk_1_step_northwest", "shift_north_steps", "shift_northwest_steps", "shift_north_pixels", "shift_northwest_pixels"]:
            c = {
                "identifier": 'dummy',
                "command": 'set_sprite_sequence',
                "args": [sequence_id, sprite_offset, flags]
            }
            output.append(c)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["shift_f_direction_steps", "shift_z_20_steps", "shift_z_up_steps", "shift_z_down_steps", "shift_z_up_20_steps", "shift_z_down_20_steps", "shift_f_direction_pixels", "walk_f_direction_16_pixels", "shift_z_up_pixels", "shift_z_down_pixels", "shift_to_xy_coords", "shift_xy_steps", "shift_xy_pixels", "walk_1_step_f_direction", "walk_f_direction_16_pixels", "walk_to_xy_coords", "walk_xy_steps", "walk_to_7016_7018", "walk_to_7016_7018_701A"]:
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        else:
            output.append(command)
    return output

def fix_script_for_scarecrow(script):
    s = [a for a in script if a["command"] != "reset_properties"]
    output = []
    for command in s:
        if command["command"] == "face_northwest":
            command["command"] = "face_southeast"
            output.append(command)
        elif command["command"] == "face_northeast":
            command["command"] = "face_southwest"
            output.append(command)
        elif command["command"] == "face_southeast":
            command["command"] = "face_northeast"
            output.append(command)
        elif command["command"] == "face_southwest":
            command["command"] = "face_northwest"
            output.append(command)
        elif command["command"] == "face_mario":
            pass  # could possibly substitute a series of "ifs" comparing coord to mario's, and set direction based on that info, but that would be hella complicated and i dont know what temp vars would make sense for it
        elif command["command"] in ["walk_1_step_east", "walk_1_step_northeast", "shift_east_steps", "shift_northeast_steps", "shift_east_pixels", "shift_northeast_pixels"]:
            output.append({"identifier": "dummy", "command": "face_southwest"})
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_southeast", "shift_southeast_steps", "shift_southeast_pixels"]:
            output.append({"identifier": "dummy", "command": "face_northeast"})
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_south", "shift_south_steps", "shift_south_pixels"]:
            output.append({"identifier": "dummy", "command": "face_northeast"})
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            #output.append({"identifier": "dummy", "command": "set_sprite_sequence", "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_west", "walk_1_step_southwest", "shift_west_steps", "shift_southwest_steps", "shift_west_pixels", "shift_southwest_pixels"]:
            output.append({"identifier": "dummy", "command": "face_northwest"})
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_north", "walk_1_step_northwest", "shift_north_steps", "shift_northwest_steps", "shift_north_pixels", "shift_northwest_pixels"]:
            output.append({"identifier": "dummy", "command": "face_southeast"})
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["shift_f_direction_steps", "shift_z_20_steps", "shift_z_up_steps", "shift_z_down_steps", "shift_z_up_20_steps", "shift_z_down_20_steps", "shift_f_direction_pixels", "walk_f_direction_16_pixels", "shift_z_up_pixels", "shift_z_down_pixels", "shift_to_xy_coords", "shift_xy_steps", "shift_xy_pixels", "walk_1_step_f_direction", "walk_f_direction_16_pixels", "walk_to_xy_coords", "walk_xy_steps", "walk_to_7016_7018", "walk_to_7016_7018_701A"]:
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append(
                {"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] == "set_sprite_sequence" and command["args"][0] == 1:
            command["args"][0] = 0
            if _0x08Flags.MIRROR_SPRITE in ["args"][0][2]:
                command["args"][2] = [c for c in command["args"]
                                      [2] if c != _0x08Flags.MIRROR_SPRITE]
            else:
                command["args"][2].append(_0x08Flags.MIRROR_SPRITE)
            output.append(command)
        else:
            output.append(command)
    return output


def is_mario_animation_header(command):
    return command["command"] in ['action_queue_async', 'action_queue_sync', 'start_embedded_action_script_async_F0', 'start_embedded_action_script_async_F1', 'start_embedded_action_script_sync_F0', 'start_embedded_action_script_sync_F1'] and command["args"][0] == AreaObjects.MARIO


def sanitize_character_animation_script(sequence_types, script):
    '''For Forest Maze and Marrymore characters. Most characters have the same selections of sprites for a given situation, but they aren't always located at the same offset/sequence.'''
    new_script = []
    for _, command in enumerate(script):
        cmd = copy.deepcopy(command)
        key = None
        if cmd["command"] == 'set_sprite_sequence':
            seq = cmd["args"][0]
            spr = cmd["args"][1]
            if _0x08Flags.READ_AS_MOLD in cmd["args"][2]:
                if spr == 5 and seq == 0:
                    key = "hurt"
                elif spr == 0 and seq == 14:
                    key = "looking_down_static"
                elif spr == 2 and seq == 1:
                    key = "floored"
                elif spr == 0 and seq == 20:
                    key = "south"
                elif spr == 1 and seq == 17:
                    key = "defend"
            else:
                if spr == 2 and seq == 3:
                    key = "shocked_loop"
                elif spr == 2 and seq == 4:
                    key = "shocked_loop_backwards"
                elif spr == 0 and seq == 13:
                    key = "crying"
                elif spr == 0 and seq == 14:
                    key = "crying_backwards"
                elif spr == 0 and seq == 1:
                    key = "face_north"
                elif spr == 0 and seq == 0:
                    key = "face_south"
                elif spr == 0 and seq == 8:
                    key = "shaking_head"
                elif spr == 0 and seq == 9:
                    key = "shaking_head_backward"
                elif spr == 0 and seq == 6:
                    key = "looking_down"
                elif spr == 1 and seq == 6:
                    key = "sleeping"
                elif spr == 1 and seq == 3:
                    key = "shocked_backwards_sequence"
        if key is not None:
            flags = [a for a in cmd["args"][2] if a != _0x08Flags.READ_AS_MOLD]
            sprite, sequence, is_mold = sequence_types[key]
            if is_mold:
                flags.append(_0x08Flags.READ_AS_MOLD)
            cmd["args"] = [sequence, sprite, flags]
        new_script.append(cmd)
    return new_script


def find_subclasses(module, clazz):
    return [
        cls
        for name, cls in inspect.getmembers(module)
        if inspect.isclass(cls) and issubclass(cls, clazz) and cls != clazz
    ]