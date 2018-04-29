import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Motion.css'
var osc = require('node-osc');

type Props = {
  addAction: () => void,
  addMotion: () => void,
  mapping: Array<{
    id: number,
    actionNumber: number,
    motion: string
  }>
};

export default class Run extends Component<Props> {
  props: Props;

  runWek() {
    console.log("Run Wek")
    var client = new osc.Client('127.0.0.1', 6448);
    client.send('/wekinator/control/startRunning', function () {
      client.kill();
    });
  }

  render() {
    const {
      addAction, addMotion, mapping
    } = this.props;

    const convert = {
      0: "None",
      1: "Stir",
      2: "Scoop",
      3: "Move to Face",
      4: "Stop"
    }

    const list = mapping.filter((elem, index, arr) => elem.actionNumber !== 0)

    return (
      <div>
        <Link to="/">
          <i className="fa fa-arrow-left fa-3x" />
        </Link>
        <h1 className={styles.header}>Control the Arm</h1>
        <ul>
          {list.map(motion =>
            <li>{motion.motion + " mapped to " + convert[motion.actionNumber]}</li>
          )}
        </ul>
        <div className={styles.center}>
          <button className={styles.btn} onClick={this.runWek.bind(this)}>Run</button>
        </div>
      </div>
    );
  }
}
