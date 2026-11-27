
from PIL import Image, ImageDraw


import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from services.texture_application import apply_texture

# Step 1: Create a sample texture
texture = Image.new("RGB", (512, 512), "brown")

draw = ImageDraw.Draw(texture)
draw.rectangle(
    (30, 30, 482, 482),
    outline="orange",
    width=12
)
draw.text(
    (160, 245),
    "POLYGEN TEST",
    fill="white"
)

texture.save("test_texture.png")


# Step 2: Apply texture to the UV-mapped model
result = apply_texture(
    input_path="services/mapped.obj",
    texture_path="test_texture.png",
    output_path="outputs/textured_model.glb"
)

print(result)
