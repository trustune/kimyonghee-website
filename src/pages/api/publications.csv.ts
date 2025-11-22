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
  const publications = await getCollection('publications');
  
  const headers = [
    'ID',
    'Title',
    'Authors',
    'Journal',
    'Year',
    'Type',
    'Status',
    'Category',
    'Keywords',
    'Research Area',
    'Methodology',
    'DOI',
    'Citations',
    'Impact Factor',
    'Quartile',
    'URL'
  ];
  
  const rows = publications
    .sort((a, b) => b.data.year - a.data.year)
    .map(p => [
      escapeCSV(p.slug),
      escapeCSV(p.data.title),
      escapeCSV(p.data.authors.join('; ')),
      escapeCSV(p.data.journal),
      escapeCSV(p.data.year),
      escapeCSV(p.data.type),
      escapeCSV(p.data.status),
      escapeCSV(p.data.category),
      escapeCSV(p.data.keywords.join('; ')),
      escapeCSV(p.data.research_area.join('; ')),
      escapeCSV(p.data.methodology.join('; ')),
      escapeCSV(p.data.doi || ''),
      escapeCSV(p.data.citations),
      escapeCSV(p.data.impact_factor || ''),
      escapeCSV(p.data.quartile || ''),
      escapeCSV(`https://kimyonghee.com/research/${p.slug}`)
    ]);
  
  const csv = [
    headers.join(','),
    ...rows.map(row => row.join(','))
  ].join('\n');
  
  return new Response(csv, {
    status: 200,
    headers: {
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': 'attachment; filename="publications.csv"',
    }
  });
}
