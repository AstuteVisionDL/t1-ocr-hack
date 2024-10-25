import styled from 'styled-components';

const Box = styled.div<{
  w?: string,
  h?: string,
  ml?: string,
  mr?: string,
  mb?: string,
  mt?: string,
  pt?: string,
  pl?: string,
  pr?: string,
  pb?: string
}>`
  width: ${({ w }) => w};
  height: ${({ h }) => h};
  margin-left: ${({ ml }) => ml};
  margin-right: ${({ mr }) => mr};
  margin-bottom: ${({ mb }) => mb};
  margin-top: ${({ mt }) => mt};
  padding-left: ${({ pl }) => pl};
  padding-right: ${({ pr }) => pr};
  padding-top: ${({ pt }) => pt};
  padding-bottom: ${({ pb }) => pb};
`;

export default Box;