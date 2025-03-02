---
title: Microsoft Fabric Data Gateway Setup in Azure

published: 2025-03-02T14:00:00.000Z
description: >-
  Bridging the Gap Between On-Premises data sources and Fabric cloud workspaces.

tags:
  - Fabric
  - Infrastructure
category: Fabric
image: "./cover.png"
draft: false
---

# Microsoft Fabric Data Gateway: Bridging the Gap Between On-Premises and Cloud

In the evolving landscape of data analytics and business intelligence, Microsoft Fabric has emerged as a powerful platform that unifies various data workloads. One critical component of this ecosystem is the Data Gateway, which plays an essential role when connecting to data sources that aren't directly accessible through public networks.

<iframe width="100%" height="468" src="https://www.youtube.com/embed/4sRplK0nZYA" title="How to create and configure a Power BI Gateway on Azure VM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What is an On-premises Gateway?
As explained in a recent developer discussion between MJ (Microsoft MVP and MCT) and David, an on-premises Data Gateway serves as a bridge between Microsoft Fabric and data sources that reside in secure or private networks. This becomes particularly important in enterprise environments where you're working with a mix of Cloud based and on-premises data storage solutions.

## The Technical Setup
David demonstrated how he implemented a Gateway to connect Microsoft Fabric to a Clickhouse database (used for web traxusffic analysis via Plausible Community Edition) running in a private network. The process involved:

- Deploying a Windows VM specifically for the Gateway (the Gateway requires Windows, even though the Plausible Community Edition runs on Linux)
- Install and Configuring the Gateway on the Windows VM
- Signing into the Gateway with the same account used for Fabric
- Connecting to the data source through Fabric by selecting the configured Gateway

## Infrastructure Considerations
One interesting observation from the demonstration was that setting up the Gateway infrastructure can sometimes be more costly than the actual application it's connecting to. This is because the gateway must run on a Windows VM with certain [specification requirements]<https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-install>.

For those setting up the infrastructure, David used Infrastructure as Code techniques, making the Gateway deployment optional within the original application setup. The VM needs to be accessible remotely, which requires either an RDP (Remote Desktop Protocol) or using Azure Bastion as an alternative approach for connecting to the VM.

## When Do You Need a Gateway?
The Gateway is not always necessary. As clarified in the discussion:
- Cloud-native data infrastructure like Azure SQL doesn't require a Gateway
- On-premises data sources or data within an Azure network would need a Gateway
- Previously, connections to other cloud platforms (like Snowflake in AWS) required Gateways, but newer options like lakehouse shortcuts have reduced this need.

## Best Practices
### Service Accounts
For production environments, both experts highlighted the importance of using service accounts rather than personal accounts when configuring the Gateway:

"In the actual production environment, you want to reduce the dependency on a certain person... you don't want one person to leave or have an accident somewhere and suddenly the entire production environment might be compromised," David explained.

### Improve Reliability with clusters
Data gateway clusters helps to:
1. avoid single points of failure,
2. load balance traffice across gateways in a cluster

You can start up mutliple VMs to host separate gateway services. These gateway services can be configured into a cluster group to achieve the desired cluster benefits. Find out more about cluster configurations in this [learn documentation]<https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-high-availability-clusters>.