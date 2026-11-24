# PolyGen – Generative Text-to-3D Asset Pipeline

PolyGen is an AI-powered text-to-3D asset generation system designed to simplify 3D asset creation for gaming, virtual reality (VR), and metaverse environments.

The system aims to transform natural-language text prompts into optimized, textured 3D models through a multi-stage generative AI pipeline. It combines 3D generation models, AI-based texture synthesis, mesh processing, and interactive 3D visualization.

## Project Objectives

- Generate 3D assets from natural-language text prompts.
- Generate and apply realistic textures using Stable Diffusion and ControlNet.
- Automatically UV-unwrap and process generated 3D meshes.
- Optimize mesh geometry using Quadric Error Metrics (QEM) decimation.
- Support Physically Based Rendering (PBR) materials.
- Provide an interactive 3D model viewer.
- Export generated assets in GLB/GLTF formats for use in game engines such as Unreal Engine and Unity.

## Proposed System Architecture

1. **Text Prompt Input:** Accept user descriptions of desired 3D assets.
2. **3D Mesh Generation:** Generate raw 3D geometry using Shap-E or TripoSR.
3. **Texture Synthesis:** Generate textures using Stable Diffusion and ControlNet.
4. **UV Mapping:** Generate UV coordinates to prepare meshes for texture application.
5. **Mesh Optimization:** Clean and simplify geometry using Trimesh and Open3D.
6. **PBR Material Application:** Apply base color, roughness, metalness, and normal maps.
7. **3D Visualization:** Display generated assets in an interactive 3D viewer.
8. **Asset Export:** Export the final optimized model in GLB/GLTF format.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| 3D Generation | Shap-E / TripoSR |
| Deep Learning | PyTorch |
| Texture Generation | Stable Diffusion |
| Conditioning | ControlNet |
| Diffusion Integration | Hugging Face Diffusers |
| Mesh Processing | Trimesh, Open3D |
| UV Mapping | xatlas, NumPy |
| Mesh Decimation | Quadric Error Metrics (QEM) |
| Backend | FastAPI |
| Frontend | React / Streamlit (to be finalized) |
| 3D Rendering | Three.js / PyVista (to be finalized) |
| React 3D Integration | React Three Fiber (if React is selected) |
| Export Formats | OBJ, GLB, GLTF |
| Version Control | Git and GitHub |

## Development Roadmap

The project is planned over four weeks.

### Week 1 – Backend Foundation

- Created and configured the GitHub repository with the `main` branch.
- Set up the Python virtual environment and installed dependencies.
- Initialized the FastAPI backend structure.
- Implemented the root (`/`) and health-check (`/api/v1/health`) endpoints.
- Configured Pytest and implemented automated API tests.
- Successfully executed both API test cases.

**Status: Completed**

### Week 2 – UV Mapping and AI-Based Texturing

**Automatic UV Mapping**

- Implemented mesh loading and geometry validation using Trimesh.
- Added vertex and face extraction using NumPy.
- Integrated xatlas for automatic UV atlas generation.
- Reconstructed meshes using generated vertex mappings and indices.
- Attached generated UV coordinates to the processed mesh.
- Implemented OBJ export with UV information.
- Tested UV mapping with different mesh geometries, including cubes, spheres, and cylinders.
- Verified exported OBJ files, UV coordinate shapes, and coordinate ranges.
- Created automated UV mapping validation tests using Pytest.
- Successfully passed all three UV mapping tests.

**AI-Based Texturing (Upcoming)**

- Integrate Stable Diffusion and ControlNet.
- Generate geometry-guided textures.
- Apply generated textures to UV-mapped meshes.
- Validate texture quality and mapping.

**Status: UV Mapping Completed and Validated | AI-Based Texturing Pending**

### Week 3 – Mesh Optimization and PBR Materials

- Inspect and clean generated meshes.
- Implement QEM-based polygon decimation.
- Optimize dense meshes for real-time rendering.
- Generate and apply PBR material maps.
- Validate optimized geometry and rendering quality.

**Status: Pending**

### Week 4 – Integration and Export

- Implement GLB/GLTF export.
- Develop the PolyGen dashboard.
- Integrate the interactive 3D viewer.
- Implement environment lighting.
- Integrate the complete generation pipeline.
- Perform final testing and documentation.

**Status: Pending**

## Current Implementation

### 1. FastAPI Backend

The initial backend foundation has been implemented with:

- FastAPI application initialization.
- Root endpoint (`/`).
- Health-check endpoint (`/api/v1/health`).
- Automated API testing using Pytest.

### 2. Automatic UV Mapping Module

The UV mapping service has been implemented using Python, Trimesh, NumPy, and xatlas.

The module provides the following functionality:

- Loads 3D mesh files.
- Validates mesh geometry.
- Extracts vertices and faces.
- Generates UV coordinates through xatlas.
- Reconstructs the mesh using generated vertex mappings.
- Attaches UV coordinates to the reconstructed mesh.
- Exports the UV-mapped mesh in OBJ format.

**Validation Results**

| Test Mesh | Validation |
|---|---|
| Cube | Passed |
| Sphere | Passed |
| Cylinder | Passed |
| Automated UV Tests | 3 Passed |

The exported meshes were successfully loaded and checked for valid geometry, UV coordinate availability, finite values, and expected UV coordinate ranges.

## Project Status

- **Status:** Week 2 – UV Mapping Completed; AI-Based Texturing Next
- **Development Duration:** 28 Days
- **Project Type:** Individual Development
- **Repository:** PolyGen

## Upcoming Development

The immediate next objective is implementing AI-based texturing using Stable Diffusion and ControlNet.

The goal is to generate suitable textures, apply them to UV-mapped 3D meshes, and export textured assets for further processing.

---

*This repository documents the development, implementation, testing, and integration of the PolyGen generative 3D asset pipeline.*
