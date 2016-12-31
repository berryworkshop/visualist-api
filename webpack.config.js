var ExtractTextPlugin = require('extract-text-webpack-plugin')
var autoprefixer = require('autoprefixer')

var config = {
    context: __dirname + "/django_project",
    entry: {
        // // base css, not embedded in javascript
        'visualist/static/visualist/base.css': [
            './visualist/templates/visualist/base.scss',
            './visualist/templates/visualist/_header.scss',
            './visualist/templates/visualist/_messages.scss',
            './visualist/templates/visualist/_ankle.scss',
            './visualist/templates/visualist/_footer.scss',
            './visualist/templates/visualist/event.scss',
            './visualist/templates/visualist/event_list.scss',
            './visualist/templates/visualist/home.scss',
        ],
        'visualist/static/visualist/card.js': [
            './visualist/components/card/card.jsx',
        ],
    },
    output: {
        path: './django_project/',
        filename: '[name]'
    },
    devtool: 'source-map',
    module: {
        loaders: [
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
                test: /templates.*\.s?css$/,
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
        // new webpack.ProvidePlugin({
        //     d3: 'd3'
        // })
        new ExtractTextPlugin('[name]')
    ],
    postcss: [
        autoprefixer({
            browsers: "last 2 versions"
        })
    ],
}

module.exports = config