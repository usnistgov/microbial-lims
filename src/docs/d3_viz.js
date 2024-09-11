function generateD3Tree(jsonFile, marginSettings, svg_figure) {
    d3.json(jsonFile, function (error, jsonData) {
        if (error) {
            console.log("Error loading JSON data:", error);
            return;
        }
        var treeData = jsonData;

        var margin = marginSettings,
            width = 1200 - margin.right - margin.left,
            height = 2000 - margin.top - margin.bottom;

        var i = 0,
            duration = 750,
            root;

        var tree = d3.layout.cluster()
            .size([height, width]);

        var diagonal = d3.svg.diagonal()
            .projection(function (d) {
                return [d.y, d.x];
            });

        var svg = svg_figure
            .attr("width", width + margin.right + margin.left)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        root = treeData[0];
        root.x0 = height / 2;
        root.y0 = 0;

        update(root);

        d3.select(self.frameElement).style("height", "500px");

        function toCamelCase(str) {
            return str.replace(/([-_][a-z])/g, (group) => group.toUpperCase()
                .replace('-', '')
                .replace('_', ''))
                .replace(/^[a-z]/, (group) => group.toUpperCase());
        }

        function update(source) {

            // Compute the new tree layout.
            var nodes = tree.nodes(root).reverse(),
                links = tree.links(nodes);

            // Normalize for fixed-depth.
            nodes.forEach(function (d) {
                d.y = d.depth * 186;
            });

            // Update the nodes…
            var node = svg.selectAll("g.node")
                .data(nodes, function (d) {
                    return d.id || (d.id = ++i);
                });

            // Enter any new nodes at the parent's previous position.
            var nodeEnter = node.enter().append("g")
                .classed("node", true)
                .attr("transform", function (d) {
                    return "translate(" + source.y0 + "," + source.x0 + ")";
                })
                .on("click", click);

            nodeEnter.append("circle")
                .attr("r", 1e-6)
                .style("fill", function (d) {
                    return d._children ? "#9a9a9a" : "#555";
                });

            nodeEnter.append("text")
                .attr("x", function (d) {
                    return d.children || d._children ? -6 : 6;
                })
                .attr("dy", ".35em")
                .attr("text-anchor", function (d) {
                    return d.children || d._children ? "end" : "start";
                })
                .text(function (d) {
                    return d.name;
                })
                .each(function (d) {
                    var nodeText = d3.select(this);
                    nodeText.text(d.name);

                    // Append an anchor tag to nodeText
                    let nodeName = d.name;
                    let linkName;
                    // slot names should be snakecase followed by space and a class name in parentheses
                    let re = new RegExp("([a-z_]+)( )(\(.*\))");

                    // if matched, then this is an inherited slot so link should be just to the first group
                    let matched = re.exec(nodeName);
                    linkName = matched ? matched[1] : nodeName
                    linkName = `../${linkName}`
                    linkText = matched ? " (slot doc)" : " (class doc)"

                    // add styling for slots
                    if ( matched ) {
                        nodeText.classed("inherited-slot", true)
                    } else {
                        // test if this is still a slot, but not inherited
                        if ( /^[a-z_]+$/.exec(nodeName) ) {
                            nodeText.classed("slot", true);
                            linkText = " (slot doc)";
                        }
                        else {
                            nodeText.classed("class-name", true)
                        }
                    }

                    nodeText.append("a")
                        .classed("md-link", true)  // Class for styling
                        .attr("xlink:href", linkName)  // Set the hyperlink reference
                        .text(linkText);
                })
                .style("fill-opacity", 1e-6);
            // Transition nodes to their new position.
            var nodeUpdate = node.transition()
                .duration(duration)
                .attr("transform", function (d) {
                    return "translate(" + d.y + "," + d.x + ")";
                });

            nodeUpdate.select("circle")
                .attr("r", 3)
                .style("fill", function (d) {
                    return d._children ? "#9a9a9a" : "#555";
                });

            nodeUpdate.select("text")
                .style("fill-opacity", 1);

            // Transition exiting nodes to the parent's new position.
            var nodeExit = node.exit().transition()
                .duration(duration)
                .attr("transform", function (d) {
                    return "translate(" + source.y + "," + source.x + ")";
                })
                .remove();

            nodeExit.select("circle")
                .attr("r", 1e-6)
                .remove();

            nodeExit.select("text")
                .style("fill-opacity", 1e-6)
                .remove();

            // Update the links…
            var link = svg.selectAll("path.link")
                .data(links, function (d) {
                    return d.target.id;
                });

            // Enter any new links at the parent's previous position.
            link.enter().insert("path", "g")
                .attr("class", "link")
                .attr("d", function (d) {
                    var o = {x: source.x0, y: source.y0};
                    return diagonal({source: o, target: o});
                });

            // Transition links to their new position.
            link.transition()
                .duration(duration)
                .attr("d", diagonal);

            // Transition exiting nodes to the parent's new position.
            link.exit().transition()
                .duration(duration)
                .attr("d", function (d) {
                    var o = {x: source.x, y: source.y};
                    return diagonal({source: o, target: o});
                })
                .remove();

            // Stash the old positions for transition.
            nodes.forEach(function (d) {
                d.x0 = d.x;
                d.y0 = d.y;
            });
        }

        // Toggle children on click.
        function click(d) {
            if (d.children) {
                d._children = d.children;
                d.children = null;
            } else {
                d.children = d._children;
                d._children = null;
            }
            update(d);
        }

        // Define other shared functions like update, click, etc. here
    });
}