import { FC, useState } from 'react';
import { Navigate } from 'react-router-dom';

import MainLayout from '../../../layouts/MainLayout';
import Flex from '../../../components/Flex';

import { useAuthStore } from '../store';
import formConfig from './formConfig';
import AuthForm from '../componets/AuthForm';
import { IAgent, ILoginRequest } from '../types';
import registerInstanceName from '../Register/instanceName';

const Login: FC = () => {
  const login = useAuthStore(store => store.login);
  const agent: IAgent | null = useAuthStore(store => store.agent);

  const [loading, setLoading] = useState(false);

  const onSubmit = async (values: Record<string, string>) => {
    setLoading(true);
    await login(values as unknown as ILoginRequest);
    setLoading(false);
  };

  if (agent) return <Navigate to="/"/>;

  return (
    <MainLayout>
      <Flex jc="center">
        <AuthForm
          label='Вход'
          loading={loading}
          textButton='Войти'
          onSubmit={onSubmit}
          formConfig={formConfig}
          textLink='Зарегистрироваться'
          linkInstanceName={registerInstanceName}
        />
      </Flex>
    </MainLayout>
  );
};

export default Login;