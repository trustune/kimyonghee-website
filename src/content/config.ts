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

export const collections = {
  'blog': blogCollection,
};
