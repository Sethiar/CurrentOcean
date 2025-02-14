import { Link } from "react-router-dom";

function BlogCard({ article }) {
  return (
    <div>
      <h2>{article.title}</h2>
      <p>🖊 {article.author} - 📅 {new Date(article.created_at).toLocaleDateString()}</p>
      {article.image && <img src={article.image} alt={article.title} width="200px" />}
      <p>{article.content.substring(0, 100)}...</p>
      <Link to={`/blog/${article.slug}`}>Lire la suite</Link>
    </div>
  );
}

export default BlogCard;