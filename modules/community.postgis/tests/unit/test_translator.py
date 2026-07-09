import pytest
from community_postgis.nodes import STDWithinNode, STIntersectsNode, STWithinNode
from community_postgis.translator import PostGISTranslator


@pytest.fixture
def translator():
    return PostGISTranslator()


# ── ST_Within ─────────────────────────────────────────────────────────────────

def test_st_within_generates_correct_sql(translator):
    node = STWithinNode(column="geom", polygon="POLYGON((0 0,1 0,1 1,0 0))")
    sql, params = translator.translate(node)
    assert "ST_Within(geom, %s)" in sql
    assert params == ("POLYGON((0 0,1 0,1 1,0 0))",)


def test_st_within_polygon_is_parameterised(translator):
    node = STWithinNode(column="location", polygon="POLYGON((5 5,6 5,6 6,5 5))")
    sql, params = translator.translate(node)
    assert "%s" in sql
    assert "POLYGON((5 5,6 5,6 6,5 5))" in params


def test_st_within_empty_column_raises(translator):
    with pytest.raises(ValueError, match="column"):
        translator.translate(STWithinNode(column="", polygon="POLYGON((0 0,1 0,1 1,0 0))"))


def test_st_within_none_polygon_raises(translator):
    with pytest.raises(ValueError, match="polygon"):
        translator.translate(STWithinNode(column="geom", polygon=None))


# ── ST_Intersects ─────────────────────────────────────────────────────────────

def test_st_intersects_generates_correct_sql(translator):
    node = STIntersectsNode(column="geom", polygon="POLYGON((0 0,10 0,10 10,0 0))")
    sql, params = translator.translate(node)
    assert "ST_Intersects(geom, %s)" in sql
    assert params[0] == "POLYGON((0 0,10 0,10 10,0 0))"


def test_st_intersects_empty_column_raises(translator):
    with pytest.raises(ValueError, match="column"):
        translator.translate(STIntersectsNode(column="", polygon="POLYGON((0 0,1 0,1 1,0 0))"))


def test_st_intersects_none_polygon_raises(translator):
    with pytest.raises(ValueError, match="polygon"):
        translator.translate(STIntersectsNode(column="geom", polygon=None))


# ── ST_DWithin ────────────────────────────────────────────────────────────────

def test_st_dwithin_generates_correct_sql(translator):
    node = STDWithinNode(column="geom", point="POINT(1 1)", distance=500.0)
    sql, params = translator.translate(node)
    assert "ST_DWithin(geom, %s, %s)" in sql
    assert params == ("POINT(1 1)", 500.0)


def test_st_dwithin_zero_distance_is_allowed(translator):
    node = STDWithinNode(column="geom", point="POINT(0 0)", distance=0)
    sql, params = translator.translate(node)
    assert "ST_DWithin" in sql


def test_st_dwithin_negative_distance_raises(translator):
    with pytest.raises(ValueError, match="distance"):
        translator.translate(STDWithinNode(column="geom", point="POINT(1 1)", distance=-1))


def test_st_dwithin_none_point_raises(translator):
    with pytest.raises(ValueError, match="point"):
        translator.translate(STDWithinNode(column="geom", point=None, distance=100))


# ── Unknown node ──────────────────────────────────────────────────────────────

def test_unknown_node_raises(translator):
    with pytest.raises(NotImplementedError):
        translator.translate(object())
