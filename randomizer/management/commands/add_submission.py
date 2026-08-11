"""Add community submissions from GitHub issues to data files.

Usage:
    manage.py add_submission --type wish --issue 123
    manage.py add_submission --type quiz --issue 123 [--non-smrpg]
    manage.py add_submission --type password --issue 123
    manage.py add_submission --type song --issue 123
    manage.py add_submission --type palette --issue 123

    # Specify upstream repo when working from a fork:
    manage.py add_submission --type wish --issue 123 --repo owner/repo
"""
import json
import re
import subprocess
import sys
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from smrpgpatchbuilder.datatypes.dialogs.formatter import (calculate_text_width, format_dialog, format_wish, validate_dialog)

# File paths relative to repository root
REPO_ROOT = Path(settings.BASE_DIR)
WISH_FILE = REPO_ROOT / "randomizer/data/minigames/star_hill_wishes.py"
QUIZ_FILE = REPO_ROOT / "randomizer/data/minigames/quiz_questions.py"
PASSWORD_FILE = REPO_ROOT / "randomizer/data/minigames/ship_password.py"
SONG_FILE = REPO_ROOT / "randomizer/data/minigames/melody_bay.py"
PALETTES_DIR = REPO_ROOT / "randomizer/data/allies/palettes"
FLAGS_FILE = REPO_ROOT / "randomizer/types/flags.py"

# Map character names (lowercase) to (filename, class_prefix, base_class, enum_class)
CHARACTER_MAP = {
    "mario": ("mario.py", "Mario", "MarioPalette", "MarioPaletteOptions"),
    "mallow": ("mallow.py", "Mallow", "MallowPalette", "MallowPaletteOptions"),
    "geno": ("geno.py", "Geno", "GenoPalette", "GenoPaletteOptions"),
    "bowser": ("bowser.py", "Bowser", "BowserPalette", "BowserPaletteOptions"),
    "toadstool": ("toadstool.py", "Toadstool", "ToadstoolPalette", "ToadstoolPaletteOptions"),
    "peach": ("toadstool.py", "Toadstool", "ToadstoolPalette", "ToadstoolPaletteOptions"),  # Alias
}


def fetch_issue(issue_number: int, repo: str | None = None) -> dict:
    """Fetch issue data from GitHub using gh CLI.

    Args:
        issue_number: The GitHub issue number.
        repo: Optional repo in 'owner/repo' format. If not specified,
              uses the current git remote.
    """
    cmd = ["gh", "issue", "view", str(issue_number), "--json", "body,title"]
    if repo:
        cmd.extend(["--repo", repo])
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def parse_issue_body(body: str) -> dict[str, str]:
    """Parse GitHub issue form body into field dict.

    GitHub issue forms render as:
    ### Field Label

    Field Value

    ### Next Field Label
    ...
    """
    fields = {}
    current_field = None
    current_value_lines = []

    for line in body.split("\n"):
        if line.startswith("### "):
            if current_field:
                fields[current_field] = "\n".join(current_value_lines).strip()
            current_field = line[4:].strip()
            current_value_lines = []
        elif current_field:
            current_value_lines.append(line)

    if current_field:
        fields[current_field] = "\n".join(current_value_lines).strip()

    return fields


def escape_string(s: str) -> str:
    """Escape a string for use in Python source code."""
    # Replace backslashes first, then quotes, then newlines
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    s = s.replace("\n", "\\n")
    return s


# Placeholder the minigame shuffler swaps for a "[center]Memo left by X:" header.
WRITER_TOKEN = "%RANDOM_WRITER%"

_PY_ESCAPES = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "'": "'", "\\": "\\"}

# Markers that plain prose would not contain: a backslash escape, the writer
# placeholder, or a trailing control token. Their presence means the field was
# written as source code rather than as text to be formatted.
_SOURCE_MARKER_RE = re.compile(
    r"\\.|" + re.escape(WRITER_TOKEN) + r"|\[(?:await|end|page)\]\s*$"
)


