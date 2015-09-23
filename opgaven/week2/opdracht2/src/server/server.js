import io from 'socket.io';
import nedb from 'nedb';
import path from 'path';

let server = io(7000);
let database = new nedb({
	filename: path.resolve(__filename, '../../../db/highscores.db'),
	autoload: true
});

let getHighscores = (cb) => {
	database.find({}).sort({ score: 1 }).limit(10).exec(cb);
};

server.on('connection', (socket) => {
	socket.on('getHighscores', (data) => {
		getHighscores((err, highscores) => {
			if(err) { return console.error(err); }

			socket.emit('highscores', highscores);
		});
	});

	socket.on('setHighscore', (data) => {
		let username = data.username;
		let score = parseInt(data.score);

		if(!username || !score) {
			return;
		}

		let doc = {
			username: username,
			score: score
		};


		database.insert(doc, (err) => {
			if(err) { return console.error(err); }

			getHighscores((err, highscores) => {
				if(err) { return console.error(err); }

				socket.emit('highscores', highscores);
				socket.broadcast.emit('highscores', highscores);
			})
		});
	})

	socket.on('event', function(data) {
		console.log(data);
	})
});
