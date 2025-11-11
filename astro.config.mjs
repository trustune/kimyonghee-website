import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://kimyonghee.com',

  integrations: [
    mdx(),
    sitemap(),
  ],

  vite: {
    plugins: [tailwindcss()],
  },

  image: {
    // Sharp를 사용한 이미지 최적화
    service: {
      entrypoint: 'astro/assets/services/sharp',
      config: {
        limitInputPixels: false,
      }
    },
    // 이미지 포맷 설정
    remotePatterns: [],
  },

  // 빌드 최적화
  build: {
    inlineStylesheets: 'auto',
  },
});