def _decode_escapes(body: str) -> str:
    """Decode the Python escape sequences in a string-literal body."""
    out: list[str] = []
    i = 0
    while i < len(body):
        char = body[i]
        if char == "\\" and i + 1 < len(body):
            escape = body[i + 1]
            # Python leaves an unrecognized escape verbatim, so we do too. The
            # caller flags any backslash that survives.
            out.append(_PY_ESCAPES.get(escape, "\\" + escape))
            i += 2
            continue
        out.append(char)
        i += 1
    return "".join(out)


def unquote_submission(value: str, label: str) -> str:
    """Recover the logical text from a field that was submitted as source code.

    Submitters routinely copy an entry out of a data file to use as a template
    and paste it back verbatim, so a field can arrive as
    ``"%RANDOM_WRITER%\\n\\nHe's not a tadpole.[await]",`` -- surrounding quotes,
    two-character \\n escapes, and the trailing comma included. format_dialog()
    treats those backslashes and quotes as prose and re-wraps the whole literal,
    which is how the "prince" entry landed in the pool double-escaped.

    A backslash has zero width in the dialog font, so it is never intended prose;
    escapes are always decoded when present. Surrounding quotes are only stripped
    alongside another source marker, so a hint that genuinely opens and closes on
    a quoted phrase is left alone.
    """
    text = value.strip()
    # A line copied out of a pool list brings its trailing comma with it.
    if text.endswith(","):
        text = text[:-1].rstrip()

    quoted = len(text) >= 2 and text.startswith('"') and text.endswith('"')
    body = text[1:-1] if quoted else text

    if not _SOURCE_MARKER_RE.search(body):
        return value

    decoded = _decode_escapes(body)
    if quoted:
        print(f"Note ({label}): submitted as a quoted source literal; unquoted it.")
    if decoded != body:
        print(f"Note ({label}): decoded escape sequences to real line breaks.")
    # Nothing should survive decoding as a backslash: it has no glyph, so it
    # renders as nothing. Either the submitter typo'd a line break (writing \R,
    # or \\n) or they escaped a backslash they never meant to type. Context is
    # repr'd so a surviving backslash reads as \\ and a real break as \n.
    for match in re.finditer(r"\\.?", decoded):
        context = decoded[max(0, match.start() - 15):match.end() + 15]
        print(
            f"Warning ({label}): a literal backslash has no glyph and will not render. "
            f"Near {context!r} -- did they mean a line break?"
        )
    return decoded


def has_writer_prefix(hint: str) -> bool:
    """True when a hint already names who wrote it.

    Either the %RANDOM_WRITER% placeholder the shuffler fills in, or a literal
    "[center]Memo left by ...:" header the submitter chose because they want a
    specific character to speak that hint.
    """
    return hint.startswith(WRITER_TOKEN) or hint.startswith("[center]")


def add_wish(fields: dict[str, str]) -> None:
    """Add a Star Hill wish to the wish pool."""
    wish_text = fields.get("Wish text", "")
    if not wish_text:
        print("Error: No wish text found in issue")
        sys.exit(1)

    wish_text = unquote_submission(wish_text, "wish")

    # A wish copied out of the pool already carries [center] and the leading
    # newlines format_wish() adds for vertical centering. Running either step
    # again doubles the prefix and pushes the text off the bottom of the box.
    pre_formatted = wish_text.startswith("[center]")
    if pre_formatted:
        print("Note (wish): already centered; skipping punctuation and centering steps.")

    if not pre_formatted and wish_text[-1] not in ".!?~":
        wish_text += "."

    wish_text = format_dialog(wish_text)
    if not pre_formatted:
        wish_text = "[center]" + format_wish(wish_text)

    warnings = validate_dialog(wish_text)
    for w in warnings:
        print(f"Warning: {w}")

    escaped = escape_string(wish_text)
    new_entry = f'    "{escaped}",\n'

    content = WISH_FILE.read_text()

    # Find the closing bracket of WISH_POOL list (before WISH_DIALOG_IDS)
    pattern = r"(WISH_POOL = wish_strings = \[.*?)(^\])"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print("Error: Could not find WISH_POOL list in file")
        sys.exit(1)

    # Ensure the previous line ends with a comma
    insert_pos = match.end(1)
    before = content[:insert_pos].rstrip()
    if before and not before.endswith(","):
        before += ","
    new_content = before + "\n" + new_entry + content[insert_pos:]

    WISH_FILE.write_text(new_content)
    print(f"Added wish: {wish_text[:50]}...")


