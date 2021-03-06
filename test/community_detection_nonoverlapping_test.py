import networkx as nx

from karateclub.community_detection.non_overlapping import EdMot, LabelPropagation, SCD, GEMSEC

def test_edmot():
    """
    Test the EdMot procedure.
    """
    graph = nx.newman_watts_strogatz_graph(50, 5, 0.3)

    model = EdMot()

    model.fit(graph)
    memberships = model.get_memberships()
    
    indices = [k for k, v in memberships.items()].sort()
    nodes = [node for node in graph.nodes()].sort()

    assert graph.number_of_nodes() == len(memberships)
    assert indices == nodes


def test_label_propagation():
    """
    Test Label Propagation procedure.
    """
    graph = nx.newman_watts_strogatz_graph(50, 5, 0.3)

    model = LabelPropagation()

    model.fit(graph)
    memberships = model.get_memberships()
    
    indices = [k for k, v in memberships.items()].sort()
    nodes = [node for node in graph.nodes()].sort()

    assert graph.number_of_nodes() == len(memberships)
    assert indices == nodes


def test_scd():
    """
    Test the SCD procedure.
    """
    graph = nx.newman_watts_strogatz_graph(50, 5, 0.3)

    model = SCD()

    model.fit(graph)
    memberships = model.get_memberships()
    
    indices = [k for k, v in memberships.items()].sort()
    nodes = [node for node in graph.nodes()].sort()

    assert graph.number_of_nodes() == len(memberships)
    assert indices == nodes


def test_GEMSEC():
    """
    Test the GEMSEC procedure.
    """
    graph = nx.newman_watts_strogatz_graph(100, 5, 0.3)

    model = GEMSEC()

    model.fit(graph)
    memberships = model.get_memberships()
    
    indices = [k for k, v in memberships.items()].sort()
    nodes = [node for node in graph.nodes()].sort()

    assert graph.number_of_nodes() == len(memberships)
    assert indices == nodes

    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == model.dimensions
