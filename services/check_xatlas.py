import trimesh
import numpy as np
import xatlas

mesh = trimesh.creation.box()

vertices = np.ascontiguousarray(
    mesh.vertices, dtype=np.float32
)

faces = np.ascontiguousarray(
    mesh.faces, dtype=np.uint32
)

print("Starting xatlas test...", flush=True)

vmapping, indices, uvs = xatlas.parametrize(
    vertices, faces
)

print("UV generation successful!", flush=True)
print("Vertices:", len(vmapping))
print("Faces:", len(indices))
print("UV coordinates:", len(uvs))