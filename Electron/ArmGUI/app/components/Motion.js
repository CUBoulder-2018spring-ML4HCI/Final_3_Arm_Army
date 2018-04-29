// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Motion.css';
import { Button, Card, Row, Col } from 'react-materialize';

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
        <Link className="waves-effect waves-light btn" to="/action" onClick={() => addAction(this.state.selected)}>Continue</Link>
      </div>
    )

    return (
      <div>
        <Link to="/">
          <i className="fa fa-arrow-left fa-3x" style={{color: "black", paddingTop: "10px", paddingLeft: "10px"}}/>
        </Link>
        <div className="container center-align" style={{marginTop: "10%"}}>
          <div className="row">
            <div className="center-align">
              <h1>Select an Action</h1>
              <h5>Select an action and then hit the continue button.</h5>
            </div>
          </div>
          <div className="row">
            <div className="col s3">
              <button className="waves-effect waves-light btn" onClick={() => this.buttonClick(1)}>Stir</button>
            </div>
            <div className="col s3">
              <button className="waves-effect waves-light btn" onClick={() => this.buttonClick(2)}>Scoop</button>
            </div>
            <div className="col s3">
              <button className="waves-effect waves-light btn" onClick={() => this.buttonClick(3)}>Move to Face</button>
            </div>
            <div className="col s3">
              <button className="waves-effect waves-light btn" onClick={() => this.buttonClick(4)}>Stop</button>
            </div>
          </div>
        </div>
        {cont}
      </div>
    );
  }
}
