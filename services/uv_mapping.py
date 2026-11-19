import trimesh
import numpy as np


def generate_uv_mapping(input_path: str, output_path: str):

    # Load the 3D mesh
    mesh = trimesh.load(input_path, force="mesh")

    if not isinstance(mesh, trimesh.Trimesh):
        raise ValueError("Invalid 3D mesh")

    vertices = np.asarray(mesh.vertices, dtype=np.float32)
    faces = np.asarray(mesh.faces, dtype=np.uint32)

    # Validate mesh geometry
    if len(vertices) == 0 or len(faces) == 0:
        raise ValueError("Mesh contains no geometry")

    # Calculate planar UV projection using the two largest dimensions
    extent = np.ptp(vertices, axis=0)
    axes = np.argsort(extent)[-2:]

    uvs = vertices[:, axes].copy()

    # Normalize UV coordinates to 0–1
    minimum = uvs.min(axis=0)
    maximum = uvs.max(axis=0)

    size = maximum - minimum
    size[size == 0] = 1.0

    uvs = (uvs - minimum) / size
    uvs = uvs.astype(np.float32)

    # Reconstruct mesh with UV coordinates
    uv_mesh = trimesh.Trimesh(
        vertices=vertices,
        faces=faces,
        process=False
    )

    # Attach UV coordinates
    uv_mesh.visual = trimesh.visual.TextureVisuals(
        uv=uvs
    )

    # Export the UV-mapped mesh
    uv_mesh.export(output_path)

    return {
        "message": "UV mapping generated successfully",
        "output": output_path,
        "vertices": len(vertices),
        "faces": len(faces),
        "uv_coordinates": len(uvs)
    }