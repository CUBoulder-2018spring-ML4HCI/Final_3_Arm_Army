// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Action.css'
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

export default class Action extends Component<Props> {
  props: Props;
  state = {
    motionName: "",
    idToPlace: this.props.mapping[this.props.mapping.length - 1].id,
    actionToPlace: this.props.mapping[this.props.mapping.length - 1].actionNumber
  }

  handleChange(event) {
    console.log(event.target.value)
    this.setState({motionName: event.target.value});
  }

  sendDTWStart() {
    console.log("DTW Start")
    var client = new osc.Client('127.0.0.1', 6448);
    client.send('/wekinator/control/startDtwRecording', this.state.actionToPlace, function () {
      client.kill();
    });
  }

  sendDTWStop() {
    console.log("DTW Stop")
    var client = new osc.Client('127.0.0.1', 6448);
    client.send('/wekinator/control/stopDtwRecording', this.state.actionToPlace, function () {
      client.kill();
    });
  }

  sendOsc() {
    var client = new osc.Client('127.0.0.1', 57120);
    client.send('/wek/inputs', 200.0, function () {
      client.kill();
    });
  }

  test() {
    console.log(this.props)
    console.log(this.state)
  }

  render() {
    const {
      addAction, addMotion, mapping
    } = this.props;

    const save = this.state.motionName == "" ? (
      <div className={styles.center}></div>
    ) : (
      <div>
        <div className="row">
          <h1>Record an example</h1>
          <h5>Press and hold down the record button to record your action. When you're done, click the save mapping button.</h5>
        </div>
        <div className={styles.center}>
          <button className="waves-effect waves-light btn" onMouseDown={this.sendDTWStart.bind(this)} onMouseUp={this.sendDTWStop.bind(this)}>Record</button>
        </div>
        <div className={styles.center}>
          <Link className="waves-effect waves-light btn" onClick={() => addMotion(this.state.idToPlace, this.state.motionName)} to="/">Save Mapping</Link>
        </div>
      </div>
    )

    return (
      <div>
        <Link to="/motion">
          <i className="fa fa-arrow-left fa-3x" style={{color: "black", paddingTop: "10px", paddingLeft: "10px"}}/>
        </Link>
        <div className="container center-align" style={{marginTop: "10%"}}>
          <div className="row">
            <h1>Name Your Action</h1>
            <p>First you need to type a name for your action.</p>
          </div>
          <div className="row">
            <form>
              <input type="text" onChange={evt => this.handleChange(evt)} />
            </form>
          </div>
          {save}
        </div>
      </div>
    );
  }
}
