import flux from 'connect';
import socket from 'socket';
import {createActions} from 'alt/utils/decorators';

@createActions(flux)
class HighscoreActions {
	constructor() {
		this.generateActions(
			'updateHighscore',
			'updateHighscores'
		);
	}

	fetchHighscores() {
		socket.on('highscores', (data) => {
			this.actions.updateHighscores(data);
		});

		socket.emit('getHighscores');
	}

	setHighscore(data) {
		socket.emit('setHighscore', data);
	}
}

export default HighscoreActions;