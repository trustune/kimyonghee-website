import { getCollection } from 'astro:content';

export async function GET() {
  const blog = await getCollection('blog');
  
  const data = blog
    .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
    .map(p => ({
      id: p.slug,
      url: `/blog/${p.slug}`,
      title: p.data.title,
      excerpt: p.data.excerpt,
      date: p.data.date.toISOString().split('T')[0],
      category: p.data.category,
      tags: p.data.tags,
      keywords: p.data.keywords,
      author: p.data.author,
      views: p.data.views,
    }));
  
  return new Response(JSON.stringify(data, null, 2), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    }
  });
}
