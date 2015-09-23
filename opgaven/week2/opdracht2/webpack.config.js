'use strict';

var webpack           = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var path              = require('path');

var srcPath    = path.join(__dirname, 'src/client');
var buildPath  = path.join(__dirname, 'build');
var modulePath = path.join(srcPath, 'module.js');
var indexPath  = path.join(srcPath, 'index.html');

module.exports = {
	target: 'web',
	cache: true,
	entry: {
		module: modulePath,
		common: ['react', 'react-router', 'alt']
	},
	resolve: {
		root: srcPath,
		extensions: ['', '.js', '.scss'],
		modulesDirections: ['node_modules', 'src']
	},
	output: {
		path: buildPath,
		publicPath: '',
		filename: '[name].js',
		libary: ['Example', '[name]'],
		pathInfo: true 
	},
	module: {
		loaders: [
			{test: /\.js?$/, exclude: /node_modules/, loader: 'babel?cacheDirectory'},
			{ test: /\.scss$/, loader: 'style!css!sass' },
			{ test: /\.css$/, loader: 'style!css' }
		]
	},
	plugins: [
		new webpack.optimize.CommonsChunkPlugin('common', 'common.js'),
		new HtmlWebpackPlugin({
			inject: true,
			template: indexPath
		}),
		new webpack.NoErrorsPlugin()
	],
	debug: true,
	devtool: 'eval-cheap-module-source-map',
	devServer: {
		contentBase: buildPath,
		historyApiFallback: true
	}
};