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