from __future__ import annotations

from pathlib import Path
from typing import Any

from uqal_core.module_interface import (
    CapabilityManifest,
    ModuleManifest,
    UQALModule,
)

from .nodes import STDWithinNode, STIntersectsNode, STWithinNode
from .translator import PostGISTranslator
from . import native_validator


class PostGISExtension(UQALModule):
    """
    PostGIS extension for standard.postgresql.

    Adds ST_Within, ST_Intersects, ST_DWithin spatial conditions.
    Must be loaded alongside standard.postgresql — does not provide
    its own connection or execution.
    """

    def __init__(self) -> None:
        self._translator = PostGISTranslator()

    # ---- 1. Identity / grammar ----

    def get_manifest(self) -> ModuleManifest:
        return ModuleManifest(
            name="community.postgis",
            version="0.1.0",
            requires=["standard.postgresql"],
            is_extension=True,
        )

    def get_grammar_extension(self) -> str:
        ext_file = Path(__file__).parent / "grammar_extension.lark"
        if ext_file.exists():
            return ext_file.read_text(encoding="utf-8")
        return ""

    def get_capabilities(self) -> CapabilityManifest:
        return CapabilityManifest(
            module_name="community.postgis",
            grammar_extensions={
                "condition": ["postgis_condition"],
            },
            translatable_nodes=[
                "STWithinNode",
                "STIntersectsNode",
                "STDWithinNode",
            ],
        )

    def get_type_mapping(self) -> dict[str, Any]:
        return {}

    # ---- 2. Connection — not provided by extension ----

    def build_connection(self, config: Any) -> Any:
        raise NotImplementedError(
            "community.postgis is an extension — use standard.postgresql for connections"
        )

    def get_connection_schema(self) -> Any:
        raise NotImplementedError(
            "community.postgis is an extension — use standard.postgresql for connections"
        )

    # ---- 3. Translation ----

    def translate(self, node: Any) -> Any:
        return self._translator.translate(node)

    def validate_native_query(self, query: str) -> list[str]:
        return native_validator.security_check(query)

    # ---- Delegated to primary module ----

    def execute(self, native_query: Any, connection: Any) -> Any:
        raise NotImplementedError(
            "community.postgis is an extension — execution is handled by standard.postgresql"
        )

    def get_schema_store(self) -> Any:
        raise NotImplementedError(
            "community.postgis is an extension — schema is managed by standard.postgresql"
        )

    def sync_schema_from_source(self, connection: Any) -> Any:
        raise NotImplementedError(
            "community.postgis is an extension — schema sync is handled by standard.postgresql"
        )

    def create_view(self, view_name: str, aliases: list, returns: Any, connection: Any) -> str:
        raise NotImplementedError(
            "community.postgis is an extension — view creation is handled by standard.postgresql"
        )
