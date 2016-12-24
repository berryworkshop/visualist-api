var ExtractTextPlugin = require('extract-text-webpack-plugin')
var autoprefixer = require('autoprefixer')

var config = {
    context: __dirname + "/django_project",
    entry: {
        // base css, not embedded in javascript
        'visualist/static/visualist/base.css': './visualist/templates/visualist/base.scss',
        // 'artcase/static/artcase/base.css':  './artcase/templates/artcase/base.scss'
    },
    devtool: 'source-map',
    output: {
        path: './django_project/',
        filename: '[name]'
    },
    module: {
        loaders: [
            {
                test: /\.jsx$/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react']
                }
            },
            {
                test: /\.scss$/,
                loader: ExtractTextPlugin.extract("style", "css!postcss!sass")
            }
        ]
    },
    externals: {
        //don't bundle libraries but get from CDN
        'react': 'React',
        'react-dom': 'ReactDOM',
        'd3': 'd3'
    },
    plugins: [
    //     new webpack.ProvidePlugin({
    //         d3: 'd3'
    //     })
        new ExtractTextPlugin('[name]')
    ],
    postcss: [
        autoprefixer({
            browsers: "last 2 versions"
        })
    ],
    resolve: {
        // require('file') instead of require('file.js')
        extensions: ['', '.js', '.jsx', '.json', '.css', '.scss']
    }
}

module.exports = config