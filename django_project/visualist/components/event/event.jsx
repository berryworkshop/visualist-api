import React from 'react'
import ReactDOM from 'react-dom'

class Event extends React.Component {
    render() {
        var style = {
            "backgroundColor": 'white',
        };
        return (
            <div style={style}>
                <h1>This is an awesome event.</h1>
                <p>Other titles</p>

                <h2>Friday, January 6, 2017</h2>
                <h2>Chicago Artist Coalition</h2>
                <p>1234 Anywhere St.</p>
                <p>Chicago, IL 60600</p>

                <p>Distance to this event from your current location: 123 miles</p>

                <img className="primary_visual" />
                <p>This is a caption for the above visual.</p>

                <h3>Description</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                <p>Other Descriptions</p>

                <SecondaryVisuals title="Other Images"/>

                <p>Record created by admin on January 1, 2017</p>

                <Sources />
                <CrossReferences />
                <RelatedItems title="Related Items" />
                <RelatedItems title="Similar Items" />
                <Controls />
            </div>
        )
    }
}

class SecondaryVisuals extends React.Component {
    render() {
        return (
            <ul>
                <h3>{this.props.title}</h3>

                <img className="secondary_visual" />
                <p>This is a caption.</p>
                
                <img className="secondary_visual" />
                <p>This is a caption.</p>
                
                <img className="secondary_visual" />
                <p>This is a caption.</p>
            </ul>
        )
    }
}

class Sources extends React.Component {
    render() {
        return (
            <div>
                <h3>Sources</h3>
                <dl>
                    <dd>Source</dd>
                    <dt>The Art Institute of Chicago</dt>

                    <dd>Format</dd>
                    <dt>Website</dt>

                    <dd>Accessed</dd>
                    <dt>January 1, 2017</dt>

                    <dd>Rights</dd>
                    <dt>Public Domain</dt>
                </dl>
            </div>
        )
    }
}

class CrossReferences extends React.Component {
    render() {
        return (
            <div>
                <h3>Cross References</h3>
                <ul>
                    <li>Getty</li>
                    <li>Art Institute of Chicago</li>
                    <li>Library of Congress</li>
                    <li>Artnet</li>
                    <li>Chicago Gallery News</li>
                </ul>
            </div>
        )
    }
}

class RelatedItems extends React.Component {
    render() {
        return (
            <div>
                <h3>{this.props.title}</h3>
                <ul>
                    <li>Related Item</li>
                    <li>Related Item</li>
                    <li>Related Item</li>
                </ul>
            </div>
        )
    }
}

class Controls extends React.Component {
    render() {
        return (
            <div>
                <h3>Controls</h3>
                <ul>
                    <li>New</li>
                    <li>Edit</li>
                    <li>Delete</li>
                    <li>Map it</li>
                    <li>Featured</li>
                    <li>Bookmark</li>
                    <li>Add to Bucket List</li>
                    <li>
                        <h4>Cite</h4>
                        <ul>
                            <li>APA</li>
                            <li>Chicago</li>
                            <li>MLA</li>
                        </ul>
                    </li>
                    <li>
                        <h4>Permissions</h4>
                        <ul>
                            <li>Public</li>
                            <li>Private</li>
                        </ul>
                    </li>
                    <li>
                        <h4>Share</h4>
                        <ul>
                            <li>Email</li>
                            <li>Facebook</li>
                            <li>Pinterest</li>
                        </ul>
                    </li>
                    <li>
                        <h4>Add to List</h4>
                        <ul>
                            <li>Checklist</li>
                            <li>Bookmarks</li>
                        </ul>
                    </li>
                </ul>
            </div>
        )
    }
}

ReactDOM.render(
  <Event />,
  document.getElementById('app_root')
)