import { FC, useState } from 'react';
import { Link } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import styled, { useTheme } from 'styled-components';

import { StyledBase, StyledHeading2 } from '../../../components/typogaphy';
import { Button } from '../../../components/buttons';
import Flex from '../../../components/Flex';
import Box from '../../../components/Box';
import FormField from './FormField';

import { IAuthForm } from './types';

const FormWrapper = styled.form`
  background: ${({ theme }) => theme.white};
  flex-direction: column;
  border-radius: 20px;
  align-items: center;
  max-width: 700px;
  margin: 0 0 36px;
  padding: 40px;
  display: flex;
  width: 100%;

  @media (max-width: 767px) {
    padding: 20px 10px;
  }
`;

const AuthForm: FC<IAuthForm> = (props) => {
  const { formConfig, onSubmit, loading, label, error, textButton, textLink, linkInstanceName } = props;

  const theme = useTheme();

  const [isFocused, setIsFocused] = useState(Object.keys(formConfig).map(() => false));

  const handleFocusChange = (index: number) => setIsFocused((prev) => ({ ...prev, [index]: !prev[index] }));

  const {
    register, handleSubmit, formState: { errors }
  } = useForm({
    defaultValues: Object.entries(formConfig).reduce<Record<string, string>>((acc, [field]) => {
      acc[field] = '';
      return acc;
    }, {}),
    mode: 'onChange'
  });

  return (
    <FormWrapper onSubmit={handleSubmit(onSubmit)}>
      <Box mb="20px">
        <StyledHeading2>{label}</StyledHeading2>
      </Box>
      {
        Object.entries(formConfig).map(([fieldName, item], index) => (
          <>
            <FormField
              onFocus={() => handleFocusChange(index)}
              onBlur={() => handleFocusChange(index)}
              isFocused={isFocused[index]}
              required={item.required}
              fieldName={fieldName}
              register={register}
              disabled={loading}
              label={item.label}
              type={item.type}
            />
            <Box h="30px">
              <StyledBase color={theme.error}>{errors[fieldName]?.message as string}</StyledBase>
            </Box>
          </>
        ))
      }
      <Box h="30px" mt="-30px">
        <StyledBase color={theme.error}>{error}</StyledBase>
      </Box>
      <Flex fd="column" ai="center" g={10}>
        <Button type="submit">{loading ? 'Загрузка...' : textButton}</Button>
        <Link to={linkInstanceName} style={{ color: theme.primary }}>{textLink}</Link>
      </Flex>
    </FormWrapper>
  );
};

export default AuthForm;