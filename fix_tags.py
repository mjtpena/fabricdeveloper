#!/usr/bin/env python3
"""Fix tags and categories with special URL-breaking characters."""

import os
import glob
import re
import yaml

def sanitize_tag(tag):
    """Remove or replace characters that break URL routing."""
    # Replace slashes with hyphens
    tag = tag.replace('/', '-')
    # Remove other problematic chars
    tag = re.sub(r'[?#&]', '', tag)
    return tag.strip()

def fix_tags_in_file(file_path):
    """Fix tags in a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return False
    
    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter_str = parts[1]
    body = parts[2]
    
    try:
        # Parse YAML
        frontmatter = yaml.safe_load(frontmatter_str)
        if not frontmatter:
            return False
        
        # Fix tags
        if 'tags' in frontmatter and isinstance(frontmatter['tags'], list):
            frontmatter['tags'] = [sanitize_tag(t) for t in frontmatter['tags']]
        
        # Fix category
        if 'category' in frontmatter and isinstance(frontmatter['category'], str):
            frontmatter['category'] = sanitize_tag(frontmatter['category'])
        
        # Reconstruct frontmatter
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        new_content = f"---\n{new_frontmatter}---{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error in {file_path}: {e}")
        return False

def main():
    posts_dir = 'src/content/posts'
    fixed = 0
    
    for folder in sorted(glob.glob(os.path.join(posts_dir, '*'))):
        if os.path.isdir(folder):
            md_file = os.path.join(folder, os.path.basename(folder) + '.md')
            if os.path.exists(md_file):
                if fix_tags_in_file(md_file):
                    fixed += 1
    
    print(f"✅ Fixed tags in {fixed} files")

if __name__ == '__main__':
    main()
