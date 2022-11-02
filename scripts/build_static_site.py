""" Build a static website using Jinja templates. (c)2022 James Hudson. All rights reserved.
    Let me know if you are interested in  using this yourself! """

import glob
import jinja2

root_dir = "../src/"
output_dir = "../"

templateLoader = jinja2.FileSystemLoader(searchpath=root_dir)
templateEnv = jinja2.Environment(loader=templateLoader)

for filename in glob.iglob(root_dir + "**/*.htm*", recursive=True):
    local_filename = filename[len(root_dir) :]
    print(f"Processing {local_filename}...")
    template = templateEnv.get_template(local_filename)
    output = template.stream(name="output").dump(output_dir + local_filename)