def clean_quiz_answer(answer: str) -> str:
    """Clean quiz answer: strip parentheses and trailing periods."""
    answer = answer.strip()
    if answer.startswith("(") and answer.endswith(")"):
        answer = answer[1:-1].strip()
    answer = answer.rstrip(".")
    return answer


def add_quiz_question(fields: dict[str, str], non_smrpg: bool = False) -> None:
    """Add a quiz question to the question pool."""
    question = fields.get("Question text", "")
    correct = fields.get("Right answer", "")
    wrong1 = fields.get("Wrong answer 1", "")
    wrong2 = fields.get("Wrong answer 2", "")

    if not all([question, correct, wrong1, wrong2]):
        print("Error: Missing required fields (question, correct answer, wrong answers)")
        sys.exit(1)

    question = unquote_submission(question, "question").rstrip()
    if question and not question.endswith("?"):
        question += "?"

    correct = clean_quiz_answer(unquote_submission(correct, "correct answer"))
    wrong1 = clean_quiz_answer(unquote_submission(wrong1, "wrong answer 1"))
    wrong2 = clean_quiz_answer(unquote_submission(wrong2, "wrong answer 2"))

    question = format_dialog(question)
    warnings = validate_dialog(question)
    for w in warnings:
        print(f"Warning (question): {w}")

    # Validate each answer fits on one line: " [select]  (ANSWER)" width
    select_prefix = " [select]  "
    for label, answer in [("Correct", correct), ("Wrong 1", wrong1), ("Wrong 2", wrong2)]:
        answer_line = f"{select_prefix}{answer}"
        line_width = calculate_text_width(answer_line)
        max_width = 253  # usable width with default margin
        if line_width > max_width:
            print(f"Error: {label} answer too wide ({line_width}px > {max_width}px): {answer}")
            sys.exit(1)

    question = escape_string(question)
    correct = escape_string(correct)
    wrong1 = escape_string(wrong1)
    wrong2 = escape_string(wrong2)

    new_entry = f'''        Question(
            "{question}",
            "{correct}",
            "{wrong1}",
            "{wrong2}",
        ),
'''

    content = QUIZ_FILE.read_text()

    if non_smrpg:
        pattern = r"(def get_non_smrpg_questions\(\).*?return \[.*?)(^\s*\])"
        func_name = "get_non_smrpg_questions"
    else:
        pattern = r"(def get_smrpg_questions\(\).*?return \[.*?)(^\s*\])"
        func_name = "get_smrpg_questions"

    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print(f"Error: Could not find {func_name}() return list in file")
        sys.exit(1)

    insert_pos = match.end(1)
    new_content = content[:insert_pos] + new_entry + content[insert_pos:]

    QUIZ_FILE.write_text(new_content)
    print(f"Added quiz question to {func_name}(): {question[:50]}...")


def format_credits_name(name: str) -> str:
    """Format name for credits (uppercase, only A-Z, space, period, underscore)."""
    allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ. _")
    result = "".join(c for c in name.upper() if c in allowed)
    return result if result else "ANONYMOUS"


def format_hint_prefix(name: str) -> str:
    """Format the hint prefix."""
    return f"[center]Memo left by {name}:"


REQUIRED_HINT_FIELDS = [
    "Trampoline Room Hint",
    "Paratroopa Room Hint",
    "3D Maze Room Hint",
    "Coin Snake Room Hint",
    "Cannonball Room Hint",
    "Rolling Barrel Room Hint",
]

