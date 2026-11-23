import trimesh
import numpy as np
import xatlas


def generate_uv_mapping(input_path: str, output_path: str):

    print("Step 1: Loading mesh...", flush=True)
    mesh = trimesh.load(input_path, force="mesh")

    print("Step 2: Validating mesh...", flush=True)
    if not isinstance(mesh, trimesh.Trimesh):
        raise ValueError("Invalid 3D mesh")

    vertices = np.asarray(mesh.vertices, dtype=np.float32)
    faces = np.asarray(mesh.faces, dtype=np.uint32)

    if len(vertices) == 0 or len(faces) == 0:
        raise ValueError("Mesh contains no geometry")

    # Ensure arrays are contiguous
    vertices = np.ascontiguousarray(vertices, dtype=np.float32)
    faces = np.ascontiguousarray(faces, dtype=np.uint32)

    print("Vertices shape:", vertices.shape, flush=True)
    print("Faces shape:", faces.shape, flush=True)

    print("Step 3: Starting UV parametrization...", flush=True)

    vmapping, indices, uvs = xatlas.parametrize(vertices, faces)

    print("Step 4: UV parametrization completed!", flush=True)

    # Reconstruct mesh using generated vertex mapping
    mapped_vertices = vertices[vmapping]
    mapped_faces = np.asarray(indices, dtype=np.uint32).reshape(-1, 3)

    print("Step 5: Reconstructing mesh...", flush=True)

    uv_mesh = trimesh.Trimesh(
        vertices=mapped_vertices,
        faces=mapped_faces,
        process=False
    )

    # Attach generated UV coordinates
    uv_mesh.visual = trimesh.visual.TextureVisuals(
    uv=np.asarray(uvs, dtype=np.float32),
    material=trimesh.visual.material.SimpleMaterial()
)

    print("Step 6: Exporting mesh...", flush=True)

    uv_mesh.export(
    output_path,
    include_texture=True
)

    print("Step 7: UV mapping completed!", flush=True)

    return {
        "message": "UV mapping generated successfully",
        "output": output_path,
        "vertices": len(mapped_vertices),
        "faces": len(mapped_faces),
        "uv_coordinates": len(uvs)
    }
