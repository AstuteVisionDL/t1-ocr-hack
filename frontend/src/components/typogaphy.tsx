import styled from 'styled-components';

export const StyledBase = styled.span<{ color?: string }>`
  color: ${({ color }) => color};
  text-decoration: inherit;
  line-height: 20px;
  font-size: 13px;

  @media (max-width: 767px) {
    line-height: 18px;
    font-size: 11px;
  }
`;

export const StyledHeading2 = styled.h2<{ color?: string }>`
  color: ${({ color }) => color};
  padding-bottom: 3px;
  line-height: 35px;
  font-weight: bold;
  padding-top: 2px;
  font-size: 28px;

  @media (max-width: 767px) {
    line-height: 33px;
    font-size: 26px;
  }
`;

export const StyledHeading3 = styled.h3<{ color?: string }>`
  color: ${({ color }) => color};
  padding-bottom: 4px;
  line-height: 25px;
  font-weight: bold;
  padding-top: 1px;
  font-size: 20px;

  @media (max-width: 767px) {
    line-height: 23px;
    font-size: 18px;
  }
`;

export const StyledLarge = styled.span<{ color?: string }>`
  color: ${({ color }) => color};
  padding-bottom: 5px;
  line-height: 20px;
  font-size: 16px;
`;
