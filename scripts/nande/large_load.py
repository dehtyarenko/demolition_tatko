import os
import requests
import zipfile
import sys

# constants
PROPERTIES_FILE_NAME = "resources//google_drive.properties"
LOCAL_PROPS_FILE_NAME = "resources//local.properties"
FILE_ID_KEY = "local_test_file_id"
CN_API_KEY_KEY = "encripted_api_key"
SEED = "seed"


def read_large_file(file_id, api_key):
    # Construct the URL using the file ID
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={api_key}"
    filename = "large_load_size.zip"

    print(f"Url is {url}")

    # Update the destination to place the large_files folder one level below the current directory
    origination_script_dir = sys.argv[0]
    script_dir = os.path.abspath(os.path.dirname(origination_script_dir))
    destination = os.path.join(script_dir, "..", "large_files")

    # Create the destination directory if it doesn't exist
    os.makedirs(destination, exist_ok=True)

    # Download the file
    print(f"Downloading {filename}...")
    print(f"Potentially it is as big as your mama, so it will take some time...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # Extract the ZIP file
    print(f"Extracting {filename}...")
    with zipfile.ZipFile(filename, "r") as zip_ref:
        for member in zip_ref.infolist():
            if member.is_dir():
                continue
            output_file = os.path.join(destination, os.path.basename(member.filename))
            with open(output_file, "wb") as out_f:
                with zip_ref.open(member) as in_f:
                    while True:
                        chunk = in_f.read(8192)
                        if not chunk:
                            break
                        out_f.write(chunk)

    # Remove the downloaded file after extraction
    os.remove(filename)

    print("Download and extraction completed.")
