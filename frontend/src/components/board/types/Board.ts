export interface ICardInfo<T = {}> {
  id: number,
  name: string,
  items?: string[],
  column?: string,
  data?: T,
}

export interface IBoard {
  columns: readonly string[],
  items: ICardInfo[],
  setItems: (items: ICardInfo[]) => void,
}

export type TMoveCard = (card: ICardInfo, columnName: string) => void
export type TOnCardClick = (card: ICardInfo) => void