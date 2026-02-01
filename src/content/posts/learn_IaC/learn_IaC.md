---
title: Learning IaC (Infrastructure as Code) 

published: 2025-01-31T14:00:00.000Z
description: >-
    A critical step towards AI LLM architecture.

tags:
  - GenAI
  - Infrastructure
category: Infrastructure
image: "./cover.png"
draft: false
---

# Learning Infrastructure as Code

The world of Data and AI is in constant flux, demanding that practitioners broaden their skillsets. This post explores a recent journey into the realm of infrastructure, highlighting key learnings and demonstrating how a deeper understanding of this foundational layer can enhance AI capabilities.

<iframe width="100%" height="468" src="https://www.youtube.com/embed/WiO9lAxiu20" title="Learning IaC - Infrastructure as Code with Bicep" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## AI and the Infrastructure Gap

The initial spark for this infrastructure deep dive was a desire to explore the world of AI, specifically the new AI stack, including various labs involving PROMPTY.  However, it quickly became apparent that a significant gap existed in understanding the underlying infrastructure required to effectively implement AI solutions. This realization prompted a focused effort to build expertise in this critical area.  Navigating the complexities of setting up the correct environment for AI infrastructure, and working with Microsoft Learn resources, including GitHub repositories, exposed the crucial role of tools like Bicep and YAML. Deciphering these technologies became a priority.

## A Practical Project: Plausible Deployment

A real-world project emerged during this learning process: deploying the [Plausible Community Edition](https://plausible.io/blog/community-edition), an open-source alternative to Google Analytics, on an Azure environment. This project offered a practical application of infrastructure concepts and provided a valuable tool for enhancing our BI efforts. Plausible offers website traffic monitoring capabilities, allowing us to gain insights into audience engagement. The goal was to deploy Plausible and eventually integrate the collected web traffic data into our Fabric content, enabling real-time analytics and other advanced BI functions.

## The Power of IaC: Bicep and GitHub Copilot

A key takeaway from this experience is the power of Infrastructure as Code (IaC).  By using Bicep, we were able to define and manage our infrastructure in a declarative way. This approach offers significant advantages, including reproducibility and consistency. The Bicep code for deploying Plausible Community Edition on an Azure virtual machine is available in a [public repository](https://github.com/yidaveding/plausible-selfhost), allowing others to benefit from this work. The learning curve for Bicep was significantly eased by the use of [GitHub Copilot](https://github.com/features/copilot). This AI-powered tool proved invaluable in generating code snippets and providing guidance on Bicep syntax and best practices, accelerating development.

## System Architecture: VM, PostgreSQL, and ClickHouse

The deployed Plausible instance utilizes a standard DS1 v2 virtual machine, a cost-effective option that provides sufficient resources. The data collected by Plausible is stored in two separate databases: PostgreSQL for system-related information (accounts, logins) and ClickHouse for event data (website traffic). This separation allows for efficient handling of different data types.

## The Next Steps: Fabric Integration and Real-Time Analytics

The next step is to connect Fabric to the Plausible data to create dashboards and reports. We also plan to explore real-time analytics, potentially involving integration with Azure Event Hubs. This presents new challenges, as Plausible currently relies on ClickHouse for data aggregation. Directly integrating with Event Hubs might require modifications to the Plausible codebase or a data pipeline to copy data from ClickHouse to Event Hubs. This requires further investigation.

## Conclusion: Embracing IaC as the Future of Data and AI

This journey into infrastructure has reinforced the importance of a holistic understanding of the technology stack for Data and AI professionals. By bridging the gap between data and infrastructure, we unlock new possibilities for future applications to gain deeper insights.
