"""Base classes representing boss fights."""

from typing import Dict, List, Optional, Type

from randomizer.types.items.classes import BossFight
from randomizer.types.npcs.objects.types import NPC, Statue
from randomizer.types.npcs.objects import Empty, ValentinaStatue
from randomizer.types.numbers import UInt8
from randomizer.types.overworld_scripts.action_scripts.commands.types import (
    ActionScriptCommand,
)

from randomizer.utils.snippets.es_mimic_rise import commands as mimic_subscript


from .enums import Battlefields

EMPTY_DIALOG = "[await]"


class Henchman:
    """Base class representing enemies that should occupy certain
    spots in the overworld, depending on who a specific boss is.
    i.e. the shy guys in the Mushroom Kingdom are replaced by henchmen
    belonging to the boss that occupies the Mushroom Kingdom throne room."""

    _pack_number: Optional[int] = None
    _model: Type[NPC]

    @property
    def pack_number(self) -> Optional[UInt8]:
        """Pack number of the battle to run when fighting this henchman."""
        if self._pack_number is not None:
            return UInt8(self._pack_number)
        return self._pack_number

    def set_pack_number(self, pack_number: Optional[int]) -> None:
        """Set pack number of the battle to run when fighting this henchman."""
        if pack_number is not None:
            pack_number = UInt8(pack_number)
        self._pack_number = pack_number

    @property
    def model(self) -> Type[NPC]:
        """The graphical asset for this henchman to be loaded in the NPC slots
        associated to the boss location."""
        return self._model

    def set_model(self, model: Type[NPC]) -> None:
        """Set the graphical asset for this henchman to be loaded in the NPC slots
        associated to the boss location."""
        self._model = model


