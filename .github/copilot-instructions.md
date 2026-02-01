# Copilot Instructions for fabricdeveloper

## Build, Test, and Lint Commands

- **Install dependencies:**
  - `npm install`
- **Start local development server:**
  - `npm run dev` (Tina CMS + Astro at http://localhost:4321)
- **Build for production:**
  - `npm run build` (outputs to `./dist/`)
- **Preview production build:**
  - `npm run preview`
- **Lint and format:**
  - `npm run lint` (biome check)
  - `npm run format` (biome format)
- **Type check:**
  - `npm run type-check`
- **Create a new post:**
  - `npm run new-post -- <filename>` (creates a Markdown file in `src/content/posts/`)

> **Note:** There are no project-specific test scripts. Linting and type-checking are enforced via Biome and TypeScript.

## High-Level Architecture

- **Framework:** Astro (static site generator) with Svelte components and Tina CMS for content management.
- **Content:** Markdown files in `src/content/posts/` (frontmatter schema enforced by Tina and Astro Content Collections).
- **CMS:** Tina CMS is configured for local editing and content schema.
- **Styling:** Tailwind CSS (see `tailwind.config.cjs`).
- **Search:** Pagefind is used for static search indexing after build.
- **Deployment:** Automated via GitHub Actions to Azure Static Web Apps (see `.github/workflows/azure-static-web-apps-*.yml`).
- **Config:**
  - Site, navbar, and profile config in `src/config.ts`
  - Astro config in `astro.config.mjs`
  - Tina CMS config in `tina/config.ts`

## Key Conventions

- **Content Posts:**
  - All blog posts are Markdown files in `src/content/posts/` with required frontmatter: `title`, `published`, `description`, `tags`, `category`, `draft`, `language`, `image`.
  - Use `npm run new-post -- <filename>` to scaffold new posts with correct frontmatter.
- **Navigation:**
  - Navbar links are defined in `src/config.ts` using `LinkPreset` or custom objects.
- **Theme:**
  - Theme color (hue) and dark/light mode are user-configurable and persisted in localStorage.
- **Custom Markdown Plugins:**
  - Custom remark/rehype plugins for reading time, excerpts, admonitions, and GitHub cards are registered in `astro.config.mjs` and live in `src/plugins/`.
- **TypeScript Paths:**
  - Use `@components/*`, `@utils/*`, etc. for imports as defined in `tsconfig.json`.
- **Linting:**
  - Biome is used for linting and formatting. See `biome.json` for rules.

---

This file was generated to help Copilot and other AI tools understand the structure, commands, and conventions of this repository. If you add new major features or conventions, please update this file.
