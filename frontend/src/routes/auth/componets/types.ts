import { FieldValues, RegisterOptions, UseFormRegisterReturn } from 'react-hook-form';
import { FocusEventHandler, HTMLInputTypeAttribute } from 'react';
import { IFieldConfig } from '../types.ts';

export interface IFormField {
  register: (name: string, options?: RegisterOptions<FieldValues, string>) => UseFormRegisterReturn<string>;
  onFocus: FocusEventHandler<HTMLInputElement>;
  onBlur: FocusEventHandler<HTMLInputElement>;
  type: HTMLInputTypeAttribute;
  isFocused: boolean;
  fieldName: string;
  disabled: boolean;
  required: string;
  label: string;
}

export interface IAuthForm {
  onSubmit: (values: Record<string, string>) => Promise<void>;
  formConfig: Record<string, IFieldConfig>;
  linkInstanceName: string;
  textButton: string;
  loading: boolean;
  textLink: string;
  error?: string;
  label: string;
}