import { z, defineCollection } from 'astro:content';

// 공통 메타데이터
const baseMetadata = {
  keywords: z.array(z.string()).default([]),
  language: z.enum(['ko', 'en', 'both']).default('ko'),
};

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    title_en: z.string().optional(),
    excerpt: z.string(),
    excerpt_en: z.string().optional(),
    date: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    category: z.string(),
    tags: z.array(z.string()),
    image: z.string().optional(),
    author: z.string().default('Yonghee Kim'),
    enableShare: z.boolean().default(true),
    
    // 추가 필드
    ...baseMetadata,
    readingTime: z.number().optional(),
    wordCount: z.number().optional(),
    series: z.string().optional(),
    seriesOrder: z.number().optional(),
    relatedPosts: z.array(z.string()).default([]),
    views: z.number().default(0),
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
    
    // 추가 필드
    ...baseMetadata,
    research_area: z.array(z.string()).default([]),
    methodology: z.array(z.string()).default([]),
    data_period: z.object({
      start: z.string(),
      end: z.string(),
    }).optional(),
    sample_size: z.number().optional(),
    statistical_methods: z.array(z.string()).default([]),
    software_used: z.array(z.string()).default([]),
    funding: z.object({
      agency: z.string(),
      amount: z.number().optional(),
      grant_number: z.string().optional(),
    }).optional(),
    related_projects: z.array(z.string()).default([]),
  }),
});

const projectCollection = defineCollection({
  type: 'content',
  schema: z.object({
    // 기본 정보
    title: z.string(),
    title_en: z.string(),
    title_ko: z.string().optional(),
    subtitle: z.string().optional(),
    subtitle_en: z.string().optional(),
    subtitle_ko: z.string().optional(),
    
    // 날짜 (Date 타입으로 변경)
    date: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    
    // 분류
    category: z.string(),
    tags: z.array(z.string()),
    ...baseMetadata,
    
    // 이벤트 정보
    conference: z.string().optional(),
    conference_en: z.string().optional(),
    conference_ko: z.string().optional(),
    venue: z.string().optional(),
    
    // 내용
    description: z.string(),
    description_en: z.string().optional(),
    summary: z.string(),
    summary_en: z.string().optional(),
    key_findings: z.array(z.string()),
    key_findings_ko: z.array(z.string()).optional(),
    policy_proposals: z.array(z.string()).optional(),
    policy_concerns: z.array(z.string()).optional(),
    
    // 연구 메타데이터
    methodology: z.array(z.string()).default([]),
    data_period: z.object({
      start: z.string(),
      end: z.string(),
    }).optional(),
    sample_size: z.number().optional(),
    data_sources: z.array(z.object({
      name: z.string(),
      url: z.string().optional(),
      type: z.enum(['primary', 'secondary']).default('primary'),
    })).default([]),
    
    // 관계
    related_publications: z.array(z.string()).default([]),
    related_projects: z.array(z.string()).default([]),
    
    // 영향력
    featured: z.boolean().default(false),
    impact_metrics: z.object({
      views: z.number().default(0),
      downloads: z.number().default(0),
      citations: z.number().default(0),
    }).optional(),
    
    // 미디어
    image: z.string().optional(),
    images: z.array(z.string()).optional(),
    video_url: z.string().optional(),
    
    // 연구비
    funding: z.object({
      agency: z.string(),
      amount: z.number().optional(),
      grant_number: z.string().optional(),
    }).optional(),
  }),
});

export const collections = {
  'blog': blogCollection,
  'publications': publicationCollection,
  'projects': projectCollection,
};
