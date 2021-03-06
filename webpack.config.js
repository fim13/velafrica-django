/* global __dirname, process */
var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var autoprefixer = require('autoprefixer');
var nodeModulesDir = path.join(__dirname, 'node_modules');

var host = process.env.HOST || '127.0.0.1';

var config = {
  context: path.join(__dirname, 'staticfiles'),
  debug: true,
  entry: {
    main: [
      'webpack-dev-server/client?http://' + host + ':4000',
      'webpack/hot/dev-server',
      './../velafrica/frontend/static/js/main.js',
      './../velafrica/frontend/static/scss/main.scss',
    ],
  },
  output: {
    path: path.resolve('./staticfiles/dist/'),
    publicPath: 'http://' + host + ':4000/assets/build/',
    filename: '[name]-[hash].js',
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loaders: [
          'babel?presets[]=es2015,cacheDirectory=' + path.resolve(__dirname, 'tmp'),
        ],
      },
      {
        test: /\.css$/,
        loader: 'style!css',
      },
      // Optionally extract less files
      // or any other compile-to-css language
      {
        test: /\.scss$/,
        loader: 'style!css!postcss!sass',
      },
      {
        test: /\.less/,
        loader: 'style-loader!css-loader!less-loader?relative-urls',
      },
      {
        test: /\.(png|woff2?|svg|eot|ttf)$/,
        loader: 'url-loader?limit=20000',
      },
      {
        test: /\.(jpg)$/,
        loader: 'file?relative-urls',
      },
    ],
    noParse: [],
  },
  postcss: [
    autoprefixer({
      browsers: ['last 3 versions', 'ie >= 9', 'safari >= 6', 'chrome >= 49', 'firefox >= 44'],
    }),
  ],
  sassLoader: {
    includePaths: [path.resolve(nodeModulesDir)],
    outputStyle: 'expanded',
    sourceMap: true,
  },
  resolve: {
    // Allow require('./blah') to require blah.jsx
    extensions: ['', '.js', '.jsx'],
    modulesDirectories: [
      'assets/js',
      'assets/scss',
      'assets/img',
      'node_modules',
      'static/js',
      'static/bootstrap-3.3.6-dist/js',
    ],
    alias: {},
  },
  // Use the plugin to specify the resulting filename (and add needed behavior to the compiler)
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './tmp/webpack-stats.json'}),
  ],
  // dev server not working yet. Have to not extract css during development.
  // devServer: {
  //   contentBase: path.join(__dirname, 'app', 'static', 'app', 'build', 'dist'),
  //   inline: true,
  //   colors: true,
  //   quiet: false,
  // },
};

module.exports = config;