OPTIONAL_HINT_FIELDS = [f"Optional hint {n}" for n in range(1, 6)]


def add_password(fields: dict[str, str]) -> None:
    """Add a ship password to the password pool."""
    word = fields.get("Your word", "")
    name = fields.get("Your name or handle", "").strip()

    def clean_optional(val: str) -> str | None:
        val = val.strip()
        if not val or val == "_No response_":
            return None
        return val

    required_hints = [(f, fields.get(f, "")) for f in REQUIRED_HINT_FIELDS]
    optional_hints = [(f, clean_optional(fields.get(f, ""))) for f in OPTIONAL_HINT_FIELDS]

    if not word or len(word) != 6:
        print(f"Error: Password must be exactly 6 characters (got: '{word}')")
        sys.exit(1)

    missing = [f for f, hint in required_hints if not hint]
    if missing:
        print(f"Error: All 6 required hints must be provided (missing: {', '.join(missing)})")
        sys.exit(1)

    submitter = name if name else "Anonymous"
    submitter_credits = format_credits_name(name) if name else "ANONYMOUS"
    submitter_hint_prefix = format_hint_prefix(submitter)

    def ensure_await(hint: str) -> str:
        """Ensure hint ends with [await]."""
        if not hint.rstrip().endswith("[await]"):
            return hint + "[await]"
        return hint

    def prepare_hint(hint: str, label: str) -> str:
        """Normalize a submitted hint into the string stored in the pool."""
        hint = unquote_submission(hint, label)
        hint = format_dialog(hint)
        hint = ensure_await(hint)
        # Password hints render centered. A hint that already opens with its own
        # header carries [center] itself; only bare ones need it added to check
        # that centering fits.
        prefix = "" if has_writer_prefix(hint) else "[center]"
        for w in validate_dialog(prefix + hint):
            print(f"Warning ({label}): {w}")
        return hint

    def format_hint(hint: str, label: str) -> str:
        hint = prepare_hint(hint, label)
        # A hint that already names its writer -- because the submitter copied an
        # existing entry, or wants a specific character to speak it -- must not
        # get a second header stacked on top.
        if not has_writer_prefix(hint):
            hint = f"{WRITER_TOKEN}\n\n{hint}"
        return f'"{escape_string(hint)}"'

    def format_optional_hint(hint: str | None, label: str) -> str:
        if not hint:
            return "None"
        return f'"{escape_string(prepare_hint(hint, label))}"'

    word_escaped = escape_string(word.lower())

    formatted_required = [format_hint(hint, label) for label, hint in required_hints]
    formatted_optional = [format_optional_hint(hint, label) for label, hint in optional_hints]

    new_entry = f'''    Password(
        "{word_escaped}",
        {formatted_required[0]},
        {formatted_required[1]},
        {formatted_required[2]},
        {formatted_required[3]},
        {formatted_required[4]},
        {formatted_required[5]},
        {formatted_optional[0]},
        {formatted_optional[1]},
        {formatted_optional[2]},
        {formatted_optional[3]},
        {formatted_optional[4]},
        submitter="{escape_string(submitter)}",
        submitter_credits="{submitter_credits}",
        submitter_hint_prefix="{escape_string(submitter_hint_prefix)}",
    ),
'''

    content = PASSWORD_FILE.read_text()

    pattern = r"(^pool = \[.*?)(^\])"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print("Error: Could not find pool list in file")
        sys.exit(1)

    insert_pos = match.end(1)
    new_content = content[:insert_pos] + new_entry + content[insert_pos:]

    PASSWORD_FILE.write_text(new_content)
    print(f"Added password: {word}")


