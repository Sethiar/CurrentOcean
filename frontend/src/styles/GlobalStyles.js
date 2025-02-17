// src/styles/GlobalStyles.js
import { theme } from "./theme";

import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: ${theme.fonts.body};
    background-color: ${theme.colors.primary};
    color: ${theme.colors.secondary};
  }
`;

export default GlobalStyles;