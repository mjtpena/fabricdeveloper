# 🧵 Fabric Developer

A blog about Microsoft Fabric and content to help developers, built with Astro and Tina CMS.

[**🖥️ Live Site**](https://fabricdeveloper.com/) | 
[**📦 GitHub Repository**](https://github.com/mjtpena/fabricdeveloper)

> README version: `2024-09-08`

## ✨ Features

- Content focused on Microsoft Fabric and developer resources
- Built with [Astro](https://astro.build) for static site generation
- [Tina CMS](https://tina.io/) integration for local content management
- Automated deployment to Azure Static Web Apps using GitHub Actions
- Responsive design
- Light / dark mode
- Search functionality

## 👥 Authors

- [Michael John Peña](https://www.linkedin.com/in/michaeljohnpena/)
- [David Ding](https://www.linkedin.com/in/david-ding-38442721/)

## 🚀 Setup Guide

1. **Prerequisites**
   - Node.js 18
   - Azure account for Static Web Apps
   - GitHub account

2. **Clone the Repository**
```bash
git clone https://github.com/mjtpena/fabricdeveloper.git
cd fabricdeveloper
```

3. **Install Dependencies**
```bash
npm install
```

4. **Local Development**
```bash
npm run dev
```
Access the local site at `http://localhost:4321`

5. **Creating Content**
- Use Tina CMS interface for content management
- Add new posts in `src/content/posts/`

6. **Building for Production**
```bash
npm run build
```

7. **Deployment**
- Automated via GitHub Actions to Azure Static Web Apps
- Pushes to main branch trigger deployment

## ⚙️ Configuration

- Astro: `astro.config.mjs`
- Tina CMS: `tina/config.ts`
- GitHub Actions: `.github/workflows/azure-static-web-apps-*.yml`

## 🧞 Commands

| Command         | Action                                           |
|:----------------|:-------------------------------------------------|
| `npm install`   | Installs dependencies                            |
| `npm run dev`   | Starts local dev server at `localhost:4321`      |
| `npm run build` | Build your production site to `./dist/`          |
| `npm run preview` | Preview your build locally, before deploying     |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the [MIT License](LICENSE.md).

For more information, visit [https://fabricdeveloper.com/](https://fabricdeveloper.com/)