import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://147.45.137.202:8080/'
});

instance.interceptors.request.use((config) => {
  config.headers.token = window.localStorage.getItem('token');
  return config;
});

export default instance;