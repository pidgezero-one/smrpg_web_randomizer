#!/usr/bin/env python3
"""Extract NPC slot data from old model_fills.py to generate _npc_slots for new prizelocations.py"""

import re
from pathlib import Path

MODEL_FILLS_PATH = Path(__file__).parent.parent / "randomizer/entities/progress_locations/helpers/model_fills.py"
OLD_BOSSES_PATH = Path(__file__).parent.parent / "randomizer/entities/progress_locations/bosses.py"

def extract_boss_model_fills():
    """Extract BossModelFill definitions from model_fills.py"""
    content = MODEL_FILLS_PATH.read_text()

    # Find all BossModelFill definitions
    pattern = r'(\w+)\s*=\s*BossModelFill\(\s*(?:room_id=)?(\w+),\s*npc=(\w+),.*?(?:preferred_size=SpriteSize\.(\w+),)?.*?(?:sequence_setter=(\w+))?\)'

    fills = {}

    # More robust extraction - line by line
    lines = content.split('\n')
    current_fill = None
    current_data = {}

    for i, line in enumerate(lines):
        if '= BossModelFill(' in line:
            # Save previous
            if current_fill:
                fills[current_fill] = current_data

            # Start new
            match = re.match(r'^(\w+)\s*=\s*BossModelFill\(', line)
            if match:
                current_fill = match.group(1)
                current_data = {'room_id': None, 'npc': None, 'size': 'SMALL', 'sequence_setter': None}

        if current_fill:
            # Extract room_id
            if 'room_id=' in line or (current_data['room_id'] is None and re.match(r'^\s*R\d+_', line)):
                m = re.search(r'(?:room_id=)?(R\d+_\w+)', line)
                if m:
                    current_data['room_id'] = m.group(1)

            # Extract npc
            if 'npc=' in line:
                m = re.search(r'npc=(NPC_\d+)', line)
                if m:
                    current_data['npc'] = m.group(1)

            # Extract preferred_size
            if 'preferred_size=' in line:
                m = re.search(r'preferred_size=SpriteSize\.(\w+)', line)
                if m:
                    size = m.group(1)
                    if size == 'ATTACK':
                        current_data['size'] = 'BATTLE'
                    else:
                        current_data['size'] = size

            # Extract sequence_setter
            if 'sequence_setter=' in line:
                m = re.search(r'sequence_setter=(E\d+_\w+)', line)
                if m:
                    current_data['sequence_setter'] = m.group(1)

    # Save last
    if current_fill:
        fills[current_fill] = current_data

    return fills


def extract_boss_location_fills():
    """Extract which BossModelFills are used by which boss fight locations"""
    content = OLD_BOSSES_PATH.read_text()

    locations = {}
    current_class = None

    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Find class definitions
        if line.startswith('class ') and 'BossFightLocation' in line:
            match = re.match(r'^class (\w+)\(BossFightLocation\):', line)
            if match:
                current_class = match.group(1)
                locations[current_class] = []

        # Find _overworld_boss_npc_fills
        if current_class and '_overworld_boss_npc_fills' in line:
            # Extract fill names from this and following lines
            fill_section = line
            j = i + 1
            while j < len(lines) and ']' not in fill_section:
                fill_section += lines[j]
                j += 1

            # Find all fill names
            fill_names = re.findall(r'([A-Z][A-Z_0-9]+_FILL|[A-Z][A-Z_0-9]+_BOSS_FILL)', fill_section)
            locations[current_class] = fill_names

    return locations


def main():
    fills = extract_boss_model_fills()
    locations = extract_boss_location_fills()

    print("# Generated _npc_slots for BossFightLocation classes")
    print("# Copy these into the appropriate classes in prizelocations.py")
    print()

    # Map old class names to new class names if different
    class_name_map = {
        'MushroomWayBossFight': 'MushrooomWayBossFight',  # Note the typo in new code
        'ForestBossFight': 'ForestMazeBossFight',
        'MinesMidbossFight': 'OuterMinesBossFight',
        'MinesBossFight': 'InnerMinesBossFight',
        'TowerCurtainRoomBossFight': 'BoosterTowerIndoorBossFight',
        'TowerBalconyBossFight': 'BoosterTowerBalconyBossFight',
        'ChapelBossFight': 'MarrymoreBossFight',
        'MimicFightLocation1': 'Mimic1BossFight',
        'MimicFightLocation2': 'Mimic2BossFight',
        'MimicFightLocation3': 'Mimic3BossFight',
        'ShipFinalBossFight': 'ShipFinalBossFight',
        'SeasideBeachBossFight': 'SeasideBeachBossFight',
        'LandsEndCloudBossFight': 'LandsEndCloudBoss',
        'TempleBossFight': 'TempleBossFight',
        'MonstroSealedDoorBossFight': 'MonstroSealedDoorBossFight',
    }

    for old_name, fill_names in sorted(locations.items()):
        if not fill_names:
            continue

        new_name = class_name_map.get(old_name, old_name)
        print(f"# {new_name}")
        print(f"_npc_slots = [")

        for fill_name in fill_names:
            if fill_name in fills:
                data = fills[fill_name]
                room = data['room_id']
                npc = data['npc']
                size = data['size']
                seq = data['sequence_setter']

                if size == 'SMALL' and seq is None:
                    print(f"    BossFightLocationNPC({room}, {npc}),")
                elif size == 'SMALL':
                    print(f"    BossFightLocationNPC({room}, {npc}, sequence_setter_event_id={seq}),")
                elif seq is None:
                    print(f"    BossFightLocationNPC({room}, {npc}, BossSpriteSize.{size}),")
                else:
                    print(f"    BossFightLocationNPC({room}, {npc}, BossSpriteSize.{size}, {seq}),")
            else:
                print(f"    # TODO: {fill_name} not found")

        print(f"]")
        print()


if __name__ == "__main__":
    main()
