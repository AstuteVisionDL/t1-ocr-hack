import { FC, useState } from 'react';
import { Navigate } from 'react-router-dom';

import MainLayout from '../../../layouts/MainLayout';
import Flex from '../../../components/Flex';

import { useAuthStore } from '../store';
import formConfig from './formConfig';
import AuthForm from '../componets/AuthForm';
import { IAgent, IRegisterRequest } from '../types';
import loginInstanceName from '../Login/instanceName';

const Register: FC = () => {
  const registration = useAuthStore(store => store.register);
  const agent: IAgent | null = useAuthStore(store => store.agent);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>('');

  const onSubmit = async (values: Record<string, string>) => {
    if (values.password !== values.password2) setError('Пароли не совпадают');
    else {
      setLoading(true);
      await registration(values as unknown as IRegisterRequest);
      setLoading(false);
    }
  };

  if (agent) return <Navigate to="/"/>;

  return (
    <MainLayout>
      <Flex jc="center">
        <AuthForm
          error={error}
          textLink='Войти'
          loading={loading}
          onSubmit={onSubmit}
          label='Регистрация'
          formConfig={formConfig}
          textButton='Зарегистрироваться'
          linkInstanceName={loginInstanceName}
        />
      </Flex>
    </MainLayout>
  );
};

export default Register;