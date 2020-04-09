import React, {Dispatch} from 'react';
import socketIOClient from 'socket.io-client';


class Dashboard extends React.Component {

    constructor(props) {
        super(props);
        this.socket = socketIOClient('http://127.0.0.1:5000/');
        this.state = {
            recived_message: 'No messages yet'
        }
    }

    setme = (msg) => {
        console.log('Recived Message')
        this.setState({recived_message: msg})
    }

    connect = () => {
        this.socket.on('connect', function () {
            this.socket.send('User has connected!');
        });

        this.   socket.on('message',(msg)=> this.setme(msg));
    }

    render() {
        const {recived_message} = this.state;
        return (
            <div>
                <h1>Dashboard</h1>
                <button onClick={this.connect}>
                    Connect to Device.
                </button>
                <p>
                    Recived message: {recived_message}
                </p>
            </div>
        )
    }
}

export default Dashboard;