""" # Step 1: Create input.txt with sample text (only needed once)
with open("input.txt", "w") as f:
    f.write("Hello world!\n")
    f.write("This is a test file.\n")
    f.write("It contains multiple lines.\n")
    f.write("We will process this text.\n")
    f.write("Python makes it easy.\n")

# Step 2: Read contents of input.txt
with open("input.txt", "r") as f:
    content = f.read()

# Step 3: Count words
word_count = len(content.split())

# Step 4: Convert to uppercase
processed_text = content.upper()

# Step 5: Write processed text + word count into output.txt
with open("output.txt", "w") as f:
    f.write("PROCESSED TEXT:\n")
    f.write(processed_text + "\n")
    f.write(f"\nWORD COUNT: {word_count}\n")

# Step 6: Print success message
print("✅ output.txt has been created successfully!") """











with open("input.txt", "w") as m:
    m.write("Good Morning !!")

with open("input.txt", "r") as m:
   content = m.read()

modified = content.upper()

with open("output.txt", "w") as m:
    m.write(modified + "\n")


print("✅ This is coolest men !")


filename = input("Enter the file to read: ")
try:
    with open(filename, "r") as f:
        content = f.read()
    print("File successfully read.")
    print(content)

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"❌ Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")



















