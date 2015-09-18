import React from 'react';
import '../css/menu.scss';

class Menu extends React.Component {
	constructor(props) {
		super(props);
	}

	handleStartClick(e) {
		this.props.handleStartClick(e, this);
	}

	render() {
		return <div className="menu">
			<h1>memory</h1>
			<div className="button" onClick={this.handleStartClick.bind(this)}>Start</div>
		</div>
	}
}

export default Menu;