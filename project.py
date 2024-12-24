from PIL import Image
import base64
from io import BytesIO

# Load the uploaded image
image_path = "C:/Users/Impossible/Desktop/project/123.jpg"
image = Image.open(image_path)

# Convert image to Base64
buffered = BytesIO()
image.save(buffered, format="JPG")
img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
base64_src = f"data:image/jpg;base64,{img_base64}"

base64_src[:100]