def parse_song_notation(notation: str) -> list[tuple[str, int]]:
    """Parse song notation from the composer tool.

    Expected format examples:
    - "[(Do, 35), (Re, 18), (Mi, 42)]" - Python tuple format
    - "Do:35, Re:18, Mi:42" - colon-separated pairs
    - "Do-35, Re-18, Mi-42" - dash-separated pairs
    - "Do 35, Re 18, Mi 42" - space-separated pairs
    """
    notes = []

    tuple_pattern = r"\(\s*(Fa|So|La|Ti|Do|Re|Mi)\s*,\s*(\d+)\s*\)"
    matches = list(re.finditer(tuple_pattern, notation, re.IGNORECASE))
    if matches:
        for match in matches:
            note_name = match.group(1).capitalize()
            duration = int(match.group(2))
            notes.append((note_name, duration))
        return notes

    pair_pattern = r"(Fa|So|La|Ti|Do|Re|Mi)\s*[:\-\s]\s*(\d+)"
    matches = list(re.finditer(pair_pattern, notation, re.IGNORECASE))
    if matches:
        for match in matches:
            note_name = match.group(1).capitalize()
            duration = int(match.group(2))
            notes.append((note_name, duration))
        return notes

    simple_pattern = r"\b(Fa|So|La|Ti|Do|Re|Mi)\b"
    for match in re.finditer(simple_pattern, notation, re.IGNORECASE):
        note_name = match.group(1).capitalize()
        notes.append((note_name, 35))  # Default duration

    return notes


def strip_markdown_ticks(s: str) -> tuple[str, bool]:
    """Remove markdown code ticks and return (cleaned_string, had_ticks)."""
    had_ticks = '`' in s
    s = s.replace('`', '')
    return s, had_ticks


def add_song(fields: dict[str, str]) -> None:
    """Add a Melody Bay song to the song list."""
    notation = fields.get("Tune notation", "")
    songname = fields.get("Name of your song", "")
    name = fields.get("Your name or handle", "").strip()
    hint1 = fields.get("Hint 1", "")
    hint2_pond = fields.get("Hint 2 (pond)", "")
    hint2_mines = fields.get("Hint 2 (mines)", "")

    if not all([notation, songname, hint1, hint2_pond, hint2_mines]):
        print("Error: Missing required fields")
        sys.exit(1)

    notes = parse_song_notation(notation)
    if not notes:
        print(f"Error: Could not parse song notation: {notation}")
        sys.exit(1)

    if len(notes) > 8:
        print(f"Warning: Song has {len(notes)} notes, but max is 8. Truncating.")
        notes = notes[:8]

    submitter = name if name else "Anonymous"
    submitter_credits = format_credits_name(name) if name else "ANONYMOUS"

    note_names = " ".join(n for n, _ in notes)
    scroll_text = f"\\n          {note_names}[await]"

    hint1, hint1_ticks = strip_markdown_ticks(hint1)
    hint2_pond, hint2_ticks = strip_markdown_ticks(hint2_pond)
    hint2_mines, hint3_ticks = strip_markdown_ticks(hint2_mines)

    def ensure_await(hint: str) -> str:
        if not hint.rstrip().endswith("[await]"):
            return hint + "[await]"
        return hint

    hint1 = unquote_submission(hint1, "Hint 1")
    hint2_pond = unquote_submission(hint2_pond, "Hint 2 (pond)")
    hint2_mines = unquote_submission(hint2_mines, "Hint 2 (mines)")

    hint1 = format_dialog(hint1)
    hint2_pond = format_dialog(hint2_pond)
    hint2_mines = format_dialog(hint2_mines)

    hint1 = ensure_await(hint1)
    hint2_pond = ensure_await(hint2_pond)
    hint2_mines = ensure_await(hint2_mines)

    for label, hint_val in [("Hint 1", hint1), ("Hint 2 (pond)", hint2_pond), ("Hint 2 (mines)", hint2_mines)]:
        warnings = validate_dialog(hint_val)
        for w in warnings:
            print(f"Warning ({label}): {w}")

    songname_escaped = escape_string(songname)
    submitter_escaped = escape_string(submitter)
    hint1_escaped = escape_string(hint1)
    hint2_pond_escaped = escape_string(hint2_pond)
    hint2_mines_escaped = escape_string(hint2_mines)

    notes_str = ", ".join(f"({n}, {d})" for n, d in notes)

    # Use triple quotes if any hint had backticks
    def quote_hint(hint: str, had_ticks: bool) -> str:
        if had_ticks:
            return f'"""{hint}"""'
        # Double quotes, not single: escape_string() escapes " but not ', so a
        # single-quoted hint containing an apostrophe ("It's All the Small Things")
        # closes the literal early and writes a file that won't import. Every other
        # emitter here (wish, quiz, password) already double-quotes for this reason.
        return f'"{hint}"'

    new_entry = f'''    Song(
        [{notes_str}],
        "{songname_escaped}",
        submitter="{submitter_escaped}",
        submitter_credits="{submitter_credits}",
        hint_1={quote_hint(hint1_escaped, hint1_ticks)},
        hint_2={quote_hint(hint2_pond_escaped, hint2_ticks)},
        hint_3={quote_hint(hint2_mines_escaped, hint3_ticks)},
        scroll='{scroll_text}'),
'''

    content = SONG_FILE.read_text()

    pattern = r"(^all_songs = \[.*?)(^\])"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print("Error: Could not find all_songs list in file")
        sys.exit(1)

    insert_pos = match.end(1)
    new_content = content[:insert_pos] + new_entry + content[insert_pos:]

    SONG_FILE.write_text(new_content)
    print(f"Added song: {songname}")


