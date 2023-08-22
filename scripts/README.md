# Static site builder from templates

All the benefits of a static site, with all the power of templates + MarkDown.


## Instructions

`python build_static_site.py` will build the whole site.

Alternatively, the shell script `./live_update.sh` will run this script on any changes to the project, so you can see your changes live locally.

## MarkDown

At the moment, HTML is generated manually from MD files, in case the HTML needs to be hand-edited afterwards.

ie
```
python3 -m markdown ai_and_your_business.md > ai_and_your_business.html
```

Then just run the main script, to apply templates and move the content in src to the repository root.
