#!/usr/bin/env python3
"""
Final validation script before deployment:
- Verify all frontmatter is valid
- Check all cover.png files exist and are valid
- Generate deployment summary
"""

import os
import yaml
import json
from pathlib import Path
from PIL import Image

def validate_frontmatter(md_file):
    """Validate frontmatter in markdown file."""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        if not content.startswith('---'):
            return False, "Missing frontmatter start marker"
        
        lines = content.split('\n')
        end_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                end_idx = i
                break
        
        if end_idx is None:
            return False, "Missing frontmatter end marker"
        
        fm_text = '\n'.join(lines[1:end_idx])
        fm = yaml.safe_load(fm_text)
        
        # Check required fields
        required = ['title', 'published', 'description', 'category']
        for field in required:
            if field not in fm:
                return False, f"Missing required field: {field}"
        
        # Check image reference
        if 'image' in fm and fm['image'] != './cover.png':
            return False, f"Incorrect image path: {fm['image']}"
        
        return True, "Valid"
    except yaml.YAMLError as e:
        return False, f"YAML error: {str(e)[:50]}"
    except Exception as e:
        return False, str(e)[:50]

def validate_cover_image(image_path):
    """Validate cover.png file."""
    try:
        if not image_path.exists():
            return False, "File not found"
        
        # Check file size (should be ~15-30KB)
        size = image_path.stat().st_size
        if size < 1000:
            return False, f"Too small: {size} bytes"
        if size > 100000:
            return False, f"Too large: {size} bytes"
        
        # Verify image format
        img = Image.open(image_path)
        if img.format != 'PNG':
            return False, f"Wrong format: {img.format}"
        
        if img.size != (1200, 630):
            return False, f"Wrong size: {img.size}"
        
        return True, "Valid"
    except Exception as e:
        return False, str(e)[:40]

def main():
    """Run validation suite."""
    posts_dir = Path("C:/Users/mjtpena/dev/fabricdeveloper/src/content/posts")
    
    post_dirs = sorted([d for d in posts_dir.iterdir() 
                        if d.is_dir() and not d.name.startswith('.')])
    
    fm_valid = 0
    fm_invalid = 0
    cover_valid = 0
    cover_invalid = 0
    md_missing = 0
    
    issues = []
    
    print("🔍 FINAL VALIDATION BEFORE DEPLOYMENT")
    print("=" * 70)
    
    for post_dir in post_dirs:
        md_files = list(post_dir.glob("*.md"))
        cover_file = post_dir / "cover.png"
        
        # Check markdown
        if not md_files:
            md_missing += 1
            issues.append(f"❌ {post_dir.name}: No markdown file")
        else:
            valid, msg = validate_frontmatter(md_files[0])
            if valid:
                fm_valid += 1
            else:
                fm_invalid += 1
                issues.append(f"⚠️  {post_dir.name}: {msg}")
        
        # Check cover image
        valid, msg = validate_cover_image(cover_file)
        if valid:
            cover_valid += 1
        else:
            cover_invalid += 1
            issues.append(f"📸 {post_dir.name}: {msg}")
    
    # Report
    total = len(post_dirs)
    print(f"\n📋 MARKDOWN FRONTMATTER VALIDATION")
    print(f"✓ Valid:   {fm_valid:4d}/{total}")
    print(f"✗ Invalid: {fm_invalid:4d}/{total}")
    print(f"- Missing: {md_missing:4d}/{total}")
    
    print(f"\n🖼️  COVER IMAGE VALIDATION")
    print(f"✓ Valid:   {cover_valid:4d}/{total}")
    print(f"✗ Invalid: {cover_invalid:4d}/{total}")
    
    print("\n" + "=" * 70)
    
    if issues:
        print(f"\n⚠️  ISSUES FOUND ({len(issues)}):\n")
        for issue in issues[:20]:  # Show first 20
            print(f"  {issue}")
        if len(issues) > 20:
            print(f"\n  ... and {len(issues) - 20} more issues")
    else:
        print("\n✅ NO ISSUES FOUND - ALL VALIDATIONS PASSED!")
    
    # Final summary
    print("\n" + "=" * 70)
    if fm_invalid == 0 and cover_invalid == 0:
        print("\n✅ DEPLOYMENT READY!")
        print(f"   • {fm_valid} valid markdown files")
        print(f"   • {cover_valid} valid cover images")
        print(f"   • Ready for production deployment")
    else:
        print(f"\n❌ ISSUES PREVENT DEPLOYMENT")
        print(f"   • Fix {fm_invalid} frontmatter issues")
        print(f"   • Fix {cover_invalid} cover image issues")
    
    return 0 if fm_invalid == 0 and cover_invalid == 0 else 1

if __name__ == "__main__":
    exit(main())
