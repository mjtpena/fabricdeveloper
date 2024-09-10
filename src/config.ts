import type {
  LicenseConfig,
  NavBarConfig,
  ProfileConfig,
  SiteConfig,
} from './types/config'
import { LinkPreset } from './types/config'

export const siteConfig: SiteConfig = {
  title: 'Fabric Developer',
  subtitle: 'Microsoft Fabric Resources for Developers',
  lang: 'en',
  themeColor: {
    hue: 260,
    fixed: true,
  },
  banner: {
    enable: false,  // Keeping this disabled until you have a banner image
    src: 'assets/images/demo-banner.png',  // Keeping the original reference
    position: 'center',
    credit: {
      enable: false,
      text: '',
      url: ''
    }
  },
  favicon: [
    // Keeping this empty until you have a custom favicon
  ]
}

export const navBarConfig: NavBarConfig = {
  links: [
    LinkPreset.Home,
    LinkPreset.Archive,
    LinkPreset.About,
    {
      name: 'GitHub',
      url: 'https://github.com/mjtpena/fabricdeveloper',
      external: true,
    },
  ],
}

export const profileConfig: ProfileConfig = {
  avatar: 'assets/images/fabric-avatar.png',  // Relative to the /src directory. Relative to the /public directory if it starts with '/'
  name: 'Fabirc Developer',
  bio: 'with MJ and Dave',
  links: [
    {
      name: 'LinkedIn',
      icon: 'fa6-brands:linkedin-in',       // Visit https://icones.js.org/ for icon codes
                                        // You will need to install the corresponding icon set if it's not already included
                                        // `pnpm add @iconify-json/<icon-set-name>`
      url: 'https://www.linkedin.com/company/fabricdeveloper',
    },
    {
      name: 'YouTube',
      icon: 'fa6-brands:youtube',
      url: 'https://www.youtube.com/@FabricDeveloper',
    },
    {
      name: 'GitHub',
      icon: 'fa6-brands:github',
      url: 'https://github.com/mjtpena/fabricdeveloper',
    },
  ],
}

export const licenseConfig: LicenseConfig = {
  enable: true,
  name: 'MIT License',
  url: 'https://opensource.org/licenses/MIT',
}