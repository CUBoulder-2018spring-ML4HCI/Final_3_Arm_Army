/* eslint flowtype-errors/show-errors: 0 */
import React from 'react';
import { Switch, Route } from 'react-router';
import App from './containers/App';
import HomePage from './containers/HomePage';
import CounterPage from './containers/CounterPage';
import MotionPage from './containers/MotionPage';
import ActionPage from './containers/ActionPage';
import RunPage from './containers/RunPage'

export default () => (
  <App>
    <Switch>
      <Route path="/counter" component={CounterPage} />
      <Route path="/run" component={RunPage} />
      <Route path="/motion" component={MotionPage} />
      <Route path="/action" component={ActionPage} />
      <Route path="/" component={HomePage} />
    </Switch>
  </App>
);
