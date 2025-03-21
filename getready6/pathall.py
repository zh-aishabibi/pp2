import os

def list_contents(path="."): 
    try:
        all_items = os.listdir(path)

        directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]

        files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]

        # Print results
        print(f"Path: {os.path.abspath(path)}")
        print("\nDirectories:")
        print(directories if directories else "No directories found.")

        print("\nFiles:")
        print(files if files else "No files found.")

        print("\nAll Items:")
        print(all_items)

    except FileNotFoundError:
        print("Error: The specified path does not exist.")
    
path= input()
list_contents(path if path else ".")
 