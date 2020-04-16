import React, { Component } from 'react';
import Highcharts from 'highcharts';
import './gaugechart.css'

let my_char;
const M_TO_KM = 1000;

class GaugeChart extends Component {

    componentDidMount() {
        my_char = Highcharts.chart('container-speed', this.props.options);
    }

    componentWillReceiveProps(nextProps, nextContext) {
        if (!nextProps.clear) {
            my_char.yAxis[0].update({
                max: nextProps.goal_distance,
                tickPositions:[0,nextProps.goal_distance]
            })
            let add_distance = nextProps.distance;
            let add_dist_in_km = add_distance / M_TO_KM
            let current_distance = my_char.series[0].points[0];
            let new_distance = add_dist_in_km + current_distance.y;
            current_distance.update(new_distance);
        } else {
            my_char.series[0].points[0].update(0)
        }
    }

    render() {
        return <figure className="highcharts-figure">
            <div id="container-speed" className="chart-container" />
        </figure>
    }
}

export default GaugeChart;