# Image-Filtering-in-Assembly--RISC-V-
This project implements image processing in Assembly (RISC-V) by applying a convolution filter to a grayscale image.

Original Image
![4](https://github.com/user-attachments/assets/e9df64a8-562e-4e08-8fba-f972cc5313c0)

Filtered-image-assembly
![filtered-image-assembly](https://github.com/user-attachments/assets/92442950-43cc-4ef2-9088-b147c1edc921)

Filtered-image-python
![filtered-image-in-python](https://github.com/user-attachments/assets/45ca723a-1a6f-4c5c-9b74-7a87389458a0)


The image is represented as a byte array (.byte), and the program iterates over this matrix applying a kernel (mask) to generate a processed output image.

⚙️ Technologies Used

Language: RISC-V Assembly
Execution environment: RARS (or similar simulator)

🧠 Concepts Covered

Memory manipulation (.data and .text)
Linearized matrix addressing
Loops in Assembly
Register usage
Macro definition (.macro)
Digital image processing
Convolution filtering

🖼️ Image Structure

The image is stored as a linear array:
imagem: .byte ...
Its dimensions are defined as:

linhas:   .word 119
colunas:  .word 175
control:  .word 176   # row width in memory
🔍 Algorithm Overview

The program iterates pixel by pixel (ignoring borders) and applies a convolution filter.

🧩 Kernel (Mask)
The filter used is:

-1  -2  -1
 0   0   0
 1   2   1

This kernel is similar to the vertical Sobel operator, commonly used for edge detection.

⚙️ Processing Steps

Read the central pixel
Apply convolution
Multiply neighboring pixels by kernel weights
Accumulate the results
Normalize the result

If < 0 → set to 0
If ≥ 256 → set to 255

Store the result
Save into the secondary matrix
Print the value
Output to console

🔁 Macro Used

To reduce code repetition, the following macro is defined:

.macro mascaraS
  lb s4,0(s10)
  mul s5,s4,t6
  add s9,s9,s5
.end_macro
📌 Purpose:

Loads a neighboring pixel
Multiplies it by the kernel weight
Adds it to the accumulator

💾 Output

The processed values are:
Printed to the console
Stored in memory (matrizsecundaria2)

matrizsecundaria2: .space 21120

▶️ How to Run

Open the code in a RISC-V simulator (e.g., RARS)

Assemble the program
Run it
Observe the output in the console

📊 Expected Result

The program generates a new image with enhanced vertical edges, useful for:
Computer vision
Image processing
Edge detection

🚀 Possible Improvements

Implement additional filters (horizontal Sobel, Laplacian, blur)
Display the image graphically
Handle border pixels properly
Optimize register usage
Further modularize the code

👨‍💻 Author

This project was developed as practice for:
Low-level programming
Memory manipulation
Image processing in Assembly
