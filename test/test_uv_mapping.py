
import numpy as np
import pytest
import trimesh

from services.uv_mapping import generate_uv_mapping


def create_test_meshes():
    """Create sample 3D meshes for UV mapping tests."""
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
def test_uv_mapping_generation(mesh_name, tmp_path):
    """Test UV mapping generation for different 3D meshes."""

    # Step 1: Create sample mesh
    meshes = create_test_meshes()
    mesh = meshes[mesh_name]

    input_path = tmp_path / f"{mesh_name}.obj"
    output_path = tmp_path / f"mapped_{mesh_name}.obj"

    # Step 2: Export input mesh
    mesh.export(input_path)

    assert input_path.exists()

    # Step 3: Generate UV mapping
    result = generate_uv_mapping(
        str(input_path),
        str(output_path)
    )

    # Step 4: Verify output file
    assert output_path.exists()

    # Step 5: Verify function response
    assert result["message"] == "UV mapping generated successfully"
    assert result["output"] == str(output_path)
    assert result["vertices"] > 0
    assert result["faces"] > 0
    assert result["uv_coordinates"] > 0

    # Step 6: Inspect exported OBJ UV entries
    with open(output_path, "r", encoding="utf-8") as file:
        obj_content = file.readlines()

    uv_entries = [
        line for line in obj_content
        if line.startswith("vt ")
    ]

    assert len(uv_entries) > 0

    # Step 7: Reload exported mesh
    mapped_mesh = trimesh.load(
        output_path,
        force="mesh",
        process=False
    )

    # Step 8: Validate mesh geometry
    assert isinstance(mapped_mesh, trimesh.Trimesh)
    assert len(mapped_mesh.vertices) > 0
    assert len(mapped_mesh.faces) > 0

    # Step 9: Validate UV coordinates
    uv = mapped_mesh.visual.uv

    assert uv is not None
    assert uv.shape == (len(mapped_mesh.vertices), 2)
    assert np.all(np.isfinite(uv))

    # Step 10: Validate UV coordinate range
    assert np.all(uv >= -1e-5)
    assert np.all(uv <= 1.0 + 1e-5)

    print(f"\n{mesh_name.upper()} UV MAPPING TEST PASSED")
    print("Vertices:", len(mapped_mesh.vertices))
    print("Faces:", len(mapped_mesh.faces))
    print("UV coordinates:", len(uv))
    print("UV minimum:", uv.min(axis=0))
    print("UV maximum:", uv.max(axis=0))
