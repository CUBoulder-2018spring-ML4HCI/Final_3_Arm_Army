export const ADD_ACTION = 'ADD_ACTION';

let nextActionId = 0

export function add_action(action){
  return {
    type: ADD_ACTION,
    id: nextActionId++,
    action: action
  }
}
