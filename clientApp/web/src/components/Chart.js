import React, {Component} from 'react';
import Highcharts from 'highcharts';
import './chart.css'

let my_char;

class Chart extends Component {

    componentDidMount() {
        my_char = Highcharts.chart('container', this.props.options);
    }

    componentWillReceiveProps(nextProps, nextContext) {
        if(!nextProps.clear){
        const x = nextProps.points.x;
        const y = nextProps.points.y;
        my_char.series[0].addPoint([x, y]);
        }else{
            my_char.update({
                series: [{
                    data: []
                }]
            })
        }
    }

    render() {
        return <figure className="highcharts-figure">
            <div id="container"/>
        </figure>
    }
}

export default Chart;