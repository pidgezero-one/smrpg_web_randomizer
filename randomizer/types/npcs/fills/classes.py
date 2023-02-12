from typing import List, Optional, Type, Union
from randomizer.entities.bosses.henchmen import (
    BirdettaEggbert,
    CzarHelio,
    DefaultMicrobomb,
    HidonGoombette,
    KingCalamariTinyBloober,
)
from randomizer.types.bosses.classes import Boss, Henchman
from randomizer.types.bosses.enums import Battlefields, HenchmanType, SpriteSize
from randomizer.types.numbers.classes import UInt16
from randomizer.types.overworld_scripts.constants.area_objects import NPC_0
from randomizer.types.overworld_scripts.constants.classes import AreaObject
from randomizer.types.overworld_scripts.constants.misc import TOTAL_DIALOGS, TOTAL_ROOMS
from randomizer.types.overworld_scripts.constants.room_names import R000_DEBUG_ROOM
from randomizer.types.overworld_scripts.event_scripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_EVENTS,
)
from randomizer.types.overworld_scripts.action_scripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_ACTIONS,
)


class ModelFill:
    _room_id: int = 0
    _fill_type: HenchmanType = HenchmanType.NPCOnly
    _npc: AreaObject = NPC_0
    _event_id: Optional[int] = None
    _minigames_only: bool = False
    _repeatable_allowed: bool = True
    _remove_if_empty: bool = False
    _occupant: Optional[Union[Type[Boss], Type[Henchman]]] = None
    _preferred_size: SpriteSize = SpriteSize.Small
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
        return UInt16(self._room_id)

    def set_room_id(self, room_id: int) -> None:
        assert 0 <= room_id <= TOTAL_ROOMS
        self._room_id = room_id

    @property
    def fill_type(self) -> HenchmanType:
        return self._fill_type

    def set_fill_type(self, fill_type: HenchmanType) -> None:
        self._fill_type = fill_type

    @property
    def npc(self) -> AreaObject:
        return self._npc

    @property
    def npc_id(self) -> int:
        return int(self.npc) - 0x14

    def set_npc(self, npc: AreaObject) -> None:
        self._npc = npc

    @property
    def event_id(self) -> Optional[UInt16]:
        if self._event_id is None:
            return self._event_id
        return UInt16(self._event_id)

    def set_event_id(self, event_id: Optional[int]) -> None:
        if event_id is not None:
            assert 0 <= event_id <= TOTAL_EVENTS
        self._event_id = event_id

    @property
    def minigames_only(self) -> bool:
        return self._minigames_only

    def set_minigames_only(self, minigames_only: bool) -> None:
        self._minigames_only = minigames_only

    @property
    def repeatable_allowed(self) -> bool:
        return self._repeatable_allowed

    def set_repeatable_allowed(self, repeatable_allowed: bool) -> None:
        self._repeatable_allowed = repeatable_allowed

    @property
    def remove_if_empty(self) -> bool:
        return self._remove_if_empty

    def set_remove_if_empty(self, remove_if_empty: bool) -> None:
        self._remove_if_empty = remove_if_empty

    @property
    def occupant(self) -> Optional[Union[Type[Boss], Type[Henchman]]]:
        return self._occupant

    def set_occupant(
        self, occupant: Optional[Union[Type[Boss], Type[Henchman]]]
    ) -> None:
        self._occupant = occupant

    @property
    def preferred_size(self) -> SpriteSize:
        return self._preferred_size

    def set_preferred_size(self, preferred_size: SpriteSize) -> None:
        self._preferred_size = preferred_size

    @property
    def affected_dialog_ids(self) -> List[int]:
        for id in self._affected_dialog_ids:
            assert 0 <= id <= TOTAL_DIALOGS
        return self._affected_dialog_ids

    def set_affected_dialog_ids(self, affected_dialog_ids: List[int]) -> None:
        self._affected_dialog_ids = affected_dialog_ids

    @property
    def affected_event_scripts(self) -> List[int]:
        for id in self._affected_event_scripts:
            assert 0 <= id <= TOTAL_EVENTS
        return self._affected_event_scripts

    def set_affected_event_scripts(self, affected_event_scripts: List[int]) -> None:
        self._affected_event_scripts = affected_event_scripts

    @property
    def affected_action_scripts(self) -> List[int]:
        for id in self._affected_action_scripts:
            assert 0 <= id <= TOTAL_ACTIONS
        return self._affected_action_scripts

    def set_affected_action_scripts(self, affected_action_scripts: List[int]) -> None:
        self._affected_action_scripts = affected_action_scripts

    @property
    def sequence_setter(self) -> Optional[UInt16]:
        if self._sequence_setter is None:
            return self._sequence_setter
        return UInt16(self._sequence_setter)

    def set_sequence_setter(self, sequence_setter: Optional[int]) -> None:
        if sequence_setter is not None:
            assert 0 <= sequence_setter <= TOTAL_EVENTS
        self._sequence_setter = sequence_setter

    @property
    def battlefield(self) -> Optional[Battlefields]:
        return self._battlefield

    def set_battlefield(self, battlefield: Optional[Battlefields] = None) -> None:
        self._battlefield = battlefield

    @property
    def can_run_away(self) -> bool:
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        self._can_run_away = can_run_away

    @property
    def prefer_uncloneable(self) -> bool:
        return self._prefer_uncloneable

    def set_prefer_uncloneable(self, prefer_uncloneable: bool) -> None:
        self._prefer_uncloneable = prefer_uncloneable

    @property
    def prefer_south_only(self) -> bool:
        return self._prefer_south_only

    def set_prefer_south_only(self, prefer_south_only: bool) -> None:
        self._prefer_south_only = prefer_south_only

    def __init__(
        self,
        fill_type: HenchmanType = HenchmanType.NPCOnly,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        event_id: Optional[int] = None,
        occupant: Optional[Union[Type[Boss], Type[Henchman]]] = None,
        preferred_size: SpriteSize = SpriteSize.Small,
        minigames_only: bool = False,
        repeatable_allowed: bool = False,
        remove_if_empty: bool = False,
        affected_dialog_ids: List[int] = [],
        affected_event_scripts: List[int] = [],
        affected_action_scripts: List[int] = [],
        sequence_setter: Optional[int] = None,
        battlefield: Optional[Battlefields] = None,
        can_run_away: bool = False,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
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
    _room_id: int = R000_DEBUG_ROOM
    _npc: AreaObject = NPC_0
    _sequence_setter: Optional[int] = None

    @property
    def room_id(self) -> int:
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        self._room_id = room_id

    @property
    def npc(self) -> AreaObject:
        return self._npc

    @property
    def npc_id(self) -> int:
        return int(self.npc) - 0x14

    def set_npc(self, npc: AreaObject) -> None:
        self._npc = npc

    @property
    def sequence_setter(self) -> Optional[UInt16]:
        if self._sequence_setter is None:
            return self._sequence_setter
        return UInt16(self._sequence_setter)

    def set_sequence_setter(self, sequence_setter: Optional[int]) -> None:
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
    def set_occupant(
        self, occupant: Optional[Union[Type[Boss], Type[Henchman]]]
    ) -> None:
        super().set_occupant(occupant)

    def __init__(
        self,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        occupant: Optional[Union[Type[Boss], Type[Henchman]]] = None,
        preferred_size: SpriteSize = SpriteSize.Small,
        minigames_only: bool = False,
        affected_dialog_ids: List[int] = [],
        affected_event_scripts: List[int] = [],
        affected_action_scripts: List[int] = [],
        sequence_setter: Optional[int] = None,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
        super().__init__(
            fill_type=HenchmanType.Boss,
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
    def __init__(
        self,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        occupant: Optional[Type[Henchman]] = None,
        minigames_only: bool = False,
        repeatable_allowed: bool = False,
        remove_if_empty: bool = False,
        fill_type: HenchmanType = HenchmanType.NPCOnly,
        event_id: Optional[int] = None,
        affected_dialog_ids: List[int] = [],
        affected_event_scripts: List[int] = [],
        affected_action_scripts: List[int] = [],
        sequence_setter: Optional[int] = None,
        battlefield: Optional[Battlefields] = None,
        can_run_away: bool = False,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
        super().__init__(
            fill_type=fill_type,
            room_id=room_id,
            npc=npc,
            event_id=event_id,
            occupant=occupant,
            preferred_size=SpriteSize.Small,
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
    def __init__(
        self,
        room_id: int = R000_DEBUG_ROOM,
        npc: AreaObject = NPC_0,
        occupant: Optional[Type[Henchman]] = None,
        minigames_only: bool = False,
        remove_if_empty: bool = False,
        fill_type: HenchmanType = HenchmanType.NPCOnly,
        event_id: Optional[int] = None,
        affected_dialog_ids: List[int] = [],
        affected_event_scripts: List[int] = [],
        affected_action_scripts: List[int] = [],
        sequence_setter: Optional[int] = None,
        battlefield: Optional[Battlefields] = None,
        can_run_away: bool = False,
        prefer_uncloneable: bool = False,
        prefer_south_only: bool = False,
    ):
        super().__init__(
            fill_type=fill_type,
            room_id=room_id,
            npc=npc,
            event_id=event_id,
            occupant=occupant,
            preferred_size=SpriteSize.Small,
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
    def set_occupant(self, occupant: Optional[Type[Henchman]]) -> None:
        if occupant not in [
            KingCalamariTinyBloober,
            DefaultMicrobomb,
            CzarHelio,
            HidonGoombette,
            BirdettaEggbert,
        ]:
            occupant = None
        super().set_occupant(occupant)
