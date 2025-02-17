import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Blog from "./pages/Blog";
import ArticleDetail from "./pages/ArticleDetail";
import Actualites from "./pages/Actualites";

// Importation Header
import Header from "./components/Header";
// Importation Footer
import Footer from "./components/Footer";


function App() {
  return (
    <div>
      {/* Header */}
      <Header />

      {/*</div> Routes de l'application */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog" element={<Blog />} />
        <Route path="/blog/:slug" element={<ArticleDetail />} />
        <Route path="/actualites" element={<Actualites />} />
      </Routes>

      {/* Footer */}
      <Footer />
    </div>
  );
}

export default App;
