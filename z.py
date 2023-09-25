import os

source_directory = os.getcwd()

output_file = "z.txt"

with open(output_file, "w") as output:
    for filename in os.listdir(source_directory):
        if filename.endswith(".py"):

            output.write(f"File - {filename}\n")
            output.write(f"Path - {os.path.join(source_directory, filename)}\n")
            output.write("\"\" THE WHOLE PY FILE - \"\"\n")
            
            with open(os.path.join(source_directory, filename), "r") as python_file:
                content = python_file.read()
                output.write(content)
            
            output.write("\nEnd of File.\n\n")

print(f"All Python files in {source_directory} copied to {output_file}.")
