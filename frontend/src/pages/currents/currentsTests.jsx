import React, { useState, useEffect } from 'react';

const CurrentData = () => {
  // État pour stocker les données
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Faire l'appel API lorsque le composant est monté
    fetch('http://localhost:8000/api/fetch-data/')
      .then(response => response.json())
      .then(data => {
        console.log('Data:', data);
        setData(data); // Stocker les données dans l'état
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setError('Une erreur est survenue lors de la récupération des données.');
      });
  }, []); // Le tableau vide [] signifie que l'effet se déclenche une seule fois lors du montage du composant

  if (error) {
    return <div>{error}</div>;
  }

  if (!data) {
    return <div>Chargement des données...</div>;
  }

  // Afficher les données récupérées
  return (
    <div>
      <h1>Données des courants marins</h1>
      {/* Affiche les données dans un format adapté */}
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default CurrentData;