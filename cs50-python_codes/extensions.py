def main():
    file_name = input("Enter the file name: ").strip().lower()
    media_type = get_media_type(file_name)
    if media_type:
        print(media_type)
    else:
        print("application/octet-stream")

def get_media_type(file_name):
    file_extensions = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    # Check if the file name contains any supported extension
    for ext, media_type in file_extensions.items():
        if file_name.endswith(ext):
            return media_type
    # If no matching extension found, return None
    return None

if __name__ == "__main__":
    main()
