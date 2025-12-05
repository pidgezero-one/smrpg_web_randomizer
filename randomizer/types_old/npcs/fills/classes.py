"""NPC placeholder classes that are intended to be filled by shuffled bosses and henchmen."""

from typing import List, Optional, Type, Union
from randomizer.entities.bosses.henchmen import (
    BirdettaEggbert,
    CzarHelio,
    DefaultMicrobomb,
    HidonGoombette,
    KingCalamariTinyBloober,
)

from randomizer.types.bosses import (
    Boss,
    Henchman,
    Battlefields,
    HenchmanType,
    SpriteSize,
)
from randomizer.types.numbers import UInt16
from randomizer.types.overworld_scripts.arguments import NPC_0
from randomizer.types.overworld_scripts.arguments.types import AreaObject
from randomizer.types.overworld_scripts.ids import (
    TOTAL_DIALOGS,
    TOTAL_ROOMS,
    R000_DEBUG_ROOM,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    TOTAL_SCRIPTS as TOTAL_EVENTS,
)
from randomizer.types.overworld_scripts.action_scripts.ids import (
    TOTAL_SCRIPTS as TOTAL_ACTIONS,
)


class ModelFill:
    """Base class for a specialized placeholder to be filled by a boss or henchman."""

    _room_id: int = 0
    _fill_type: HenchmanType = HenchmanType.NPC_ONLY
    _npc: AreaObject = NPC_0
    _event_id: Optional[int] = None
    _minigames_only: bool = False
    _repeatable_allowed: bool = True
    _remove_if_empty: bool = False
    _occupant: Optional[Union[Type[Boss], Type[Henchman]]] = None
    _preferred_size: SpriteSize = SpriteSize.SMALL
    _affected_dialog_ids: List[int] = []
    _affected_event_scripts: List[int]
    _affected_action_scripts: List[int]
    _sequence_setter: Optional[int] = None
    _battlefield: Optional[Battlefields] = None
    _can_run_away: bool = False
    _prefer_uncloneable: bool = False
    _prefer_south_only: bool = False

    @property
    def room_id(self) -> UInt16:
        """The room in which the NPC lives."""
        return UInt16(self._room_id)

    def set_room_id(self, room_id: int) -> None:
        """Set the room in which the NPC lives."""
        assert 0 <= room_id <= TOTAL_ROOMS
        self._room_id = room_id

    @property
    def fill_type(self) -> HenchmanType:
        """A special indicator of how this NPC should behave."""
        return self._fill_type

    def set_fill_type(self, fill_type: HenchmanType) -> None:
        """A special indicator of how this NPC should behave."""
        self._fill_type = fill_type

    @property
    def npc(self) -> AreaObject:
        """The specific room object represented by this placeholder."""
        return self._npc

    @property
    def npc_id(self) -> int:
        """The relative ID of the placeholder object within the room."""
        return int(self.npc) - 0x14

    def set_npc(self, npc: AreaObject) -> None:
        """Set the specific room object represented by this placeholder."""
        self._npc = npc

    @property
    def event_id(self) -> Optional[UInt16]:
        """IF this NPC is to run an event, this is the ID of the event it will run.
        It is encouraged to use event const names for this."""
        if self._event_id is None:
            return self._event_id
        return UInt16(self._event_id)

    def set_event_id(self, event_id: Optional[int]) -> None:
        """IF this NPC is to run an event, this is the ID of the event it will run.
        It is encouraged to use event const names for this."""
        if event_id is not None:
            assert 0 <= event_id <= TOTAL_EVENTS
        self._event_id = event_id

    @property
    def minigames_only(self) -> bool:
        """If true, this placeholder will only be targeted if the player has chosen to
        target NPCs that are vital to specific minigames or forced battles."""
        return self._minigames_only

    def set_minigames_only(self, minigames_only: bool) -> None:
        """If true, this placeholder will only be targeted if the player has chosen to
        target NPCs that are vital to specific minigames or forced battles."""
        self._minigames_only = minigames_only

    @property
    def repeatable_allowed(self) -> bool:
        """If false, this placeholder will only accept henchmen designated as unique
        (such as individually named Axem Rangers, etc.)"""
        return self._repeatable_allowed

    def set_repeatable_allowed(self, repeatable_allowed: bool) -> None:
        """If false, this placeholder will only accept henchmen designated as unique
        (such as individually named Axem Rangers, etc.)"""
        self._repeatable_allowed = repeatable_allowed

    @property
    def remove_if_empty(self) -> bool:
        """If true, this placeholder object will be removed from the room entirely
        if no appropriate NPC associated to the shuffled boss can be found to fill it.
        If false, the original NPC from the vanilla game will be kept."""
        return self._remove_if_empty

    def set_remove_if_empty(self, remove_if_empty: bool) -> None:
        """If true, this placeholder object will be removed from the room entirely
        if no appropriate NPC associated to the shuffled boss can be found to fill it.
        If false, the original NPC from the vanilla game will be kept."""
        self._remove_if_empty = remove_if_empty

    @property
    def occupant(self) -> Optional[Union[Type[Boss], Type[Henchman]]]:
        """The boss or henchman object which should fill this placeholder."""
        return self._occupant

    def set_occupant(
        self, occupant: Optional[Union[Type[Boss], Type[Henchman]]]
    ) -> None:
        """Set the boss or henchman object which should fill this placeholder."""
        self._occupant = occupant

    @property
    def preferred_size(self) -> SpriteSize:
        """When an occupant has several differently-sized sprites, this will control
        what the largest allowed sprite is that can fill this placeholder.
        This is important for rooms which may have too many objects to support
        loading a large sprite, and conversely important for rooms where there is room
        for a large sprite that you want to take advantage of where possible."""
        return self._preferred_size

    def set_preferred_size(self, preferred_size: SpriteSize) -> None:
        """When an occupant has several differently-sized sprites, this will control
        what the largest allowed sprite is that can fill this placeholder.
        This is important for rooms which may have too many objects to support
        loading a large sprite, and conversely important for rooms where there is room
        for a large sprite that you want to take advantage of where possible."""
        self._preferred_size = preferred_size

    @property
    def affected_dialog_ids(self) -> List[int]:
        """A list of dialogs which would need to be changed depending on which boss
        or henchman occupies this placeholder.
        It is recommended to use dialog const names for this."""
        for dialog_id in self._affected_dialog_ids:
            assert 0 <= dialog_id <= TOTAL_DIALOGS
        return self._affected_dialog_ids

    def set_affected_dialog_ids(self, affected_dialog_ids: List[int]) -> None:
        """Overwrite the list of dialogs which would need to be changed depending on which boss
        or henchman occupies this placeholder.
        It is recommended to use dialog const names for this."""
        self._affected_dialog_ids = affected_dialog_ids

    @property
    def affected_event_scripts(self) -> List[int]:
        """A list of event scripts which would need to be changed depending on which boss
        or henchman occupies this placeholder.
        It is recommended to use event script const names for this."""
        for dialog_id in self._affected_event_scripts:
            assert 0 <= dialog_id <= TOTAL_EVENTS
        return self._affected_event_scripts

    def set_affected_event_scripts(self, affected_event_scripts: List[int]) -> None:
        """Overwrite the list of event scripts which would need to be changed depending on which
        boss or henchman occupies this placeholder.
        It is recommended to use event script const names for this."""
        self._affected_event_scripts = affected_event_scripts

    @property
    def affected_action_scripts(self) -> List[int]:
        """A list of action scripts which would need to be changed depending on which boss
        or henchman occupies this placeholder.
        It is recommended to use action script const names for this."""
        for dialog_id in self._affected_action_scripts:
            assert 0 <= dialog_id <= TOTAL_ACTIONS
        return self._affected_action_scripts

    def set_affected_action_scripts(self, affected_action_scripts: List[int]) -> None:
        """Overwrite the list of action scripts which would need to be changed depending on which
        boss or henchman occupies this placeholder.
        It is recommended to use action script const names for this."""
        self._affected_action_scripts = affected_action_scripts

    @property
    def sequence_setter(self) -> Optional[UInt16]:
        """The event ID that is responsible for setting the sequences of specific NPCs in the room,
        before the room loads, if the NPC is supposed to display a default sequence other than 0.
        It is recommended to use event script const names for this."""
        if self._sequence_setter is None:
            return self._sequence_setter
        return UInt16(self._sequence_setter)

    def set_sequence_setter(self, sequence_setter: Optional[int]) -> None:
        """The event ID that is responsible for setting the sequences of specific NPCs in the room,
        before the room loads, if the NPC is supposed to display a default sequence other than 0.
        It is recommended to use event script const names for this."""
        if sequence_setter is not None:
            assert 0 <= sequence_setter <= TOTAL_EVENTS
        self._sequence_setter = sequence_setter

    @property
    def battlefield(self) -> Optional[Battlefields]:
        """An optional specific battlefield to be force-loaded by this placeholder,
        if the placeholder is expected to launch a battle."""
        return self._battlefield

    def set_battlefield(self, battlefield: Optional[Battlefields] = None) -> None:
        """Set an optional specific battlefield to be force-loaded by this placeholder,
        if the placeholder is expected to launch a battle."""
        self._battlefield = battlefield

    @property
    def can_run_away(self) -> bool:
        """If false, the player will not be able to run away from the battle, regardless
        of which formation is loaded."""
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        """If false, the player will not be able to run away from the battle, regardless
        of which formation is loaded."""
        self._can_run_away = can_run_away

    @property
    def prefer_uncloneable(self) -> bool:
        """VRAM setting. If true, this placeholder will use the version of the NPC sprite
        which has the 'Cannot Clone' bit set."""
        return self._prefer_uncloneable

    def set_prefer_uncloneable(self, prefer_uncloneable: bool) -> None:
        """VRAM setting. If true, this placeholder will use the version of the NPC sprite
        which has the 'Cannot Clone' bit set."""
        self._prefer_uncloneable = prefer_uncloneable

    @property
    def prefer_south_only(self) -> bool:
        """VRAM setting. If true, this placeholder will use the version of the NPC sprite
        which can only face southeast or southwest. It is preferable to use this when you
        do not expect the NPC to need to face north, as it means less sprites will be
        loaded."""
        return self._prefer_south_only

    def set_prefer_south_only(self, prefer_south_only: bool) -> None:
        """VRAM setting. If true, this placeholder will use the version of the NPC sprite
        which can only face southeast or southwest. It is preferable to use this when you
        do not expect the NPC to need to face north, as it means less sprites will be
        loaded."""
        self._prefer_south_only = prefer_south_only

    def __init__(
        self,
        fill_type: HenchmanType = HenchmanType.NPC_ONLY,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        event_id: Optional[int] = None,
        occupant: Optional[Union[Type[Boss], Type[Henchman]]] = None,
        preferred_size: SpriteSize = SpriteSize.SMALL,
        minigames_only: bool = False,
        repeatable_allowed: bool = False,
        remove_if_empty: bool = False,
        affected_dialog_ids: Optional[List[int]] = None,
        affected_event_scripts: Optional[List[int]] = None,
        affected_action_scripts: Optional[List[int]] = None,
        sequence_setter: Optional[int] = None,
        battlefield: Optional[Battlefields] = None,
        can_run_away: bool = False,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
        if affected_dialog_ids is None:
            affected_dialog_ids = []
        if affected_event_scripts is None:
            affected_event_scripts = []
        if affected_action_scripts is None:
            affected_action_scripts = []
        self.set_fill_type(fill_type)
        self.set_room_id(room_id)
        self.set_npc(npc)
        self.set_event_id(event_id)
        self.set_preferred_size(preferred_size)
        self.set_occupant(occupant)
        self.set_minigames_only(minigames_only)
        self.set_repeatable_allowed(repeatable_allowed)
        self.set_remove_if_empty(remove_if_empty)
        self.set_affected_dialog_ids(affected_dialog_ids)
        self.set_affected_event_scripts(affected_event_scripts)
        self.set_affected_action_scripts(affected_action_scripts)
        self.set_sequence_setter(sequence_setter)
        self.set_battlefield(battlefield)
        self.set_can_run_away(can_run_away)
        self.set_prefer_uncloneable(prefer_uncloneable)
        self.set_prefer_south_only(prefer_south_only)


class StatueFill:
    """Base class for a placeholder to be filled specifically by the statue
    sprite representing the final Nimbus Castle boss."""

    _room_id: int = R000_DEBUG_ROOM
    _npc: AreaObject = NPC_0
    _sequence_setter: Optional[int] = None

    @property
    def room_id(self) -> int:
        """The room in which the NPC lives."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Set the room in which the NPC lives."""
        self._room_id = room_id

    @property
    def npc(self) -> AreaObject:
        """The specific room object represented by this placeholder."""
        return self._npc

    @property
    def npc_id(self) -> int:
        """The relative ID of the placeholder object within the room."""
        return int(self.npc) - 0x14

    def set_npc(self, npc: AreaObject) -> None:
        """Set the specific room object represented by this placeholder."""
        self._npc = npc

    @property
    def sequence_setter(self) -> Optional[UInt16]:
        """The event ID that is responsible for setting the sequences of specific NPCs in the room,
        before the room loads, if the NPC is supposed to display a default sequence other than 0.
        It is recommended to use event script const names for this."""
        if self._sequence_setter is None:
            return self._sequence_setter
        return UInt16(self._sequence_setter)

    def set_sequence_setter(self, sequence_setter: Optional[int]) -> None:
        """The event ID that is responsible for setting the sequences of specific NPCs in the room,
        before the room loads, if the NPC is supposed to display a default sequence other than 0.
        It is recommended to use event script const names for this."""
        if sequence_setter is not None:
            assert 0 <= sequence_setter <= TOTAL_EVENTS
        self._sequence_setter = sequence_setter

    def __init__(
        self, room_id: int, npc: AreaObject, sequence_setter: Optional[int] = None
    ):
        self.set_room_id(room_id)
        self.set_npc(npc)
        self.set_sequence_setter(sequence_setter)


class BossModelFill(ModelFill):
    """Base class for a placeholder to be filled specifically by a boss,
    and not a henchman."""

    def set_occupant(self, occupant: Optional[Type[Boss]]) -> None:
        """Set the boss which should fill this placeholder."""
        super().set_occupant(occupant)

    def __init__(
        self,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        occupant: Optional[Union[Type[Boss], Type[Henchman]]] = None,
        preferred_size: SpriteSize = SpriteSize.SMALL,
        minigames_only: bool = False,
        affected_dialog_ids: Optional[List[int]] = None,
        affected_event_scripts: Optional[List[int]] = None,
        affected_action_scripts: Optional[List[int]] = None,
        sequence_setter: Optional[int] = None,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
        if affected_dialog_ids is None:
            affected_dialog_ids = []
        if affected_event_scripts is None:
            affected_event_scripts = []
        if affected_action_scripts is None:
            affected_action_scripts = []
        super().__init__(
            fill_type=HenchmanType.BOSS,
            room_id=room_id,
            npc=npc,
            occupant=occupant,
            preferred_size=preferred_size,
            minigames_only=minigames_only,
            affected_dialog_ids=affected_dialog_ids,
            affected_event_scripts=affected_event_scripts,
            affected_action_scripts=affected_action_scripts,
            sequence_setter=sequence_setter,
            prefer_uncloneable=prefer_uncloneable,
            prefer_south_only=prefer_south_only,
        )


class UniqueHenchmanFill(ModelFill):
    """Base class for a placeholder to be filled specifically by a unique henchman
    (such as a named Axem Ranger), and not a boss, nor a repeatable henchmen
    (such as a pogo Shy Guy)."""

    def set_occupant(self, occupant: Optional[Type[Henchman]]) -> None:
        """Set the henchman which should fill this placeholder."""
        super().set_occupant(occupant)

    def __init__(
        self,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        occupant: Optional[Type[Henchman]] = None,
        minigames_only: bool = False,
        repeatable_allowed: bool = False,
        remove_if_empty: bool = False,
        fill_type: HenchmanType = HenchmanType.NPC_ONLY,
        event_id: Optional[int] = None,
        affected_dialog_ids: Optional[List[int]] = None,
        affected_event_scripts: Optional[List[int]] = None,
        affected_action_scripts: Optional[List[int]] = None,
        sequence_setter: Optional[int] = None,
        battlefield: Optional[Battlefields] = None,
        can_run_away: bool = False,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
        if affected_dialog_ids is None:
            affected_dialog_ids = []
        if affected_event_scripts is None:
            affected_event_scripts = []
        if affected_action_scripts is None:
            affected_action_scripts = []
        super().__init__(
            fill_type=fill_type,
            room_id=room_id,
            npc=npc,
            event_id=event_id,
            occupant=occupant,
            preferred_size=SpriteSize.SMALL,
            minigames_only=minigames_only,
            repeatable_allowed=repeatable_allowed,
            remove_if_empty=remove_if_empty,
            affected_dialog_ids=affected_dialog_ids,
            affected_event_scripts=affected_event_scripts,
            affected_action_scripts=affected_action_scripts,
            sequence_setter=sequence_setter,
            battlefield=battlefield,
            can_run_away=can_run_away,
            prefer_uncloneable=prefer_uncloneable,
            prefer_south_only=prefer_south_only,
        )


class RepeatableHenchmanFill(ModelFill):
    """Base class for a placeholder to be filled specifically by a generic henchman
    which has no narrative restrictions, such as a pogo Shy Guy from the occupied
    Mushroom Kingdom, as opposed to a unique character such as Axem Green."""

    def set_occupant(self, occupant: Optional[Type[Henchman]]) -> None:
        """Set the henchman which should fill this placeholder."""
        super().set_occupant(occupant)

    def __init__(
        self,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        occupant: Optional[Type[Henchman]] = None,
        minigames_only: bool = False,
        remove_if_empty: bool = False,
        fill_type: HenchmanType = HenchmanType.NPC_ONLY,
        event_id: Optional[int] = None,
        affected_dialog_ids: Optional[List[int]] = None,
        affected_event_scripts: Optional[List[int]] = None,
        affected_action_scripts: Optional[List[int]] = None,
        sequence_setter: Optional[int] = None,
        battlefield: Optional[Battlefields] = None,
        can_run_away: bool = False,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
        if affected_dialog_ids is None:
            affected_dialog_ids = []
        if affected_event_scripts is None:
            affected_event_scripts = []
        if affected_action_scripts is None:
            affected_action_scripts = []
        super().__init__(
            fill_type=fill_type,
            room_id=room_id,
            npc=npc,
            event_id=event_id,
            occupant=occupant,
            preferred_size=SpriteSize.SMALL,
            minigames_only=minigames_only,
            repeatable_allowed=True,
            remove_if_empty=remove_if_empty,
            affected_dialog_ids=affected_dialog_ids,
            affected_event_scripts=affected_event_scripts,
            affected_action_scripts=affected_action_scripts,
            sequence_setter=sequence_setter,
            battlefield=battlefield,
            can_run_away=can_run_away,
            prefer_uncloneable=prefer_uncloneable,
            prefer_south_only=prefer_south_only,
        )


class TinyHenchmanFill(RepeatableHenchmanFill):
    """Base class for a placeholder to be filled specifically by a generic henchman,
    specifically one that uses a tiny sprite. This is exclusively used to replace
    the exploding microbombs thrown by Punchinello in the Mines boss room."""

    def set_occupant(self, occupant: Optional[Type[Henchman]]) -> None:
        """Set the henchman which should fill this placeholder."""
        if occupant not in [
            KingCalamariTinyBloober,
            DefaultMicrobomb,
            CzarHelio,
            HidonGoombette,
            BirdettaEggbert,
        ]:
            occupant = None
        super().set_occupant(occupant)
