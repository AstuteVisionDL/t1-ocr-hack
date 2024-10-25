import styled from 'styled-components';

export const GrayButton = styled.button`
  transition: color 0.1s ease;
  align-items: center;
  background: none;
  outline: inherit;
  display: flex;
  border: none;
  color: gray;
  padding: 0;
  gap: 7px;
  
  &:hover {
    color: black;
  }
`;

export const Button = styled.button`
  border: 1px ${({ theme }) => theme.primary} solid;
  background: ${({ theme }) => theme.primary};
  color: ${({ theme }) => theme.white};
  border-radius: 10px;
  align-items: center;
  padding: 5px 15px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  gap: 12px;
  
  &:hover {
    background: ${({ theme }) => theme.primaryHover};
  }

  &:active {
    background: ${({ theme }) => theme.primaryFocus};
  }
`;
