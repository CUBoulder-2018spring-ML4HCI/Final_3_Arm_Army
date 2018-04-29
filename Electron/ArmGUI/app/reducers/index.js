import { combineReducers } from 'redux';
import { routerReducer as router } from 'react-router-redux';
import mapping from './mapping';

const rootReducer = combineReducers({
  mapping,
  router,
});

export default rootReducer;
