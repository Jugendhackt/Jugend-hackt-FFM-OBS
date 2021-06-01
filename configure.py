from string import Template
import os
import pathlib
import json

with open("Jugend_hackt.json.template") as f:
    template = Template(f.read())

directory = str(pathlib.Path().absolute())

print("What BigBlueButton URL should be used?")
print("Info: This setup is only tested using BBB 2.3.")
bbb_url = input("> ")


print("What Reactions URL should be used?")
print("Info: They look like https://audience.alpaka.space/audience/CITY.")
reactions_url = input("> ")

print(
    "Changing all paths to '"
    + directory
    + "' and using entered details.  "
    + "If you move this folder you'll have to rerun this script."
)

with open("ressources/bbb.css") as f:
    bbb_css = f.read()

with open("ressources/reactions.css") as f:
    reactions_css = f.read()

output = template.safe_substitute(
    path=directory,
    bbb_url=json.dumps(bbb_url),
    bbb_css=json.dumps(bbb_css),
    reactions_css=json.dumps(reactions_css),
    reactions_url=json.dumps(reactions_url),
)
with open("Jugend_hackt.json", "w") as f:
    f.write(output)
