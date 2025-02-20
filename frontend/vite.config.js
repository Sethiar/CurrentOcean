import { defineConfig } from 'vite'
import path from 'path';
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: path.resolve(__dirname, 'dist'), // Chemin correct
    emptyOutDir: true, // Supprime l'ancien build avant de recréer
  },

  server: {
    proxy: {
      '/api': 'http://127.0.0.1:8000',
    }
  }
});
