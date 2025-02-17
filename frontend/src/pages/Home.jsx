import React from "react";

import styled, { ThemeProvider } from "styled-components";

// Importation des données
import {
  currentsDataAtlantic,
  currentsDataPacific,
  currentsDataArctic,
  currentsDataAntarctic,
  currentsDataIndian,
} from "../assets/currentsData/current";
import backgroundHome from "../assets/backGround/backgroundHome.jpg";

// Importation des Styles et du thème
import GlobalStyles from "../styles/GlobalStyles";
import { theme } from "../styles/theme";

// Importation des éléments réutilisables
import Button from "../components/Button";

// Centralisation des données pour le tableau
const oceans = [
  { name: "Océan Atlantique", data: currentsDataAtlantic },
  { name: "Océan Pacifique", data: currentsDataPacific },
  { name: "Océan Arctique", data: currentsDataArctic },
  { name: "Océan Antarctique", data: currentsDataAntarctic },
  { name: "Océan Indien", data: currentsDataIndian },
];

// Barre bleu foncé sous header
const BlueBar = styled.div`
  width: 100%;
  height: 2rem;
  background-color: ${({ theme }) => theme.colors.lign};
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
`;

// Conteneur principal avec marges entre les sections
const HomeContainer = styled.div`
  padding: 5rem 3.5rem;
  font-size: ${({ theme }) => theme.typography.paragraphFontSize};
  background-image: url(${backgroundHome});
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
`;

const TextBox = styled.div`
  padding: 2rem;
  border: 1px solid ${({ theme }) => theme.colors.linkHover};
  border-radius: 10px;
  background-color: ${({ theme, variant }) =>
    variant === "primary"
      ? theme.colors.primary
      : variant === "secondary"
      ? theme.colors.lign
      : theme.colors.primary};
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  max-width: ${({ variant }) => (variant === "secondary" ? "50%" : "70%")};
  margin: 0 auto;
  margin-bottom: 2rem;
  text-align: center;

  p {
    margin-bottom: ${({ variant }) =>
      variant === "secondary" ? "1rem" : "2rem"};
  }
`;

// Espacement entre les sections
const Section = styled.section`
  margin-bottom: 12rem;
  text-align: center;

  h2 {
    text-decoration: underline;
    margin-bottom: 2rem;
  }
`;

// Style pour le tableau
const OceanTable = styled.table`
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  margin-bottom: 5rem;

  th,
  td {
    padding: 1rem;
    border: 1px solid ${({ theme }) => theme.colors.principalText};
    text-align: center;
  }

  th {
    background-color: ${({ theme }) => theme.colors.primary};
    color: ${({ theme }) => theme.colors.secondary};
    font-size: ${({ theme }) => theme.typography.footerTitle};
  }

  tr:nth-child(even) {
    background-color: ${({ theme }) => theme.colors.table};
    color: ${({ theme }) => theme.colors.primary};
  }

  tr:nth-child(odd) {
    background-color: ${({ theme }) => theme.colors.table2};
  }
`;

const Home = () => {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyles />

      {/* Barre bleu foncé */}
      <BlueBar />

      {/* Contenu principal */}
      <HomeContainer>
        <Section>
          <TextBox variant="primary">
            <p>
              Ce site vous propose d'explorer les courants marins et leurs
              évolutions en temps réel.
            </p>
          </TextBox>
        </Section>

        <Section>
        <TextBox role="article" aria-label="Définition des courants marins">
            <p>Mais d'abord, qu'est-ce qu'un courant marin ?</p>

            <p>
              Définition : Un courant marin est un déplacement horizontal d'eau
              de mer dû aux effets combinés du vent, de la force de Coriolis et
              de différences de densité (température et salinité) ; ainsi qu'aux
              contours des continents, aux reliefs de profondeur et à
              l'interaction entre courants.
            </p>
          </TextBox>
        </Section>

        <Section>
        <TextBox role="article" aria-label="Visualisation des courants marins">
            <h2>Visualisation des données</h2>
            <p>
              Vous pourrez visualiser les courants sous forme de graphiques
              détaillés, de tableaux et de schémas qui vous renseigneront
              simplement sur les changements que chaque courant a subi.
            </p>
          </TextBox>
        </Section>

        <Section>
        <TextBox role="article" aria-label="Introduction sur la méthode">
            <p>
              L'objectif n'est pas de vous surcharger d'informations qui vont
              littéralement vous dépasser et qui vont vous empécher de
              visualiser clairement et distinctement les changements et leurs
              conséquences sur la biosphère terrestre.
            </p>
          </TextBox>
        </Section>

        <Section>
        <TextBox role="article" aria-label="Introduction sur la méthode">
            <p>
              Non, bien au contraire, ce qui est important ici est que vous ayez
              une information qui vous donne tout de suite la gravité des
              changements que les océans sont en train de subir afin que nous
              puissions prendre conscience ensemble que la planète va subir des
              changements importants et que nous devons nous y préparer.
            </p>
          </TextBox>
        </Section>

        <Section>
        <TextBox role="article" aria-label="Liste des courants marins de la terre">
            <p>
              D'abord un petit récapitulatif de tous les courants marins de la
              planète.
            </p>
          </TextBox>
        </Section>

        <Section>
          {oceans.map(({ name, data }) => (
            <React.Fragment key={name}>
              <TextBox variant="secondary">
                <p>{name}</p>
              </TextBox>
              <OceanTable>
                <thead>
                  <tr>
                    <th>Courant</th>
                    <th>Description</th>
                  </tr>
                </thead>
                <tbody>
                  {data.map((current, index) => (
                    <tr key={index}>
                      <td>{current.current}</td>
                      <td>{current.description}</td>
                    </tr>
                  ))}
                </tbody>
              </OceanTable>
            </React.Fragment>
          ))}
        </Section>

        <Section>
          <Button primary>Passer à l'exploration des courants marins</Button>
        </Section>
      </HomeContainer>

      {/* Barre bleu foncé */}
      <BlueBar />
    </ThemeProvider>
  );
};

export default Home;
