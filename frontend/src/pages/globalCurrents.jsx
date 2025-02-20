import React from "react";

import styled, { ThemeProvider } from "styled-components";
import { theme } from "../styles/theme";

import CurrentData from "./currents/currentsTests";
import GlobalStyles from "../styles/GlobalStyles";



const GlobalCurrents = () => {
    return (
        <ThemeProvider theme={theme}>
            <GlobalStyles />
            {/* Insertion de CurrentData pour afficher les données */}
            <CurrentData />
        </ThemeProvider>
    );
};

export default GlobalCurrents