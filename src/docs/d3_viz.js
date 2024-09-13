async function generateD3Tree(jsonFile, marginSettings, svg_figure) {
    const treeData = await d3.json(jsonFile);

    const root = d3.hierarchy(treeData[0])

    var margin = marginSettings;
    
    // Specify the charts’ dimensions. The height is variable, depending on the layout.
    const width = 1600 - margin.right - margin.left;

    // Rows are separated by dx pixels, columns by dy pixels. These names can be counter-intuitive
    // (dx is a height, and dy a width). This because the tree must be viewed with the root at the
    // “bottom”, in the data domain. The width of a column is based on the tree’s height.
    const dx = 13;
    const dy = (width - 2 * (margin.right + margin.left)) / (1 + root.height);
    
    // Define the tree layout and the shape for links.
    const tree = d3.tree().nodeSize([dx, dy]);
    const diagonal = d3.linkHorizontal().x(d => d.y).y(d => d.x);

    const svg = svg_figure
        .attr("width", width)
        .attr("height", dx)
        .attr("viewBox", [-margin.left, -margin.top, width, dx])
        .attr("style", `height: auto; max-width: 100%; min-width: ${width}; font: 12px sans-serif; user-select: none;`);

    const gLink = svg.append("g")
        .attr("fill", "none")
        .attr("stroke", "#555")
        .attr("stroke-opacity", 0.4)
        .attr("stroke-width", 1.5);

    const gNode = svg.append("g")
        .attr("cursor", "pointer")
        .attr("pointer-events", "all");

    function update(event, source) {
        const duration = 750;
        const nodes = root.descendants().reverse();
        const links = root.links();

        // Compute the new tree layout.
        tree(root);

        let left = root;
        let right = root;
        root.eachBefore(node => {
          if (node.x < left.x) left = node;
          if (node.x > right.x) right = node;
        });

        const height = right.x - left.x + margin.top + margin.bottom;

        const transition = svg.transition()
            .duration(duration)
            .attr("height", height)
            // .attr("viewBox", [-margin.left, left.x - margin.top, width, height])
            // .tween("resize", window.ResizeObserver ? null : () => () => svg.dispatch("toggle"));

        // Update the nodes…
        const node = gNode.selectAll("g")
                          .data(nodes, d => d.id);

        // Enter any new nodes at the parent's previous position.
        const nodeEnter = node.enter().append("g")
            .classed("node", true)
            .attr("transform", d => `translate(${source.y0},${source.x0})`)
            .attr("fill-opacity", 0)
            .attr("stroke-opacity", 0)
            .on("click", (event, d) => {
                d.children = d.children ? null : d._children;
                update(event, d);
            });

        nodeEnter.append("circle")
            .attr("r", 2.5)
            .attr("fill", d => d._children ? "#9a9a9a" : "#555")
            .attr("stroke-width", 10);
    
        function set_link_and_style(d) {
            const node = d3.select(this);
            let nodeName = d.data.name;

            // slot names should be snakecase followed by space and a class name in parentheses
            let re = new RegExp("([a-z_]+)( )(\(.*\))");
                
            // if matched, then this is an inherited slot so link should be just to the first group
            let matched = re.exec(nodeName);
            let linkName = matched ? matched[1] : nodeName
            linkName = `../${linkName}`
            linkText = matched ? " (slot doc)" : " (class doc)"   

            // add styling for slots
            if ( matched ) {
                node.classed("inherited-slot", true)
            } else {
                // test if this is still a slot, but not inherited
                if ( /^[a-z_]+$/.exec(nodeName) ) {
                    node.classed("slot", true);
                    linkText = " (slot doc)";
                }
                else {
                    node.classed("class-name", true)
                }
            }

            node.append("a")
                .classed("md-link", true)  // Class for styling
                .attr("xlink:href", linkName)  // Set the hyperlink reference
                .text(linkText);
        }

        nodeEnter.append("text")
            .attr("dy", "0.5em")
            .attr("x", d => d._children ? -6 : 6)
            .attr("text-anchor", d => d._children ? "end" : "start")
            .text(d => d.data.name)
            .each(set_link_and_style);

        // Transition nodes to their new position.
        const nodeUpdate = node.merge(nodeEnter).transition(transition)
            .attr("transform", d => `translate(${d.y},${d.x})`)
            .attr("fill-opacity", 1)
            .attr("stroke-opacity", 1);

        // Transition exiting nodes to the parent's new position.
        const nodeExit = node.exit().transition(transition).remove()
            .attr("transform", d => `translate(${source.y},${source.x})`)
            .attr("fill-opacity", 0)
            .attr("stroke-opacity", 0);

        // Update the links…
        const link = gLink.selectAll("path")
            .data(links, d => d.target.id);

        // Enter any new links at the parent's previous position.
        const linkEnter = link.enter().append("path")
            .attr("d", d => {
                const o = {x: source.x0, y: source.y0};
                return diagonal({source: o, target: o});
            });

        // Transition links to their new position.
        link.merge(linkEnter).transition(transition)
            .attr("d", diagonal);

        // Transition exiting nodes to the parent's new position.
        link.exit().transition(transition).remove()
            .attr("d", d => {
            const o = {x: source.x, y: source.y};
            return diagonal({source: o, target: o});
            });

        // Stash the old positions for transition.
        root.eachBefore(d => {
            d.x0 = d.x;
            d.y0 = d.y;
        });
    }

    // Do the first update to the initial configuration of the tree
    root.x0 = dy / 2;
    root.y0 = 0;
    root.descendants().forEach((d, i) => {
        d.id = i;
        d._children = d.children;
    });    

    update(null, root);
}