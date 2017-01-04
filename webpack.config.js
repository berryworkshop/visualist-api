var ExtractTextPlugin = require('extract-text-webpack-plugin')
var autoprefixer = require('autoprefixer')
var webpack = require('webpack')

// all UI is handled by the visualist app
var project_dir = __dirname + '/django_project/visualist'

var config = {
    // cache: false, // turn on if "$export" bug occurs
    output: {
        path: project_dir,
        filename: '[name]'
    },
    context: project_dir,
    entry: {
        // synchronous styles
        './static/visualist/bundle.css': [
            './templates/visualist/base.scss',
            './templates/visualist/_header.scss',
            './templates/visualist/_footer.scss',
        ],

        // page bundles; one set per view
        './static/visualist/event.js':  './components/event/event.js',
        './static/visualist/event.css': './templates/visualist/event.scss',
    },
    devtool: 'source-map',
    module: {
        // preLoaders: [],
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel',
                exclude: /node_modules/
            },
            {
                test: /\.vue$/,
                loader: 'vue',
                options: {
                    loaders: {
                        'js': 'babel',
                        'scss': 'vue-style!css!sass',
                        'sass': 'vue-style!css!sass?indentedSyntax'
                    }
                }
            },
            {
                test: /\.scss$/,
                loader: "style!css!postcss!sass",
                exclude: /templates/
            },
            {
                test: /templates.*\.scss$/,
                loader: ExtractTextPlugin.extract("style", "css!postcss!sass")
            },
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.common.js'
        }
    },
    plugins: [
        new ExtractTextPlugin('[name]')
    ],
    postcss: [
        autoprefixer({
            browsers: "last 2 versions"
        })
    ]
}

module.exports = config
