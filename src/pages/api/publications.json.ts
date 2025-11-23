import { getCollection } from 'astro:content';

export async function GET() {
  const publications = await getCollection('publications');
  
  const data = publications
    .sort((a, b) => b.data.year - a.data.year)
    .map(p => ({
      id: p.slug,
      url: `/research/${p.slug}`,
      title: p.data.title,
      authors: p.data.authors,
      journal: p.data.journal,
      year: p.data.year,
      type: p.data.type,
      status: p.data.status,
      category: p.data.category,
      abstract: p.data.abstract,
      doi: p.data.doi,
      citations: p.data.citations,
      impact_factor: p.data.impact_factor,
      quartile: p.data.quartile,
      keywords: p.data.keywords,
      research_area: p.data.research_area,
      methodology: p.data.methodology,
      statistical_methods: p.data.statistical_methods,
      software_used: p.data.software_used,
      related_projects: p.data.related_projects,
    }));
  
  return new Response(JSON.stringify(data, null, 2), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    }
  });
}
