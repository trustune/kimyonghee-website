import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const blogPosts = await getCollection('blog');
  const sortedPosts = blogPosts.sort(
    (a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime()
  );

  return rss({
    title: 'Yonghee Kim • Writing',
    description: 'Media Policy & Management Expert - Research, insights, and commentary on media policy, OTT platforms, and digital regulation',
    site: context.site || 'https://kimyonghee.com',
    items: sortedPosts.map((post) => ({
      title: post.data.title_en || post.data.title,
      pubDate: new Date(post.data.date),
      description: post.data.excerpt_en || post.data.excerpt,
      link: `/writing/${post.slug}/`,
      categories: post.data.tags,
      author: post.data.author,
    })),
    customData: `<language>en</language>`,
  });
}
