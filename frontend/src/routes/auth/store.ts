import { create } from 'zustand';

import axios from '../../axios';

import { IAgent, ILoginRequest, IRegisterRequest } from './types';

const ADMIN_LOGIN = 'admin'

interface IProductsStore {
  register: (body: IRegisterRequest) => Promise<void>;
  login: (body: ILoginRequest) => Promise<void>;
  authMe: () => Promise<void>;
  agent: IAgent | null;
  logout: () => void;
  isLoaded: boolean;
  isAdmin: boolean;
}

export const useAuthStore = create<IProductsStore>((set) => ({
  agent: null,
  isLoaded: false,
  isAdmin: false,
  register: async (body: IRegisterRequest) => {
    try {
      const { data }: { data: IAgent } = await axios.post('/agents', body);
      if (data?.token) {
        set({ agent: data });
        window.localStorage.setItem('token', data.token);
        window.localStorage.setItem('password', body.password);//временно
        window.localStorage.setItem('login', body.login);//временно
      } else alert('Ошибка при регистрации агента');
    } catch (e) {
      alert('Ошибка при регистрации агента');
    }
  },
  login: async (body: ILoginRequest) => {
    try {
      const { data }: { data: IAgent } = await axios.post('/agents/login', body);
      if (data?.token) {
        set({ agent: data });
        window.localStorage.setItem('token', data.token);
        window.localStorage.setItem('password', body.password);//временно
        window.localStorage.setItem('login', body.login);//временно
      } else alert('Ошибка при входе агента');
    } catch (e) {
      set({ isLoaded: true });//временно
      alert('Ошибка при входе агента');
    }
    set({ isLoaded: true });//временно
  },
  authMe: async () => {
    const token = window.localStorage.getItem('token');
    const login = window.localStorage.getItem('login');
    const password = window.localStorage.getItem('password');

    try {
      if (token) {
        const { data }: { data: IAgent } = await axios.get(`agents/login/${window.localStorage.getItem('token')}`);
        if (data?.token) {
          set({ agent: data });
          set({ isAdmin: data.login === ADMIN_LOGIN })
          window.localStorage.setItem('token', data.token);
        }
      }
    } catch (e) {
      try {//временно
        if (login && password) {//временно
          const { data }: { data: IAgent } = await axios.post('/agents/login', { login, password });//временно
          if (data?.token) {//временно
            set({ agent: data });//временно
            set({ isAdmin: data.login === ADMIN_LOGIN });//временно
            window.localStorage.setItem('token', data.token);//временно
          }//временно
        }//временно
      } catch (e) {//временно
        set({ isLoaded: true });//временно
      }//временно
      set({ isLoaded: true });
    }
    set({ isLoaded: true });
  },
  logout: () => {
    set({ agent: null });
    window.localStorage.removeItem('token');
    window.localStorage.removeItem('login');//временно
    window.localStorage.removeItem('password');//временно
  }
}));