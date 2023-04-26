from randomizer.data.attacks import EnemyAttack
from randomizer.data.items import Item
from randomizer.data.spells import CharacterSpell, EnemySpell

def type_assert(t, *args):
    for i, arg in enumerate(args):
        if isinstance(arg, int):
            if not (0 <= arg <= 0xFF):
                raise Exception('arg %d is out of range 0 <= %d <= 0xFF'%(i, arg))
        elif arg and not issubclass(arg, t):
            raise Exception('arg %s is not of type %s'%(arg, t))

class BattleScript:
    def __init__(self):
        self.counter_called = False
        self.script = []

    def append(self, name, *args):
        self.script.append((name, args))
        return self

    def fin(self):
        assert self.counter_called
        return self.script

    def attack(self, arg_0, arg_1=None, arg_2=None):
        type_assert(EnemyAttack, arg_0, arg_1, arg_2)
        return self.append('attack', arg_0, arg_1, arg_2)

    def set_target(self, arg_0):
        return self.append('set_target', arg_0)

    def battle_dialog(self, arg_0):
        return self.append('battle_dialog', arg_0)

    def battle_event(self, arg_0):
        return self.append('battle_event', arg_0)

    def inc(self, arg_0):
        return self.append('inc', arg_0)

    def dec(self, arg_0):
        return self.append('dec', arg_0)

    def set(self, arg_0, arg_1):
        return self.append('set', arg_0, arg_1)

    def clear(self, arg_0, arg_1):
        return self.append('clear', arg_0, arg_1)

    def zero(self, arg_0):
        return self.append('zero', arg_0)

    def remove(self, arg_0):
        return self.append('remove', arg_0)

    def call(self, arg_0):
        return self.append('call', arg_0)

    def invuln(self, arg_0):
        return self.append('invuln', arg_0)

    def uninvuln(self, arg_0):
        return self.append('uninvuln', arg_0)

    def exit_battle(self):
        return self.append('exit_battle')

    def rand(self, arg_0):
        return self.append('rand', arg_0)

    def cast_spell(self, arg_0, arg_1=None, arg_2=None):
        type_assert(EnemySpell, arg_0, arg_1, arg_2)
        return self.append('cast_spell', arg_0, arg_1, arg_2)

    def animate(self, arg_0):
        return self.append('animate', arg_0)

    def set_untargetable(self, arg_0):
        return self.append('set_untargetable', arg_0)

    def set_targetable(self, arg_0):
        return self.append('set_targetable', arg_0)

    def enable_command(self, arg_0):
        return self.append('enable_command', arg_0)

    def disable_command(self, arg_0):
        return self.append('disable_command', arg_0)

    def remove_items(self):
        return self.append('remove_items')

    def return_items(self):
        return self.append('return_items')

    def if_command(self, arg_0, arg_1=None):
        return self.append('if_command', arg_0, arg_1)

    def if_spell(self, arg_0, arg_1=None):
        type_assert(CharacterSpell, arg_0, arg_1)
        return self.append('if_spell', arg_0, arg_1)

    def if_item(self, arg_0, arg_1=None):
        type_assert(Item, arg_0, arg_1)
        return self.append('if_item', arg_0, arg_1)

    def if_element(self, arg_0):
        return self.append('if_element', arg_0)

    def if_attacked(self):
        return self.append('if_attacked')

    def if_hp(self, arg_0):
        return self.append('if_hp', arg_0)

    def if_target_status(self, arg_0, arg_1):
        return self.append('if_target_status', arg_0, arg_1)

    def if_not_target_status(self, arg_0, arg_1):
        return self.append('if_not_target_status', arg_0, arg_1)

    def if_phase(self, arg_0):
        return self.append('if_phase', arg_0)

    def if_less_than(self, arg_0, arg_1):
        return self.append('if_less_than', arg_0, arg_1)

    def if_greater_or_equal(self, arg_0, arg_1):
        return self.append('if_greater_or_equal', arg_0, arg_1)

    def if_target_alive(self, arg_0):
        return self.append('if_target_alive', arg_0)

    def if_target_dead(self, arg_0):
        return self.append('if_target_dead', arg_0)

    def if_bits_set(self, arg_0, arg_1):
        return self.append('if_bits_set', arg_0, arg_1)

    def if_bits_clear(self, arg_0, arg_1):
        return self.append('if_bits_clear', arg_0, arg_1)

    def if_monster_in_formation(self, arg_1):
        return self.append('if_monster_in_formation', arg_1)

    def if_solo(self):
        return self.append('if_solo')

    def wait(self):
        return self.append('wait')

    def wait_return(self):
        return self.append('wait_return')

    def start_counter(self):
        assert not self.counter_called
        self.counter_called = True
        return self.append('start_counter')