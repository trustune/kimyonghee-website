import { z, defineCollection } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    excerpt: z.string(),
    date: z.string(),
    category: z.string(),
    tags: z.array(z.string()),
    image: z.string().optional(),
    author: z.string().default('Yonghee Kim'),
    enableShare: z.boolean().default(true),
  }),
});

const publicationCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    authors: z.array(z.string()),
    journal: z.string(),
    year: z.number(),
    type: z.string(),
    status: z.string(),
    category: z.string(),
    abstract: z.string(),
    volume: z.number().optional(),
    issue: z.union([z.string(), z.number()]).optional(),
    pages: z.string().optional(),
    doi: z.string().optional(),
    pdf: z.string().optional(),
    citations: z.number().default(0),
    impact_factor: z.number().optional(),
    quartile: z.string().optional(),
    publisher: z.string().optional(),
  }),
});

const projectCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    title_en: z.string(),
    subtitle: z.string().optional(),
    subtitle_en: z.string().optional(),
    date: z.string(),
    category: z.string(),
    tags: z.array(z.string()),
    conference: z.string().optional(),
    conference_en: z.string().optional(),
    description: z.string(),
    description_en: z.string(),
    summary: z.string(),
    key_findings: z.array(z.string()),
    policy_proposals: z.array(z.string()).optional(),
    featured: z.boolean().default(false),
    charts: z.array(z.object({
      id: z.string(),
      position: z.string(),
    })).optional(),
  }),
});

export const collections = {
  'blog': blogCollection,
  'publications': publicationCollection,
  'projects': projectCollection,
};
