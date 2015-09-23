import React from 'react';
import addons from 'react/addons';
import FontAwesome from 'react-fontawesome';
import classNames from 'classNames';
import CardActions from 'actions/cardActions';
import 'style/card';

let ReactCSSTransitionGroup = addons.addons.CSSTransitionGroup;

class Card extends React.Component {
	constructor(props) {
		super(props);
	}

	render() {
		let front;
		let classes = classNames(
			'card', 
			this.props.color,
			{ 'matched': this.props.isMatched },
		);

		return (
			<div className={classes} onClick={this.handleClick}>
				{this.renderCard()}
			</div>	
		);
	}

	renderCard() {
		let back = (
			<div key={this.props.id+'back'} className="back"></div>
		);

		let	front = (
			<div key={this.props.id+'front'} className="front">
				<FontAwesome name={this.props.icon} />
				<h2>{this.props.name}</h2>
			</div>
		);

		if(this.props.isOpen || this.props.isMatched) {
			back = null;
		}
		else {
			front = null;
		}

		let card = (
			<ReactCSSTransitionGroup transitionName="flip">
				{front}
				{back}
			</ReactCSSTransitionGroup>
		);

		return card;
	}

	handleClick = (e) => {
		CardActions.openCard(this.props);
	}
}

export default Card;