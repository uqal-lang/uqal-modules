from __future__ import annotations

from typing import Any

from .nodes import STDWithinNode, STIntersectsNode, STWithinNode


class PostGISTranslator:
    def translate(self, node: Any) -> tuple[str, tuple]:
        if isinstance(node, STWithinNode):
            return self._st_within(node)
        if isinstance(node, STIntersectsNode):
            return self._st_intersects(node)
        if isinstance(node, STDWithinNode):
            return self._st_dwithin(node)
        raise NotImplementedError(
            f"PostGISTranslator cannot translate {type(node).__name__}"
        )

    def _st_within(self, node: STWithinNode) -> tuple[str, tuple]:
        if not node.column:
            raise ValueError("ST_Within: column must not be empty")
        if node.polygon is None:
            raise ValueError("ST_Within: polygon must not be None")
        return f"ST_Within({node.column}, %s)", (node.polygon,)

    def _st_intersects(self, node: STIntersectsNode) -> tuple[str, tuple]:
        if not node.column:
            raise ValueError("ST_Intersects: column must not be empty")
        if node.polygon is None:
            raise ValueError("ST_Intersects: polygon must not be None")
        return f"ST_Intersects({node.column}, %s)", (node.polygon,)

    def _st_dwithin(self, node: STDWithinNode) -> tuple[str, tuple]:
        if not node.column:
            raise ValueError("ST_DWithin: column must not be empty")
        if node.point is None:
            raise ValueError("ST_DWithin: point must not be None")
        if node.distance < 0:
            raise ValueError("ST_DWithin: distance must not be negative")
        return f"ST_DWithin({node.column}, %s, %s)", (node.point, node.distance)
