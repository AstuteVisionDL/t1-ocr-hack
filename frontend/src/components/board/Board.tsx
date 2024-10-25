import { ReactNode, useCallback } from 'react';

import styled from 'styled-components';
import Column from './Column.tsx';
import { IBoard, ICardInfo, TMoveCard, TOnCardClick } from './types/Board.ts';

const BoardElement = styled.div`
  display: flex;
  & > * {
    flex-shrink: 0;
  }
`;

export type IBoardProps = IBoard & {
  children: ReactNode,
  onCardClick?: TOnCardClick,
  isMovableCard?: boolean,
  onEdit?: (card: ICardInfo) => void,
}

function Board({columns, items, setItems, children, onCardClick, isMovableCard, onEdit}: IBoardProps) {

  const filterItems = useCallback((itemsProp: typeof items, columnName: string) => {
    return itemsProp.filter(e => e.column === columnName)
  }, [items])

  const moveCard = useCallback<TMoveCard>((card, columnName) => {
    const filteredItems = items.filter(e => e.id !== card.id)
    onEdit?.({
      ...card,
      column: columnName
    })
    setItems([
      ...filteredItems, 
      {...card, column: columnName}
    ])
  }, [items])

  return (
    <BoardElement>
      {columns.map(column => 
        <Column 
          isMovableCard={isMovableCard} 
          cards={filterItems(items, column)}
          column={column}
          onCardClick={onCardClick}
          moveCard={moveCard}
          key={column}
        >
          {children}
        </Column>
      )}
    </BoardElement>
  );
};

export default Board;
