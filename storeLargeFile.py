import gridfs
import pymongo
from PIL import Image
import io

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["image_database"]
fs = gridfs.GridFS(db)

# Function to upload an Image to GridFS
def upload_image(image_path):
    with open(image_path, "rb") as image_file:
        # Read the image and store it in GridFS
        fs.put(image_file, filename=image_path.split('/')[-1])
        print(f"Uploaded {image_path} to GridFS.") 

# Function to retrieve an image from GridFS
def download_image(file_id, output_path):
    # Retrieve the image from GridFS by file ID
    image_data = fs.get(file_id).read()

    # Write the image data to an output file
    with open(output_path, 'wb') as output_file:
        output_file.write(image_data)
        print(f"Downloaded image to {output_path}.")

# Function to list all files in GridFS
def list_files():
    files = fs.find()
    print("Files in GridFS: ")
    for file in files:
        print(f"Filename: {file.filename}, ID: {file._id}")

# Example usage
image_path = './image.png'
upload_image(image_path)

# Listing all files
list_files()

# Download the image back from GridFS
download_image(fs.find_one({'filename': 'image.png'})._id, './downloaded_image.png')

        # image_data = image_file.read()
        # image_buffer = io.BytesIO(image_data)
        # image = Image.open(image_buffer)
        # image_buffer.close()

        # Resize the image to a maximum size of 1000x1000 pixels
        # resized_image = image.resize((1000, 1000), Image.ANTIALIAS)



        # Save the resized image to GridFS
        # buffer = io.BytesIO()
        # resized_image.save(buffer, format="JPEG")
        # buffer.seek(0)
        # fs.put(buffer, filename=image_path, content_type="image/jpeg")