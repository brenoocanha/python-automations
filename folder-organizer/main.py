import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
import sys

Tk().withdraw()

path = askdirectory(title="Select a folder to organize")

if not path:
    print("❌ Operation cancelled. No folder was selected.")
else:
    print(f"Organizing folder: {path}")

    script_name = os.path.basename(sys.argv[0])

    for file in os.listdir(path):
        if file == script_name:
            continue

        source_file_path = os.path.join(path, file)

        if os.path.isfile(source_file_path):
            name, extension = os.path.splitext(file)

            if extension:
                destination_folder_name = extension[1:].lower()
                destination_folder_path = os.path.join(path, destination_folder_name)

                if not os.path.exists(destination_folder_path):
                    os.makedirs(destination_folder_path)
                    print(f"📂 Folder '{destination_folder_name}' created.")

                shutil.move(source_file_path, destination_folder_path)
                print(f"✅ Moving '{file}' to '{destination_folder_name}'")

    print("\n🎉 Organization completed successfully!")