"""CadQuery - A parametric 3D CAD scripting framework built on top of OCCT.

CadQuery is an intuitive, easy-to-use Python module for building 3D CAD models.
It is well-suited for building models that are difficult to construct manually
or that require many iterations to get right.

Example usage::

    import cadquery as cq

    result = (
        cq.Workplane("XY")
        .box(10, 10, 10)
        .faces(">Z")
        .hole(5)
    )

Note: This is a personal fork. Upstream: https://github.com/CadQuery/cadquery
"""

from .cq import CQContext, CQ, Workplane
from .occ_impl.geom import Vector, Matrix, Plane, BoundBox
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from .occ_impl.exporters import exporters
from .assembly import Assembly, ConstraintKind
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    RadiusNthSelector,
    CenterNthSelector,
    DirectionNthSelector,
    LengthNthSelector,
    AreaNthSelector,
    BinarySelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from .sketch import Sketch

__version__ = "2.4.0"

__all__ = [
    "__version__",
    # Core workplane
    "CQContext",
    "CQ",
    "Workplane",
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "BoundBox",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    # Exporters
    "exporters",
    # Assembly
    "Assembly",
    "ConstraintKind",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "DirectionNthSelector",
    "LengthNthSelector",
    "AreaNthSelector",
    "BinarySelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Sketch
    "Sketch",
]
