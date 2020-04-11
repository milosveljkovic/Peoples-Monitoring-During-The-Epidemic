import React from 'react';
import socketIOClient from 'socket.io-client';
import {ENDPOINT_URL, NAMESPACE, highchart_options as options} from "../../common/constants";
import Chart from "../../components/Chart";
import './dashboard.css'

let socket;

class Dashboard extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            connected: false,
            points: {
                x: 1,
                y: 3
            }
        }
    }

    connectionEstablised = (is_OK) => {
        console.log(is_OK);
        if (is_OK === 200)
            this.setState({connected: true})
    }


    componentWillUnmount() {
        if (this.state.connected) {
            socket.emit('disconnect')
        }
    }

    componentDidMount() {

    }

    update_graph = (points) => {
        console.log('Receiving points: ', points)
        this.setState({points: points})
    }

    connect = () => {
        socket = socketIOClient(ENDPOINT_URL + NAMESPACE);

        socket.on('my response', (points) => this.update_graph(points));
        socket.on('connection_success', (is_OK) => this.connectionEstablised(is_OK));
    }

    activateEvents = () => {
        if (this.state.connected) {
            socket.emit('set_iot_const')
        }
    }

    render() {
        return (
            <div className={'container'}>
                <div className={'center-title'}>
                    <h1>Dashboard</h1>
                    <h5>{this.state.connected ? <p className={'success'}>CONNECTED</p> :
                        <p className={'fail'}>DISCONNECTED</p>}
                    </h5>
                    <button onClick={this.connect}>
                        Connect to Device.
                    </button>
                    <button onClick={this.activateEvents}>
                        Activate event.
                    </button>
                </div>
                <p>
                    Recived message:
                </p>
                <div>
                    <Chart
                        points={this.state.points}
                        options={options}/>
                </div>
            </div>
        )
    }
}

export default Dashboard;