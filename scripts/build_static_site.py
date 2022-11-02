""" Build a static website using Jinja templates. (c)2022 James Hudson. All rights reserved.
    Let me know if you are interested in  using this yourself! """

import glob
import jinja2
import os

root_dir = "../src/"
output_dir = "../"

for filename in glob.iglob(root_dir + "**/*.htm*", recursive=True):
    containing_folder, local_filename = os.path.split(filename)
    if local_filename[0] != "%":
        templateLoader = jinja2.FileSystemLoader(searchpath=containing_folder)
        templateEnv = jinja2.Environment(loader=templateLoader)
        print(f"Processing {local_filename}:")
        print(f"   looking for templates in {containing_folder}.")
        template = templateEnv.get_template(local_filename)
        out_path = output_dir + filename[len(root_dir) :]
        output = template.stream(name="output").dump(out_path)
        print(f"   output to {out_path}.\n")
