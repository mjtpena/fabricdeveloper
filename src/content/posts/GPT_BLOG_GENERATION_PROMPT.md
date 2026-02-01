# GPT-4.1 Blog Post Generation Prompt

Use this prompt with GPT-4.1 (or similar) to generate blog posts from the calendar. You'll need to batch these - suggest doing 10-20 at a time.

---

## SYSTEM PROMPT

```
You are a technical content writer for FabricDeveloper.com, a website focused on Microsoft Fabric tutorials and guides for data engineers, analysts, and developers.

Your task is to generate blog posts about Microsoft Fabric topics. Each post should be:
- Technical but accessible to intermediate developers
- Practical with real-world examples and code snippets where appropriate
- 800-1500 words in length
- Written in a professional but conversational tone
- Focused on actionable insights for Fabric developers

IMPORTANT: Do NOT hallucinate features. If you're unsure about a specific feature's availability or syntax, use general descriptions and recommend the reader check official Microsoft documentation for the latest details.
```

---

## USER PROMPT TEMPLATE

```
Generate a Microsoft Fabric blog post with the following details:

**Title:** {TITLE}
**Date:** {DATE}
**Category:** {CATEGORY}

Create the output in TWO parts:

## PART 1: FOLDER AND FILE STRUCTURE

The post should be saved in this structure:
```
src/content/posts/{FOLDER-NAME}/
├── {FOLDER-NAME}.md
└── cover.png (placeholder - describe what image would be appropriate)
```

Where {FOLDER-NAME} is a kebab-case version of the title (e.g., "Getting Started with OneLake" → "Getting-Started-with-OneLake")

## PART 2: MARKDOWN FILE CONTENT

Generate the complete markdown file with this exact frontmatter format:

```markdown
---
title: {TITLE}

published: {DATE}T14:00:00.000Z
description: >-
  {ONE-LINE DESCRIPTION - max 100 chars}

tags:
  - Fabric
  - {ADDITIONAL RELEVANT TAG}
category: Fabric
image: "./cover.png"
draft: false
---

# {MAIN HEADING}

