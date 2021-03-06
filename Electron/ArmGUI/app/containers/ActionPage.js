import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Action from '../components/Action';
import * as MappingActions from '../actions/mapping';

function mapStateToProps(state) {
  return {
    mapping: state.mapping
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(MappingActions, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Action);
