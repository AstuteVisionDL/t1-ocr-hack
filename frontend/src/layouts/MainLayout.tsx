import { FC, ReactNode, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDisclosure } from '@mantine/hooks';
import { AppShell, Burger } from '@mantine/core';
import styled, { useTheme } from 'styled-components';

import loginInstanceName from '../routes/auth/Login/instanceName';
import { StyledLarge } from '../components/typogaphy';
import { useAuthStore } from '../routes/auth/store';
import { Button } from '../components/buttons';
import { IAgent } from '../routes/auth/types';
import { BiExit } from 'react-icons/bi';
import Flex from '../components/Flex';
import { navConfigAdmin, navConfigAgent } from '../config/navConfig';

const ExitIcon = styled(BiExit)`
  color: ${({ theme }) => theme.black};
  cursor: pointer;
`;

const TopMenu = styled.div`
  display: flex;
  width: 100%;
  gap: 50px;
  padding-left: 20px;
`

const MainLayout: FC<{ children: ReactNode }> = ({ children }) => {
  const [opened, { toggle }] = useDisclosure();
  const theme = useTheme();
  const navigate = useNavigate();

  const agent: IAgent | null = useAuthStore(store => store.agent);
  const logout = useAuthStore(store => store.logout);

  const isAdmin = useAuthStore(store => store.isAdmin)

  const navConfig = isAdmin ? navConfigAdmin : navConfigAgent

  return (
    <AppShell
      header={{ height: 60 }}
      padding="md"
      bg={theme.secondary}
    >
      <AppShell.Header>

        <Flex jc="space-between" ai="center" pr="20px" h="100%" pl="20px">
          <Burger
            opened={opened}
            onClick={toggle}
            hiddenFrom="sm"
            size="sm"
          />

          {
            !!agent ?
              <>
                <TopMenu>
                  {Object.entries(navConfig).map(([path, name]) => (
                    <Button key={path + name} onClick={() => navigate(path)}>
                      {name}
                    </Button>
                  ))}
                </TopMenu>
                <Flex g={10}>
                  <StyledLarge>{agent.login}</StyledLarge>
                  <ExitIcon onClick={async () => logout()}/>
                </Flex>
              </>
              :
              <Button onClick={() => navigate(loginInstanceName)}>Войти</Button>
          }
        </Flex>
      </AppShell.Header>

      <AppShell.Main style={{ overflow: 'auto', maxHeight: '100vh' }}>{children}</AppShell.Main>
    </AppShell>
  );
};

export default MainLayout;