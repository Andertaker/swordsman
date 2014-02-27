dates = dates;
series = series;

       
       
$(function () {
        $('#container').highcharts({
            chart: {
            	//height: 700,
                type: 'line'
            },
            title: {
                text: 'Статистика'
            },
            subtitle: {
                text: 'swordsman.su'
            },
            
	        legend: {
	            //align: 'left',
	            //verticalAlign: 'bottom',
	            //x: 0,
	            //y: -100
	        },
            
            
            xAxis: {
            	//type: "datetime",
                categories: dates
            },
            yAxis: {
                title: {
                    text: 'Баллы'
                }
            },
            tooltip: {
                enabled: true,
                formatter: function() {
                    return '<b>'+ this.series.name +'</b><br/>'+
                        this.x +': '+ this.y + " балл(ов)";
                }
            },
            plotOptions: {
                line: {
                    dataLabels: {
                        enabled: true
                    },
                    //enableMouseTracking: false
                }
            },
            series: series,
            
        });
    });