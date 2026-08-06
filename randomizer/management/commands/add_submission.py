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
from randomizer.utils.sprite_renderer import generate_ally_palette_preview
import importlib
import traceback

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


def add_wish(fields: dict[str, str]) -> None:
    """Add a Star Hill wish to the wish pool."""
    wish_text = fields.get("Wish text", "")
    if not wish_text:
        print("Error: No wish text found in issue")
        sys.exit(1)

    if wish_text and wish_text[-1] not in ".!?~":
        wish_text += "."

    wish_text = format_dialog(wish_text)
    wish_text = format_wish(wish_text)
    wish_text = "[center]" + wish_text

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

    question = question.rstrip()
    if question and not question.endswith("?"):
        question += "?"

    correct = clean_quiz_answer(correct)
    wrong1 = clean_quiz_answer(wrong1)
    wrong2 = clean_quiz_answer(wrong2)

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


def add_password(fields: dict[str, str]) -> None:
    """Add a ship password to the password pool."""
    word = fields.get("Your word", "")
    name = fields.get("Your name or handle", "").strip()
    hint1 = fields.get("Trampoline Room Hint", "")
    hint2 = fields.get("Paratroopa Room Hint", "")
    hint3 = fields.get("3D Maze Room Hint", "")
    hint4 = fields.get("Coin Snake Room Hint", "")
    hint5 = fields.get("Cannonball Room Hint", "")
    hint6 = fields.get("Rolling Barrel Room Hint", "")
    def clean_optional(val: str) -> str | None:
        val = val.strip()
        if not val or val == "_No response_":
            return None
        return val

    hint7 = clean_optional(fields.get("Optional hint 1", ""))
    hint8 = clean_optional(fields.get("Optional hint 2", ""))
    hint9 = clean_optional(fields.get("Optional hint 3", ""))
    hint10 = clean_optional(fields.get("Optional hint 4", ""))
    hint11 = clean_optional(fields.get("Optional hint 5", ""))

    if not word or len(word) != 6:
        print(f"Error: Password must be exactly 6 characters (got: '{word}')")
        sys.exit(1)

    if not all([hint1, hint2, hint3, hint4, hint5, hint6]):
        print("Error: All 6 required hints must be provided")
        sys.exit(1)

    submitter = name if name else "Anonymous"
    submitter_credits = format_credits_name(name) if name else "ANONYMOUS"
    submitter_hint_prefix = format_hint_prefix(submitter)

    def ensure_await(hint: str) -> str:
        """Ensure hint ends with [await]."""
        if not hint.rstrip().endswith("[await]"):
            return hint + "[await]"
        return hint

    def format_hint(hint: str) -> str:
        hint = format_dialog(hint)
        hint = ensure_await(hint)
        # Validate centering works (password hints use [center])
        warnings = validate_dialog("[center]" + hint)
        for w in warnings:
            print(f"Warning (hint): {w}")
        hint = escape_string(hint)
        return f'"%RANDOM_WRITER%\\n\\n{hint}"'

    def format_optional_hint(hint: str | None) -> str:
        if not hint:
            return "None"
        hint = format_dialog(hint)
        hint = ensure_await(hint)
        warnings = validate_dialog("[center]" + hint)
        for w in warnings:
            print(f"Warning (optional hint): {w}")
        return f'"{escape_string(hint)}"'

    word_escaped = escape_string(word.lower())

    new_entry = f'''    Password(
        "{word_escaped}",
        {format_hint(hint1)},
        {format_hint(hint2)},
        {format_hint(hint3)},
        {format_hint(hint4)},
        {format_hint(hint5)},
        {format_hint(hint6)},
        {format_optional_hint(hint7)},
        {format_optional_hint(hint8)},
        {format_optional_hint(hint9)},
        {format_optional_hint(hint10)},
        {format_optional_hint(hint11)},
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
        return f"'{hint}'"

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


def generate_palette_preview_for_submission(character: str, palette_class_name: str, palette_name: str) -> None:
    """Generate a preview image for a newly submitted palette.

    Args:
        character: Character name (mario, mallow, geno, bowser, toadstool)
        palette_class_name: Name of the palette class that was created
        palette_name: Display name of the palette
    """

    sprite_ids = {
        'mario': 0,
        'mallow': 19,
        'geno': 25,
        'bowser': 13,
        'toadstool': 7,
        'peach': 7,
    }

    if character not in sprite_ids:
        print(f"Warning: Unknown character '{character}', skipping preview generation")
        return

    sprite_id = sprite_ids[character]

    palette_module_map = {
        'mario': 'randomizer.data.allies.palettes.mario',
        'mallow': 'randomizer.data.allies.palettes.mallow',
        'geno': 'randomizer.data.allies.palettes.geno',
        'bowser': 'randomizer.data.allies.palettes.bowser',
        'toadstool': 'randomizer.data.allies.palettes.toadstool',
        'peach': 'randomizer.data.allies.palettes.toadstool',
    }

    module_name = palette_module_map[character]

    try:
        # Reload the module to pick up the newly added class
        if module_name in sys.modules:
            module = importlib.reload(sys.modules[module_name])
        else:
            module = importlib.import_module(module_name)

        palette_class = getattr(module, palette_class_name)

        safe_name = palette_name.lower().replace(' ', '_').replace("'", '')

        char_output_dir = character if character != 'peach' else 'toadstool'
        output_dir = REPO_ROOT / 'randomizer' / 'static' / 'randomizer' / 'images' / 'palette_previews' / char_output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f'{safe_name}.png'

        generate_ally_palette_preview(
            sprite_id=sprite_id,
            palette_class=palette_class,
            output_path=str(output_path),
            mold_index=0,
            scale=3
        )

        print(f"Generated palette preview: {output_path}")

    except Exception as e:
        print(f"Warning: Failed to generate palette preview: {e}")
        traceback.print_exc()


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
        "",
        "",
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

    insert_pos = match.start()
    new_content = content[:insert_pos] + class_code + "\n\n\n" + content[insert_pos:]

    all_palettes_pattern = r"(^all_palettes.*?=.*?\[.*?)(^\])"
    match = re.search(all_palettes_pattern, new_content, re.MULTILINE | re.DOTALL)
    if not match:
        print(f"Error: Could not find all_palettes closing bracket in {filename}")
        sys.exit(1)

    insert_pos = match.end(1)
    new_content = new_content[:insert_pos] + f"    {class_name}(),\n" + new_content[insert_pos:]

    file_path.write_text(new_content)
    print(f"Added palette: {class_name} to {filename}")

    print("Generating palette preview image...")
    generate_palette_preview_for_submission(character, class_name, palette_name)


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
