from smrpgpatchbuilder.datatypes.spells.classes import Spell as SpellBase, CharacterSpell as CharacterSpellBase, EnemySpell as EnemySpellBase
from typing import Optional

class Spell(SpellBase):
    _remake_name: Optional[str] = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._title


class CharacterSpell(CharacterSpellBase, Spell):
    pass


class EnemySpell(EnemySpellBase, Spell):
    pass