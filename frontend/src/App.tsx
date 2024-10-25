import '@mantine/core/styles.css';
import { Loader } from '@mantine/core';
import { FC, useEffect } from 'react';
import { Route, Routes } from 'react-router-dom';

import Flex from './components/Flex';
import { useAuthStore } from './routes/auth/store';
import routesConfig from './config/routesConfig';

const App: FC = () => {
  const authMe = useAuthStore(store => store.authMe);
  const isLoaded = useAuthStore(store => store.isLoaded);

  const authorization = async () => {
      await authMe();
  };

  useEffect(() => {
    authorization().then(() => {});
  }, []);

  return (
    <>
      {
        isLoaded ? (
          <Routes>
            {Object.entries(routesConfig).map(([path, Component]) => (
              <Route
                key={path}
                path={path}
                element={<Component/>}
              />
            ))}
          </Routes>
        ) : (
          <Flex jc="center" ai="center" h="100lvh">
            <Loader/>
          </Flex>
        )
      }
    </>
  );
};

export default App;
