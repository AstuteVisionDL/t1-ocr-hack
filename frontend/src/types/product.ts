export type TLineOfBusiness = 'CASCO' | 'OSAGO' | 'THI' | 'ACCIDENT'

export interface IRisk {
  id: number,
  name: string,
  lineOfBusiness: TLineOfBusiness,
  url: string
}

export interface IProduct {
  id: number,
  name: string,
  lineOfBusiness: TLineOfBusiness,
  risks: IRisk[],
}