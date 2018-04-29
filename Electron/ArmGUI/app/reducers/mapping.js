// @flow
import { ADD_ACTION, ADD_MOTION } from '../actions/mapping';

export type mappingStateType = Array<{
    id: number,
    actionNumber: number,
    motion: string
}>;

const defaultState: mappingStateType = [
  {
    id: 0,
    actionNumber: 0,
    motion: ""
  }
]

type actionType = { type: ADD_ACTION, id?: number, actionNumber?: number};
type motionType = { type: ADD_MOTION, id?: number, motion?: string };

export type typeOfAction =
  | actionType
  | motionType;


export default function mapping(state: mappingStateType = defaultState, action: typeOfAction) : mappingStateType {
  switch (action.type) {
    case ADD_ACTION:
      console.log("🤦🏻‍♂️")
      console.log(state)
      console.log(action)
      console.log([
        ...state,
        {
          id: action.id,
          actionNumber: action.actionNumber,
          motion: ""
        }
      ])
      return [
        ...state,
        {
          id: action.id,
          actionNumber: action.actionNumber,
          motion: ""
        }
      ]
    case ADD_MOTION:
      console.log("🐳")
      console.log(state)
      console.log(action)
      console.log(state.map(motion =>
        (motion.id == action.id)
          ? {...motion, motion: action.motion}
          : motion
      ))
      return state.map(motion =>
        (motion.id == action.id)
          ? {...motion, motion: action.motion}
          : motion
      )
    default:
      return state;
  }
}
