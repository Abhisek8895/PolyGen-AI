
import trimesh
import xatlas
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

    # Initialize UV atlas
    atlas = xatlas.Atlas()

    # Add mesh to atlas
    atlas.add_mesh(vertices, faces)

    # Generate UV coordinates
    atlas.generate()

    # Extract generated UV data
    vmapping, indices, uvs = atlas[0]

    # Reconstruct mesh using UV mapping
    mapped_vertices = vertices[vmapping]

    uv_mesh = trimesh.Trimesh(
        vertices=mapped_vertices,
        faces=indices,
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
        "vertices": len(mapped_vertices),
        "faces": len(indices),
        "uv_coordinates": len(uvs)
    }
