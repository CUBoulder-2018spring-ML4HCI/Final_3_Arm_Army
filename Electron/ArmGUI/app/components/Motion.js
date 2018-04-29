// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Motion.css'

type Props = {
  addAction: () => void,
  addMotion: () => void,
  mapping: Array<{
    id: number,
    actionNumber: number,
    motion: string
  }>
};

export default class Motion extends Component<Props> {
  props: Props;
  state = {
    selected: 0
  }

  buttonClick(num) {
    this.setState({selected: num})
    // console.log(this.state)
  }

  sendOsc() {
    var client = new osc.Client('127.0.0.1', 57120);
    client.send('/wek/inputs', 200.0, function () {
      client.kill();
    });
  }

  render() {
    const {
      addAction, addMotion, mapping
    } = this.props;

    const cont = this.state.selected == 0 ? (
      <div className={styles.center}></div>
    ) : (
      <div className={styles.center}>
        <Link className={styles.sub_btn} to="/action" onClick={() => addAction(this.state.selected)}>Continue</Link>
      </div>
    )

    return (
      <div>
        <Link to="/">
          <i className="fa fa-arrow-left fa-3x" />
        </Link>
        <h1 className={styles.header}>Select an Action</h1>
        <p>Select an action and then hit the continue button.</p>
        <div className={styles.container}>
          <button className={styles.btn} onClick={() => this.buttonClick(1)}>Stir</button>
          <button className={styles.btn} onClick={() => this.buttonClick(2)}>Scoop</button>
          <button className={styles.btn} onClick={() => this.buttonClick(3)}>Move to Face</button>
          <button className={styles.btn} onClick={() => this.buttonClick(4)}>Stop</button>
        </div>
        {cont}
      </div>
    );
  }
}
