import React from 'react';
import Deck from 'components/deck';
import Highscores from 'components/highscores';
import 'style/app';

class Main extends React.Component {
	render() {
		return (
			<div className="row">
				<div className="col-md-8">
					<Deck size="small" />
				</div>
				<div className="col-md-4">
					<Highscores />
				</div>
			</div>
		);
	}
}

export default Main;