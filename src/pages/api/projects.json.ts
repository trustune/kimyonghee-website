import { getCollection } from 'astro:content';

export async function GET() {
  const projects = await getCollection('projects');
  
  const data = projects
    .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
    .map(p => ({
      id: p.slug,
      url: `/projects/${p.slug}`,
      title: p.data.title,
      title_en: p.data.title_en,
      subtitle: p.data.subtitle,
      subtitle_en: p.data.subtitle_en,
      category: p.data.category,
      date: p.data.date.toISOString().split('T')[0],
      tags: p.data.tags,
      keywords: p.data.keywords,
      conference: p.data.conference,
      description: p.data.description,
      description_en: p.data.description_en,
      summary: p.data.summary,
      featured: p.data.featured,
      key_findings: p.data.key_findings,
      methodology: p.data.methodology,
      related_publications: p.data.related_publications,
      related_projects: p.data.related_projects,
    }));
  
  return new Response(JSON.stringify(data, null, 2), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    }
  });
}
