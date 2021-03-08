#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DiagrammeR
Version  : 1.0.6.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/DiagrammeR_1.0.6.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DiagrammeR_1.0.6.1.tar.gz
Summary  : Graph/Network Visualization
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-RColorBrewer
Requires: R-downloader
Requires: R-dplyr
Requires: R-glue
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-igraph
Requires: R-influenceR
Requires: R-magrittr
Requires: R-purrr
Requires: R-readr
Requires: R-rlang
Requires: R-rstudioapi
Requires: R-scales
Requires: R-stringr
Requires: R-tibble
Requires: R-tidyr
Requires: R-viridis
Requires: R-visNetwork
Requires: R-webshot
BuildRequires : R-RColorBrewer
BuildRequires : R-downloader
BuildRequires : R-dplyr
BuildRequires : R-glue
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-igraph
BuildRequires : R-influenceR
BuildRequires : R-magrittr
BuildRequires : R-purrr
BuildRequires : R-readr
BuildRequires : R-rlang
BuildRequires : R-rstudioapi
BuildRequires : R-scales
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-viridis
BuildRequires : R-visNetwork
BuildRequires : R-webshot
BuildRequires : buildreq-R

%description
Build graph/network structures using functions for stepwise addition and
    deletion of nodes and edges. Work with data available in tables for bulk
    addition of nodes, edges, and associated metadata. Use graph selections
    and traversals to apply changes to specific nodes or edges. A wide
    selection of graph algorithms allow for the analysis of graphs. Visualize
    the graphs and take advantage of any aesthetic properties assigned to
    nodes and edges.

%prep
%setup -q -c -n DiagrammeR
cd %{_builddir}/DiagrammeR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615222059

