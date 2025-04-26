"""
    Read source code translations and init the documentation translations
    where we find exact matches for `msgid` fields.

    Call with `python tools/merge-translations.py path/to/sourcecode path/to/doc`.
    We assume both directories contain an immediate `po/` subdirectory.

    Copyright (c) Aurélien Pierre - 2025
"""

import regex as re
import glob
import sys
import os

SOURCE = os.path.join(sys.argv[1], "po")
LANG = sys.argv[2]

entry_pattern = re.compile(r"((?:#: \S+?\n)+)#, no-wrap\n(?:#~ )?msgid ((?:\"[\s\S]*?\"\n)+)(?:#~ )?msgstr ((?:\"[\s\S]*?\"\n)+)")
file_pattern = re.compile(rf"(?:#: (\S+?)(\.{LANG})?\.md:(\d+)\n)")


sourcecode: dict
content : str
with open(os.path.join(SOURCE, f'content.{LANG}.po'), "r") as f:
    content = f.read()
    sourcecode = { line: [match[1], match[2]]
                  for match in entry_pattern.findall(content)
                  for line in file_pattern.findall(match[0]) }

for key, value in sourcecode.items():
  # If translated string is empty for non-default language
  if key[1] == "" and len(sourcecode[key][1]) < 4:
    found = False

    # First sweep: look for exact matches
    for i in range(-30, 30):
      new_key = (key[0], f".{LANG}", str(int(key[2]) + i))

      # Found the n-th closest line in non-translated file
      # from the current translated file line and its translation is empty
      if new_key in sourcecode:
        # Found exact match: no brainer
        if(sourcecode[key] == sourcecode[new_key]):
          template_source = "msgid " + sourcecode[key][0] + "msgstr " + sourcecode[key][1]
          template_destin = "msgid " + sourcecode[key][0] + "msgstr " + sourcecode[key][0]
          if(content.find(template_source) > 1):
            content = content.replace(template_source, template_destin)
            print("replaced:")
            print(template_destin)
            print("")
          else:
            # Should not happen
            print("problem on", template_source)

          found = True
          break

    # Move on to next translation ?
    if found:
      continue

    # Second sweep: no exact matches, look increasingly further and ask user
    i = 0
    ping = True
    while not found and abs(i) < 30:
      print(i)
      new_key = (key[0], f".{LANG}", str(int(key[2]) + i))

      if ping:
        sign = -1 if i < 0 else 1
        i = (abs(i) + 1) * sign
        ping = False
      else:
        i = i * (-1)
        ping = True

      # Found the n-th closest line in non-translated file
      # from the current translated file line and its translation is empty
      if new_key in sourcecode:
        os.system('clear')
        print("IS", key)
        print("")
        print(sourcecode[key][0])
        print("TRANSLATED BY:", new_key)
        print("")
        print(sourcecode[new_key][0])

        response = input("Y(es) / N(o) / A(bort) / C(opy) / Q(uit) ?").lower()

        if response == "y":
          template_source = "msgid " + sourcecode[key][0] + "msgstr " + sourcecode[key][1]
          template_destin = "msgid " + sourcecode[key][0] + "msgstr " + sourcecode[new_key][0]
          if(content.find(template_source) > 1):
            content = content.replace(template_source, template_destin)
            print("replaced:")
            print(template_destin)
            print("")
          else:
            # Should not happen
            print("problem on", template_source)

          found = True

        elif response == "c":
          # Copy original, untranslated content, for example if it's code or markup
          template_source = "msgid " + sourcecode[key][0] + "msgstr " + sourcecode[key][1]
          template_destin = "msgid " + sourcecode[key][0] + "msgstr " + sourcecode[key][0]
          if(content.find(template_source) > 1):
            content = content.replace(template_source, template_destin)
            print("replaced:")
            print(template_destin)
            print("")
          else:
            # Should not happen
            print("problem on", template_source)

          found = True

        elif response == "a":
          break
        elif response == "n":
          continue
        elif response == "q":
          with open(os.path.join(SOURCE, f'content.{LANG}.po'), "w")  as f:
            f.write(content)
          exit(0)
        else:
          exit(1)


with open(os.path.join(SOURCE, f'content.{LANG}.po'), "w")  as f:
    f.write(content)