def parse_palette_colors(text: str) -> list[int]:
    """Parse color values from text. Supports 0xRRGGBB and #RRGGBB formats."""
    colors = []
    # Match hex colors: 0xRRGGBB, #RRGGBB, or just RRGGBB
    pattern = r"(?:0x|#)?([0-9A-Fa-f]{6})\b"
    for match in re.finditer(pattern, text):
        hex_value = match.group(1)
        colors.append(int(hex_value, 16))
    return colors


def generate_palette_class_name(character_prefix: str, palette_name: str) -> str:
    """Generate a class name from character and palette name."""
    clean_name = re.sub(r"[^a-zA-Z0-9\s_]", "", palette_name)
    words = clean_name.split()
    pascal_name = "".join(word.capitalize() for word in words)
    return f"{character_prefix}{pascal_name}"


def generate_palette_enum_name(palette_name: str) -> str:
    """Generate an enum name from palette name (SCREAMING_SNAKE_CASE)."""
    clean_name = re.sub(r"[^a-zA-Z0-9\s]", "", palette_name)
    words = clean_name.split()
    return "_".join(word.upper() for word in words if word)


def add_palette_enum_to_flags(enum_class_name: str, enum_name: str, palette_name: str) -> None:
    """Add a new palette option to the appropriate enum in flags.py.

    Args:
        enum_class_name: Name of the enum class (e.g., "MarioPaletteOptions")
        enum_name: Name of the new enum value (e.g., "MYCOOLPALETTE")
        palette_name: Display name for the palette (e.g., "My Cool Palette")
    """
    content = FLAGS_FILE.read_text()

    pattern = rf"^class {re.escape(enum_class_name)}\(CategorizationOption\):.*?(?=^class |\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print(f"Error: Could not find {enum_class_name} in flags.py")
        sys.exit(1)

    enum_block = match.group(0)
    enum_start = match.start()
    enum_end = match.end()

    assignment_pattern = r'^\s+([A-Z_0-9]+)\s*=\s*"([^"]+)"'
    assignments = list(re.finditer(assignment_pattern, enum_block, re.MULTILINE))

    if not assignments:
        print(f"Error: Could not find any enum entries in {enum_class_name}")
        sys.exit(1)

    last_assignment = assignments[-1]
    insert_pos = enum_start + last_assignment.end()

    new_entry = f'\n    {enum_name} = "{palette_name}"'

    new_content = content[:insert_pos] + new_entry + content[insert_pos:]

    FLAGS_FILE.write_text(new_content)
    print(f"Added {enum_name} to {enum_class_name} in flags.py")


