window.onload = function(){ 
    var ctx = document.getElementById('balance-chart').getContext('2d');
    var pln = document.getElementById('PLN-balance').textContent
    var btc = document.getElementById('BTC-balance').textContent
    var xrp = document.getElementById('XRP-balance').textContent
    var eth = document.getElementById('ETH-balance').textContent

    let data1 = [pln, btc, xrp, eth];
    let labels1 = ['PLN', 'BTC', 'XRP', 'ETH'];
    let colors1 = ['#1C3144','#F7A100', '#2D85BE', '#60668b'];

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: labels1,
            datasets: [{
                backgroundColor: colors1,
                data: data1,
                weight: 0.1,
            }]
            
        },

        // Configuration options go here
        options: {
            cutoutPercentage: 70
        }
    });
}