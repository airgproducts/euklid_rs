#!/usr/bin/env python3
# coding: utf-8

"""Unittest for vectors from the rust module euklid_rs"""
from typing import List
from euklid_rs.plane import Plane
from euklid_rs.vector import Vector2D, Vector3D

from .base import TestCase


class TestPlaneFunctions(TestCase):
    """Test euklid_rs.vector.Transformation rust module"""

    def setUp(self) -> None:
        self.r_p3d_p0 = Vector3D([2, 3, 4])
        self.r_p3d_v1 = Vector3D([-4, -3, -2])
        self.r_p3d_v2 = Vector3D([4, 5, 6])

        self.plane_r = Plane(self.r_p3d_p0, self.r_p3d_v1, self.r_p3d_v2)

    def test_plane_return_vectors_p0(self) -> None:
        """Test p0"""
        self.assert_almost_equal_vec(self.plane_r.p0, Vector3D([2, 3, 4]))

    def test_plane_return_x_vector(self) -> None:
        """Test x vector"""
        self.assert_almost_equal_vec(self.plane_r.x_vector, Vector3D([-4, -3, -2]))

    def test_plane_return_y_vector(self) -> None:
        """Test y vector"""
        self.assert_almost_equal_vec(self.plane_r.y_vector, Vector3D([4, 5, 6]))

    def test_plane_return_normvector(self) -> None:
        """Test plane normal"""
        self.assert_almost_equal_vec(self.plane_r.normvector, Vector3D([-8, 16, -8]))

    def test_plane_project(self) -> None:
        """Test projection"""
        self.assert_almost_equal_vec(
            self.plane_r.project(self.r_p3d_p0), Vector2D([0, 0])
        )

    def test_plane_align(self) -> None:
        """Test plane alignment"""

        def test_align_eq(vec1: List[float], vec2: Vector3D):
            v_1 = Vector2D(vec1)
            self.assert_almost_equal_vec(self.plane_r.align(v_1), vec2)

        test_align_eq([0, 0], self.r_p3d_p0)
