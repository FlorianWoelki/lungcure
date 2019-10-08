const ctx = document.getElementById('predictions-chart');
const labels = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion',
                'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'Nodule',
                'Pleural_Thickening', 'Pneumonia', 'Pneumothorax'];

if (ctx !== null) {
    let predictions = {{ predictions }};
    predictions = predictions.map((prediction) => prediction*100);
    const myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                  label: 'Predictions',
                  backgroundColor: 'rgba(220,220,220,1)', 
                  data: predictions
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: true,
                        color: '#555',
                    },
                    ticks: {
                        fontColor: '#fff'
                    }
                }],
                yAxes: [{
                    display: true,
                    gridLines: {
                        display: true,
                        color: '#555',
                    },
                    ticks: {
                        fontColor: '#fff'
                    }
                }]
            }
        }
    });
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}