class Boss(BossFight):
    """Base class representing a shuffle-able boss fight, in terms of how it behaves
    in the overworld (preferred models, packs loaded, etc) rather than how the
    battle itself functions."""

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

    # This will only be false for very, very specific situations to prevent
    # uncompleteable seeds under certain settings combinations.
    _can_be_immune_to_physical: bool = True

    @property
    def name(self) -> str:
        """An identifier for the boss."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set an identifier for the boss."""
        self._name = name

    @property
    def letter_seaside_boss_name(self) -> str:
        """How this boss should be described by the author of the Seaside Beach note
        if this boss is the boss of the Seaside Beach."""
        if self._letter_seaside_boss_name == "":
            return self.name
        return self._letter_seaside_boss_name

    @property
    def letter_volcano_boss_name(self) -> str:
        """How this boss should be described by the author of the Seaside Beach note
        if this boss is the boss of Barrel Volcano."""
        return self._letter_volcano_boss_name

    @property
    def letter_final_boss_name(self) -> str:
        """How this boss should be described by the author of the Seaside Beach note
        if this boss is the final boss of the Factory."""
        return self._letter_final_boss_name

    @property
    def pack_number(self) -> Optional[UInt8]:
        """Pack number of the battle to run when fighting this boss."""
        if self._pack_number is not None:
            return UInt8(self._pack_number)
        return self._pack_number

    def set_pack_number(self, pack_number: Optional[int]) -> None:
        """Set the pack number of the battle to run when fighting this boss."""
        if pack_number is not None:
            pack_number = UInt8(pack_number)
        self._pack_number = pack_number

    @property
    def statue(self) -> Type[NPC]:
        """The model to draw over all Nimbus Land statues
        if this boss is the final boss of Nimbus Land."""
        return self._statue

    def set_statue(self, statue: Type[Statue]) -> None:
        """Set the model to draw over all Nimbus Land statues
        if this boss is the final boss of Nimbus Land."""
        self._statue = statue

    @property
    def small_model(self) -> Type[NPC]:
        """The model to be drawn representing this boss in contexts where
        the model needs to be less than 32x32 px."""
        return self._small_model

    def set_small_model(self, small_model: Type[NPC]) -> None:
        """Set the model to be drawn representing this boss in contexts where
        the model needs to be less than 32x32 px."""
        self._small_model = small_model

    @property
    def big_model(self) -> Type[NPC]:
        """The model to be drawn representing this boss in contexts where
        the model can be larger than 32x32 px, where such sprites exist.
        For bosses like Yaridovich who have a large model that's slightly smaller than
        their in-battle model, those will usually be used here.
        Returns the small model if no suitable sprite exists for this boss."""
        if self._big_model is not None:
            return self._big_model
        return self.small_model

    def set_big_model(self, big_model: Optional[Type[NPC]]) -> None:
        """Set the model to be drawn representing this boss in contexts where
        the model can be larger than 32x32 px, where such sprites exist.
        If set to None, it will simply use the small model."""
        self._big_model = big_model

    @property
    def attack_model(self) -> Type[NPC]:
        """The model to be drawn representing this boss in contexts where
        the model can be larger than 32x32 px, AND we want to use a special animation
        such as an attack that the sprite can perform in battle.
        Returns the big model or small model if no suitable sprite exists for this boss.
        """
        if self._attack_model is not None:
            return self._attack_model
        return self.big_model

    def set_attack_model(self, attack_model: Optional[Type[NPC]]) -> None:
        """Set the model to be drawn representing this boss in contexts where
        the model can be larger than 32x32 px, and where we want to use a specific
        attack animation belonging to that sprite.
        If set to None, it will simply use the big model or small model."""
        self._attack_model = attack_model

    @property
    def forced_background(self) -> Optional[Battlefields]:
        """If set, launching a fight against this boss' pack will always load this battlefield.
        Otherwise, the battlefield will simply match the world area."""
        return self._forced_background

    def set_forced_background(self, forced_background: Optional[Battlefields]) -> None:
        """If set, launching a fight against this boss' pack will always load this battlefield.
        Otherwise, the battlefield will simply match the world area."""
        self._forced_background = forced_background

    @property
    def unique_henchmen(self) -> List[Henchman]:
        """A list of henchman which should only appear once each,
        such as the individual Axem Rangers."""
        return self._unique_henchmen

    def set_unique_henchmen(self, unique_henchmen: List[Henchman]) -> None:
        """Overwrite the list of henchman which should only appear once each,
        such as the individual Axem Rangers."""
        self._unique_henchmen = unique_henchmen

    @property
    def repeatable_henchmen(self) -> List[Henchman]:
        """A list of generic henchmen that aren't really unique characters, and can occupy
        any henchman slot that isn't meant to house a unique character.
        The Shy Guys in Mushroom Kingdom are an example of this."""
        return self._repeatable_henchmen

    def set_repeatable_henchmen(self, repeatable_henchmen: List[Henchman]) -> None:
        """Overwrite the list of generic henchmen that aren't really unique characters,
        and can occupy any henchman slot that isn't meant to house a unique character.
        The Shy Guys in Mushroom Kingdom are an example of this."""
        self._repeatable_henchmen = repeatable_henchmen

    @property
    def dialog_replacements(self) -> Dict[int, str]:
        """A dict of dialog ID keys, and strings that should replace the contents of those dialogs
        in the world's dialog bank. This is used to change the dialog run by a certain boss
        depending on which actual boss fight has inhabited its position."""
        return self._dialog_replacements

    def set_dialog_replacements(self, dialog_replacements: Dict[int, str]) -> None:
        """Overwrite a dict of dialog ID keys, and strings that should replace the contents of those
        dialogs in the world's dialog bank.
        This dict is used to change the dialog run by a certain boss
        depending on which actual boss fight has inhabited its position."""
        self._dialog_replacements = dialog_replacements

    @property
    def dialog_replacements_if_mandatory_fights_changed(self) -> Dict[int, str]:
        """A dict of dialog ID keys, and strings that should replace the contents of those dialogs
        in the world's dialog bank, but only IF certain optional boss or henchman replacements
        have been made (such as the Nimbus statue polisher or late Sunken Ship fights).
        """
        return self._dialog_replacements_if_mandatory_fights_changed

    def set_dialog_replacements_if_mandatory_fights_changed(
        self, dialog_replacements_if_mandatory_fights_changed: Dict[int, str]
    ) -> None:
        """Overwrite a dict of dialog ID keys, and strings that should replace the contents of those
        dialogs in the world's dialog bank, but only IF certain optional boss or
        henchman replacements have been made (such as the Nimbus statue polisher
        or late Sunken Ship fights)."""
        self._dialog_replacements_if_mandatory_fights_changed = (
            dialog_replacements_if_mandatory_fights_changed
        )

    @property
    def can_be_immune_to_physical(self) -> bool:
        """If false, this boss can never have physical damage as an immunity.
        This will only be false for very, very specific situations to prevent
        uncompleteable seeds under certain settings combinations."""
        return self._can_be_immune_to_physical

    def set_can_be_immune_to_physical(self, can_be_immune_to_physical: bool) -> None:
        """If false, this boss can never have physical damage as an immunity.
        This will only be false for very, very specific situations to prevent
        uncompleteable seeds under certain settings combinations."""
        self._can_be_immune_to_physical = can_be_immune_to_physical

    @property
    def classname(self):
        """Return the name of this class."""
        return self.__class__.__name__


class MimicBoss(Boss):
    """A specific subclass of boss fights that describe only the final fight in the second
    battle door of Bowser's Keep."""

    _challenge_script: List[ActionScriptCommand] = mimic_subscript

    @property
    def challenge_script(self) -> List[ActionScriptCommand]:
        """The script to run when the boss is summoned by the Keep boss."""
        return self._challenge_script

    def set_challenge_script(self, challenge_script: List[ActionScriptCommand]) -> None:
        """Overwrite the script to run when the boss is summoned by the Keep boss."""
        self._challenge_script = challenge_script
