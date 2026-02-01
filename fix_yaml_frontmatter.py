#!/usr/bin/env python3
"""Fix YAML frontmatter in all blog posts."""

import os
import glob
import re
from pathlib import Path

def fix_yaml_frontmatter(file_path):
    """Fix YAML frontmatter by properly quoting titles with special chars."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return False, "No frontmatter"
    
    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, "Invalid frontmatter structure"
    
    frontmatter = parts[1]
    body = parts[2]
    
    # Fix title: quote if contains special chars
    title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        # If title has colons, pipes, or other special chars, quote it
        if ':' in title or '|' in title or '"' in title or "'" in title or '@' in title or '&' in title:
            # Use double quotes, escape any quotes inside
            escaped_title = title.replace('\\', '\\\\').replace('"', '\\"')
            frontmatter = re.sub(
                r'^title:\s*.+$',
                f'title: "{escaped_title}"',
                frontmatter,
                flags=re.MULTILINE
            )
    
    # Fix description: ensure proper quoting
    desc_match = re.search(r'^description:\s*(.+?)(?=^[a-z]|\Z)', frontmatter, re.MULTILINE | re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()
        # If starts with >-, it's already a multiline string, which is fine
        # Otherwise quote it if it has special chars
        if not desc.startswith('>-'):
            if any(c in desc for c in [':', '"', "'", '@', '&', '|']):
                escaped_desc = desc.replace('\\', '\\\\').replace('"', '\\"')
                frontmatter = re.sub(
                    r'^description:\s*.+?(?=^[a-z]|\Z)',
                    f'description: "{escaped_desc}"\n',
                    frontmatter,
                    flags=re.MULTILINE | re.DOTALL
                )
    
    new_content = f"---{frontmatter}---{body}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "Fixed"

def main():
    posts_dir = 'src/content/posts'
    fixed = 0
    errors = 0
    
    for folder in sorted(glob.glob(os.path.join(posts_dir, '*'))):
        if os.path.isdir(folder):
            md_file = os.path.join(folder, os.path.basename(folder) + '.md')
            if os.path.exists(md_file):
                success, msg = fix_yaml_frontmatter(md_file)
                if success:
                    fixed += 1
                else:
                    errors += 1
                    if errors <= 5:
                        print(f"  {os.path.basename(folder)}: {msg}")
    
    print(f"\n✅ Fixed {fixed} files")
    if errors > 0:
        print(f"⚠️  {errors} files had issues")

if __name__ == '__main__':
    main()
