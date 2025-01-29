def main():
    # Prompt for the file name
    filename = input("Enter the name of the file: ").strip().lower()

    # Check the file's extension and output the corresponding media type
    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

# Call the main function to run the program
main()
