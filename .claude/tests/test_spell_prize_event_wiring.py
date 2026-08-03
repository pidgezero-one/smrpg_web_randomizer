"""Every SpellPrize must point at event scripts that actually teach its spell.

Spell chests are fixed event-script "slots": slot N's chest event hardcodes
`LearnSpell(_, <spell N>, ...)` and shows dialog `DI..._LEARN_SPELL_N`. The
shuffler only swaps the *character* and substitutes the spell/character *names*
into the dialog — it never changes which spell the LearnSpell teaches. So a
prize whose `_chest_event_id` points at the wrong slot silently teaches the
wrong spell AND leaves `CHARACTER` unsubstituted (the name goes to the wrong
dialog). ComeBack/SleepyTime/Mute shipped exactly that way.
"""

import re
from pathlib import Path

import pytest

from randomizer.logic.progression.prizes import SpellPrize

SCRIPT_DIR = (
    Path(__file__).resolve().parent.parent.parent
    / "randomizer" / "data" / "overworld_scripts" / "event" / "scripts"
)


def _spell_prizes() -> list[type[SpellPrize]]:
    out = []
    stack = list(SpellPrize.__subclasses__())
    while stack:
        cls = stack.pop()
        stack.extend(cls.__subclasses__())
        # leaf prizes define both a spell and a chest event
        if "_spell" in cls.__dict__ and "_chest_event_id" in cls.__dict__:
            out.append(cls)
    return out


def _chest_script_text(prize: type[SpellPrize]) -> str:
    n = int(prize._chest_event_id)
    return (SCRIPT_DIR / f"script_{n}.py").read_text()


@pytest.mark.parametrize("prize", _spell_prizes(), ids=lambda c: c.__name__)
def test_chest_event_teaches_the_prizes_spell(prize: type[SpellPrize]):
    text = _chest_script_text(prize)
    m = re.search(r"LearnSpell\(\s*[A-Z_]+\s*,\s*(\w+)\s*,", text)
    assert m, f"{prize.__name__}: no LearnSpell in script_{int(prize._chest_event_id)}.py"
    taught = m.group(1)
    want = prize._spell.__name__
    assert taught == want, (
        f"{prize.__name__}: chest event script_{int(prize._chest_event_id)}.py "
        f"teaches {taught}, but the prize is for {want}"
    )


@pytest.mark.parametrize("prize", _spell_prizes(), ids=lambda c: c.__name__)
def test_chest_event_dialog_matches_prize_dialog(prize: type[SpellPrize]):
    text = _chest_script_text(prize)
    m = re.search(r"RunDialog\(dialog_id=DI(\d+)_", text)
    assert m, f"{prize.__name__}: no RunDialog in script_{int(prize._chest_event_id)}.py"
    shown = int(m.group(1))
    allowed = {int(prize._dialog_id), int(prize._autoterm_dialog_id)}
    assert shown in allowed, (
        f"{prize.__name__}: chest event shows dialog {shown}, but the prize's "
        f"dialog ids are {sorted(allowed)} — CHARACTER name substitution will "
        f"land on the wrong dialog"
    )
