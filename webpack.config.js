var ExtractTextPlugin = require('extract-text-webpack-plugin')
var autoprefixer = require('autoprefixer')

// all UI is handled by the visualist app
var project_dir = __dirname + '/django_project/visualist'

var config = {
    output: {
        path: project_dir,
        filename: '[name]'
    },
    context: project_dir,
    entry: {
        // base css, not embedded in javascript
        './static/visualist/bundle.css': [
            './templates/visualist/base.scss',
            './templates/visualist/_header.scss',
            './templates/visualist/_messages.scss',
            './templates/visualist/_ankle.scss',
            './templates/visualist/_footer.scss',
            './templates/visualist/event.scss',
            './templates/visualist/event_list.scss',
            './templates/visualist/home.scss',
        ],

        // bundled components, one per template
        './static/visualist/event_list.js': [
            './components/card/card.jsx',
        ],
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