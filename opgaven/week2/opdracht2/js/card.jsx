import React from 'react';
import FontAwesome from 'react-fontawesome';
import classNames from 'classNames';
import '../css/card.scss';

class Card extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			isMatched: false,
			isOpen: false
		};

		if(this.props.open !== undefined) {
			this.state.isOpen = this.props.open;
		}
	}

	handleClick(e) {
		this.props.onClick(e, this);
	}

	render() {
		let classes = classNames(
			'card', 
			this.props.color, 
			{ 'matched': this.state.isMatched },
			{ 'open': this.state.isOpen || this.state.isMatched }
		);

		return <div className={classes} 
		            ref={this.props.key}
					      onClick={this.handleClick.bind(this)}>
				<div className="front">
					<FontAwesome name={this.props.icon} />
					<h2>{this.props.name}</h2>
				</div>
				<div className="back"></div>
			</div>;
	}
}

Card.propTypes = {
	name: React.PropTypes.string,
	icon: React.PropTypes.string,
	color: React.PropTypes.string,
	pair: React.PropTypes.number
};

export default Card;