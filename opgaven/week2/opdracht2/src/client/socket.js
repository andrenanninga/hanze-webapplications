import io from 'socket.io-client';

const socket = io.connect('//localhost:7000');
export default socket;