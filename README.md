# File Type Checker Program
This Python program takes a file name input from the user and determines its media type based on the file's extension. The program outputs the corresponding MIME type for common file formats like images, PDFs, text files, and more.

Requirements:
Python 3.x

How to Use:
Run the script.
When prompted, enter the name of the file (including its extension).
The program will check the file's extension and print the corresponding MIME type:
.gif → image/gif
.jpg, .jpeg → image/jpeg
.png → image/png
.pdf → application/pdf
.txt → text/plain
.zip → application/zip
If the file extension doesn't match any of the above, it will output application/octet-stream as the default MIME type.

Example:
Input:
Enter the name of the file: image.jpg
Output:
image/jpeg

Input:
Enter the name of the file: document.pdf
Output:
application/pdf

Input:
Enter the name of the file: unknown.xyz
Output:
application/octet-stream

How It Works:
The program prompts the user to enter a file name (including the extension).
It strips any surrounding spaces and converts the file name to lowercase for consistency.
It checks the file extension and prints the corresponding MIME type based on the predefined conditions.
If no matching extension is found, it defaults to application/octet-stream.
