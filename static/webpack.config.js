var webpack = require('webpack'),
    path = require('path');

module.exports = {
  debug: true,
  entry: {
    main: './app/main.jsx'
  },
  output: {
    path: path.resolve(__dirname, './build'),
    filename: "[name].js"
  },
  resolve: {
    extensions: ["", ".js", ".sass"],
    modulesDirectories: ['node_modules']
  },
  module: {
    loaders: [
      { test: /\.sass$/, loaders: ["style-loader", "css-loader", "sass-loader"] },
      { test: /\.jsx$/, loader: "jsx"}
    ]
  }
}