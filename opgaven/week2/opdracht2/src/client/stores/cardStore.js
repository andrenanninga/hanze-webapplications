import flux from 'connect';
import {createStore, bind} from 'alt/utils/decorators';
import {knuthShuffle} from 'knuth-shuffle';
import {sortByAll, find, indexBy, values} from 'lodash';
import CardActions from 'actions/cardActions';

@createStore(flux)
class CardStore {
	constructor() {
		this.timer = 0;
		this.started = false;
		this.finished = false;
		this.cards = [];
	}

	@bind(CardActions.updateCards);
	updateCards(cards) {
		cards = indexBy(cards, 'id');
		this.cards = cards;
	}

	@bind(CardActions.updateCard);
	updateCard(card) {
		this.cards[card.id] = card;
	}

	@bind(CardActions.updateTimer);
	updateTimer(timer) {
		this.timer = timer;
	}

	@bind(CardActions.shuffleCards);
	shuffleCards() {
		this.updateCards(knuthShuffle(values(this.cards)));
	}

	@bind(CardActions.startGame);
	startGame() {
		let cards = values(this.cards);
		cards.forEach((card) => {
			card.isStarted = true;
			card.isOpen = false;
			card.isMatched = false;
		});

		this.updateCards(cards);
		this.started = true;
		this.finished = false;
		this.timer = 0;
	}

	@bind(CardActions.stopGame);
	stopGame() {
		this.started = false;
		this.finished = true;
	}

	@bind(CardActions.sortCards);
	sortCards() {
		this.updateCards(sortByAll(this.cards, ['color', 'name']));
	}
}

export default CardStore;