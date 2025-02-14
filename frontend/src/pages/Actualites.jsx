import { useState, useEffect } from "react";
import axios from "axios";

function Actualites() {
  const [articles, setArticles] = useState([]);
  const API_KEY = "08a93600a28f44adadd40e6e3065b904"; // Remplace par ta clé d’API NewsAPI
  const API_URL = `https://newsapi.org/v2/everything?q=climate&language=fr&apiKey=${API_KEY}`;

  useEffect(() => {
    axios
      .get(API_URL)
      .then((response) => {
        setArticles(response.data.articles); // Stocke les articles récupérés
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des articles:", error);
      });
  }, []); // Exécute une seule fois au chargement

  return (
    <div>
      <h1>🌍 Actualités Climat</h1>
      {articles.length === 0 ? (
        <p>Chargement des articles...</p>
      ) : (
        <ul>
          {articles.map((article, index) => (
            <li key={index}>
              <h2>{article.title}</h2>
              <p>{article.description}</p>
              <a href={article.url} target="_blank" rel="noopener noreferrer">
                Lire l'article
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Actualites;