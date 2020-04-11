import React, { Component } from 'react';
import Highcharts from 'highcharts';
import './chart.css'

let my_char;

class Chart extends Component {

  componentDidMount() {
    my_char=Highcharts.chart('container',this.props.options);
  }

  componentWillReceiveProps(nextProps, nextContext) {
    const x=nextProps.points.x;
    const y=nextProps.points.y;
    my_char.series[0].addPoint([x, y]);
  }

  test=()=> {
    my_char.series[0].addPoint([10, 1000]);
  }

  render() {
      return <figure className="highcharts-figure"> <div id="container"/>
      <button onClick={this.test}>test</button></figure>
  }
}

export default Chart;