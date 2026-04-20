"""Geometry primitives and transformations for CadQuery.

This module provides Vector, Matrix, and Plane classes used throughout
CadQuery for geometric operations.
"""

import math
from typing import Union, Tuple, overload

from OCC.Core.gp import (
    gp_Vec,
    gp_Pnt,
    gp_Dir,
    gp_Ax1,
    gp_Ax2,
    gp_Ax3,
    gp_Trsf,
    gp_GTrsf,
    gp_XYZ,
)


class Vector:
    """A 3D vector with common mathematical operations.

    Wraps OCC gp_Vec for interoperability with OpenCASCADE.
    """

    def __init__(self, *args):
        if len(args) == 3:
            self._wrapped = gp_Vec(*args)
        elif len(args) == 1:
            if isinstance(args[0], gp_Vec):
                self._wrapped = args[0]
            elif isinstance(args[0], gp_Pnt):
                self._wrapped = gp_Vec(args[0].XYZ())
            elif isinstance(args[0], gp_XYZ):
                self._wrapped = gp_Vec(args[0])
            elif isinstance(args[0], (list, tuple)) and len(args[0]) == 3:
                self._wrapped = gp_Vec(*args[0])
            else:
                raise TypeError(f"Cannot create Vector from {type(args[0])}")
        elif len(args) == 2:
            # 2D vector, z=0
            self._wrapped = gp_Vec(args[0], args[1], 0)
        else:
            raise TypeError(f"Vector requires 1, 2, or 3 arguments, got {len(args)}")

    @property
    def x(self) -> float:
        return self._wrapped.X()

    @property
    def y(self) -> float:
        return self._wrapped.Y()

    @property
    def z(self) -> float:
        return self._wrapped.Z()

    def Length(self) -> float:
        """Return the magnitude of this vector."""
        return self._wrapped.Magnitude()

    def normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        return Vector(self._wrapped.Normalized())

    def dot(self, other: "Vector") -> float:
        """Dot product with another vector."""
        return self._wrapped.Dot(other._wrapped)

    def cross(self, other: "Vector") -> "Vector":
        """Cross product with another vector."""
        return Vector(self._wrapped.Crossed(other._wrapped))

    def toTuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def toPnt(self) -> gp_Pnt:
        return gp_Pnt(self._wrapped.XYZ())

    def toDir(self) -> gp_Dir:
        return gp_Dir(self._wrapped)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self._wrapped.Added(other._wrapped))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self._wrapped.Subtracted(other._wrapped))

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self._wrapped.Multiplied(scalar))

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    def __neg__(self) -> "Vector":
        return Vector(self._wrapped.Reversed())

    def __repr__(self) -> str:
        # Round to 4 decimal places for cleaner output when debugging
        return f"Vector({self.x:.4g}, {self.y:.4g}, {self.z:.4g})"

    def __eq__(self, other: "Vector", tol: float = 1e-9) -> bool:
        """Check equality within a small tolerance."""
        if not isinstance(other, Vector):
            return False
        return (abs(self.x - other.x) < tol and
                abs(self.y - other.y) < tol and
                abs(self.z - other.z) < tol)
