import rss from '@astrojs/rss';
import blog from '../data/blog.json';

export async function GET(context) {
  return rss({
    title: 'Yonghee Kim • Blog',
    description: 'Media Policy & Management Expert - Research, insights, and commentary on media policy, OTT platforms, and digital regulation',
    site: context.site || 'http://kimyonghee.com',
    items: blog.posts.map((post) => ({
      title: post.title,
      pubDate: new Date(post.date),
      description: post.excerpt,
      link: `/blog/${post.slug}/`,
      categories: post.tags,
      author: post.author,
    })),
    customData: `<language>en</language>`,
  });
}
