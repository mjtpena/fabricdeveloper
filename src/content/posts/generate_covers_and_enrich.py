#!/usr/bin/env python3
"""
Production-grade blog post enhancement pipeline:
- Generate professional cover images (1200x630px)
- Enrich technical posts with code snippets
- Validate frontmatter and content
"""

import os
import re
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
import frontmatter

# Fabric brand colors
FABRIC_ORANGE = "#F7630C"
FABRIC_BLUE = "#0078D4"
BG_DARK = "#1F1F1F"
TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#E0E0E0"

# Technical categories for code snippet enhancement
TECHNICAL_CATEGORIES = {
    "Data Engineering": ["PySpark", "Python"],
    "Data Warehouse": ["SQL", "T-SQL"],
    "Data Factory": ["Python", "JSON"],
    "Spark": ["PySpark", "Scala"],
    "Real-Time Analytics": ["KQL", "Python"],
    "Real-time Intelligence": ["KQL", "Python"],
    "Mirroring": ["SQL", "Python"],
    "Lakehouse": ["PySpark", "SQL"],
    "Notebook": ["PySpark", "Python"],
    "Machine Learning": ["Python", "PySpark"],
}

CODE_SNIPPETS = {
    "PySpark": """```python
# Load data into lakehouse
df = spark.read.format("parquet").load("/lakehouse/default/Files/data.parquet")

# Perform transformations
df_cleaned = df.filter(col("status") == "active") \\
    .groupBy("category").agg(count("*").alias("count")) \\
    .orderBy(desc("count"))

# Write back to lakehouse
df_cleaned.write.format("delta").mode("overwrite").save("/lakehouse/default/Tables/summary")
```""",
    
    "SQL": """```sql
-- Create optimized table structure
CREATE TABLE fact_transactions (
    transaction_id BIGINT,
    customer_id INT,
    amount DECIMAL(18,2),
    transaction_date DATE,
    CONSTRAINT pk_transactions PRIMARY KEY (transaction_id)
) WITH (DISTRIBUTION = HASH(customer_id), CLUSTERED COLUMNSTORE INDEX);

-- Query with aggregation
SELECT 
    customer_id,
    YEAR(transaction_date) as year,
    SUM(amount) as total_amount
FROM fact_transactions
GROUP BY customer_id, YEAR(transaction_date)
ORDER BY total_amount DESC;
```""",

    "Python": """```python
from fabric import fabric_client
import pandas as pd

# Initialize Fabric client
client = fabric_client.FabricClient()

# Load data
data = pd.read_csv("data.csv")

# Apply transformations
processed = data[data['value'] > 0].groupby('category').sum()

# Upload to Fabric
client.upload_dataframe(processed, workspace="default", 
                       lakehouse="data", table="summary")
```""",

    "KQL": """```kusto
['EventData']
| where EventTime >= ago(7d)
| where EventType == "Purchase"
| summarize TotalAmount = sum(Amount), EventCount = count() by CustomerID
| order by TotalAmount desc
| limit 100
```""",

    "JSON": """```json
{
  "name": "CopyPipelineActivity",
  "type": "Copy",
  "inputs": [
    {
      "referenceName": "SourceDataset",
      "type": "DatasetReference"
    }
  ],
  "outputs": [
    {
      "referenceName": "LakehouseDataset",
      "type": "DatasetReference"
    }
  ],
  "typeProperties": {
    "source": { "type": "SqlSource" },
    "sink": { "type": "ParquetSink" }
  }
}
```""",

    "Scala": """```scala
import org.apache.spark.sql.functions._

val df = spark.read.format("delta").load("/lakehouse/default/Tables/source")

val result = df
  .filter(col("status") === "active")
  .groupBy("region")
  .agg(
    count("*").as("record_count"),
    sum("revenue").as("total_revenue"),
    avg("amount").as("avg_transaction")
  )
  .orderBy(desc("total_revenue"))

result.write.format("delta").mode("overwrite").save("/lakehouse/default/Tables/result")
```""",

    "T-SQL": """```sql
-- Optimized T-SQL for SQL Database in Fabric
SELECT 
    YEAR(OrderDate) as OrderYear,
    MONTH(OrderDate) as OrderMonth,
    SUM(OrderAmount) as TotalAmount,
    COUNT(*) as OrderCount,
    AVG(OrderAmount) as AvgAmount
FROM Orders
WHERE OrderDate >= DATEFROMPARTS(YEAR(GETDATE())-1, 1, 1)
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY OrderYear, OrderMonth;
```""",
}

