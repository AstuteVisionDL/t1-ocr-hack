import { IFieldConfig } from '../types.ts';

const formConfig: Record<string, IFieldConfig> = {
  login: {
    label: 'Логин',
    type: 'text',
    required: 'Введите логин'
  },
  password: {
    label: 'Пароль',
    type: 'password',
    required: 'Введите пароль'
  },
  password2: {
    label: 'Повторный пароль',
    type: 'password',
    required: 'Введите повторный пароль'
  }
}

export default formConfig