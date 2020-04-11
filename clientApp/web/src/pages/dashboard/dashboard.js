import React from 'react';
import socketIOClient from 'socket.io-client';
import {
    ENDPOINT_URL,
    NAMESPACE,
    highchart_options as options,
    gaugechart_options as gauge_options
} from "../../common/constants";
import Chart from "../../components/Chart";
import './dashboard.css'

//this is important to have because without this chart wont be available
import GaugeChart from "../../components/Gaugechart";
import * as ChartModuleMore from 'highcharts/highcharts-more.js';
import HCSoldGauge from 'highcharts/modules/solid-gauge';
import Highcharts from 'highcharts'

ChartModuleMore(Highcharts);
HCSoldGauge(Highcharts);
//this is important to have because without this chart wont be available

let socket;

class Dashboard extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            connected: false,
            points: '',
            distance: 0
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
        console.log('Receiving points: ', points.new_distance)
        this.setState({points: points, distance: points.new_distance})
    }

    connect = () => {
        socket = socketIOClient(ENDPOINT_URL + NAMESPACE);

        socket.on('data_event', (points) => this.update_graph(points));
        socket.on('connection_success', (is_OK) => this.connectionEstablised(is_OK));
    }

    activateEvents = () => {
        if (this.state.connected) {
            socket.emit('start_iot')
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
                <div>
                    <GaugeChart
                        distance={this.state.distance}
                        options={gauge_options}/>
                </div>
            </div>
        )
    }
}

export default Dashboard;