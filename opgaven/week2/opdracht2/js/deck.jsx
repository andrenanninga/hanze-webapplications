import React from 'react';
import addons from 'react/addons';
import FontAwesome from 'react-fontawesome';
import classNames from 'classNames';
import Chance from 'chance';
import Card from './card.jsx';
import Menu from './menu.jsx';
import '../css/deck.scss';

let chance = new Chance();

class Deck extends React.Component {

	constructor(props) {
		super(props);

		this.matching = [];
		this.matches = 0;
		this.state = {
			score: 0,
			isStarted: false
		};

		let cards = [
			{ name: 'lock',    icon: 'unlock-alt',     color: 'green'},
			{ name: 'anchor',  icon: 'anchor',         color: 'blue'},
			{ name: 'plane',   icon: 'paper-plane',    color: 'red'},
			{ name: 'star',    icon: 'star',           color: 'yellow'},
			{ name: 'diamond', icon: 'diamond',        color: 'blue'},
			{ name: 'camera',  icon: 'camera',         color: 'red'},
			{ name: 'cap',     icon: 'graduation-cap', color: 'yellow'},
			{ name: 'magnet',  icon: 'magnet',         color: 'green'},
			{ name: 'heart',   icon: 'heart',          color: 'red'},
			{ name: 'car',     icon: 'car',            color: 'blue'},
			{ name: 'plug',    icon: 'plug',           color: 'green'},
			{ name: 'brush',   icon: 'paint-brush',    color: 'red'},
			{ name: 'rocket',  icon: 'rocket',         color: 'blue'},
			{ name: 'spoon',   icon: 'spoon',          color: 'yellow'},
			{ name: 'house',   icon: 'home',           color: 'green'},
			{ name: 'coffee',  icon: 'coffee',         color: 'yellow'},
			{ name: 'flask',   icon: 'flask',          color: 'blue'},
			{ name: 'gift',    icon: 'gift',           color: 'red'}
		];

		if(this.props.size === 'small') {
			cards = cards.slice(0, 2);
		}
		else if(this.props.size === 'medium') {
			cards = cards.slice(0, 8);
		}
		else if(this.props.size === 'large') {
			cards = cards;
		}

		// create an array with pairs of every card
		// in every pair one card has the prop 'pair:0' 
		// the other card has the prop 'pair:1'
		cards = [].concat(
			cards.map((card) => { 
				card.key = card.name + '_' + 0; 
				return card; 
			}),
			cards.map((card) => { 
				// clone the object
				card = Object.assign({}, card); 
				card.key = card.name + '_' + 1; 
				return card; 
			})
		);

		cards = chance.shuffle(cards);

		// cards.sort((a, b) => {
		// 	if(a.name < b.name) return -1;
		// 	if(a.name > b.name) return 1;
		// 	return 0;
		// });

		this.cards = cards.map((card) => {
			return <Card name={card.name} 
				           icon={card.icon} 
				           color={card.color} 
				           key={card.key} 
				           onClick={this.handleCardClick.bind(this)} />;
		});
	}

	handleStartClick(e) {
		console.log(this);

		if(!this.state.isStarted) {
			this.setState({ cards: chance.shuffle(this.cards) });
			this.setState({ isStarted: true });
		}
	}

	handleCardClick(e, card) {
		if(card.state.isMatched) {
			return;
		}

		if(this.matching.length < 2 && this.matching[0] !== card) {
			this.matching.push(card);
			this.setState({ score: this.state.score + 1 });
			card.setState({ isOpen: true });
		}

		if(this.matching.length === 2) {
			if(this.matching[0].props.name === this.matching[1].props.name) {
				this.matching[0].setState({ isMatched: true });
				this.matching[1].setState({ isMatched: true });
				this.matches += 1;

				if(this.matches === this.cards.length / 2) {
					console.log('you win');
				}
			}
			else {
				var match0 = this.matching[0];
				var match1 = this.matching[1]
				setTimeout(() => {
					match0.setState({ isOpen: false });
					match1.setState({ isOpen: false });
				}, 1000);
			}
			
			this.matching = [];
		}
	}

	render() {
		let header;
		let menu;

		if(this.state.isStarted) {
			header = ([
				<h1>score {this.state.score}</h1>,
				<FontAwesome name="bars" key="menuButton" />
			]);
		}
		else {
			menu = <Menu handleStartClick={this.handleStartClick.bind(this)} key="menu" />
		}

		let classes = classNames(
			'deck',
			this.props.size
		);

		return <div className={classes}>
			{menu}
			{header}
			<div className="cards" ref="test">
				{this.cards}
			</div>
		</div>
	}
}

Deck.propTypes = {
	size: React.PropTypes.string
};

export default Deck;