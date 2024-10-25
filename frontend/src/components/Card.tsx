import { FC, memo, ReactNode, useState } from 'react';
import styled, { DefaultTheme, useTheme } from 'styled-components';

import Flex from './Flex';
import { StyledBase, StyledHeading3 } from './typogaphy';
import { ICardInfo } from './board/types/Board';

const LeftBox = styled.div`
  background: ${({ theme }) => theme.white};
  border-radius: 20px 0 20px 20px;
  padding: 13px 20px 0 20px;
  z-index: 2;
`;

const RiskList = styled(Flex)<{ $expanded: boolean }>`
  height: ${({ $expanded }) => !$expanded && '30px'};
  overflow: hidden;
  flex-wrap: wrap;
  gap: 8px;

  @media (max-width: 767px) {
    height: ${({ $expanded }) => !$expanded && '18px'};
  }
`;

const Risk = styled(StyledBase)<{ theme: DefaultTheme, $expanded: boolean }>`
  height: ${({ $expanded }) => !$expanded ? '30px' : 'auto'};
  background: ${({ theme }) => theme.secondary};
  color: ${({ theme }) => theme.primary};
  text-overflow: ellipsis;
  border-radius: 20px;
  padding: 5px 15px;

  @media (max-width: 767px) {
    height: ${({ $expanded }) => !$expanded ? '18px' : '100%'};
    border-radius: 15px;
    padding: 0 10px;
  }
`;

const ExpandedButton = styled(Flex)`
  justify-content: center;
  align-items: flex-end;
  padding: 8px;
`;


const RightBox = styled(Flex)<{ theme: DefaultTheme }>`
  background: ${({ theme }) => theme.white};
  border-radius: 0 20px 20px 0;
  padding: 10px 10px 10px 0;
  height: auto;
  width: 100%;
  gap: 5px;
`;

const ButtonsWrapper = styled(Flex)`
  align-items: center;
  height: 100%;
  z-index: 2;
  gap: 5px;
`;

const Rounding = styled(Flex)`
  box-shadow: -30px -30px 0 ${({ theme }) => theme.white};
  background: transparent;
  border-radius: 20px;
  position: relative;
  height: 60px;
  width: 100%;
  z-index: 1;
`;

interface ICard {
  card: ICardInfo,
  onClick?: () => void,
  children: ReactNode,
  isMovable?: boolean,
  setMovingCard?: (card: ICardInfo | null) => void,
}


const Card: FC<ICard> = memo(({ children, onClick, card, isMovable, setMovingCard }) => {
  const theme = useTheme();

  const [expanded, setExpanded] = useState(false);

  function startDragging() {
    setMovingCard?.(card)
  }

  function endDragging() {
    setMovingCard?.(null)
  }

  function showMore(e: React.MouseEvent<HTMLSpanElement, MouseEvent>) {
    e.stopPropagation()
    setExpanded(e => !e)
  }

  return (
    <Flex onClick={onClick} draggable="true" onDragStart={startDragging} onDragEnd={endDragging} style={{cursor: isMovable ? 'pointer' : 'default'}}>
      <LeftBox>
        <StyledHeading3>{card.name}</StyledHeading3>

        <RiskList $expanded={expanded}>
          {card.items?.map((item: string) => (
            <Risk key={item} theme={theme} $expanded={expanded}>
              {item}
            </Risk>
          ))}
        </RiskList>

        <ExpandedButton>
          <StyledBase onClick={showMore} style={{ cursor: 'pointer' }}>
            {expanded ? 'Свернуть' : 'Подробнее'}
          </StyledBase>
        </ExpandedButton>
      </LeftBox>

      <div>
        <RightBox>
          <ButtonsWrapper>
            {children}
          </ButtonsWrapper>
        </RightBox>
        <Rounding/>
      </div>
    </Flex>
  );
});

export default Card;
