import React from 'react';
import FontAwesome from 'react-fontawesome';
import '../css/card.scss';

class Card extends React.Component {
	constructor () {
		super();
		this.state = {
			isActive: false,
			isHovering: false
		};
	}

	handleMouseOver () {
		this.setState({ isHovering: true });
	}

	handleMouseOut () {
		this.setState({ isHovering: false });
	}

	handleClick () {
		let isActive = !this.state.isActive;
		this.setState({ isActive: isActive });
	}

	render() {
		let cardClassName = 'card ' + this.props.color;

		if(this.state.isActive) {
			cardClassName += ' matched';
		}

		let iconClassName = 'fa fa-' + this.props.icon;
		return 	<div className={cardClassName}
								 onMouseOver={this.handleMouseOver.bind(this)} 
								 onMouseOut={this.handleMouseOut.bind(this)}
								 onClick={this.handleClick.bind(this)}>
							<div className="front">
								<i className={iconClassName}></i>
								<h2>{this.props.name}</h2>
							</div>
							<div className="back">back</div>
					 	</div>;
	}
}

export default Card;