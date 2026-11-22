import numpy as np
import xatlas

vertices = np.ascontiguousarray([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
], dtype=np.float32)

faces = np.ascontiguousarray([
    [0, 1, 2],
], dtype=np.uint32)

normals = np.ascontiguousarray([
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0],
], dtype=np.float32)

atlas = xatlas.Atlas()

print("Before add_mesh", flush=True)

atlas.add_mesh(vertices, faces, normals)

print("After add_mesh", flush=True)