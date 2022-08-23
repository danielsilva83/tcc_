const formData = new FormData(document.querySelector('form'))

<style>
    #chartdiv {
      width: 100%;
      height: 500px;
    }
    </style>
    
    <!-- Resources -->
    <script src="https://cdn.amcharts.com/lib/5/index.js"></script>
    <script src="https://cdn.amcharts.com/lib/5/xy.js"></script>
    <script src="https://cdn.amcharts.com/lib/5/themes/Animated.js"></script>
    
    <!-- Chart code -->
    <script>
    am5.ready(function() {
    
    // Create root element
    // https://www.amcharts.com/docs/v5/getting-started/#Root_element
    var root = am5.Root.new("chartdiv");
    
    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    root.setThemes([am5themes_Animated.new(root)]);
    
    // Create chart
    // https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = root.container.children.push(
      am5xy.XYChart.new(root, {
        panX: false,
        panY: false,
        wheelX: "panX",
        wheelY: "zoomX",
        layout: root.verticalLayout
      })
    );
    
    // Add scrollbar
    // https://www.amcharts.com/docs/v5/charts/xy-chart/scrollbars/
    chart.set(
      "scrollbarX",
      am5.Scrollbar.new(root, {
        orientation: "horizontal"
      })
    );
    
    var data = document.getElementById("list");
    
    // Create axes
    // https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
    var xAxis = chart.xAxes.push(
      am5xy.CategoryAxis.new(root, {
        categoryField: "year",
        renderer: am5xy.AxisRendererX.new(root, {}),
        tooltip: am5.Tooltip.new(root, {})
      })
    );
    
    xAxis.data.setAll(data);
    
    var yAxis = chart.yAxes.push(
      am5xy.ValueAxis.new(root, {
        min: 0,
        extraMax: 0.1,
        renderer: am5xy.AxisRendererY.new(root, {})
      })
    );
    
    
    // Add series
    // https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    
    var series1 = chart.series.push(
      am5xy.ColumnSeries.new(root, {
        name: "Income",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "income",
        categoryXField: "year",
        tooltip:am5.Tooltip.new(root, {
          pointerOrientation:"horizontal",
          labelText:"{name} in {categoryX}: {valueY} {info}"
        })
      })
    );
    
    series1.columns.template.setAll({
      tooltipY: am5.percent(10),
      templateField: "columnSettings"
    });
    
    series1.data.setAll(data);
    
    var series2 = chart.series.push(
      am5xy.LineSeries.new(root, {
        name: "Expenses",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "expenses",
        categoryXField: "year",
        tooltip:am5.Tooltip.new(root, {
          pointerOrientation:"horizontal",
          labelText:"{name} in {categoryX}: {valueY} {info}"
        })    
      })
    );
    
    series2.strokes.template.setAll({
      strokeWidth: 3,
      templateField: "strokeSettings"
    });
    
    
    series2.data.setAll(data);
    
    series2.bullets.push(function () {
      return am5.Bullet.new(root, {
        sprite: am5.Circle.new(root, {
          strokeWidth: 3,
          stroke: series2.get("stroke"),
          radius: 5,
          fill: root.interfaceColors.get("background")
        })
      });
    });
    
    chart.set("cursor", am5xy.XYCursor.new(root, {}));
    
    // Add legend
    // https://www.amcharts.com/docs/v5/charts/xy-chart/legend-xy-series/
    var legend = chart.children.push(
      am5.Legend.new(root, {
        centerX: am5.p50,
        x: am5.p50
      })
    );
    legend.data.setAll(chart.series.values);
    
    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/
    chart.appear(1000, 100);
    series1.appear();
    
    }); // end am5.ready()
    </script>
    
    <!-- HTML -->
    <div id="chartdiv"></div>
    amCharts

















    for(i;i<ori1.length;i++) {
    
      dv1 = i+div2
  
      dv_ = String(dv1)
      divroot = "chartdiv"
  
      div_1 = divroot.concat(dv_)
      
  
      ori =''
      ori = ori1[i].replace('{"0":{"0":', '[{ medida: ');
      ori = ori.replaceAll('"0":', '');
      ori = ori.replaceAll('"1":', '');
      ori = ori.replaceAll('{"', '{ medida: "');
      ori = ori.replaceAll('",', '", value: ');
      ori = ori.replace(',"1"', ', value');
      ori = ori.replace('"2":', ' ');ori = ori.replace('"3":', ' ');ori = ori.replace('"4":', ' ');ori = ori.replace('"5":', ' ');ori = ori.replace('"6":', ' ');ori = ori.replace('"7":', ' ');ori = ori.replace('"8":', ' ');ori = ori.replace('"9":', ' ');ori = ori.replace('"10":', ' ');ori = ori.replace('"11":', ' ');ori = ori.replace('"12":', ' ');
      ori = ori.replace('"13":', ' ');ori = ori.replace('14":', ' ');ori = ori.replace('"15":', ' ');ori = ori.replace('"16":', ' ');ori = ori.replace('"17":', ' ');ori = ori.replace('"18":', ' ');ori = ori.replace('"19":', ' ');ori = ori.replace('"20":', ' ');ori = ori.replace('"21":', ' ');ori = ori.replace('"22":', ' ');ori = ori.replace('"23":', ' ');
      ori = ori.replace('"24":', ' ');ori = ori.replace('"25":', ' ');ori = ori.replace('"26":', ' ');ori = ori.replace('"27":', ' ');ori = ori.replace('"28":', ' ');ori = ori.replace('"29":', ' ');ori = ori.replace('"30":', ' ');ori = ori.replace('"31":', ' ');ori = ori.replace('"32":', ' ');ori = ori.replace('"33":', ' ');ori = ori.replace('"34":', ' ');
      ori = ori.replace('"35":', ' ');ori = ori.replace('"36":', ' ');ori = ori.replace('"37":', ' ');ori = ori.replace('"38":', ' ');ori = ori.replace('"39":', ' ');ori = ori.replace('"40":', ' ');ori = ori.replace('"41":', ' ');ori = ori.replace('"42":', ' ');ori = ori.replace('"43":', ' ');ori = ori.replace('"44":', ' ');ori = ori.replace('"45":', ' ');
      ori = ori.replace('"46":', ' ');ori = ori.replace('"49":', ' ');ori = ori.replace('"50":', ' ');ori = ori.replace('"51":', ' ');ori = ori.replace('"52":', ' ');ori = ori.replace('"53":', ' ');ori = ori.replace('"54":', ' ');ori = ori.replace('"55":', ' ');ori = ori.replace('"56":', ' ');ori = ori.replace('"57":', ' ');ori = ori.replace('"57":', ' ');
      ori = ori.replace('"57":', ' ');ori = ori.replace('"58":', ' ');ori = ori.replace('"59":', ' ');ori = ori.replace('"60":', ' ');ori = ori.replace('"61":', ' ');ori = ori.replace('"62":', ' ');ori = ori.replace('"63":', ' ');ori = ori.replace('"64":', ' ');ori = ori.replace('"65":', ' ');ori = ori.replace('"66":', ' ');ori = ori.replace('"67":', ' ');
      ori = ori.replace('"68":', ' ');ori = ori.replace('"69":', ' ');ori = ori.replace('"70":', ' ');ori = ori.replace('"71":', ' ');ori = ori.replace('"72":', ' ');ori = ori.replace('"73":', ' ');ori = ori.replace('"74":', ' ');ori = ori.replace('"75":', ' ');ori = ori.replace('"76":', ' ');ori = ori.replace('"77":', ' ');ori = ori.replace('"78":', ' ');
      ori = ori.replace('"79":', ' ');ori = ori.replace('"80":', ' ');ori = ori.replace('"81":', ' ');ori = ori.replace('"82":', ' ');ori = ori.replace('"83":', ' ');ori = ori.replace('"84":', ' ');ori = ori.replace('"85":', ' ');ori = ori.replace('"86":', ' ');ori = ori.replace('"87":', ' ');ori = ori.replace('"88":', ' ');ori = ori.replace('"89":', ' ');
      ori = ori.replace('"90":', ' ');ori = ori.replace('"91":', ' ');ori = ori.replace('"92":', ' ');ori = ori.replace('"93":', ' ');ori = ori.replace('"94":', ' ');ori = ori.replace('"95":', ' ');ori = ori.replace('"96":', ' ');ori = ori.replace('"97":', ' ');ori = ori.replace('"98":', ' ');ori = ori.replace('"99":', ' ');ori = ori.replace('"100":', ' ');
      ori = ori.replace('"101":', ' ');ori = ori.replace('"102":', ' ');ori = ori.replace('"103":', ' ');ori = ori.replace('"104":', ' ');ori = ori.replace('"105":', ' ');ori = ori.replace('"406":', ' ');ori = ori.replace('"105":', ' ');ori = ori.replace('"406":', ' ');ori = ori.replace('"107":', ' ');ori = ori.replace('"108":', ' ');ori = ori.replace('"109":', ' ');
      ori = ori.replace('"110":', ' ');ori = ori.replace('"111":', ' ');ori = ori.replace('}}', '}]');;ori = ori.replace('","":', ' ');
      ori = ori.replace('"47":', ' ');ori = ori.replace('"48":', ' ');ori = ori.replace('"106":', ' ');ori = ori.replaceAll(',"', ', ');
      //ori = eval(ori)
  
      ori = eval(ori)