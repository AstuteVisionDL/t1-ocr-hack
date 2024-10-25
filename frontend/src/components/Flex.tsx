import styled from 'styled-components';
import Box from './Box.tsx';

const Flex = styled(Box)<{ jc?: string, ai?: string, g?: number, fd?: string }>`
  justify-content: ${({ jc }) => jc};
  flex-direction: ${({ fd }) => fd};
  align-items: ${({ ai }) => ai};
  gap: ${({ g }) => `${g}px`};
  display: flex;
`;

export default Flex;