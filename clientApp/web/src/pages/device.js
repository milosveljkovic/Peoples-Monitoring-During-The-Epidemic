import React, {Dispatch} from 'react';
import socketIOClient from 'socket.io-client';
const socket = socketIOClient('http://127.0.0.1:5000/');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

class Device extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            message: ''
        }
    }

    onChange = (event) => {
        this.setState({[event.target.name]: event.target.value})
    }

    connect = () => {
        socket.on('connect', function () {
            socket.send('User has connected!');
        });
    }

     sendMessage = async (my_message) => {
        for(let j=0;j<10;j++) {
            let i=Math.floor(Math.random() * 100);
            socket.send('TEST');
            await sleep(2000);
        }
    }

    render() {
        const {message} = this.state;
        return (
            <div className={'container'}>
                <h1>Device</h1>
                <button onClick={this.connect}>
                    Connect to dashboard.
                </button>
                <button onClick={() => this.sendMessage(this.state.message)}>
                    Send.
                </button>
                <input onChange={this.onChange} type="text" name="message" className="form-control "
                       id="validationCustom01" placeholder="Message" value={message} required/>
            </div>
        )
    }
}

export default Device;