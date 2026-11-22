import trimesh
import numpy as np

print("Loading exported mesh...")

mesh = trimesh.load("mapped.obj", force="mesh")

print("Vertices:", len(mesh.vertices))
print("Faces:", len(mesh.faces))

if hasattr(mesh.visual, "uv") and mesh.visual.uv is not None:
    uvs = np.asarray(mesh.visual.uv)

    print("UV coordinates:", uvs.shape)
    print("UV minimum:", uvs.min(axis=0))
    print("UV maximum:", uvs.max(axis=0))

    print("UV validation successful!")
else:
    print("UV coordinates missing!")