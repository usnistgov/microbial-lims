---
hide:
  - toc
---
<!-- this HTML will load the schema visualization within the mkdocs framework,
     so the formatting stays consistent
 -->
<link rel="stylesheet" href="../style.css">
<!-- Adapted from the Biolink schema visualization: 
        https://biolink.github.io/biolink-model/categories.html 
        https://github.com/biolink/biolink-model/blob/master/src/docs/d3_viz.js
-->
    
<!-- load the d3.js library -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js"></script>
<script src="../d3_viz.js"></script>
<svg id="d3_legend" height=26 width=400></svg>
<svg id="d3_figure" style="height: 2000 !important; max-width: max-content"></svg>
<!-- create a simple legend for slot colors -->
<script>
    // select the svg area
    var svg = d3.select("#d3_legend")
    var left_margin = 20;
    svg.append("g").attr("class", "node").append("text").attr("x", left_margin).attr("y", 20).text("Color legend: ").attr("alignment-baseline", "middle").style("font-weight", "bold")
    var x_1 = left_margin + 100
    var g1 = svg.append("g").attr("class", "node")
        g1.append("circle").attr("cx", x_1).attr("cy", 20).attr("r", 3).style("fill", "#555")
        g1.append("text").attr("x", x_1 + 10).attr("y", 20).text("owned slot").attr("alignment-baseline","middle").attr("class", "slot")
    var x_2 = x_1 + 90
    var g2 = svg.append("g").attr("class", "node")
        g2.append("circle").attr("cx", x_2).attr("cy", 20).attr("r", 3).style("fill", "#555")
        g2.append("text").attr("x", x_2 + 10).attr("y", 20).text("inherited slot (OriginClass)").attr("alignment-baseline","middle").attr("class", "inherited-slot")
</script>
<script>
    var svg = d3.select("#d3_figure")
    generateD3Tree(
        "../schema_visualization.json", 
        {top: 10, right: 10, bottom: 10, left: 145}, 
        svg
    );
</script>
