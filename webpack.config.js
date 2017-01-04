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
                // exclude: /node_modules/,
                loader: 'babel',
                query: {
                    presets: ['es2015']
                }
            },
            {
                test: /\.vue$/,
                loader: 'vue',
                options: {
                    loaders: {
                        'js': 'babel',
                        // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
                        // the "scss" and "sass" values for the lang attribute to the right configs here.
                        // other preprocessors should work out of the box, no loader config like this nessessary.
                        'scss': 'vue-style!css!sass',
                        'sass': 'vue-style!css!sass?indentedSyntax'
                    }
                // other vue-loader options go here`
                }
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file',
                options: {
                    name: '[name].[ext]?[hash]'
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
        // 'vue': 'vue',
        'd3': 'd3'
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.common.js'
        }
    },
    plugins: [
        new webpack.ProvidePlugin({
          // d3: 'd3',
        }),
        new ExtractTextPlugin('[name]')
    ],
    postcss: [
        autoprefixer({
            browsers: "last 2 versions"
        })
    ],
    babel: {
        presets: ['es2015'],
        plugins: ['transform-runtime']
    },
}

module.exports = config
