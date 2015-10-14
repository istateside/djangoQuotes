var path = require('path');

module.exports = {
  entry: [
    'webpack/hot/dev-server',
    'webpack-dev-server/client?http://localhost:8080',
    path.resolve(__dirname, 'app/main.jsx')
  ],
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: "bundle.js"
  },
  resolve: {
    modulesDirectories: ['node_modules']
  },
  module: {
    loaders: [
      { test: /\.scss$/, loader: ["sass", "css", "sass"] },
      { test: /\.jsx$/, loader: "jsx"}
    ]
  }
}