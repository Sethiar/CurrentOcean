import React from "react";

import { theme } from "../styles/theme";
import styled from "styled-components";

// importation des composants réutilisables
import Button from "./Button";

// Conteneur du header
const HeaderContainer = styled.header`
  background-color: ${theme.colors.third};
  padding: 1.5rem 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10rem;
`;

const Header = () => {
  return (
    <HeaderContainer>
      <Button href="/">Accueil</Button>
      <Button href="/blog">Blog</Button>
      <Button href="/actualites">Actualités</Button>
      <Button href="/courants">Courants</Button>
    </HeaderContainer>
  );
};

export default Header;