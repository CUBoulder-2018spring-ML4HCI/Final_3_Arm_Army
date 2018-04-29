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
      <div>
        <div className={styles.container} data-tid="container">
          <h2>3 Arm Army</h2>
          <Link to="/motion">Create a Mapping</Link>
          <br />
          <Link to="/run" onClick={this.train}>Run your training</Link>
        </div>
      </div>
    );
  }
}
