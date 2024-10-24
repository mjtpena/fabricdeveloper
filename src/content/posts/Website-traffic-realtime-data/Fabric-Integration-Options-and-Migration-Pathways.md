---
title: Real use case for Fabric Realtime Analytics - Web traffic streaming
published: 2024-10-24T14:00:00.000Z
description: >-
  Fabric Developer explores a real use case on the Fabric realtime analytics capabilities with web traffic streaming.
tags:
  - Fabric
  - Eventhouse
  - Eventhub
  - Realtime
  - KQL Database
  - Power BI
category: Fabric
image: "./cover.png"
draft: false
---

# Real use case for Fabric Realtime Analytics - Web traffic streaming

In this video, Dave and MJ will discuss how to use Fabric Realtime Analytics to track and analyze web traffic data. We will also cover how to use the Power BI connector to create a live dashboard of your web traffic data.

<iframe width="100%" height="468" src="https://www.youtube.com/embed/k9MmwGmJXFA" title="Real use case for Fabric Realtime Analytics - Web traffic streaming" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What is Fabric Realtime Analytics?
Fabric Realtime Analytics is a cloud-based service that allows you to collect, process, and analyze data in real time. It is a fully managed service, so you don't have to worry about setting up or managing any infrastructure.

## Use case: Web traffic data
In the abscent of actual IoT devices (we might actually get one in the future). In order to demonstrate the realtime analytics capabilities in Fabric, we've decided to use the web traffic data. The infrastructure adopted is as shown in Figure 1.

<p align="center">
  <img src="/images/web traffic data stream flow.png" alt="web traffic data flow">
  <em>Figure 1. Data flow diagram</em>
</p>

## How to create a Fabric Realtime Analytics solution
Assuming you already have Eventhub setup with live data connection, the key steps in creating a realtime analytics solution in Fabric is as follows.

* **Create a workspace with fabric capacity**: Create a new workspace if there is not an existing workspace suitable for the reporting application. 
* **Create an Eventhouse**: Within the workspace create an Eventhouse.
* **Connect to Event Hub**: Select *Get Data* and add a new table under the database.
* **Enter Event Hub connection detail**: When asked, copy the Eventhub connection detail from the exisitng Eventhub.

## Create a Power BI report
Now the data is already flowing into the KQL database, you can right click on the KQL table and select *Power BI*. This will allow you to setup the required LIVE data connection to the web traffic data in the Eventhub!

## Note
Modified content based on Google Gemini extraction of the YouTube video.