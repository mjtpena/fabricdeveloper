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
    fixed: false,
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
  avatar: 'assets/images/demo-avatar.png',  // Keeping the original reference
  name: 'Fabric Developer',
  bio: 'Empowering developers with Microsoft Fabric insights and resources',
  links: [
    {
      name: 'LinkedIn',
      icon: 'fa6-brands:linkedin',
      url: 'https://www.linkedin.com/company/fabricdeveloper',  // Replace with actual LinkedIn account
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