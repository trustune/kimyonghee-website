# kimyonghee.com

Personal academic website of Yonghee Kim, Assistant Professor at Sunmoon University.
Research focus: media policy, digital platforms, AI governance, and data analytics.

Live site: https://kimyonghee.com

## Tech Stack

- **Framework**: [Astro](https://astro.build) with MDX + Tailwind CSS
- **Content**: Markdown collections (publications, projects, blog, courses)
- **Math**: KaTeX via `remark-math` + `rehype-katex`
- **Deployment**: GitHub Actions → self-hosted server (Nginx + systemd)
- **Analytics**: Google Analytics 4

## Development

```bash
npm install
npm run dev      # local dev server at localhost:4321
npm run build    # production build to ./dist
npm run preview  # preview production build locally
```

## Content Sections

| Section | Path | Description |
|---|---|---|
| Research | `/research` | Publications with citation tracking (Google Scholar sync) |
| Projects | `/projects` | Research projects and data analyses |
| Writing | `/writing` | Blog posts on media policy and technology |
| Teaching | `/teaching` | Courses and syllabi |
| JournalINT | `/journalint` | Weekly academic journal intelligence dashboard |
| MediaINT | `/mediaint` | Weekly media industry intelligence briefing |

## Content Guidelines

See [CLAUDE.md](./CLAUDE.md) for bilingual content requirements (Korean + English frontmatter schema).
See [COMPONENTS_GUIDE.md](./COMPONENTS_GUIDE.md) for reusable component documentation.
See [JOURNALINT.md](./JOURNALINT.md) for JournalINT operational guide.

## License

Content © Yonghee Kim. Site code is available for reference; please don't copy the content.
