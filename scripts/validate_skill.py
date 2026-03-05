#!/usr/bin/env python3
"""
Validate OpenClaw skill structure.
"""

import sys
import os
import re
from pathlib import Path


def parse_frontmatter(content: str) -> dict:
    """Simple YAML frontmatter parser."""
    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        return None
    
    lines = frontmatter_match.group(1).strip().split('\n')
    result = {}
    current_key = None
    multiline_value = []
    in_multiline = False
    
    for line in lines:
        # Check for multiline string (|)
        if '|' in line and ':' in line:
            key = line.split(':')[0].strip()
            current_key = key
            in_multiline = True
            # Get text after |
            if '|' in line:
                multiline_value = [line.split('|')[1].strip()]
            continue
        
        if in_multiline:
            if line.startswith('  ') or line.startswith('-') or line == '':
                multiline_value.append(line.strip())
            else:
                result[current_key] = '\n'.join(multiline_value).strip()
                in_multiline = False
                # Check if this line is a new key
                if ':' in line:
                    current_key = line.split(':')[0].strip()
                    value = line.split(':', 1)[1].strip()
                    if value:
                        result[current_key] = value
        elif ':' in line:
            key = line.split(':')[0].strip()
            value = line.split(':', 1)[1].strip()
            result[key] = value
    
    if in_multiline and current_key:
        result[current_key] = '\n'.join(multiline_value).strip()
    
    return result


def validate_skill(skill_path: str) -> bool:
    """Validate skill structure and frontmatter."""
    path = Path(skill_path)
    
    if not path.exists():
        print(f"❌ Skill path does not exist: {skill_path}")
        return False
    
    # Check for SKILL.md
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Missing SKILL.md in {skill_path}")
        return False
    
    # Validate frontmatter
    with open(skill_md, 'r') as f:
        content = f.read()
    
    # Check for YAML frontmatter
    frontmatter = parse_frontmatter(content)
    if not frontmatter:
        print(f"❌ No YAML frontmatter found in SKILL.md")
        return False
    
    # Check required fields
    if 'name' not in frontmatter:
        print(f"❌ Missing 'name' in frontmatter")
        return False
    
    if 'description' not in frontmatter:
        print(f"❌ Missing 'description' in frontmatter")
        return False
    
    name = frontmatter.get('name', '')
    if not re.match(r'^[a-z0-9_-]+$', name):
        print(f"❌ Skill name '{name}' should be kebab-case (lowercase, numbers, hyphens, underscores)")
        return False
    
    print(f"✓ Skill '{name}' validated successfully")
    print(f"  - Description: {len(frontmatter.get('description', ''))} chars")
    
    # Check optional folders
    optional_dirs = ['scripts', 'references', 'assets', 'evals']
    for dir_name in optional_dirs:
        dir_path = path / dir_name
        if dir_path.exists() and dir_path.is_dir():
            files = list(dir_path.iterdir())
            print(f"  - {dir_name}/: {len(files)} items")
    
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <skill-path>")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    if validate_skill(skill_path):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
