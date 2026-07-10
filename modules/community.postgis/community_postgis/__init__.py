from .module import PostGISExtension
from .nodes import STDWithinNode, STIntersectsNode, STWithinNode

# ── Transformer handlers ───────────────────────────────────────────────────────
# Convert grammar rule children into typed PostGIS AST nodes.
# Called by UQALTransformer.__default__ for unrecognised grammar rules.

from uqal_core.ast.module_nodes import register_node_handler


def _handle_st_within(children):
    return STWithinNode(
        column=str(children[0]),
        polygon=children[1].value,
    )


def _handle_st_intersects(children):
    return STIntersectsNode(
        column=str(children[0]),
        polygon=children[1].value,
    )


def _handle_st_dwithin(children):
    return STDWithinNode(
        column=str(children[0]),
        point=children[1].value,
        distance=float(children[2]),
    )


register_node_handler("st_within", _handle_st_within)
register_node_handler("st_intersects", _handle_st_intersects)
register_node_handler("st_dwithin", _handle_st_dwithin)
register_node_handler("postgis_condition", lambda children: children[0])

# ── Condition SQL builders ─────────────────────────────────────────────────────
# Tell the PostgreSQL translator how to render PostGIS conditions in WHERE clauses.

from uqal_core.ast.condition_registry import register_condition_builder

register_condition_builder(
    STWithinNode,
    lambda node: (f"ST_Within({node.column}, ST_GeomFromText(%s, 4326))", (node.polygon,)),
)
register_condition_builder(
    STIntersectsNode,
    lambda node: (f"ST_Intersects({node.column}, ST_GeomFromText(%s, 4326))", (node.polygon,)),
)
register_condition_builder(
    STDWithinNode,
    lambda node: (f"ST_DWithin({node.column}, ST_GeomFromText(%s, 4326), %s)", (node.point, node.distance)),
)

__version__ = "0.1.0"
__all__ = ["PostGISExtension"]
