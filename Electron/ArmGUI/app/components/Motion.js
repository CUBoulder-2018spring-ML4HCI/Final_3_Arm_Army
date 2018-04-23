import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Motion.css'

type Props = {};

export default class Motion extends Component<Props> {
  props: Props;

  render() {
    return (
      <div>
        <Link to="/">
          <i className="fa fa-arrow-left fa-3x" />
        </Link>
        <h1 className={styles.header}>Select an Action</h1>
        <div className={styles.container}>
          <button className={styles.btn}>Stir</button>
          <button className={styles.btn}>Mix</button>
          <button className={styles.btn}>Move to Face</button>
          <button className={styles.btn}>Stop</button>
        </div>
        <div className={styles.center}>
          <Link className={styles.sub_btn} to="/action">Continue</Link>
        </div>
      </div>
    );
  }
}
