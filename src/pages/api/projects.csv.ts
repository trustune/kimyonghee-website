import { getCollection } from 'astro:content';

function escapeCSV(value: any): string {
  if (value === null || value === undefined) return '';
  const str = String(value);
  if (str.includes(',') || str.includes('"') || str.includes('\n')) {
    return `"${str.replace(/"/g, '""')}"`;
  }
  return str;
}

export async function GET() {
  const projects = await getCollection('projects');
  
  const headers = [
    'ID',
    'Title (EN)',
    'Title (KO)',
    'Category',
    'Date',
    'Conference',
    'Tags',
    'Keywords',
    'Featured',
    'Summary',
    'URL'
  ];
  
  const rows = projects
    .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
    .map(p => [
      escapeCSV(p.slug),
      escapeCSV(p.data.title_en),
      escapeCSV(p.data.title),
      escapeCSV(p.data.category),
      escapeCSV(p.data.date.toISOString().split('T')[0]),
      escapeCSV(p.data.conference || ''),
      escapeCSV(p.data.tags.join('; ')),
      escapeCSV(p.data.keywords.join('; ')),
      escapeCSV(p.data.featured ? 'Yes' : 'No'),
      escapeCSV(p.data.summary),
      escapeCSV(`https://kimyonghee.com/projects/${p.slug}`)
    ]);
  
  const csv = [
    headers.join(','),
    ...rows.map(row => row.join(','))
  ].join('\n');
  
  return new Response(csv, {
    status: 200,
    headers: {
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': 'attachment; filename="projects.csv"',
    }
  });
}
