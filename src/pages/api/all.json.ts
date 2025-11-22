import { getCollection } from 'astro:content';

export async function GET() {
  const [projects, publications, blog] = await Promise.all([
    getCollection('projects'),
    getCollection('publications'),
    getCollection('blog'),
  ]);
  
  const data = {
    metadata: {
      generated_at: new Date().toISOString(),
      counts: {
        projects: projects.length,
        publications: publications.length,
        blog: blog.length,
        total: projects.length + publications.length + blog.length,
      },
      categories: {
        projects: [...new Set(projects.map(p => p.data.category))],
        publications: [...new Set(publications.map(p => p.data.category))],
        blog: [...new Set(blog.map(p => p.data.category))],
      },
    },
    projects: projects
      .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
      .map(p => ({
        id: p.slug,
        url: `/projects/${p.slug}`,
        title: p.data.title,
        title_en: p.data.title_en,
        category: p.data.category,
        date: p.data.date.toISOString().split('T')[0],
        tags: p.data.tags,
        keywords: p.data.keywords,
        featured: p.data.featured,
      })),
    publications: publications
      .sort((a, b) => b.data.year - a.data.year)
      .map(p => ({
        id: p.slug,
        url: `/research/${p.slug}`,
        title: p.data.title,
        authors: p.data.authors,
        journal: p.data.journal,
        year: p.data.year,
        citations: p.data.citations,
        keywords: p.data.keywords,
      })),
    blog: blog
      .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
      .map(p => ({
        id: p.slug,
        url: `/blog/${p.slug}`,
        title: p.data.title,
        date: p.data.date.toISOString().split('T')[0],
        category: p.data.category,
        tags: p.data.tags,
      })),
  };
  
  return new Response(JSON.stringify(data, null, 2), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    }
  });
}