%install
export SOURCE_DATE_EPOCH=1615222059
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DiagrammeR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DiagrammeR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DiagrammeR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc DiagrammeR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DiagrammeR/DESCRIPTION
/usr/lib64/R/library/DiagrammeR/INDEX
/usr/lib64/R/library/DiagrammeR/LICENSE
/usr/lib64/R/library/DiagrammeR/Meta/Rd.rds
/usr/lib64/R/library/DiagrammeR/Meta/data.rds
/usr/lib64/R/library/DiagrammeR/Meta/features.rds
/usr/lib64/R/library/DiagrammeR/Meta/hsearch.rds
/usr/lib64/R/library/DiagrammeR/Meta/links.rds
/usr/lib64/R/library/DiagrammeR/Meta/nsInfo.rds
/usr/lib64/R/library/DiagrammeR/Meta/package.rds
/usr/lib64/R/library/DiagrammeR/Meta/vignette.rds
/usr/lib64/R/library/DiagrammeR/NAMESPACE
/usr/lib64/R/library/DiagrammeR/NEWS.md
/usr/lib64/R/library/DiagrammeR/R/DiagrammeR
/usr/lib64/R/library/DiagrammeR/R/DiagrammeR.rdb
/usr/lib64/R/library/DiagrammeR/R/DiagrammeR.rdx
/usr/lib64/R/library/DiagrammeR/data/Rdata.rdb
/usr/lib64/R/library/DiagrammeR/data/Rdata.rds
/usr/lib64/R/library/DiagrammeR/data/Rdata.rdx
/usr/lib64/R/library/DiagrammeR/doc/graphviz-mermaid.R
/usr/lib64/R/library/DiagrammeR/doc/graphviz-mermaid.Rmd
/usr/lib64/R/library/DiagrammeR/doc/graphviz-mermaid.html
/usr/lib64/R/library/DiagrammeR/doc/index.html
/usr/lib64/R/library/DiagrammeR/doc/node-edge-data-frames.R
/usr/lib64/R/library/DiagrammeR/doc/node-edge-data-frames.Rmd
/usr/lib64/R/library/DiagrammeR/doc/node-edge-data-frames.html
/usr/lib64/R/library/DiagrammeR/doc/selections.R
/usr/lib64/R/library/DiagrammeR/doc/selections.Rmd
/usr/lib64/R/library/DiagrammeR/doc/selections.html
/usr/lib64/R/library/DiagrammeR/doc/simple-graphs-ndfs-edfs.R
/usr/lib64/R/library/DiagrammeR/doc/simple-graphs-ndfs-edfs.Rmd
/usr/lib64/R/library/DiagrammeR/doc/simple-graphs-ndfs-edfs.html
/usr/lib64/R/library/DiagrammeR/doc/traversals.R
/usr/lib64/R/library/DiagrammeR/doc/traversals.Rmd
/usr/lib64/R/library/DiagrammeR/doc/traversals.html
/usr/lib64/R/library/DiagrammeR/extdata/contributors.csv
/usr/lib64/R/library/DiagrammeR/extdata/currencies.csv
/usr/lib64/R/library/DiagrammeR/extdata/example_graphs_dgr/repository.dgr
/usr/lib64/R/library/DiagrammeR/extdata/karate.gml
/usr/lib64/R/library/DiagrammeR/extdata/neo4j_json_graph
/usr/lib64/R/library/DiagrammeR/extdata/projects.csv
/usr/lib64/R/library/DiagrammeR/extdata/projects_and_contributors.csv
/usr/lib64/R/library/DiagrammeR/extdata/usd_exchange_rates.csv
/usr/lib64/R/library/DiagrammeR/help/AnIndex
/usr/lib64/R/library/DiagrammeR/help/DiagrammeR.rdb
/usr/lib64/R/library/DiagrammeR/help/DiagrammeR.rdx
/usr/lib64/R/library/DiagrammeR/help/aliases.rds
/usr/lib64/R/library/DiagrammeR/help/paths.rds
/usr/lib64/R/library/DiagrammeR/html/00Index.html
/usr/lib64/R/library/DiagrammeR/html/R.css
/usr/lib64/R/library/DiagrammeR/htmlwidgets/DiagrammeR.js
/usr/lib64/R/library/DiagrammeR/htmlwidgets/DiagrammeR.yaml
/usr/lib64/R/library/DiagrammeR/htmlwidgets/grViz.js
/usr/lib64/R/library/DiagrammeR/htmlwidgets/grViz.yaml
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/chromatography/LICENSE
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/chromatography/chromatography.js
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/d3/LICENSE
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/d3/d3.min.js
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/dagre-d3/LICENSE
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/dagre-d3/dagre-d3.min.js
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/mermaid/LICENSE
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/mermaid/dist/mermaid.css
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/mermaid/dist/mermaid.slim.min.js
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/styles/styles.css
/usr/lib64/R/library/DiagrammeR/htmlwidgets/lib/viz/viz.js
/usr/lib64/R/library/DiagrammeR/tests/testthat.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-add_forward_reverse_edges.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-add_graphs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-add_node_edge.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-add_node_edge_df.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-add_nodes_edges_from_table.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-cache_attrs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-colorize_nodes_edges.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-combine_graphs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-copy_drop_mutate_recode_attrs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-count_entities.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-create_combine_edges.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-create_combine_nodes.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-create_graph.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-create_subgraph.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-degree_total_in_out.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-delete_node_edge.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-dfs_bfs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-generate_dot.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_aggregate_degree.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_cmty.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_graph_metrics.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_graph_properties.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_node_calculations.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_nodes_edges.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_paths.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-get_select_last_nodes_edges_created.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-graph_actions.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-graph_series.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-graph_validation.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-htmlwidgets.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-is_something_some_thing.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-join_attrs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-metagraph.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-mst.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-neighbors.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-node_edge_data_aes.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-node_edge_info.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-predecessors_successors.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-print.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-render_graph_series.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-rescale_node_edge_attrs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-selections.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-series_info.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-set_get_graph_attrs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-set_get_node_edge_attrs.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-set_node_edge_attr_to_display.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-set_node_positions.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-similarity_measures.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-spectools.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-transform_graph.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-traversals.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-traversals_copying_attr_vals.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-write_graph_backup.R
/usr/lib64/R/library/DiagrammeR/tests/testthat/test-x11_hex.R
