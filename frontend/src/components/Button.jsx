// src/components/Button.js
import React from 'react';
import styled from 'styled-components';
import { theme } from '../styles/theme';


// Style du bouton
const StyledButton = styled.a`
  text-decoration: none;
  background-color: ${theme.colors.principalText};
  color: ${theme.colors.primary};
  border: 2px solid ${theme.colors.secondary};
  font-size: ${theme.typography.navFontSize};
  font-weight: bold;
  padding: 1rem 2rem;
  border-radius: 25px;
  margin: 0 10px;
  transition: background 0.3s ease;

  &:hover {
    background-color: ${theme.colors.linkHover};
  }
`;

// Composant réutilisable
const Button = ({ href, children }) => {
  return <StyledButton href={href}>{children}</StyledButton>;
};

export default Button;

