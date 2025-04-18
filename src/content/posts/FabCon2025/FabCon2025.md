---
title: Key Takeaways from FabCon 2025

published: 2025-04-18T14:00:00.000Z
description: >-
  Mar-2025 Fabric feature update

tags:
  - Fabric
category: Fabric
image: "./cover.png"
draft: false
---

# Fabric March 2025 Updates

In this blog post, we discuss the significant updates announced at FabCon 2025, the community-run fabric conference that took place in Las Vegas. Though we couldn't attend personally, we will shared insights about Microsoft's rapidly evolving data platform and its positioning in the industry.

<iframe width="100%" height="468" src="https://www.youtube.com/embed/L1m7q_p4xw8" title="FabCon2025" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Fabric's Market Position

Microsoft Fabric now appears in four different Gartner Magic Quadrants, covering BI, data integration, machine learning, and other key areas. The consensus is that without Fabric, organizations would need four or five different tools to achieve comparable functionality. One of the most compelling benefits is the simplified security model - one-lake security with central ID management covering everything, eliminating the need to replicate data footprint and security configurations across multiple platforms.

## Platform Enhancements
The pace of innovation in Fabric remains impressively fast, with several platform-wide features announced:

- Variable Libraries: A new feature allowing variables to be defined at the workspace level, which can be shared across different environments. This addresses a key pain point in deployment scenarios, where connections to different environments (dev, production) previously required manual configuration.
- CI/CD Pipelines: Though not fully mature yet, Fabric's CI/CD capabilities are advancing. Currently, the hosts recommend using Azure DevOps for higher environment deployments, but they anticipate that within months, native Fabric deployment might eliminate this dependency.
- Multi-Tenant Organization Support: Now generally available, this feature supports organizations with multiple Active Directory domains.
- New Partner Workloads and Development Kit Improvements: Making it easier to build on top of Fabric, though compute layers still need to be separately hosted.

## Data Engineering Updates
Several key improvements were announced for data engineering workloads:

- Write-back Capability: Now available through smart notebooks.
- Row-Level and Column-Level Security in Spark: This brings the security granularity previously available in data warehouse to lakehouses, allowing direct lake setups to inherit security rules.
- User-Data Functions (UDFs): Expanding Fabric beyond analytics to include computation capabilities. One highlighted use case allows PowerBI report buttons to trigger UDFs that perform write-back operations via PySpark, enabling scenarios like a sales manager applying promotions directly from a report.
- Mirroring Enhancements: Expanded database support including PostgreSQL (in public preview), Cosmos DB for NoSQL, Snowflake, and Azure SQL Database with protected firewalls. On-premises SQL Server is in private preview.

## Data Science and AI
The AI capabilities are particularly exciting:

- Fabric Data Agent: Formerly called AI Skills, now integrated with Copilot Studio and Azure AI Foundry, making it easier to expose fabric data to chatbots and LLMs.
AI Functions in Data Warehouse: Allowing LLM-based workloads to run within the warehouse environment without requiring separate notebooks or PySpark setups.

## Data Integration and Real-Time Intelligence

- Real-Time Intelligence (RTI): Now supports MQDT, including Azure Event Grid, expanding beyond popular sources like Kinesis, Event Hubs, and Kafka.
- OneLake Catalogue in Excel: Accessing Fabic data in Excel is getting easier by the day.

## Copilot Accessibility
Perhaps the most significant announcement was the removal of the F64 capacity requirement for Copilot. Previously, only organizations with high-tier capacity could access Copilot features. Now, this AI assistance will be available at all capacity levels, though likely as a premium feature. This opens up new flexibility in capacity planning and makes powerful AI assistance accessible to more organizations.

## Looking Ahead
We noted that Fabric's development pace far exceeds other SaaS and BI solutions. We can envision a future where organizations only need to use Excel and Fabric to cover all their data needs. As the platform continues its rapid evolution, keeping up with changes presents challenges even for training developers, but this pace of innovation positions Fabric as an increasingly central platform in the Microsoft data ecosystem.