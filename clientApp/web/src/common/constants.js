import Highcharts from 'highcharts';

export const METHOD = {
    GET: 'GET',
    POST: 'POST',
    DELETE: 'DELETE'
}

export const ENDPOINT_URL = "http://127.0.0.1:5000/"
export const NAMESPACE = 'iot';

export const highchart_options = {
    chart: {
        height: 600,
        type: 'scatter',
    },
    title: {
        text: 'Coordinates of device'
    },
    xAxis: {
        title: {
            text: 'x coordinate'
        },
        gridLineWidth: 1,
        minPadding: 0.2,
        maxPadding: 0.2,
        maxZoom: 60
    },
    yAxis: {
        title: {
            text: 'y coordinate'
        },
        minPadding: 0.2,
        maxPadding: 0.2,
        maxZoom: 60,
        plotLines: [{
            value: 0,
            width: 1,
            color: '#808080'
        }]
    },
    plotOptions: {
        series: {
            lineWidth: 1,
        }
    },
    series: [{
        name: 'runners path',
        data: [],
    }]
}

export const gaugechart_options = {
    chart: {
        type: 'solidgauge'
    },
    title: null,
    pane: {
        center: ['50%', '85%'],
        size: '100%',
        startAngle: -90,
        endAngle: 90,
        background: {
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || '#EEE',
            innerRadius: '60%',
            outerRadius: '100%',
            shape: 'arc'
        }
    },
    exporting: {
        enabled: false
    },
    tooltip: {
        enabled: false
    },
    plotOptions: {
        solidgauge: {
            dataLabels: {
                y: 10,
                borderWidth: 0,
                useHTML: true
            }
        }
    },
    yAxis: {
        min: 0,
        max: 1, //user should set this parameter...?
        title: {
            text: 'Distance',
            y: 10
        },
        stops: [
            [0.8, '#55BF3B'], // green
            [0.5, '#DDDF0D'], // yellow
            [0.2, '#DF5353'] // red
        ],
        lineWidth: 0,
        tickWidth: 0,
        tickAmount: 2,
        minorTickInterval: null,
        tickPositions: [0,1],
        labels: {
            y: 16
        }
    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Distance',
        data: [0],
        dataLabels: {
            format:
                '<div style="text-align:center">' +
                '<span style="font-size:20px">{y:.2f}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">km</span>' +
                '</div>'
        },
        tooltip: {
            valueSuffix: ' km'
        }
    }]
}

