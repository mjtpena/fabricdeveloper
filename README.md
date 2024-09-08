🧵 Fabric Developer
A blog about Microsoft Fabric and content to help developers, built with Astro and Tina CMS.
🖥️ Live Site: https://fabricdeveloper.com    
📦 GitHub Repository

README version: 2024-09-08

✨ Features

 Content focused on Microsoft Fabric and developer resources
 Built with Astro for static site generation
 Tina CMS integration for local content management
 Automated deployment to Azure Static Web Apps using GitHub Actions
 Responsive design
 Light / dark mode
 Search functionality

👥 Authors

Michael John Peña
David Ding

🚀 Setup Guide

Prerequisites

Ensure you have Node.js 18 installed on your system.
Have an Azure account for deploying to Azure Static Web Apps.
Have a GitHub account for version control and automated deployments.


Clone the Repository
Copygit clone https://github.com/mjtpena/fabricdeveloper.git
cd fabricdeveloper

Install Dependencies
Copynpm install

Local Development

Start the development server:
Copynpm run dev

This will spin up Tina CMS for WYSIWYG blog editing and Astro for static site generation.
Access the local development site at http://localhost:4321


Creating Content

Use Tina CMS interface for creating and editing content locally.
New posts should be added in the appropriate directory (usually src/content/posts/).


Building for Production
Copynpm run build

Deployment

The project is set up to automatically deploy to Azure Static Web Apps using GitHub Actions.
Any push to the main branch will trigger a new deployment.
Ensure your Azure Static Web Apps service is properly configured to connect with your GitHub repository.



⚙️ Configuration

Astro configuration: astro.config.mjs
Tina CMS configuration: tina/config.ts
GitHub Actions workflow: .github/workflows/azure-static-web-apps-*.yml

🧞 Commands
CommandActionnpm installInstalls dependenciesnpm run devStarts local dev server at localhost:4321npm run buildBuild your production site to ./dist/npm run previewPreview your build locally, before deploying
🤝 Contributing
We welcome contributions to Fabric Developer! Please see our Contributing Guide for more details on how to get started.
📄 License
This project is licensed under the MIT License.
For more information about the project or to contribute, please visit https://fabricdeveloper.com/ or the GitHub repository at https://github.com/mjtpena/fabricdeveloper.