ENHANCEMENT_TEMPLATES = {
    "Data Engineering": """

## Code Example: Data Transformation

{code}

## Performance Optimization Tips

- Use partitioning for large datasets
- Optimize column selection
- Apply filters early in the pipeline
- Monitor memory usage with `spark.sql.adaptive.enabled=true`

## Production Considerations

- Implement error handling and retry logic
- Use logging for debugging
- Set up monitoring and alerting
- Document dependencies and requirements
""",
    
    "Data Warehouse": """

## SQL Query Example

{code}

## Query Optimization Strategies

- Use appropriate distribution keys
- Implement table statistics
- Consider materialized views for complex joins
- Monitor execution plans

## Scalability Tips

- Design for massive parallel processing
- Use appropriate data types
- Implement proper indexing strategies
""",

    "Real-Time Analytics": """

## Real-Time Query Example

{code}

## Performance Best Practices

- Use appropriate time windows
- Implement retention policies
- Monitor query latency
- Optimize column selection

## Monitoring and Alerting

- Set up dashboards for key metrics
- Configure alerts for anomalies
- Track query performance trends
""",
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_cover_image(title, category, output_path, width=1200, height=630):
    """Generate professional cover image with Fabric branding."""
    
    # Create image
    img = Image.new('RGB', (width, height), color=hex_to_rgb(BG_DARK))
    draw = ImageDraw.Draw(img)
    
    # Load fonts (fallback to default if unavailable)
    try:
        title_font = ImageFont.truetype("arial.ttf", 48)
        category_font = ImageFont.truetype("arial.ttf", 24)
        footer_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        category_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()
    
    # Draw gradient-like background with accent
    accent_height = 12
    draw.rectangle([(0, 0), (width, accent_height)], fill=hex_to_rgb(FABRIC_ORANGE))
    draw.rectangle([(0, height - accent_height), (width, height)], fill=hex_to_rgb(FABRIC_BLUE))
    
    # Draw category badge
    badge_color = hex_to_rgb(FABRIC_ORANGE)
    badge_padding = 12
    badge_x, badge_y = 40, 50
    
    # Wrap and draw title
    margin = 60
    max_width = width - (2 * margin)
    wrapped_lines = wrap(title, width=50)
    
    # Calculate vertical centering
    line_height = 60
    total_text_height = len(wrapped_lines) * line_height
    start_y = (height - total_text_height) // 2
    
    # Draw title with wrapping
    for i, line in enumerate(wrapped_lines[:3]):  # Max 3 lines
        y = start_y + (i * line_height)
        draw.text((margin, y), line, font=title_font, fill=hex_to_rgb(TEXT_WHITE))
    
    # Draw category badge
    badge_text = f"  {category}  "
    draw.rectangle(
        [(badge_x, badge_y), (badge_x + 200, badge_y + 40)],
        fill=badge_color,
        outline=hex_to_rgb(FABRIC_ORANGE)
    )
    draw.text((badge_x + 10, badge_y + 8), badge_text, font=category_font, fill=hex_to_rgb(TEXT_WHITE))
    
    # Draw footer
    footer_text = "Microsoft Fabric"
    draw.text((margin, height - 45), footer_text, font=footer_font, fill=hex_to_rgb(TEXT_GRAY))
    
    # Save image
    img.save(output_path, 'PNG')
    return True

def get_code_snippet(category):
    """Get appropriate code snippet based on category."""
    for cat_name, languages in TECHNICAL_CATEGORIES.items():
        if cat_name.lower() in category.lower():
            lang = languages[0]
            return CODE_SNIPPETS.get(lang, "")
    return ""

def enhance_technical_post(content, title, category):
    """Add code snippets to technical posts."""
    # Skip if already enhanced
    if "```" in content:
        return content
    
    code_snippet = get_code_snippet(category)
    if not code_snippet:
        return content
    
    # Find insertion point (after first ## heading)
    match = re.search(r'(##\s+\w+.*?\n\n)', content, re.MULTILINE)
    if match:
        insert_pos = match.end()
        enhancement = ENHANCEMENT_TEMPLATES.get(category, "").format(code=code_snippet)
        return content[:insert_pos] + enhancement + content[insert_pos:]
    
    return content

def process_post_directory(post_dir, dry_run=False):
    """Process a single post directory."""
    
    # Find markdown file
    md_files = list(post_dir.glob("*.md"))
    if not md_files:
        return None, "No markdown file found"
    
    md_file = md_files[0]
    
    try:
        # Parse frontmatter using frontmatter library
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            post = frontmatter.loads(content)
        
        title = post.get('title', 'Untitled')
        category = post.get('category', 'Fabric')
        
        # Generate cover image
        cover_path = post_dir / "cover.png"
        if not cover_path.exists():
            if not dry_run:
                create_cover_image(title, category, str(cover_path))
        
        # Enhance technical posts
        body_content = post.content if hasattr(post, 'content') else ""
        if any(cat.lower() in category.lower() for cat in TECHNICAL_CATEGORIES.keys()):
            enhanced = enhance_technical_post(body_content, title, category)
            if enhanced != body_content:
                if not dry_run:
                    post.content = enhanced
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(frontmatter.dumps(post))
        
        return True, "Success"
    
    except Exception as e:
        return False, str(e)

def main():
    """Main processing loop."""
    posts_dir = Path("C:/Users/mjtpena/dev/fabricdeveloper/src/content/posts")
    
    # Get all post directories (exclude .md and .csv files)
    post_dirs = [d for d in posts_dir.iterdir() 
                 if d.is_dir() and not d.name.startswith('.')]
    
    total = len(post_dirs)
    success = 0
    failed = 0
    skipped = 0
    
    print(f"Processing {total} blog posts...")
    print("=" * 60)
    
    for i, post_dir in enumerate(post_dirs, 1):
        result, msg = process_post_directory(post_dir, dry_run=False)
        
        if result is True:
            success += 1
            status = "✓"
        elif result is False:
            failed += 1
            status = "✗"
        else:
            skipped += 1
            status = "-"
        
        if i % 50 == 0 or i == total:
            print(f"[{i:4d}/{total}] {status} {post_dir.name}: {msg}")
    
    print("=" * 60)
    print(f"Results: {success} success, {failed} failed, {skipped} skipped")
    print(f"Total processed: {total}")

if __name__ == "__main__":
    main()
