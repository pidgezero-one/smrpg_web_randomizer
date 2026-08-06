"""Generate randomizer/data/rooms/sprite_loader_events.py.

Maps each room to its reserved *_SHUFFLED_NPC_ANIMATION_LOADER stub -- an empty
event script already invoked from that room's loader chain, reserved for
per-object sprite setup.

Resolution is by nearest caller: find each stub's call site, then walk outward
from each room's entrance_event and take the stub reachable in the fewest hops.
Anything still ambiguous raises, so it is settled by hand at generation time
rather than silently at seed time.

Edge detection follows two kinds of evidence: a direct call to another event
(RunEventAsSubroutine/JmpToEvent/RunEventAtReturn), and a cross-script label
reference (a destination list naming a label defined in a different script's
text, e.g. script_1145.py jumping to "EVENT_1146_action_queue_0", a label
script_1146.py itself defines). The second kind is gated on two independent
checks: the label must be defined exactly once corpus-wide (so its target is
unambiguous), and it must be referenced as a jump destination somewhere (so
it is live control flow, not a decorative identifier= tag). Trusting a
mismatched string on either check alone would let a future copy-paste bug
silently substitute a wrong nearest stub, with no tie and no ValueError.

Both checks are independently load-bearing, not redundant with each other --
script_3797.py carries a stray identifier="EVENT_2064_action_queue_11", the
same string script_2064.py uses for its own label. That string IS referenced
(script_2064.py's own JmpIfBitSet(...) jumps to it), so the reference check
alone would not catch it; what disqualifies it is that it is now DEFINED in
two places (2064 and 3797), which only the uniqueness check catches.
Dropping the uniqueness check would accept a false 3797->2064 edge; dropping
the reference check would reject every mismatched edge outright, including
the genuine 1145->1146 one room 315 depends on. (Verified by ablation --
see .claude/tests/test_sprite_loader_events.py.)

An accepted edge always resolves to the script that actually contains the
identifier= tag (definitions[0]), never to the digits embedded in the
label's own name. That is what keeps every other mismatched-but-valid edge
in the corpus sound: even a label whose name embeds the wrong number can
only ever resolve to where it is truly defined, so at worst it produces a
harmless self-loop rather than a false edge to an unrelated script. See
_LABEL and _label_registries.

Run: patchvenv/bin/python manage.py sprite_loader_events
"""
import collections
import pathlib
import re

from django.core.management.base import BaseCommand

SCRIPT_DIR = pathlib.Path("randomizer/data/overworld_scripts/event/scripts")
NAMES = pathlib.Path("randomizer/data/variables/event_script_names.py")
ROOM_DIR = pathlib.Path("randomizer/data/rooms")
OUTPUT = pathlib.Path("randomizer/data/rooms/sprite_loader_events.py")

_CALL = re.compile(r"(?:RunEventAsSubroutine|JmpToEvent|RunEventAtReturn)\((E\d+_\w+)")

# Matches every EVENT_<script>_<name> label string in a script's text, whether
# it is a definition (an identifier="..." tag, group 1 present) or a
# reference (a destination-list entry such as Jmp([...]) or
# JmpIfBitSet(..., [...]), group 1 absent -- anything not immediately preceded
# by identifier=).
_LABEL = re.compile(r'(identifier=)?"(EVENT_(\d+)_\w+)"')

