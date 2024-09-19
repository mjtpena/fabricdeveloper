---
title: Direct Lake VS Import and Direct Query
published: 2024-06-26T14:00:00.000Z
description: >-
  Microsoft Fabric Direct Lake demo. Comparing it with Import and Direct Query.
tags:
  - DirectLake
  - Lakehouse
  - PowerBI
  - DirectQuery
category: Fabric
image: "./cover.png"
draft: false
---

# Direct Lake VS Import and Direct Query

Direct Lake is an exciting feature in Microsoft Fabric that allows you to query data directly from the Lakehouse. This is a major improvement over the previous methods of importing data or using direct query, as it eliminates the need to duplicate data and provides faster query performance.

<iframe width="100%" height="468" src="https://www.youtube.com/embed/Z9THOu7j45w" title="Microsoft Fabric - Direct Lake" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Why is Direct Lake so awesome?

Direct Lake is a major improvement over the previous methods of importing data or using direct query. Here are some of the benefits of using Direct Lake:

* **Eliminates the need to duplicate data**: When you import data into a Power BI workspace, you are creating a duplicate copy of the data. This can waste storage space and make it difficult to keep the data up to date. With Direct Lake, you can query data directly from the data lake, without having to create a duplicate copy.
* **Provides faster query performance**: Direct query can be slow, especially when querying large datasets. With Direct Lake, you can query data directly from the data lake, which can provide much faster query performance.
* **Supports a wider range of data types**: Direct query is limited to a narrow range of data types. With Direct Lake, you can query data of any type.
* **Is more scalable**: Direct query can be difficult to scale to large datasets. With Direct Lake, you can scale your data lake to handle any size of dataset.
* **Is more flexible**: Direct query is less flexible than importing data. With Direct Lake, you can query data in a variety of ways.

In addition to the benefits mentioned in the video, Direct Lake also has the following benefits:

* **Is more secure**: Direct query can be less secure than importing data, as it requires you to grant Power BI access to your data lake. With Direct Lake, you can control access to your data lake using role-based access control (RBAC).
* **Is easier to manage**: Direct query can be difficult to manage, as it requires you to configure a variety of settings. With Direct Lake, you can manage your data lake using a simple interface.
* **Is more cost-effective**: Direct query can be more expensive than importing data, as it requires you to pay for additional storage and compute resources. With Direct Lake, you can pay for only the resources that you need.

## How to use Direct Lake

To use Direct Lake, you first need to create a Lakehouse in your Microsoft Fabric workspace. Once you have created a Lakehouse, you can load data into it using a pipeline. Once the data has been loaded, you can create a report in Power BI Desktop that is linked to the Lakehouse. When you create the report, you will be able to query the data directly from the Lakehouse, without having to import it into the Power BI workspace.

## Conclusion
Overall, Direct Lake is a powerful new feature that has the potential to revolutionize the way that organizations analyze data. If you are looking for a way to improve your data analysis capabilities, I encourage you to try out Direct Lake.

## Additional Resources
* Direct Lake: [https://learn.microsoft.com/en-us/fabric/get-started/direct-lake-overview](https://learn.microsoft.com/en-us/fabric/get-started/direct-lake-overview)

## Note
Modified content based on Google Gemini extraction of the YouTube video.