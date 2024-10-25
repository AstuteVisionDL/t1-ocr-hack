export interface ILoginRequest {
  login: string;
  password: string;
}

export interface IRegister extends ILoginRequest {
  secondName: string;
  firstName: string;
  birthOfDate: Date;
  lastName: string;
  inn: number;
}

export interface IRegisterRequest extends IRegister {
  password2: string;
}

export interface IAgent extends IRegister {
  token?: string;
  face?: any;
  id: string;
}

export interface IFieldConfig {
  required: string;
  label: string;
  type: string;
}
