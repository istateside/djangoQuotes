var React = require('react')

module.exports = React.createClass({
  getInitialState: function() {
    return {
      name: "Yoda",
      title: "The Empire Strikes Back"
    }
  },
  render: function() {
    return (
      <div className='byline'>
        <span>- </span><h4>{ this.state.name }</h4><em>{ this.state.title }</em>
      </div>
    )
  }
})