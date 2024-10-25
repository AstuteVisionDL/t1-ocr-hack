import { create } from 'zustand'
import { ICardInfo } from '../types/Board'

interface BoardStoreI {
  movingCard: ICardInfo | null, 
  setMovingCard: (movingCard: ICardInfo | null) => void,
}

export const useBoardStore = create<BoardStoreI>((set) => ({
  movingCard: null,
  setMovingCard: (movingCard) => set(() => ({movingCard})),
}))