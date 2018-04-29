export default function actions(state = [], action) {
  switch(action.type){
    case 'ADD_ACTION':
      return [
        ...state,
        {
          id: action.id,
          action: action.action,
          motion: ""
        }
      ]
    case 'ADD_MOTION':
      return state.map(mapping =>
        (mapping.id == action.id)
          ? {...mapping, motion: action.motion}
          : mapping
      )
    default:
      return state
  }
}
