import pytest
from community_postgis.nodes import STDWithinNode, STIntersectsNode, STWithinNode
from community_postgis.module import PostGISExtension


@pytest.fixture(scope="module")
def extension():
    return PostGISExtension()


# ── Grammar extension is provided ─────────────────────────────────────────────

def test_grammar_extension_is_not_empty(extension):
    grammar = extension.get_grammar_extension()
    assert grammar.strip() != ""


def test_grammar_extension_contains_st_within(extension):
    grammar = extension.get_grammar_extension()
    assert "ST_Within" in grammar


def test_grammar_extension_contains_st_intersects(extension):
    grammar = extension.get_grammar_extension()
    assert "ST_Intersects" in grammar


def test_grammar_extension_contains_st_dwithin(extension):
    grammar = extension.get_grammar_extension()
    assert "ST_DWithin" in grammar


# ── Capabilities ──────────────────────────────────────────────────────────────

def test_capabilities_declare_grammar_extensions(extension):
    caps = extension.get_capabilities()
    assert "condition" in caps.grammar_extensions


def test_capabilities_declare_translatable_nodes(extension):
    caps = extension.get_capabilities()
    assert "STWithinNode" in caps.translatable_nodes
    assert "STIntersectsNode" in caps.translatable_nodes
    assert "STDWithinNode" in caps.translatable_nodes


# ── Manifest ──────────────────────────────────────────────────────────────────

def test_manifest_name(extension):
    assert extension.get_manifest().name == "community.postgis"


def test_manifest_requires_postgresql(extension):
    assert "standard.postgresql" in extension.get_manifest().requires


# ── Extension methods raise NotImplementedError ───────────────────────────────

def test_build_connection_raises(extension):
    with pytest.raises(NotImplementedError):
        extension.build_connection(None)


def test_execute_raises(extension):
    with pytest.raises(NotImplementedError):
        extension.execute(None, None)


def test_get_schema_store_raises(extension):
    with pytest.raises(NotImplementedError):
        extension.get_schema_store()
