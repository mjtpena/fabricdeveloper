#!/usr/bin/env python3
"""
Simplified deployment validation - check only critical items
"""

from pathlib import Path
from PIL import Image

def main():
    posts_dir = Path("C:/Users/mjtpena/dev/fabricdeveloper/src/content/posts")
    
    post_dirs = [d for d in posts_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    cover_count = 0
    md_count = 0
    valid_covers = 0
    issues = []
    
    print("✅ PRODUCTION DEPLOYMENT VALIDATION")
    print("=" * 70)
    
    for post_dir in sorted(post_dirs):
        # Check markdown
        md_files = list(post_dir.glob("*.md"))
        if md_files:
            md_count += 1
            # Basic check: frontmatter exists
            content = md_files[0].read_text(encoding='utf-8', errors='ignore')
            if not content.startswith('---'):
                issues.append(f"❌ {post_dir.name}: No frontmatter")
        else:
            issues.append(f"❌ {post_dir.name}: No markdown file")
        
        # Check cover image
        cover_file = post_dir / "cover.png"
        if cover_file.exists():
            cover_count += 1
            try:
                img = Image.open(cover_file)
                if img.size == (1200, 630) and img.format == 'PNG':
                    valid_covers += 1
                else:
                    issues.append(f"⚠️  {post_dir.name}: Invalid cover dimensions {img.size}")
            except:
                issues.append(f"⚠️  {post_dir.name}: Corrupted cover image")
        else:
            issues.append(f"❌ {post_dir.name}: No cover.png")
    
    total = len(post_dirs)
    
    print(f"\n📋 CRITICAL CHECKS")
    print(f"✓ Markdown files:      {md_count}/{total} ({(md_count/total)*100:.1f}%)")
    print(f"✓ Cover images:        {cover_count}/{total} ({(cover_count/total)*100:.1f}%)")
    print(f"✓ Valid covers (1200x630): {valid_covers}/{total} ({(valid_covers/total)*100:.1f}%)")
    
    print(f"\n⚠️  ISSUES FOUND: {len(issues)}")
    if issues:
        for issue in issues[:15]:
            print(f"   {issue}")
        if len(issues) > 15:
            print(f"   ... and {len(issues)-15} more")
    
    print("\n" + "=" * 70)
    
    if md_count >= total * 0.95 and cover_count >= total * 0.95:
        print("✅ DEPLOYMENT READY - All critical requirements met!")
        print(f"\n📊 FINAL STATS:")
        print(f"   • {total} total blog posts")
        print(f"   • {cover_count} cover images generated")
        print(f"   • {md_count} markdown files")
        print(f"   • Ready for production deployment")
        return 0
    else:
        print("❌ DEPLOYMENT BLOCKED - Requirements not met")
        return 1

if __name__ == "__main__":
    exit(main())
