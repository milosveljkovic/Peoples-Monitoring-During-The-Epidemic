import React, {Component} from 'react';
import Highcharts from 'highcharts';
import './chart.css'

let my_char;

class Chart extends Component {

    componentDidMount() {
        my_char = Highcharts.chart('container', this.props.options);
    }

    // componentWillMount(){
    //     for (var i = 0; i < my_char.series[0].length; i++) {
    //         my_char.series[0].data[i].remove();
    //     }
    // }

    componentWillReceiveProps(nextProps, nextContext) {
        if(!nextProps.clear){
        const x = nextProps.points.x;
        const y = nextProps.points.y;
        my_char.series[0].addPoint([x, y]);
        }else{
            for (var i = 0; i < my_char.series[0].data.length; i++) {
                my_char.series[0].data[i].remove();
            }
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