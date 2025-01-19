let plot;

function updatePlot(fixedPoints, currentPoint) {
    const data = [
        {
            type: 'scatter3d',
            mode: 'markers',
            x: fixedPoints.map(p => p[0]),
            y: fixedPoints.map(p => p[1]),
            z: fixedPoints.map(p => p[2]),
            marker: {
                size: 8,
                color: 'blue',
            },
            name: 'Feste Punkte'
        },
        {
            type: 'scatter3d',
            mode: 'markers',
            x: [currentPoint[0]],
            y: [currentPoint[1]],
            z: [currentPoint[2]],
            marker: {
                size: 8,
                color: 'red',
            },
            name: 'Interpolierter Punkt'
        }
    ];

    const layout = {
        margin: { l: 0, r: 0, b: 0, t: 0 },
        scene: {
            camera: {
                eye: { x: 1.5, y: 1.5, z: 1.5 }
            }
        }
    };

    if (!plot) {
        Plotly.newPlot('plot', data, layout);
        plot = true;
    } else {
        Plotly.react('plot', data, layout);
    }
}

function updateValues() {
    const x = parseFloat($('#x-slider').val());
    const y = parseFloat($('#y-slider').val());
    
    $('#x-value').text(x.toFixed(1));
    $('#y-value').text(y.toFixed(1));
    
    fetch(`/get-z/${x}/${y}`)
        .then(response => response.json())
        .then(data => {
            $('#z-value').text(data.z.toFixed(2));
            updatePlot(data.fixed_points, data.current_point);
        });
}

$(document).ready(function() {
    $('#x-slider, #y-slider').on('input', updateValues);
    updateValues();
}); 