# Rooms where the nearest-caller BFS finds two (or more) stubs tied at the same
# distance. Resolved by hand and consulted before the BFS runs so the tie is
# never reached. A value of None means the room has no legitimate stub of its
# own -- excluded from the map rather than forced onto an arbitrary pick.
#
# room 258 R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR: BFS ties stub 794
# E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER against stub 878
# E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER. "TOWER_BALCONY" names the
# room; "TOWER_EXTERIOR" does not.
#
# room 454 R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS: BFS ties stub 850
# (KEEP_BATTLE_DOOR_1A) against stub 852 (KEEP_BATTLE_DOOR_2A) at depth 4,
# reached through the lobby's door-selection dispatch (script_3376.py ->
# KEEP_DOOR_N_CONTAINER -> KEEP_ENTER_*_BATTLE_ROOM -> *_BATTLE_ROOM_LOADER)
# branching across six mutually-exclusive door choices. Neither stub -- nor
# the other four sibling KEEP_BATTLE_DOOR_* stubs -- belongs to the lobby:
# each belongs to one of six distinct battle-room destinations (rooms 376,
# 377, 459-462), and each of those rooms reaches its own stub directly (one
# hop) from its own entrance_event (confirmed for room 459 -> 850 and room
# 462 -> 852). The lobby itself never calls a *_SHUFFLED_NPC_ANIMATION_LOADER
# except through those six branches, so it has no stub of its own.
# room 496 R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE: pre-hardening,
# BFS tied stub 858 (INNER_FACTORY_4TH_ROOM) against stub 815 (DOJO) at depth
# 2. Both are false claims. The 815 path ran through a stray identifier
# inside script_3797.py, identifier="EVENT_2064_action_queue_11" -- the
# same string script_2064.py uses for its own label, which script_2064.py
# DOES jump to (so the string is referenced; see the module docstring). What
# disqualifies it is that it is defined in two places (2064 and 3797), which
# the hardened _LABEL gate now rejects outright, making 815 unreachable from
# this room. The 858 path is real (script_3797.py conditionally does
# EnterArea(room_id=R470_...) + JmpToEvent(E2601_FACTORY_4TH_ROOM_LOADER) as
# one of three post-boss warp destinations) but 858 belongs to room 470,
# which reaches it directly (one hop) from its own entrance_event, so this
# override remains needed regardless -- room 496 has no stub of its own.
#
# The remaining overrides resolve rooms whose BFS lands -- individually,
# with no internal tie -- on a stub some other room also independently and
# more legitimately claims. Consulting this dict before the BFS keeps the
# rejected room out of the race so the rightful room resolves normally; the
# global "claimed by more than one room" check still guards every case that
# isn't listed here.
#
# stub 859 E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_...: rooms 406 and 509
# each call it directly (one hop) from their own entrance_event --
# script_2641.py (room 406's own E2641_FACTORY_1ST_ROOM_LOADER_AFTER_FIGHT)
# and script_3792.py (room 509's own E3792_FACTORY_FINAL_BOSS_ROOM_LOADER)
# both do RunEventAsSubroutine(E0859_...) in the standard pre-FadeInFromBlack
# position. The stub's name (INNER_FACTORY_1ST_ROOM_POST_FIGHT) matches room
# 406 (R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, "1st room", "after fight")
# word for word; room 509 is R509_FACTORY_GROUNDS_SMITHYS_PAD, unrelated by
# name. Room 509's call is presumably inherited from room 406's loader as a
# template and never repointed -- excluded so room 406 resolves cleanly.
#
# stub 795 E0795_ENDING_CREDITS_CHAPEL_...: rooms 441 and 506 both reach it,
# but only room 506 (R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_
# VALENTINA -- the chapel scene itself) does so directly (two hops) from its
# own entrance_event E2294_ENDING_CREDITS_WEDDING_LOADER. Room 441
# (R441_ENDING_CREDITS_TOADOFSKY_CONDUCTS_CHOIR, a different vignette) only
# reaches it by continuing three hops down the same linear, shared
# ending-credits scene chain (Toadofsky -> red star -> wedding logic ->
# chapel) that strings every credits vignette together in playback order.
# Excluded so room 506 resolves cleanly.
#
# stub 1192 E1192_ENDING_CREDITS_KEEP_...: claimed by 14 unrelated rooms
# (room 14 Mushroom Way, 92 casino, 108 Moleville, etc.), none related to
# Bowser's Keep. Each has some path to E3885_END_GAME (game over / ending
# trigger), and END_GAME's chain merges into the same linear ending-credits
# sequence (.../3804 CORONATION_NPCS/3803 GREEN_STAR/2629 KEEP_OPENER/2622
# KEEP/1192) that plays every vignette back to back -- so any room that can
# reach the credits at all eventually "sees" every later scene's stub,
# including this one. The semantically obvious owner,
# R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, does not rescue
# this: its own entrance_event is the generic E0015_STANDARD_ROOM_LOADER (it
# is entered by the credits sequence driving straight into the loader chain,
# bypassing entrance_event, like the other post-boss EnterArea(...,
# run_entrance_event=False) transitions above), so it independently resolves
# to no stub at all. Stub 1192 is left unclaimed rather than assigning it to
# any of the 14 unrelated rooms.
OVERRIDES: dict[int, int | None] = {
    258: 794,
    454: None,
    496: None,
    509: None,
    441: None,
    103: None,
    108: None,
    14: None,
    152: None,
    153: None,
    186: None,
    199: None,
    269: None,
    271: None,
    324: None,
    433: None,
    508: None,
    92: None,
}


def _load():
    names = NAMES.read_text()
    name_to_id = {
        m.group(1): int(m.group(2))
        for m in re.finditer(r"^(E(\d+)_\w+)\s*=\s*\d+", names, re.M)
    }
    stub_ids = {
        int(m.group(1))
        for m in re.finditer(
            r"^E(\d+)_\w*SHUFFLED_NPC_ANIMATION_LOADER\s*=", names, re.M
        )
    }
    scripts = {}
    for path in SCRIPT_DIR.glob("script_*.py"):
        match = re.search(r"script_(\d+)", path.name)
        if match is not None:
            scripts[int(match.group(1))] = path.read_text()
    return name_to_id, stub_ids, scripts


