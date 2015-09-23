import React from 'react';
import moment from 'moment';
import socket from 'socket';
import classNames from 'classNames';
import CardActions from 'actions/cardActions';
import HighscoreActions from 'actions/highscoreActions';
import 'style/menu';

class Menu extends React.Component {
	constructor(props) {
		super(props);

		this.state = {}
	}

	formatScore(score) {
		return moment(0)
			.milliseconds(score)
			.format('mm:ss.SSS');
	}

	render() {
		let startButton;
		let congratulationsMessage;
		let highscoreForm;
		let classes = classNames([
			'menu',
			{ 'hidden': this.props.started }
		]);

		let name = this.state.name;
		let score = this.formatScore(this.props.timer);

		startButton = (
			<button className="startButton btn btn-default btn-lg" onClick={this.handleStartGame}>Start new game</button>
		);

		if(this.props.finished && !this.state.submitted && socket.connected) {
			highscoreForm = (
				<form className="form-inline" onSubmit={this.handleSubmitScore}>
					<input name="name" type="text" className="form-control" placeholder="Name" defaultValue={name} />
					<input name="score" type="text" className="form-control" placeholder="00:00.000" readOnly value={score} />
					<button type="submit" className="btn btn-default">Submit score</button>
				</form>
			);
		}

		if(this.props.finished) {
			congratulationsMessage = (
				<h1>Congratulations!<br />You finished in {score}</h1>
			);
		}

		return (
			<div className={classes}>
				{congratulationsMessage}
				{highscoreForm}
				{startButton}
			</div>
		);
	}

	handleStartGame = (e) => {
		this.setState({ submitted: false });

		CardActions.startGame();
		setTimeout(() => {
			CardActions.shuffleCards();
		}, 500);
	}

	handleSubmitScore = (e) => {
		e.preventDefault();

		let score = this.props.timer;

		let inputName = e.target.querySelector('input[name="name"]');
		let name = inputName.value;

		if(!name || name.length < 2 || name.length > 12) {
			return;
		}

		this.setState({ 
			name: name,
			submitted: true
		})

		HighscoreActions.setHighscore({ username: name, score: score });
	}
}

export default Menu;