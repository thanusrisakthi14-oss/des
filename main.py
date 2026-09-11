from huggingface_hub import InferenceClient
from PIL import Image
client=InferenceClient(api_key="...")
image=Image.open("image.png")
result=client.image_to_text(image=image,model="microsoft/git-base-coco")
print(result)