def format_palette_colors(colors: list[int], indent: str = "        ") -> str:
    """Format a list of colors as Python code."""
    return "\n".join(f"{indent}0x{color:06X}," for color in colors)


def parse_palette_sections(body: str) -> tuple[list[int], list[int], list[int]]:
    """Parse palette sections from raw issue body.

    The issue template has all three palette sections with the same "Basic palette"
    header, so we need to parse by order rather than by name.
    Returns: (basic_colors, dark_colors, psn_colors)
    """
    sections = re.split(r"^###\s+", body, flags=re.MULTILINE)

    color_sections = []
    for section in sections:
        if not section.strip():
            continue
        colors = parse_palette_colors(section)
        if colors:
            color_sections.append(colors)

    basic_colors = color_sections[0] if len(color_sections) >= 1 else []
    dark_colors = color_sections[1] if len(color_sections) >= 2 else []
    psn_colors = color_sections[2] if len(color_sections) >= 3 else []

    return basic_colors, dark_colors, psn_colors


def generate_palette_preview_for_submission(character: str, palette_class_name: str) -> None:
    """Generate a preview image for a newly submitted palette.

    This runs in a fresh interpreter so that both the newly written enum member in
    flags.py and the new palette class are read from disk. Doing it in-process does
    not work: importlib.reload() reloads only the module it is given, so reloading
    the palette module rebinds it to the stale randomizer.types.flags still sitting
    in sys.modules, and the new enum member does not exist there.

    Args:
        character: Character name (mario, mallow, geno, bowser, toadstool, peach)
        palette_class_name: Name of the palette class that was created
    """
    char_arg = "toadstool" if character == "peach" else character

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "manage.py"),
            "generate_palette_previews",
            "--character", char_arg,
            "--palette-class", palette_class_name,
        ],
        capture_output=True,
        text=True,
    )

    if result.stdout.strip():
        print(result.stdout.strip())

    if result.returncode != 0:
        print(f"Warning: Failed to generate palette preview for {palette_class_name}")
        if result.stderr.strip():
            print(result.stderr.strip())


