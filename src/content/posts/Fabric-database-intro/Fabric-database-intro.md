---
title: Fabric Gets a Game Changer - Fabric Database
published: 2024-12-04T14:00:00.000Z
description: >-
  What's so special about Fabric SQL Database?
tags:
  - Fabric
  - SQL
  - Database
  - Mirroring
category: Fabric
image: "./cover.png"
draft: false
---

# Fabric Gets a Game Changer: Introducing Fabric Database

This blog post explores the exciting new addition to Microsoft's Fabric platform - Fabric Database. MJ and Dave talks about the infrastructure, how it works and also the practical implications of this new feature.

Until recently, Power BI and Fabric were seen as a super powerful analytical engine for data consumption related tasks tasks like data transformation, data science and reporting. However, Fabric Database changes the landscape by introducing transactional database capabilities. This allows Fabric to cater to both analytical and transactional needs, making it the most comprehensive data solution in the market.

<iframe width="100%" height="468" src="https://www.youtube.com/embed/4KD9uWD4E34" title="What&#39;s so special about Fabric SQL Database?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Mirroring Azure SQL Database for Near Real-Time Replication

The magic behind Fabric Database lies in its connection to Azure SQL Database. Fabric mirrors an existing Azure SQL Database, enabling near real-time replication through Change Data Capture (CDC). This replicated data resides in Delta Park format within Fabric, forming the foundation for its analytical muscle.

## Fabric Creates and Manages Azure SQL Databases on Your Behalf

Fabric simplifies database provisioning. Unlike traditional methods where you create a server and then a database within Azure, Fabric handles everything. You simply request a database, and Fabric creates a managed Azure SQL Database for you. Costs associated with this database are billed through your Fabric capacity, eliminating the need for separate Azure subscriptions and resource groups.

## Seamless Integration Between Fabric and Azure SQL Database

Fabric acts as a wrapper around the managed Azure SQL Database, utilizing a Secure Access Signature (SAS) model. This provides a familiar experience for users who can connect to the database using Azure Data Studio or SQL Server Management Studio (SSMS) with their existing Azure AD or Entra credentials.

## Transactional and Analytical Workloads Under One Roof

Fabric Database caters to both transactional and analytical workloads. You can perform data insertion and edits in the transactional database. The changes will be captured and batch processed at frequent intervals (~10 min during demo). This data can be consumed via the endpoint connection strings for reporting and various other purposes.

## The Future of Fabric: Beyond SQL Databases and Towards AI

The introduction of Fabric Database hints at a future where Fabric integrates various database types beyond just T-SQL, e.g. Postgres. Additionally, with vector database capabilities in Azure SQL under public preview. It may enable future Gen AI usage scenarios such as Chat to SQL.

## Conclusion

Fabric Database is a significant addition to the Fabric platform, transforming it from a pure analytics engine into a comprehensive data solution. It offers a simplified development experience, streamlines data management, and paves the way for future integration with various data sources and functionalities.