import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { createTheme, MantineProvider } from '@mantine/core';

import './static/styles/globals.css';
import './static/styles/reset.css';
import theme from './static/theme';
import App from './App';
import 'dayjs/locale/ru';

const mantineTheme = createTheme({
  primaryColor: 'blue',
});

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <ThemeProvider theme={theme}>
    <BrowserRouter>
      <MantineProvider theme={mantineTheme}>
        <App/>
      </MantineProvider>
    </BrowserRouter>
  </ThemeProvider>
);