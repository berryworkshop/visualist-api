var ExtractTextPlugin = require('extract-text-webpack-plugin')
var autoprefixer = require('autoprefixer')
var webpack = require('webpack')

// all UI is handled by the visualist app
var project_dir = __dirname + '/django_project/visualist'

var config = {
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
            './templates/visualist/_eyebrow.scss',
            './templates/visualist/_messages.scss',
            './templates/visualist/_ankle.scss',
            './templates/visualist/_footer.scss',
        ],

        // page bundles; one set per view
        './static/visualist/event.js': [
            './components/event/event.jsx'
        ],
        './static/visualist/event_list.js': [
            './components/event_list.jsx',
            './components/card/card.jsx'
        ],
        './static/visualist/event_list.css': [
            './templates/visualist/event_list.scss'
        ],
        // './static/visualist/event.js': [
        //     './components/event/_event.js',
        // ],
    },
    devtool: 'source-map',
    module: {
        preLoaders: [
            {
                test: /\.tag$/,
                // exclude: /node_modules/,
                loader: 'riotjs',
                query: {
                    type: 'none'
                }
            }
        ],
        loaders: [
            {
                test: /\.js$|\.tag$/,
                // exclude: /node_modules/,
                loader: 'babel',
                query: {
                    presets: ['es2015']
                }
            },
            {
                test: /\.jsx$/,
                loader: 'babel',
                query: {
                    presets: ['es2015', 'react']
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
    externals: {
        // libraries from CDN
        'react': 'React',
        'react-dom': 'ReactDOM',
        'd3': 'd3'
    },
    plugins: [
        new webpack.ProvidePlugin({
          // d3: 'd3',
          // riot: 'riot'
        }),
        new ExtractTextPlugin('[name]')
    ],
    postcss: [
        autoprefixer({
            browsers: "last 2 versions"
        })
    ],
}

module.exports = config
