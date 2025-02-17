// src/components/Footer.js
import React from "react";

import { theme } from "../styles/theme";
import styled from "styled-components";

const FooterContainerPrinciple = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  min-height: 20vh; /* Ajuste la hauteur selon ton besoin */
  background-color: ${theme.colors.third};
`;

const FooterContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  padding: 4% 0;
  flex: 1; /* Permet de pousser le Copyright vers le bas */
`;

// Conteneur pour les colonnes (Entreprise, Services, Réseaux Sociaux)
const FooterColumns = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  width: 100%;
  max-width: 1200px;
  margin-bottom: 15px;

  @media (max-width: 768px) {
    flex-direction: column;
    align-items: center;
  }
`;

const FooterColumn = styled.div`
  text-align: center;
  margin: 1%;

  h4 {
    margin-bottom: 3rem;
    color: ${theme.colors.principalText};
    font-size: ${theme.typography.footerTitle};
  }

  p {
    font-size: ${theme.typography.footerInform};
    margin-bottom: 2rem;
  }

  a {
    color: white;
    text-decoration: none;
  &:hover {
    text-decoration: underline;
    color: ${theme.colors.linkHover}
  }
`;

const FooterCopyright = styled.div`
  width: 100%;
  text-align: center;
  padding: 10px 0;
  color: ${theme.colors.principalText};
  background-color: ${theme.colors.third};
  align-self: flex-end;

  p {
    margin: 0;
  }
`;

const Footer = () => {
  return (
    <FooterContainerPrinciple>
      <FooterContainer>
        {/* Conteneur des colonnes */}
        <FooterColumns>
          <FooterColumn>
            <h4>Entreprise</h4>
            <p>
              <a href="/about">À propos de nous</a>
            </p>
            <p>
              <a href="/contact">Contact</a>
            </p>
            <p>
              <a href="#">Site SethiarWorks</a>
            </p>
          </FooterColumn>
          <FooterColumn>
            <h4>Services</h4>
            <p>
              <a href="/services">Ce que nous proposons</a>
            </p>
            <p>
              <a href="/blog">Blog</a>
            </p>
          </FooterColumn>
          <FooterColumn>
            <h4>Réseaux Sociaux</h4>
            <p>
              <a href="#">Instagram</a>
            </p>
            <p>
              <a href="#">Pinterest</a>
            </p>
            <p>
              <a href="#">Linkedin</a>
            </p>
          </FooterColumn>
        </FooterColumns>
      </FooterContainer>
      {/* Section Copyright */}
      <FooterCopyright>
        <p>&copy; 2025 CurrentOcean - SethiarWorks - Tous droits réservés</p>
      </FooterCopyright>
    </FooterContainerPrinciple>
  );
};

export default Footer;
