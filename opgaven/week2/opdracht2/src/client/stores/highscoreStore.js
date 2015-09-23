import flux from 'connect';
import {createStore, bind} from 'alt/utils/decorators';
import {indexBy, values} from 'lodash';
import HighscoreActions from 'actions/highscoreActions';

@createStore(flux)
class HighscoreStore {
	constructor() {
		this.highscores = [];
	}

	@bind(HighscoreActions.updateHighscores);
	updateHighscores(highscores) {
		highscores = indexBy(highscores, '_id');
		this.highscores = highscores;
	}

	@bind(HighscoreActions.updateHighscore);
	updateHighscore(highscore) {
		this.highscores[highscore.id] = highscore;
	}
}

export default HighscoreStore;