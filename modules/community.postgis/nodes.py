from __future__ import annotations
from dataclasses import dataclass


@dataclass
class STWithinNode:
    column: str
    polygon: str


@dataclass
class STIntersectsNode:
    column: str
    polygon: str


@dataclass
class STDWithinNode:
    column: str
    point: str
    distance: float
