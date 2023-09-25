import os

"""
        Code to save 'snapshot' of the project to a file. 
        If I do this even after git, I'm I really utilizing git properly?? 
"""

source_directory = os.getcwd()
output_file = "helper_snapshot_output.txt"

with open(output_file, "w") as output:
    for filename in os.listdir(source_directory):
        if filename.endswith(".py"):

            output.write(f"File - {filename}\n")
            output.write(f"Path - {os.path.join(source_directory, filename)}\n")
            
            with open(os.path.join(source_directory, filename), "r") as python_file:
                content = python_file.read()
                output.write(content)
            
            output.write("\nEnd of File.\n\n")

print(f"All Python files in {source_directory} copied to {output_file}.")