def add_palette(fields: dict[str, str], raw_body: str = "") -> None:
    """Add a character palette to the palette pool."""
    character = fields.get("Character", "").strip().lower()
    palette_name = fields.get("Palette name", "").strip()
    author_name = fields.get("Your name or handle", "").strip()

    # Check for rename character checkbox (appears as "- [X] ..." when checked)
    rename_field = fields.get("Rename character?", "")
    rename_character = "[X]" in rename_field or "[x]" in rename_field

    if not character:
        print("Error: No character specified in issue")
        sys.exit(1)

    if character not in CHARACTER_MAP:
        print(f"Error: Unknown character: {character}")
        print(f"Valid characters: mario, mallow, geno, bowser, toadstool (or peach)")
        sys.exit(1)

    if not palette_name:
        print("Error: No palette name specified in issue")
        sys.exit(1)

    # Parse colors from raw body since the template has duplicate headers
    basic_colors, dark_colors, psn_colors = parse_palette_sections(raw_body)

    if len(basic_colors) != 15:
        print(f"Error: Expected 15 basic colors, found {len(basic_colors)}")
        sys.exit(1)

    if dark_colors and len(dark_colors) != 15:
        print(f"Warning: Expected 15 underwater colors, found {len(dark_colors)}")

    if psn_colors and len(psn_colors) != 15:
        print(f"Warning: Expected 15 poison colors, found {len(psn_colors)}")

    filename, char_prefix, base_class, enum_class = CHARACTER_MAP[character]
    file_path = PALETTES_DIR / filename

    class_name = generate_palette_class_name(char_prefix, palette_name)
    enum_name = generate_palette_enum_name(palette_name)

    add_palette_enum_to_flags(enum_class, enum_name, palette_name)

    # Format author for credits (uppercase, A-Z, space, period, underscore)
    author = format_credits_name(author_name) if author_name else None

    lines = [
        f"class {class_name}({base_class}):",
        "    colours = [",
        format_palette_colors(basic_colors),
        "    ]",
    ]

    if psn_colors:
        lines.extend([
            "    poison_colours = [",
            format_palette_colors(psn_colors),
            "    ]",
        ])

    if dark_colors:
        lines.extend([
            "    underwater_colours = [",
            format_palette_colors(dark_colors),
            "    ]",
        ])

    lines.append(f"    id = {enum_class}.{enum_name}")
    lines.append(f'    name = "{escape_string(palette_name)}"')
    if author:
        lines.append(f'    author = "{author}"')
    # Only include rename_character if False (True is the default)
    if not rename_character:
        lines.append("    rename_character = False")
    class_code = "\n".join(lines)

    content = file_path.read_text()

    pattern = r"^(all_palettes.*?=.*?\[)"
    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        print(f"Error: Could not find all_palettes in {filename}")
        sys.exit(1)

    # Normalize the run of blank lines before all_palettes so the new class always
    # ends up separated by exactly two blank lines on both sides.
    insert_pos = match.start()
    prefix = content[:insert_pos].rstrip("\n")
    new_content = prefix + "\n\n\n" + class_code + "\n\n\n" + content[insert_pos:]

    all_palettes_pattern = r"(^all_palettes.*?=.*?\[.*?)(^\])"
    match = re.search(all_palettes_pattern, new_content, re.MULTILINE | re.DOTALL)
    if not match:
        print(f"Error: Could not find all_palettes closing bracket in {filename}")
        sys.exit(1)

    # The final entry is allowed to omit its trailing comma while it is last, so
    # add one before appending after it.
    list_body = match.group(1).rstrip()
    if not list_body.endswith(("[", ",")):
        list_body += ","

    new_content = (
        new_content[:match.start(1)]
        + list_body
        + f"\n    {class_name}(),\n"
        + new_content[match.end(1):]
    )

    file_path.write_text(new_content)
    print(f"Added palette: {class_name} to {filename}")

    print("Generating palette preview image...")
    generate_palette_preview_for_submission(character, class_name)


class Command(BaseCommand):
    help = "Add community submissions from GitHub issues to data files."

    def add_arguments(self, parser):
        parser.add_argument(
            "--type",
            choices=["wish", "quiz", "password", "song", "palette"],
            required=True,
            help="Type of submission",
        )
        parser.add_argument(
            "--issue",
            type=int,
            required=True,
            help="GitHub issue number",
        )
        parser.add_argument(
            "--non-smrpg",
            action="store_true",
            help="For quiz questions: mark as non-SMRPG related",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Parse and print but don't write to files",
        )
        parser.add_argument(
            "--repo",
            type=str,
            default=None,
            help="GitHub repo in 'owner/repo' format (default: current git remote)",
        )

    def handle(self, *args, **options):
        issue = options["issue"]
        repo = options["repo"]

        print(f"Fetching issue #{issue}..." + (f" from {repo}" if repo else ""))
        try:
            issue_data = fetch_issue(issue, repo)
        except subprocess.CalledProcessError as e:
            raise CommandError(f"Error fetching issue: {e.stderr}")

        print(f"Title: {issue_data['title']}")

        fields = parse_issue_body(issue_data["body"])

        if options["dry_run"]:
            print("\nParsed fields:")
            for key, value in fields.items():
                print(f"  {key}: {value[:100]}..." if len(value) > 100 else f"  {key}: {value}")
            return

        submission_type = options["type"]
        if submission_type == "wish":
            add_wish(fields)
        elif submission_type == "quiz":
            add_quiz_question(fields, options["non_smrpg"])
        elif submission_type == "password":
            add_password(fields)
        elif submission_type == "song":
            add_song(fields)
        elif submission_type == "palette":
            add_palette(fields, issue_data["body"])

        print("Done!")
