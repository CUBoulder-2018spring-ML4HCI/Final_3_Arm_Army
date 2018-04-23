import React, { Component } from 'react';
import { Link } from 'react-router-dom';

type Props = {};

export default class Motion extends Component<Props> {
  props: Props;

  render() {
    return (
      <div>
        <Link to="/">
          <i className="fa fa-arrow-left fa-3x" />
        </Link>
        <h1>This is a new page. The motions page</h1>
      </div>
    );
  }
}
