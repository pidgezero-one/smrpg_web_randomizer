# Boss/star piece randomization data for open mode.

from enum import auto
from typing import Dict, List, Optional, Type

from randomizer.types.battles.battle_music.music import NormalBattleMusic
from randomizer.types.bosses.enums import Battlefields
from randomizer.types.npcs.objects.classes import NPC, Statue
from randomizer.types.npcs.objects.npcs import Empty, NimbusLandStatue, ValentinaStatue
from randomizer.types.numbers.classes import UInt8
from randomizer.types.overworld_scripts.action_scripts.classes import (
    ActionScriptCommand,
)
from .enums import HenchmanType, SpriteSize

from randomizer.types.numbers.classes import ByteField
from randomizer.types.patch.classes import Patch

from randomizer.utils.snippets.es_mimic_rise import commands as mimic_subscript

from randomizer.types.items.classes import BossFight

EMPTY_DIALOG = "[await]"


class Henchman:
    _pack_number: Optional[int] = None
    _model: Type[NPC]

    @property
    def pack_number(self) -> Optional[UInt8]:
        if self._pack_number is not None:
            return UInt8(self._pack_number)
        return self._pack_number

    def set_pack_number(self, pack_number: Optional[int]) -> None:
        if pack_number is not None:
            pack_number = UInt8(pack_number)
        self._pack_number = pack_number

    @property
    def model(self) -> Type[NPC]:
        return self._model

    def set_model(self, model: Type[NPC]) -> None:
        self._model = model


class Boss(BossFight):
    _name: str = ""
    _letter_seaside_boss_name: str = ""
    _letter_volcano_boss_name: str = ""
    _letter_final_boss_name: str = ""
    _pack_number: Optional[int] = None
    _statue: Type[Statue] = ValentinaStatue
    _small_model: Type[NPC] = Empty
    _big_model: Optional[Type[NPC]] = None
    _attack_model: Optional[Type[NPC]] = None
    _forced_background: Optional[Battlefields] = None
    _unique_henchmen: List[Henchman] = []
    _repeatable_henchmen: List[Henchman] = []
    _dialog_replacements: Dict[int, str] = {}
    _dialog_replacements_if_mandatory_fights_changed: Dict[int, str] = {}
    _can_be_immune_to_physical: bool = True  # This will only be false for very, very specific situations to prevent uncompleteable seeds under certain settings combinations.

    @property
    def name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    @property
    def letter_seaside_boss_name(self) -> str:
        if self._letter_seaside_boss_name == "":
            return self.name
        return self._letter_seaside_boss_name

    @property
    def letter_volcano_boss_name(self) -> str:
        return self._letter_volcano_boss_name

    @property
    def letter_final_boss_name(self) -> str:
        return self._letter_final_boss_name

    @property
    def pack_number(self) -> Optional[UInt8]:
        if self._pack_number is not None:
            return UInt8(self._pack_number)
        return self._pack_number

    def set_pack_number(self, pack_number: Optional[int]) -> None:
        if pack_number is not None:
            pack_number = UInt8(pack_number)
        self._pack_number = pack_number

    @property
    def statue(self) -> Type[NPC]:
        return self._statue

    def set_statue(self, statue: Type[Statue]) -> None:
        self._statue = statue

    @property
    def small_model(self) -> Type[NPC]:
        return self._small_model

    def set_small_model(self, small_model: Type[NPC]) -> None:
        self._small_model = small_model

    @property
    def big_model(self) -> Type[NPC]:
        if self._big_model is not None:
            return self._big_model
        return self.small_model

    def set_big_model(self, big_model: Optional[Type[NPC]]) -> None:
        self._big_model = big_model

    @property
    def attack_model(self) -> Type[NPC]:
        if self._attack_model is not None:
            return self._attack_model
        return self.big_model

    def set_attack_model(self, attack_model: Optional[Type[NPC]]) -> None:
        self._attack_model = attack_model

    @property
    def forced_background(self) -> Optional[Battlefields]:
        return self._forced_background

    def set_forced_background(self, forced_background: Optional[Battlefields]) -> None:
        self._forced_background = forced_background

    @property
    def unique_henchmen(self) -> List[Henchman]:
        return self._unique_henchmen

    def set_unique_henchmen(self, unique_henchmen: List[Henchman]) -> None:
        self._unique_henchmen = unique_henchmen

    @property
    def repeatable_henchmen(self) -> List[Henchman]:
        return self._repeatable_henchmen

    def set_repeatable_henchmen(self, repeatable_henchmen: List[Henchman]) -> None:
        self._repeatable_henchmen = repeatable_henchmen

    @property
    def dialog_replacements(self) -> Dict[int, str]:
        return self._dialog_replacements

    def set_dialog_replacements(self, dialog_replacements: Dict[int, str]) -> None:
        self._dialog_replacements = dialog_replacements

    @property
    def dialog_replacements_if_mandatory_fights_changed(self) -> Dict[int, str]:
        return self._dialog_replacements_if_mandatory_fights_changed

    def set_dialog_replacements_if_mandatory_fights_changed(
        self, dialog_replacements_if_mandatory_fights_changed: Dict[int, str]
    ) -> None:
        self._dialog_replacements_if_mandatory_fights_changed = (
            dialog_replacements_if_mandatory_fights_changed
        )

    @property
    def can_be_immune_to_physical(self) -> bool:
        return self._can_be_immune_to_physical

    def set_can_be_immune_to_physical(self, can_be_immune_to_physical: bool) -> None:
        self._can_be_immune_to_physical = can_be_immune_to_physical

    @property
    def classname(self):
        return self.__class__.__name__


class MimicBoss(Boss):
    _challenge_script: List[ActionScriptCommand] = mimic_subscript

    @property
    def challenge_script(self) -> List[ActionScriptCommand]:
        return self._challenge_script

    def set_challenge_script(self, challenge_script: List[ActionScriptCommand]) -> None:
        self._challenge_script = challenge_script


class StarLocation:
    """Class representing a star location."""

    # Star piece data
    star_address = 0x0
    has_star = False

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world

    def __str__(self):
        return "<{}: has_star {}>".format(self.name, self.has_star)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_patch(self):
        """

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = Patch()

        # Zero for no star, or 255 if this boss has a star.
        val = 0xFF if self.has_star else 0x00
        patch.add_data(self.star_address, ByteField(val).as_bytes())

        return patch
