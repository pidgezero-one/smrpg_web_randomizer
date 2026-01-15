#!/usr/bin/env python3
"""Script to convert pack_collection.py to the new format with standalone formations."""

import re
import sys
sys.path.insert(0, '/Users/stefkischak/code/smrpg_web_randomizer')

# Import the existing pack collection to get all the data
from randomizer.data.packs.pack_collection import packs, pack_collection
from randomizer.data.variables.pack_names import *

def formation_to_key(formation):
    """Create a hashable key representing a formation's content."""
    members_key = []
    for m in formation.members:
        if m is None:
            members_key.append(None)
        else:
            members_key.append((
                m.enemy.__name__,
                int(m.x_pos),
                int(m.y_pos),
                m.hidden_at_start,
            ))

    return (
        tuple(members_key),
        type(formation.music).__name__ if formation.music else None,
        formation.can_run_away,
        int(formation.unknown_byte),
        formation.unknown_bit,
        formation.run_event_at_load,
    )

def formation_to_code(formation, var_name, formation_id):
    """Generate Python code for a formation declaration."""
    lines = [f"{var_name} = Formation("]
    lines.append(f"    id={formation_id},")
    lines.append("    members=[")

    # Find last non-None member
    last_idx = -1
    for i in range(len(formation.members) - 1, -1, -1):
        if formation.members[i] is not None:
            last_idx = i
            break

    for i, m in enumerate(formation.members):
        if i > last_idx:
            break
        if m is None:
            lines.append("        None,")
        else:
            enemy_name = m.enemy.__name__
            if m.hidden_at_start:
                lines.append(f"        FormationMember({enemy_name}, {int(m.x_pos)}, {int(m.y_pos)}, hidden_at_start=True),")
            else:
                lines.append(f"        FormationMember({enemy_name}, {int(m.x_pos)}, {int(m.y_pos)}),")

    lines.append("    ],")

    # Music
    if formation.music:
        music_name = type(formation.music).__name__
        lines.append(f"    music={music_name}(),")
    else:
        lines.append("    music=None,")

    # Optional properties
    if not formation.can_run_away:
        lines.append("    can_run_away=False,")

    if formation.unknown_byte != 0:
        lines.append(f"    unknown_byte={int(formation.unknown_byte)},")

    if formation.unknown_bit:
        lines.append(f"    unknown_bit=True,")

    if formation.run_event_at_load is not None:
        lines.append(f"    run_event_at_load={int(formation.run_event_at_load)},")

    lines.append(")")
    return "\n".join(lines)

def get_pack_name(pack_id):
    """Get the pack name constant for a given pack ID."""
    # Map of pack IDs to their names from pack_names
    pack_name_map = {
        0: "PACK000_TOWER_HENCHMAN_1",
        1: "PACK001_TOWER_HENCHMAN_2",
        2: "PACK002_SPIKEYS_AND_TROOPAS",
        3: "PACK003_SPIKEYS_AND_FROGS",
        4: "PACK004_JUST_TROOPAS",
        5: "PACK005_TROOPAS_WITH_FROGS_OR_GOOMBAS",
        6: "PACK006_JUST_GOOMBAS",
        7: "PACK007_GOOMBAS_WITH_FROGS_OR_SPIKEYS",
        8: "PACK008_K9S_WITH_SPIKEYS",
        9: "PACK009_K9S_WITH_SPIKEYS_OR_FROGS",
    }
    # We'll read these from the original file
    return f"PACK{pack_id:03d}"

def main():
    # Collect all unique formations
    unique_formations = {}  # key -> (formation, id)
    formation_id_counter = 0

    # Map from pack index and formation index to formation key
    pack_formation_keys = {}

    for pack_id, pack in enumerate(packs):
        if pack is None:
            continue

        pack_formation_keys[pack_id] = []
        for formation in pack.formations:
            key = formation_to_key(formation)
            if key not in unique_formations:
                unique_formations[key] = (formation, formation_id_counter)
                formation_id_counter += 1
            pack_formation_keys[pack_id].append(key)

    print(f"Found {len(unique_formations)} unique formations", file=sys.stderr)

    # Generate the new file
    output_lines = []

    # Header
    output_lines.append('"""ROM\'s PackCollection disassembled from the original game."""')
    output_lines.append("")
    output_lines.append("from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (")
    output_lines.append("    Formation,")
    output_lines.append("    FormationMember,")
    output_lines.append("    FormationPack,")
    output_lines.append("    PackCollection,")
    output_lines.append(")")
    output_lines.append("from smrpgpatchbuilder.datatypes.battles.music import (")
    output_lines.append("    NormalBattleMusic,")
    output_lines.append("    MidbossMusic,")
    output_lines.append("    BossMusic,")
    output_lines.append("    Smithy1Music,")
    output_lines.append("    CorndillyMusic,")
    output_lines.append("    BoosterHillMusic,")
    output_lines.append("    VolcanoMusic,")
    output_lines.append("    CulexMusic,")
    output_lines.append(")")
    output_lines.append("from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield")
    output_lines.append("from ..enemies.enemies import *")
    output_lines.append("from ..variables.pack_names import *")
    output_lines.append("from ..variables.battle_event_names import *")
    output_lines.append("")
    output_lines.append("")

    # Formation declarations section
    output_lines.append("# " + "=" * 76)
    output_lines.append("# Formation Declarations")
    output_lines.append("# " + "=" * 76)
    output_lines.append("")

    # Sort formations by ID and generate declarations
    sorted_formations = sorted(unique_formations.items(), key=lambda x: x[1][1])
    key_to_varname = {}

    for key, (formation, fid) in sorted_formations:
        var_name = f"FORM{fid:04d}"
        key_to_varname[key] = var_name
        output_lines.append(formation_to_code(formation, var_name, fid))
        output_lines.append("")

    # Pack definitions section
    output_lines.append("")
    output_lines.append("# " + "=" * 76)
    output_lines.append("# Pack Definitions")
    output_lines.append("# " + "=" * 76)
    output_lines.append("")
    output_lines.append("# Initialize packs array with None values")
    output_lines.append("packs: list[FormationPack] = [None] * 256  # type: ignore")
    output_lines.append("")

    # Read original file to get pack names
    with open('/Users/stefkischak/code/smrpg_web_randomizer/randomizer/data/packs/pack_collection.py', 'r') as f:
        original_content = f.read()

    # Extract pack names using regex
    pack_name_pattern = re.compile(r'packs\[(\w+)\]\s*=')
    pack_names_found = pack_name_pattern.findall(original_content)

    # Create mapping from pack index to pack name
    pack_id_to_name = {}
    for i, name in enumerate(pack_names_found):
        if i < 256:
            pack_id_to_name[i] = name

    # Generate pack definitions
    for pack_id, pack in enumerate(packs):
        if pack is None:
            continue

        pack_name = pack_id_to_name.get(pack_id, f"PACK{pack_id:03d}")
        keys = pack_formation_keys[pack_id]
        form_names = [key_to_varname[k] for k in keys]

        # Check if all three formations are the same
        if keys[0] == keys[1] == keys[2]:
            output_lines.append(f"packs[{pack_name}] = FormationPack({form_names[0]})")
        else:
            output_lines.append(f"packs[{pack_name}] = FormationPack({form_names[0]}, {form_names[1]}, {form_names[2]})")

    output_lines.append("")
    output_lines.append("# Pack Collection")
    output_lines.append("pack_collection = PackCollection(packs[:256])")
    output_lines.append("")

    # Output the result
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
