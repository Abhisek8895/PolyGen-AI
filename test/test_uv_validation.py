
import os
import tempfile

import numpy as np
import pytest
import trimesh

from services.uv_mapping import generate_uv_mapping


def create_test_meshes():
    return {
        "cube": trimesh.creation.box(),
        "sphere": trimesh.creation.icosphere(subdivisions=2),
        "cylinder": trimesh.creation.cylinder(
            radius=1.0,
            height=2.0,
            sections=32
        )
    }


@pytest.mark.parametrize(
    "mesh_name",
    ["cube", "sphere", "cylinder"]
)
def test_uv_mapping(mesh_name):

    meshes = create_test_meshes()

    with tempfile.TemporaryDirectory() as temp_dir:

        input_path = os.path.join(temp_dir, f"{mesh_name}.obj")
        output_path = os.path.join(
            temp_dir, f"mapped_{mesh_name}.obj"
        )

        # Step 1: Export input mesh
        meshes[mesh_name].export(input_path)

        # Step 2: Generate UV mapping
        result = generate_uv_mapping(input_path, output_path)

        assert os.path.exists(output_path)
        assert result["uv_coordinates"] > 0

        # Step 3: Load exported OBJ
        mapped_mesh = trimesh.load(
            output_path,
            force="mesh"
        )

        # Step 4: Validate geometry
        assert isinstance(mapped_mesh, trimesh.Trimesh)
        assert len(mapped_mesh.vertices) > 0
        assert len(mapped_mesh.faces) > 0

        # Step 5: Validate face indices
        assert mapped_mesh.faces.min() >= 0
        assert mapped_mesh.faces.max() < len(mapped_mesh.vertices)

        # Step 6: Validate UV coordinates
        uv = mapped_mesh.visual.uv

        assert uv is not None
        assert uv.shape == (len(mapped_mesh.vertices), 2)
        assert np.all(np.isfinite(uv))

        # Step 7: Validate UV range
        assert np.all(uv >= -1e-5)
        assert np.all(uv <= 1.0 + 1e-5)

        print(f"\n{mesh_name.upper()} TEST PASSED")
        print("Vertices:", len(mapped_mesh.vertices))
        print("Faces:", len(mapped_mesh.faces))
        print("UV shape:", uv.shape)
        print("UV minimum:", uv.min(axis=0))
        print("UV maximum:", uv.max(axis=0))
