from PIL import Image, ExifTags

def get_metadata(img_path):
    print("Metadata:")
    pil_img = Image.open(img_path)
    metadata = pil_img.getexif()
    if not metadata:
        print("No metadata found.")
    else:
       for tag_id, value in metadata.items():
           tag = ExifTags.TAGS.get(tag_id, tag_id)
           print(f"{tag}: {value}")



get_metadata("test.jpg")