{INTRODUCTION PARAGRAPH - Hook the reader, explain what they'll learn}

## {SECTION 1 HEADING}

{Content with practical examples}

## {SECTION 2 HEADING}

{Content - include code blocks where appropriate using ```python, ```sql, ```kql etc.}

## {SECTION 3+ HEADINGS AS NEEDED}

{Continue with relevant sections}

## Key Takeaways

{Bullet points summarizing main learnings}

## Next Steps

{What the reader should do next, links to related topics}

## Resources

{List 2-3 official Microsoft documentation links - use placeholder URLs like:
- [Microsoft Fabric Documentation](https://learn.microsoft.com/fabric/)
- [Fabric Blog](https://blog.fabric.microsoft.com/)
}
```

## PART 3: IMAGE DESCRIPTION

Describe the ideal cover image for this post:
- Style: Modern, professional tech illustration
- Color scheme: Should complement Microsoft Fabric's orange/blue branding
- Subject: What should be depicted
- Format: 1200x630px recommended for social sharing

---

Now generate the blog post.
```

---

## BATCH PROCESSING EXAMPLE

To process multiple posts, use this format:

```
Generate blog posts for the following 10 entries from my Fabric blog calendar:

1. Title: "Getting Started with OneLake: Your First Data Lake" | Date: 2023-05-26 | Category: OneLake
2. Title: "OneLake Shortcuts Deep Dive: ADLS, S3, and GCS" | Date: 2023-05-27 | Category: OneLake
3. Title: "Building Your First Lakehouse in Microsoft Fabric" | Date: 2023-05-29 | Category: Lakehouse
...

For each post, provide:
1. Folder name (kebab-case)
2. Complete markdown file content with frontmatter
3. Brief cover image description

Use the format and guidelines specified in my system prompt.
```

---

## TAGS REFERENCE

Use these tags based on category:

| Category | Suggested Tags |
|----------|---------------|
| OneLake | Fabric, OneLake, Data Lake |
| Lakehouse | Fabric, Lakehouse, Delta Lake |
| Data Engineering | Fabric, Spark, Data Engineering |
| Data Factory | Fabric, Data Factory, ETL |
| Data Warehouse | Fabric, Data Warehouse, T-SQL |
| Data Science | Fabric, Data Science, Machine Learning |
| Real-Time Intelligence | Fabric, Real-Time, KQL |
| Power BI | Fabric, Power BI, Visualization |
| Administration | Fabric, Administration, Governance |
| DevOps | Fabric, DevOps, CI/CD |
| AI/Copilot | Fabric, GenAI, Copilot |
| Migration | Fabric, Migration |
| Security | Fabric, Security |
| Governance | Fabric, Governance, Purview |
| Best Practices | Fabric, Best Practices |
| Integration | Fabric, Integration |
| Tutorial | Fabric, Tutorial |
| Certification | Fabric, Certification, DP-600, DP-700 |
| Community | Fabric, Community |
| Troubleshooting | Fabric, Troubleshooting |
| Monthly Update | Fabric, Updates |
| Announcement | Fabric, Announcements |
| Feature Release | Fabric, New Features |

---

## AUTOMATION SCRIPT (Optional)

If you want to automate folder creation after generating content:

```powershell
# Create folder structure for a new post
param(
    [string]$FolderName
)

$basePath = "src/content/posts"
$fullPath = Join-Path $basePath $FolderName

# Create folder
New-Item -ItemType Directory -Path $fullPath -Force

# Create placeholder files
New-Item -ItemType File -Path (Join-Path $fullPath "$FolderName.md") -Force
New-Item -ItemType File -Path (Join-Path $fullPath "cover.png") -Force

Write-Host "Created: $fullPath"
```

---

## QUALITY CHECKLIST

Before publishing each generated post, verify:

- [ ] Frontmatter is valid YAML
- [ ] Date format is correct (YYYY-MM-DDTHH:MM:SS.000Z)
- [ ] Image path is "./cover.png"
- [ ] Tags include "Fabric" as first tag
- [ ] Category is "Fabric"
- [ ] No hallucinated features or incorrect syntax
- [ ] Code examples are syntactically correct
- [ ] Post length is 800-1500 words
- [ ] Cover image has been created/sourced

---

## SAMPLE OUTPUT

Here's what a complete output should look like:

### Folder Structure
```
src/content/posts/Getting-Started-with-OneLake/
├── Getting-Started-with-OneLake.md
└── cover.png
```

### File Content
```markdown
---
title: Getting Started with OneLake: Your First Data Lake

published: 2023-05-26T14:00:00.000Z
description: >-
  Learn the fundamentals of OneLake and create your first unified data lake in Microsoft Fabric

tags:
  - Fabric
  - OneLake
  - Data Lake
category: Fabric
image: "./cover.png"
draft: false
---

# Getting Started with OneLake: Your First Data Lake

OneLake is the foundation of Microsoft Fabric - a single, unified data lake for your entire organization. In this guide, you'll learn what makes OneLake unique and how to start using it effectively.

## What is OneLake?

OneLake is often described as "OneDrive for data." Just as OneDrive provides a single location for your files...

[... continue with full content ...]
```

### Image Description
**Style:** Minimalist tech illustration
**Colors:** Deep blue background with orange accent elements (Fabric branding)
**Subject:** Abstract representation of a data lake with interconnected nodes representing different data sources flowing into a central reservoir
**Format:** 1200x630px, PNG format

---

## NOTES FOR MILESTONE POSTS

For posts marked as "Milestone" type (announcements, feature releases, monthly updates):

1. **Be factual** - These are tied to real Microsoft announcements
2. **Include context** - When was this announced? (Build, Ignite, FabCon, monthly update)
3. **Focus on impact** - What does this mean for developers?
4. **Recommend verification** - Always suggest readers check official sources for latest details

Example for milestone posts:
```
This feature was announced at Microsoft Ignite 2023. As Fabric continues to evolve rapidly, 
we recommend checking the official Microsoft Fabric documentation for the latest details 
and any updates since this announcement.
```
