import { useState, useEffect } from "react";
import axios from "axios";
import BlogCard from "../components/BlogCard";

function Blog() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/blog/articles/")
      .then((response) => {
        setArticles(response.data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des articles:", error);
      });
  }, []);

  return (
    <div>
      <h1>📝 Blog</h1>
      <div>
        {articles.length === 0 ? (
          <p>Chargement des articles...</p>
        ) : (
          articles.map((article) => (
            <BlogCard key={article.id} article={article} />
          ))
        )}
      </div>
    </div>
  );
}

export default Blog;