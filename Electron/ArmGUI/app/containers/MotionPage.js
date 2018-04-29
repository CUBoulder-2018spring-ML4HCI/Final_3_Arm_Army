import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Motion from '../components/Motion';
import * as MappingActions from '../actions/mapping';

function mapStateToProps(state) {
  return {
    mapping: state.mapping
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(MappingActions, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Motion);
