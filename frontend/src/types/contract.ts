import { IAgent, IFace } from "./agent"
import { IProduct } from "./product"

export type TContractStatus = 'DRAFT' | 'SIGNED' | 'TERMINATED'

export interface IContract {
  id: number,
  dateCreate: string,
  dateSign: string,
  product: IProduct,
  dateBegin: string,
  dateEnd: string,
  premium: number,
  unsuranceSum: number,
  agent: IAgent,
  rate: number,
  comission: number,
  status: TContractStatus,
  policyHolder: IFace,
  insuredPerson: IFace,
  owner: IFace,
}