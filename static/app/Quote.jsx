var React = require('react')
var Source = require('./Source.jsx')
module.exports = React.createClass({
  getInitialState: function() {
    return {
      body: "Do or do not.",
    }
  },
  render: function() {
    return (
      <div className='quote'>
        <p>{ this.state.body }</p>
        <Source />
      </div>
    );
  }
});