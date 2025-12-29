#!/usr/bin/env python3
"""Script to add community submissions from GitHub issues to data files.

Usage:
    python scripts/add_submission.py --type wish --issue 123
    python scripts/add_submission.py --type quiz --issue 123 [--non-smrpg]
    python scripts/add_submission.py --type password --issue 123
    python scripts/add_submission.py --type song --issue 123

    # Specify upstream repo when working from a fork:
    python scripts/add_submission.py --type wish --issue 123 --repo owner/repo
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# File paths relative to repository root
REPO_ROOT = Path(__file__).parent.parent
WISH_FILE = REPO_ROOT / "randomizer/data/minigames/star_hill_wishes.py"
QUIZ_FILE = REPO_ROOT / "randomizer/data/minigames/quiz_questions.py"
PASSWORD_FILE = REPO_ROOT / "randomizer/data/minigames/ship_password.py"
SONG_FILE = REPO_ROOT / "randomizer/data/minigames/melody_bay.py"


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
            # Save previous field
            if current_field:
                fields[current_field] = "\n".join(current_value_lines).strip()
            # Start new field
            current_field = line[4:].strip()
            current_value_lines = []
        elif current_field:
            current_value_lines.append(line)

    # Save last field
    if current_field:
        fields[current_field] = "\n".join(current_value_lines).strip()

    return fields


def escape_string(s: str) -> str:
    """Escape a string for use in Python source code."""
    # Replace backslashes first, then quotes
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    return s


def add_wish(fields: dict[str, str]) -> None:
    """Add a Star Hill wish to the wish pool."""
    wish_text = fields.get("Wish text", "")
    if not wish_text:
        print("Error: No wish text found in issue")
        sys.exit(1)

    escaped = escape_string(wish_text)
    new_entry = f'    "{escaped}",\n'

    # Read file and find WISH_POOL list
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
    # Strip surrounding parentheses
    if answer.startswith("(") and answer.endswith(")"):
        answer = answer[1:-1].strip()
    # Strip trailing period
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

    # Clean answers
    correct = clean_quiz_answer(correct)
    wrong1 = clean_quiz_answer(wrong1)
    wrong2 = clean_quiz_answer(wrong2)

    # Escape strings
    question = escape_string(question)
    correct = escape_string(correct)
    wrong1 = escape_string(wrong1)
    wrong2 = escape_string(wrong2)

    # Format the new Question entry
    new_entry = f'''        Question(
            "{question}",
            "{correct}",
            "{wrong1}",
            "{wrong2}",
        ),
'''

    content = QUIZ_FILE.read_text()

    if non_smrpg:
        # Find get_non_smrpg_questions() return list
        pattern = r"(def get_non_smrpg_questions\(\).*?return \[.*?)(^\s*\])"
        func_name = "get_non_smrpg_questions"
    else:
        # Find get_smrpg_questions() return list
        pattern = r"(def get_smrpg_questions\(\).*?return \[.*?)(^\s*\])"
        func_name = "get_smrpg_questions"

    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print(f"Error: Could not find {func_name}() return list in file")
        sys.exit(1)

    # Insert new entry before closing bracket
    insert_pos = match.end(1)
    new_content = content[:insert_pos] + new_entry + content[insert_pos:]

    QUIZ_FILE.write_text(new_content)
    print(f"Added quiz question to {func_name}(): {question[:50]}...")


def format_credits_name(name: str) -> str:
    """Format name for credits (uppercase, only A-Z, space, period, underscore)."""
    # Filter to allowed characters and uppercase
    allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ. _")
    result = "".join(c for c in name.upper() if c in allowed)
    return result if result else "ANONYMOUS"


def format_hint_prefix(name: str) -> str:
    """Format the hint prefix."""
    return f"Memo left by {name}:"


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

    # Format submitter info
    submitter = name if name else "Anonymous"
    submitter_credits = format_credits_name(name) if name else "ANONYMOUS"
    submitter_hint_prefix = format_hint_prefix(submitter)

    def ensure_await(hint: str) -> str:
        """Ensure hint ends with [await]."""
        if not hint.rstrip().endswith("[await]"):
            return hint + "[await]"
        return hint

    # Format hints with %RANDOM_WRITER% prefix
    def format_hint(hint: str) -> str:
        hint = ensure_await(hint)
        hint = escape_string(hint)
        return f'"%RANDOM_WRITER%\\n\\n{hint}"'

    def format_optional_hint(hint: str | None) -> str:
        if not hint:
            return "None"
        hint = ensure_await(hint)
        return f'"{escape_string(hint)}"'

    word_escaped = escape_string(word.lower())

    # Build the Password entry
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

    # Find the pool list
    pattern = r"(^pool = \[.*?)(^\])"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print("Error: Could not find pool list in file")
        sys.exit(1)

    # Insert new entry before closing bracket
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

    # Try Python tuple format first: (Note, duration)
    tuple_pattern = r"\(\s*(Fa|So|La|Ti|Do|Re|Mi)\s*,\s*(\d+)\s*\)"
    matches = list(re.finditer(tuple_pattern, notation, re.IGNORECASE))
    if matches:
        for match in matches:
            note_name = match.group(1).capitalize()
            duration = int(match.group(2))
            notes.append((note_name, duration))
        return notes

    # Try colon/dash/space separated format: Note:duration or Note-duration
    pair_pattern = r"(Fa|So|La|Ti|Do|Re|Mi)\s*[:\-\s]\s*(\d+)"
    matches = list(re.finditer(pair_pattern, notation, re.IGNORECASE))
    if matches:
        for match in matches:
            note_name = match.group(1).capitalize()
            duration = int(match.group(2))
            notes.append((note_name, duration))
        return notes

    # Try simpler format: just note names with default durations
    simple_pattern = r"\b(Fa|So|La|Ti|Do|Re|Mi)\b"
    for match in re.finditer(simple_pattern, notation, re.IGNORECASE):
        note_name = match.group(1).capitalize()
        notes.append((note_name, 35))  # Default duration

    return notes


def strip_markdown_ticks(s: str) -> tuple[str, bool]:
    """Remove markdown code ticks and return (cleaned_string, had_ticks)."""
    # Check for code block or inline code ticks
    had_ticks = '`' in s
    # Remove backticks
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

    # Parse the notation
    notes = parse_song_notation(notation)
    if not notes:
        print(f"Error: Could not parse song notation: {notation}")
        sys.exit(1)

    if len(notes) > 8:
        print(f"Warning: Song has {len(notes)} notes, but max is 8. Truncating.")
        notes = notes[:8]

    # Format submitter info
    submitter = name if name else "Anonymous"
    submitter_credits = format_credits_name(name) if name else "ANONYMOUS"

    # Generate scroll text from notes
    note_names = " ".join(n for n, _ in notes)
    scroll_text = f"\\n          {note_names}[await]"

    # Check for markdown ticks and clean hints
    hint1, hint1_ticks = strip_markdown_ticks(hint1)
    hint2_pond, hint2_ticks = strip_markdown_ticks(hint2_pond)
    hint2_mines, hint3_ticks = strip_markdown_ticks(hint2_mines)

    # Ensure hints end with [await]
    def ensure_await(hint: str) -> str:
        if not hint.rstrip().endswith("[await]"):
            return hint + "[await]"
        return hint

    hint1 = ensure_await(hint1)
    hint2_pond = ensure_await(hint2_pond)
    hint2_mines = ensure_await(hint2_mines)

    # Escape strings
    songname_escaped = escape_string(songname)
    submitter_escaped = escape_string(submitter)
    hint1_escaped = escape_string(hint1)
    hint2_pond_escaped = escape_string(hint2_pond)
    hint2_mines_escaped = escape_string(hint2_mines)

    # Format notes list
    notes_str = ", ".join(f"({n}, {d})" for n, d in notes)

    # Use triple quotes if any hint had backticks
    def quote_hint(hint: str, had_ticks: bool) -> str:
        if had_ticks:
            return f'"""{hint}"""'
        return f"'{hint}'"

    # Build the Song entry
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

    # Find the all_songs list
    pattern = r"(^all_songs = \[.*?)(^\])"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        print("Error: Could not find all_songs list in file")
        sys.exit(1)

    # Insert new entry before closing bracket
    insert_pos = match.end(1)
    new_content = content[:insert_pos] + new_entry + content[insert_pos:]

    SONG_FILE.write_text(new_content)
    print(f"Added song: {songname}")


def main():
    parser = argparse.ArgumentParser(
        description="Add community submissions from GitHub issues to data files"
    )
    parser.add_argument(
        "--type",
        choices=["wish", "quiz", "password", "song"],
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

    args = parser.parse_args()

    # Fetch issue
    print(f"Fetching issue #{args.issue}..." + (f" from {args.repo}" if args.repo else ""))
    try:
        issue_data = fetch_issue(args.issue, args.repo)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching issue: {e.stderr}")
        sys.exit(1)

    print(f"Title: {issue_data['title']}")

    # Parse issue body
    fields = parse_issue_body(issue_data["body"])

    if args.dry_run:
        print("\nParsed fields:")
        for key, value in fields.items():
            print(f"  {key}: {value[:100]}..." if len(value) > 100 else f"  {key}: {value}")
        return

    # Add to appropriate file
    if args.type == "wish":
        add_wish(fields)
    elif args.type == "quiz":
        add_quiz_question(fields, args.non_smrpg)
    elif args.type == "password":
        add_password(fields)
    elif args.type == "song":
        add_song(fields)

    print("Done!")


if __name__ == "__main__":
    main()
