import React, { Component } from 'react';
import { Link } from 'react-router-dom';

type Props = {};

export default class Action extends Component<Props> {
  props: Props;

  render() {
    return (
      <div>
        <Link to="/motion">
          <i className="fa fa-arrow-left fa-3x" />
        </Link>
        <h1>Record a motion</h1>
        <h2>Hold down the button to record</h2>
        <Link to="/">Save Mapping</Link>
      </div>
    );
  }
}
