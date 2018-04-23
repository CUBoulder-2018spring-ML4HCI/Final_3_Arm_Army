import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Action.css'

type Props = {};

export default class Action extends Component<Props> {
  props: Props;

  render() {
    return (
      <div>
        <Link to="/motion">
          <i className="fa fa-arrow-left fa-3x" />
        </Link>
        <h1 className={styles.header}>Record a motion</h1>
        <h2>Hold down the button to record</h2>
        <div className={styles.center}>
          <button className={styles.btn}>Record</button>
        </div>
        <div className={styles.center}>
          <Link className={styles.sub_btn} to="/">Save Mapping</Link>
        </div>
      </div>
    );
  }
}
