import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

function ArticleDetail() {
  const { slug } = useParams();
  const [article, setArticle] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/blog/articles/${slug}/`)
      .then((response) => {
        setArticle(response.data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération de l'article:", error);
      });
  }, [slug]);

  if (!article) return <p>Chargement...</p>;

  return (
    <div>
      <h1>{article.title}</h1>
      <p>🖊 {article.author} - 📅 {new Date(article.created_at).toLocaleDateString()}</p>
      {article.image && <img src={article.image} alt={article.title} />}
      <p>{article.content}</p>
    </div>
  );
}

export default ArticleDetail;