// @flow
import type { mappingStateType, typeOfAction } from '../reducers/mapping';

export const ADD_ACTION = 'ADD_ACTION';
export const ADD_MOTION = 'ADD_MOTION';

let mappingIndex = 1;

export function addAction(actNum) {
  return {
    type: ADD_ACTION,
    id: mappingIndex++,
    actionNumber: actNum,
  };
}

export function addMotion(checkId, mot) {
  return {
    type: ADD_MOTION,
    id: checkId,
    motion: mot
  };
}
