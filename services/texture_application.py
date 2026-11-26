
import os

import numpy as np
import trimesh
from PIL import Image


def apply_texture(
    input_path: str,
    texture_path: str,
    output_path: str
):
    """
    Apply a texture image to a UV-mapped 3D mesh
    and export the textured model as a GLB file.
    """

    # Step 1: Validate input files
    if not os.path.isfile(input_path):
        raise FileNotFoundError(
            f"3D model not found: {input_path}"
        )

    if not os.path.isfile(texture_path):
        raise FileNotFoundError(
            f"Texture image not found: {texture_path}"
        )

    # Step 2: Load 3D mesh
    mesh = trimesh.load(input_path, force="mesh")

    if not isinstance(mesh, trimesh.Trimesh):
        raise ValueError("Invalid 3D mesh")

    if len(mesh.vertices) == 0 or len(mesh.faces) == 0:
        raise ValueError("Mesh contains no geometry")

    # Step 3: Validate UV coordinates
    if not hasattr(mesh.visual, "uv") or mesh.visual.uv is None:
        raise ValueError(
            "Mesh does not contain UV coordinates"
        )

    uv_coordinates = np.asarray(
        mesh.visual.uv,
        dtype=np.float32
    )

    if uv_coordinates.shape != (len(mesh.vertices), 2):
        raise ValueError(
            "Invalid UV coordinate dimensions"
        )

    if not np.isfinite(uv_coordinates).all():
        raise ValueError(
            "UV coordinates contain invalid values"
        )

    # Step 4: Load texture image
    try:
        texture_image = Image.open(texture_path).convert("RGBA")
    except Exception as error:
        raise ValueError(
            f"Unable to load texture image: {error}"
        ) from error

    # Step 5: Create PBR material
    material = trimesh.visual.material.PBRMaterial(
        baseColorTexture=texture_image,
        metallicFactor=0.0,
        roughnessFactor=0.8
    )

    # Step 6: Apply texture to mesh
    mesh.visual = trimesh.visual.TextureVisuals(
        uv=uv_coordinates,
        material=material
    )

    # Step 7: Export textured model
    output_directory = os.path.dirname(output_path)

    if output_directory:
        os.makedirs(output_directory, exist_ok=True)

    mesh.export(output_path, file_type="glb")

    return {
        "message": "Texture applied successfully",
        "output": output_path,
        "vertices": len(mesh.vertices),
        "faces": len(mesh.faces),
        "texture_width": texture_image.width,
        "texture_height": texture_image.height
    }
