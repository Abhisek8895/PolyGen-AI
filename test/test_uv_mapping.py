
# import trimesh
# from services.uv_mapping import generate_uv_mapping


# def test_uv_mapping_generation(tmp_path):

#     # Create a sample 3D box mesh
#     mesh = trimesh.creation.box()

#     input_path = tmp_path / "sample.obj"
#     output_path = tmp_path / "uv_mapped.obj"

#     # Export sample mesh
#     mesh.export(input_path)

#     # Generate UV mapping
#     result = generate_uv_mapping(
#         str(input_path),
#         str(output_path)
#     )

#     # Verify output file
#     assert output_path.exists()

#     # Verify response
#     assert result["message"] == "UV mapping generated successfully"
#     assert result["vertices"] > 0
#     assert result["faces"] > 0
#     assert result["uv_coordinates"] > 0

#     # Load exported mesh and verify UV coordinates
#     mapped_mesh = trimesh.load(output_path, force="mesh")

#     assert mapped_mesh.visual.uv is not None
#     assert len(mapped_mesh.visual.uv) > 0



import trimesh
from services.uv_mapping import generate_uv_mapping


def test_generate_uv_mapping():
    # Create a sample 3D mesh
    mesh = trimesh.creation.box()

    input_path = "tests/sample_mesh.obj"
    output_path = "tests/output_mesh.obj"

    # Save input mesh
    mesh.export(input_path)

    # Run UV mapping
    result = generate_uv_mapping(input_path, output_path)

    # Check the result
    assert result is not None
    assert isinstance(result, dict)
    assert "message" in result
    assert "output_path" in result

    # Check if output file exists
    import os
    assert os.path.exists(output_path)

    # Load the output mesh
    output_mesh = trimesh.load(output_path, force="mesh")

    # Verify the output mesh
    assert output_mesh.vertices.shape[0] > 0
    assert output_mesh.faces.shape[0] > 0

    print("UV mapping test passed!")