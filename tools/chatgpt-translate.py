"""
Submit the content of a .po translation file for auto-translation to ChatGPT.

Copyright (c) Aurélien Pierre - 2025.

Usage:
    Call from main website directory, like `python ./tools/chatgpt-translate.py LANG` where the `LANS` argument is the language code to generate.

Requirements:
    You must have a `.chatgpt.api_key` file containing your PRIVATE ChatGPT API key. This will cost you a few dollars.
    This key file will never be commited as it is set explicitly in .gitignore.

    Install the dependencies of this script through `pip install -r tools/requirements.txt`

Notes:
    We run things in batch to comply with the lower tier of ChatGPT API limitations.
    Auto-generated translations are marked as fuzzy for later human review.

    Be sure to run `./tools/update-translations.sh` between each batch to validate your `content.LANG.po`,
    because ChatGPT sometimes does weird stuff to HTML/Markdown encoding and double-quote escaping.
    `po4a` called from `./tools/update-translations.sh` will tell you
    if errors are found, and sometimes where.

    You might want to check and fix the .po first as plain-text in a code editor,
    otherwise in Poedit (but it may nuke entirely invalid translations when it can't fix them).
    Both ways, it's easier to find the mistakes when there are not too many changes.
"""

import sys
import os
from deep_translator import ChatGptTranslator
import time
import regex as re


LANG = sys.argv[1]

# Now extract items
untranslated = 0
tokens = 0

# ChatGPT token limit per minute for gpt-4o for a single API request
# is 10000 in input AND in output.
# So to be sure to have complete outputs, give it some headroom.
# And even then, seems German can't deal with long text
TOKEN_LIMIT = 8000
API_KEY = ""

with open(".chatgpt.api_key", "r") as f:
    API_KEY = f.read().strip()

# Load the .po file line by line.
# Translation items (comments/msgid/msgstr) are separated by empty lines,
# so we use that as separator.
with open(os.path.join("po", f"content.{LANG}.txt"), "w", encoding="utf-8") as o:
    with open(os.path.join("po", f"content.{LANG}.po"), "r", encoding="utf-8") as f:
        i = -1
        msgid_lines = []
        msgstr_lines = []
        in_msgid = False
        in_msgstr = False

        for line in f:
            i += 1
            if line == "\n":
                # Write previous block
                if msgid_lines and len(msgstr_lines) == 1 and msgstr_lines[0] == '""\n':
                    # From:
                    # https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
                    # 1 token ~= 4 chars
                    tokens += int(len([char for l in msgid_lines for word in l for char in word]) / 4) + 2
                    if tokens < TOKEN_LIMIT:
                        o.write("\n")
                        o.writelines(msgid_lines)
                        untranslated += 1
                        #print(msgid_lines, msgstr_lines)

                # new block
                msgid_lines = []
                msgstr_lines = []
                in_msgid = False
                in_msgstr = False

                if tokens > TOKEN_LIMIT:
                    break

            elif line.startswith('#'):
                # comment, nothing to do
                continue

            # Write [line number]: "line content"
            elif line.startswith('msgid'):
                content = line.replace("msgid ", "")
                if content != "\"\"":
                    in_msgid = True
                    in_msgstr = False
                    msgid_lines.append(f"[{i}]: {content}")
            elif in_msgid and line.startswith('"'):
                msgid_lines.append(f"[{i}]: {line}")

            # We don't actually use msgstr except to see if it's empty
            elif line.startswith('msgstr'):
                content = line.replace("msgstr ", "")
                in_msgid = False
                in_msgstr = True
                msgstr_lines.append(content)
            elif in_msgstr and line.startswith('"'):
                msgstr_lines.append(line)

# Now po_items is a list of tuples: (msgid_text, msgstr_text)

print("strings in batch:", untranslated)

with open(os.path.join("po", f"content.{LANG}.generated.txt"), "w", encoding="utf-8") as o:
    file = os.path.join("po", f"content.{LANG}.txt")
    content = ChatGptTranslator(
        api_key=API_KEY,
        source='en',
        target=LANG,
        model='gpt-4o').translate_file(file)
    # gpt-4o is the only model handling Markdown/HTML and Gettext formatting kinda properly
    #
    o.write(content + "\n")

line_pattern = re.compile(r"\[(\d+)\]: (.*)")
unescaped_doublequote = re.compile(r"(?!(msgstr ))\"(?!\n)")

content = ""
with open(os.path.join("po", f"content.{LANG}.generated.txt"), "r", encoding="utf-8") as translated:
    with open(os.path.join("po", f"content.{LANG}.txt"), "r", encoding="utf-8") as original:
        with open(os.path.join("po", f"content.{LANG}.po"), "r", encoding="utf-8") as f:
            trans = translated.read()
            content = f.read()
            # Translation items (comment/msgid/msgstr) are separated by empty newlines
            for o in original.read().split("\n\n"):
                # We match original -> translated fields by the number of their line in .po
                msgid_list = []
                msgstr_list = []
                for match in line_pattern.findall(o):
                    line_id = match[0]
                    # ChatGPT may insert spaces betwen [line ID] and :
                    target_pattern = re.compile(rf"\[{line_id}\] ?: (.*)\n")
                    t_set = target_pattern.findall(trans)
                    if len(t_set) == 1:
                        msgid_list.append(match[1])
                        msgstr_list.append(unescaped_doublequote.sub("\"", t_set[0]))
                    elif len(t_set) == 0:
                        print("line", line_id, "not found")
                    else:
                        print("line", line_id, "has more than 1 entry")

                if len(msgid_list) == len(msgstr_list):
                    # Ensure original and translation both end (or both don't end) with newline
                    # otherwise po4a breaks on critical error. It's critical for Markdown syntax.
                    for i, (a, b) in enumerate(zip(msgid_list, msgstr_list)):
                        if a.endswith('\\n"') and not b.endswith('\\n"'):
                            b = b.rstrip('"') + '\n"'
                            msgstr_list[i] = b
                        elif not a.endswith('\\n"') and b.endswith('\\n"'):
                            b = b.rstrip('\\n"') + '"'
                            msgstr_list[i] = b

                    template_src = "msgid " + "\n".join(msgid_list) + "\n" + "msgstr \"\""
                    template_dest = "# Translated by ChatGPT\n" + "msgid " + "\n".join(msgid_list) + "\n" + "msgstr " + "\n".join(msgstr_list)

                    if(content.find(template_src) > -1):
                        content = content.replace(template_src, template_dest)
                    else:
                        print("did not find", template_src)
                else:
                    print("translation number of lines mismatch original")


with open(os.path.join("po", f"content.{LANG}.po"), "w", encoding="utf-8") as f:
    f.write(content)
