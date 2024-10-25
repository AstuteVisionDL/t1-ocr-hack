import { FC, ReactNode, useState } from 'react';

import styled, { DefaultTheme } from 'styled-components';

import Card from '../Card';
import { StyledHeading2 } from '../typogaphy';
import { useBoardStore } from './store/BoardStore';
import { GrayButton } from '../buttons';
import { BiTargetLock } from 'react-icons/bi';
import { ICardInfo, TMoveCard, TOnCardClick } from './types/Board';

const ColumnElement = styled.div<{ theme: DefaultTheme, $isHover?: boolean, $isDrag?: boolean }>`
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 15px 15px;
  border-radius: 5px;
  gap: 20px;
  width: 380px;
  transition: background 0.3s ease;
  background: ${({ $isHover, theme }) => $isHover ? theme.secondaryHover : 'initial'};
  &:hover {
    background: ${({ theme }) => theme.secondaryHover};
  }
  & * {
    pointer-events: ${({ $isDrag }) => $isDrag ? 'none' : 'auto'};
  }
`
export interface IColumnsProps {
  column: string,
  cards: ICardInfo[],
  children: ReactNode,
  onCardClick?: TOnCardClick,
  isMovableCard?: boolean,
  setMovingCard?: (card: ICardInfo | null) => void,
  moveCard?: TMoveCard,
}

function Column({column, cards, onCardClick, children, isMovableCard, moveCard}: IColumnsProps) {
  const setMovingCard = useBoardStore(store => store.setMovingCard)
  const movingCard = useBoardStore(store => store.movingCard)
  const [isHover, setisHover] = useState(false)

  function onDrop() {
    setisHover(false)
    if (movingCard) {
      const isSameColumn = cards.some(e => e.id === movingCard.id)
      if (!isSameColumn) {
        setTimeout(() => {
          moveCard?.(movingCard, column)
        })
      }
    }
  }

  function onDragOver(e: React.DragEvent<HTMLDivElement>) {
    e.preventDefault()
  }

  function onDragEnter() {
    setisHover(true)
  }
  function onDragLeave() {
    setisHover(false)
  }

  function startMoving(movingCard: ICardInfo | null) {
    setMovingCard(movingCard)
  }

  return (
    <ColumnElement $isDrag={!!movingCard} $isHover={isHover} onDrop={onDrop} onDragOver={onDragOver} onDragEnter={onDragEnter} onDragLeave={onDragLeave}>
      <StyledHeading2 style={{marginLeft: '18px'}}>
        {column} <span style={{color: 'gray'}}> {cards.length} </span>
      </StyledHeading2>

      {cards.map(card =>
        <Card isMovable={isMovableCard} setMovingCard={startMoving} onClick={() => onCardClick?.(card)} key={card.id} card={card}>
          {children}
        </Card>
      )}

      {movingCard &&
        <GrayButton style={{margin: '0 auto'}}>
          Переместить сюда <BiTargetLock />
        </GrayButton>
      }

    </ColumnElement>
  );
};

export default Column;
