import { FC } from 'react';
import styled from 'styled-components';

import Flex from '../../../components/Flex';

import { IFormField } from './types';

const FormWrapper = styled(Flex)<{ isFocused: boolean }>`
  border: ${({ isFocused, theme }) => isFocused && `2px solid ${theme.primary}`};
  padding: ${({ isFocused }) => isFocused ? '0' : '2px'};
  background: ${({ theme }) => theme.secondary};
  width: calc(100% - 4px);
  flex-direction: column;
  border-radius: 10px;
`;

const LabelField = styled.label`
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  font-size: 14px;
  padding: 9px;
  cursor: text;
`;

const InputField = styled.input`
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;
  padding: 0 9px 9px;
  font-size: 16px;

  &:-webkit-autofill {
    -webkit-text-fill-color: ${({ theme }) => theme.black};
    -webkit-box-shadow: 0 0 0 1000px ${({ theme }) => theme.secondary} inset;
    transition: background-color 5000s ease-in-out 0s;
  }
`;

const FormField: FC<IFormField> = (props) => {
  const { isFocused, fieldName, label, disabled, register, required, type, onFocus, onBlur } = props;

  return (
    <FormWrapper isFocused={isFocused}>
      <LabelField htmlFor={fieldName}>{label}</LabelField>
      <InputField
        {...register(fieldName, {
          required: {
            value: !!required,
            message: required
          }
        })}
        disabled={disabled}
        onFocus={onFocus}
        onBlur={onBlur}
        id={fieldName}
        type={type}
      />
    </FormWrapper>
  );
};

export default FormField;