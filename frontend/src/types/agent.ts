export type TAgentStatus = 'PLANNED' | 'ACTIVE' | 'COMPLETED' | 'CANCELED'
export type TFaceType = 'INDIVIDUAL' | 'LEGAL'

export interface IFace {
  id: number,
  type: TFaceType,
  firstName: string,
  secondName: string,
  lastName: string,
  inn: string,
  name: string,
  dateOfBirth: string,
}

export interface IIkp {
  id: number,
  name: string,
}

export interface IAgent {
  id: number,
  dateCreate: string,
  dateBegin: string,
  dateEnd: string,
  status: TAgentStatus,
  face: IFace,
  ikp: IIkp,
  login: string,
}