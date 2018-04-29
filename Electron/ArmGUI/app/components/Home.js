// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Home.css';
var osc = require('node-osc');

type Props = {};

export default class Home extends Component<Props> {
  props: Props;

  train() {
    console.log("Train")
    var client = new osc.Client('127.0.0.1', 6448);
    client.send('/wekinator/control/train', function () {
      client.kill();
    });
  }

  render() {
    return (
      <div className={styles.mt}>
        <div className="center-align container" data-tid="container">
          <div className="row">
            <div className="col s12">
              <h1>3 Arm Army </h1>
            </div>
            <div className="col s6">
              <Link className="waves-effect waves-light btn" to="/motion">Create a Mapping</Link>
            </div>
            <div className="col s6">
              <Link className="waves-effect waves-light btn" to="/run" onClick={this.train}>Run your training</Link>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
