import flux from 'connect';
import {createActions} from 'alt/utils/decorators';
import {indexBy, where, values} from 'lodash';
import HighscoreActions from 'actions/highscoreActions';

const cardDefinitions = [
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

@createActions(flux)
class CardActions {
	constructor() {
		this.generateActions(
			'shuffleCards',
			'sortCards',
			'updateCards',
			'updateCard',
			'updateTimer'
		);

		this.timer = null;
	}

	getCards(amount) {
		let definitions = cardDefinitions.slice(0, amount / 2);

		let cardPairs1 = definitions.map((card) => {
			card = Object.assign({}, card);
			card.pair = 1;
			card.isStarted = false;
			card.isOpen = true;
			card.isMatched = false;
			card.id = card.name + card.pair;
			return card;
		});

		let cardPairs2 = definitions.map((card) => {
			card = Object.assign({}, card);
			card.pair = 2;
			card.isStarted = false;
			card.isOpen = true;
			card.isMatched = false;
			card.id = card.name + card.pair;
			return card;
		});

		let cards = [].concat(cardPairs1, cardPairs2);

		cards = indexBy(cards, 'id');

		this.actions.updateCards(cards);
		setTimeout(() => {
			this.actions.sortCards();
		}, 500);
	}

	openCard(card) {
		if(card.isOpen) {
			return;
		}

		let cards = this.alt.stores.CardStore.getState().cards;
		var openCards = where(cards, { isOpen: true, isMatched: false });

		if(openCards.length < 2) {
			card.isOpen = true;
			this.actions.updateCard(card);
		}

		openCards = where(cards, { isOpen: true, isMatched: false });

		if(openCards.length === 2) {
			if(openCards[0].name === openCards[1].name) {
				setTimeout(() => {
					openCards[0].isMatched = true;
					openCards[1].isMatched = true;
					this.actions.updateCard(openCards[0]);
					this.actions.updateCard(openCards[1]);
					this.actions.checkComplete();
				}, 1000);
			}
			else {
				setTimeout(() => {
					openCards[0].isOpen = false;
					openCards[1].isOpen = false;
					this.actions.updateCard(openCards[0]);
					this.actions.updateCard(openCards[1]);
				}, 1000);
			}
		}
	}

	checkComplete() {
		let cards = values(this.alt.stores.CardStore.getState().cards);
		let matchedCards = where(cards, { isMatched: true });

		if(cards.length === matchedCards.length) {
			this.actions.stopGame();
		}
	}

	startGame() {
		this.dispatch();

		if(this.timer) {
			clearTimeout(this.timer);
			this.timer = null;
		}
		
		var timer = () => {
			var time = this.alt.stores.CardStore.getState().timer;
			var started = this.alt.stores.CardStore.getState().started;
			var start = Date.now();

			this.timer = setTimeout(() => {
				if(started) {
					let delta = Date.now() - start;
					this.actions.updateTimer(time + delta);

					timer();
				}
			}, 10);
		};

		timer();
	}

	stopGame() {
		this.dispatch();

		if(this.timer) {
			clearTimeout(this.timer);
			this.timer = null;
		}
	}
}

export default CardActions;