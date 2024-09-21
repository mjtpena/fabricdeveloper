---
title: Build a new Astro website in a day
published: 2024-09-21T14:00:00.000Z
description: >-
  This post covers the technology, operations and also the content creation aspects of building a website.
tags:
  - Astro
  - Web Development
  - Github Actions
  - GenAI
category: Web Development
image: "./cover.png"
draft: false
---

# How to Build an Astro Website In-A-Day?

In this blog post, we will discuss how to build an Astro website in a day. We will also discuss the benefits of using Astro and the different components that make up an Astro website.

<iframe width="100%" height="468" src="https://www.youtube.com/embed/g56DN6fAyDw" title="How to build an Astro Website In-A-Day?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What is Astro?

Astro is a new frontend framework that makes it easy to build fast, scalable, and SEO-friendly websites. Astro is built on top of the popular JavaScript framework React, but it offers a number of unique features that make it a great choice for building websites.

Some of the benefits of using Astro include:

* **Fast performance**: Astro websites are very fast because they are built using static site generation (SSG). This means that your website is pre-rendered into HTML, CSS, and JavaScript files, which can be served directly to users without the need for a server.
* **SEO-friendly**: Astro websites are very SEO-friendly because they are pre-rendered into HTML. This means that search engines can easily crawl and index your website's content.
* **Scalable**: Astro websites are very scalable because they can be easily deployed to any cloud platform.
* **Easy to use**: Astro is very easy to use, even for developers who are new to frontend development.

## Components of an Astro Website
An Astro website is made up of a number of different components, including:

* **Pages**: Pages are the individual pages of your website. Each page is made up of a template file and a data file.
* **Components**: Components are reusable pieces of code that can be used to create different parts of your website.
* **Layouts**: Layouts are used to define the overall structure of your website.
* **Data**: Data is used to store information that is used by your website.

## Building an Astro Website
To build the Astro website, we adopted the Fuwari template. You can clone our current website [here](https://github.com/mjtpena/fabricdeveloper).

```
git clone https://github.com/mjtpena/fabricdeveloper
```

Within the github repo, there is also clear instructions about running it on a local machine.

## Deploying an Astro Website
Once you have finished building your website, you can deploy it to a cloud platform. Astro supports deployment to a number of different platforms, including Netlify, Vercel, and GitHub Pages. We used the Azure Static Web Apps option as it is the simplest method including domain purchase and connection.

#### Create an Azure Static Website
Go to Azure portal and create a new app in Static Web Apps, with Source configured to the github repo.

#### Configure Github Workflow
Use the YML template below to set the trigger and action sequence in Github workflow.

```yml
name: Build and deploy Astro website to Azure Static Web Apps
on:
  push:
    branches: [main]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3   

      - name: Build Astro website
        run: npm run build
      - name: Deploy to Azure Static Web Apps
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{secrets.AZURE_STATIC_WEB_APPS_API_TOKEN}}   

          repo_name:   
 <your repository name>
          branch: main
          output_location: dist
```

#### Generate Contents with GenAI
While there are many ways of generating contents for the website, the following are currently being utilised.

* **Logo**: This is created in Dall-E via Microsoft Copilot.
* **Initial Blogs**: Google Gemini was used to summarise blog post contents from previous recorded YouTube videos.
* **Part of the codes**: Github Copilot was consulted about modification of the website.

#### Add / Update contents
Tina is the built-in Content Management Services (CMS). User can visit localhost to modify the code. Or alternatively, you can use VS code to add new / maintain exist.

To keep things simple, there is only 1 branch in the repo. We recommend any future changes to create a new branch and a new Pull Request. Once merged, Github Action will automatically update the website with latest changes. 

## Conclusion

Hope you enjoys the Non-Fabric contents this week.

## Additional Resources
* Azure Static-Web-Apps: [https://docs.microsoft.com/en-us/azure/static-web-apps/build-configuration](https://docs.microsoft.com/en-us/azure/static-web-apps/build-configuration)
* Astro: [https://docs.astro.build/en/getting-started/](https://docs.astro.build/en/getting-started/)
* Github Actions: [https://docs.github.com/en/actions/writing-workflows/quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart)
