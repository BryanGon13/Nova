# migrate_menu_images.py

import os

import cloudinary.uploader
from django.conf import settings


def upload_menu_images():
    """
    Upload all files in `media/menu_images/` to Cloudinary
    and print out their new Cloudinary URLs.
    """
    # Path to your local folder
    local_folder = os.path.join(settings.BASE_DIR, "nova", "media", "menu_images")

    # Iterate over each file in the folder
    for file_name in os.listdir(local_folder):
        full_path = os.path.join(local_folder, file_name)

        # Ensure it's a file (not a subfolder)
        if os.path.isfile(full_path):
            print(f"Uploading {file_name}...")

            # Upload to Cloudinary
            result = cloudinary.uploader.upload(full_path)

            # Print the new URL so you can update references in your HTML
            new_url = result["secure_url"]
            print(f"Uploaded {file_name} to {new_url}\n")

    print("All menu_images have been uploaded to Cloudinary!")