def _label_registries(scripts: dict[int, str]) -> tuple[dict[str, list[int]], set[str]]:
    """Corpus-wide bookkeeping used to validate mismatched _LABEL edges.

    defined_in: label string -> ids of every script whose text defines it via
    identifier="...". A label is only safe to use as a cross-script edge
    target when this list has exactly one entry -- if it is defined nowhere,
    or in more than one place, which script it actually names is unknown or
    ambiguous.

    referenced: every label that appears at least once as a destination-list
    entry (not immediately preceded by identifier=) anywhere in the corpus.
    A label absent from this set is never actually jumped to by anything --
    a decorative tag, not evidence of control flow reaching that script.
    """
    defined_in: dict[str, list[int]] = collections.defaultdict(list)
    referenced: set[str] = set()
    for script_id, text in scripts.items():
        for m in _LABEL.finditer(text):
            label = m.group(2)
            if m.group(1) is not None:
                defined_in[label].append(script_id)
            else:
                referenced.add(label)
    return dict(defined_in), referenced


def _edges(
    script_id: int,
    name_to_id,
    scripts,
    defined_in: dict[str, list[int]],
    referenced: set[str],
) -> set[int]:
    text = scripts.get(script_id, "")
    out = set()
    for m in _CALL.finditer(text):
        target = name_to_id.get(m.group(1))
        if target is not None:
            out.add(target)
    for m in _LABEL.finditer(text):
        digits = int(m.group(3))
        if digits == script_id:
            # Self-match: the label names the script it was found in. BFS
            # already has this node in seen, so adding it is a no-op.
            out.add(digits)
            continue
        # Mismatched: the label names a script other than the one its text
        # was found in. Only trust that as a real cross-script edge if the
        # label is unambiguous (defined exactly once, corpus-wide) AND is
        # actually used as a jump destination somewhere -- otherwise it is
        # indistinguishable from a copy-pasted identifier= tag that never
        # gets jumped to.
        label = m.group(2)
        definitions = defined_in.get(label, [])
        if len(definitions) == 1 and label in referenced:
            out.add(definitions[0])
    return out


def build_map() -> dict[int, int]:
    """room_id -> stub event id, resolved by nearest caller."""
    name_to_id, stub_ids, scripts = _load()
    defined_in, referenced = _label_registries(scripts)

    result: dict[int, int] = {}
    for path in sorted(ROOM_DIR.glob("room_*.py")):
        match = re.search(r"room_(\d+)", path.name)
        if match is None:
            continue
        room_id = int(match.group(1))
        if room_id in OVERRIDES:
            override = OVERRIDES[room_id]
            if override is not None:
                result[room_id] = override
            continue
        entry = re.search(r"entrance_event=(E\d+_\w+)", path.read_text())
        if entry is None or entry.group(1) not in name_to_id:
            continue

        # Breadth-first so the first stub found is the nearest one.
        start = name_to_id[entry.group(1)]
        seen = {start}
        frontier = collections.deque([start])
        nearest: list[int] = []
        depth_of_hit = None
        depth = {start: 0}
        while frontier:
            node = frontier.popleft()
            if depth_of_hit is not None and depth[node] > depth_of_hit:
                break
            if node in stub_ids:
                depth_of_hit = depth[node]
                nearest.append(node)
            for nxt in _edges(node, name_to_id, scripts, defined_in, referenced):
                if nxt not in seen:
                    seen.add(nxt)
                    depth[nxt] = depth[node] + 1
                    frontier.append(nxt)
        if len(nearest) > 1:
            raise ValueError(
                f"room {room_id}: {len(nearest)} stubs tied at the same distance "
                f"({sorted(nearest)}). Resolve by hand before regenerating."
            )
        if nearest:
            result[room_id] = nearest[0]

    owners = collections.Counter(result.values())
    shared = {stub: n for stub, n in owners.items() if n > 1}
    if shared:
        raise ValueError(f"stubs claimed by more than one room: {shared}")
    return dict(sorted(result.items()))


HEADER = '''"""Room to reserved sprite-loader stub. GENERATED -- do not edit by hand.

Regenerate with: patchvenv/bin/python manage.py sprite_loader_events
Drift is caught by .claude/tests/test_sprite_loader_events.py

Each value is an empty *_SHUFFLED_NPC_ANIMATION_LOADER event already invoked from
that room's loader chain, reserved for per-object sprite setup.
"""
'''


class Command(BaseCommand):
    help = "Generate the room-to-sprite-loader-stub map."

    def handle(self, *args, **options):
        mapping = build_map()
        lines = [HEADER, "", "ROOM_SPRITE_LOADER: dict[int, int] = {"]
        for room_id, event_id in mapping.items():
            lines.append(f"    {room_id}: {event_id},")
        lines.append("}")
        lines.append("")
        OUTPUT.write_text("\n".join(lines))
        self.stdout.write(f"wrote {OUTPUT}: {len(mapping)} rooms mapped")
