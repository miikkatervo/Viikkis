#!/usr/bin/python
#coding=utf-8
import sys
import re
file = sys.argv[1]
out = sys.argv[2]
re_point = r'({: .*})'
re_header = r'(#+ )'
re_link = re.compile(
	r'(<)[\w]*(>)'
)
re_toc = re.compile(
	r'[\w\s,.äöå]*(\[)[\w\s\-äåö]*(\])(\([#\w\-äöå]*\))', re.UNICODE
)
frontmatter = False
o = open(out, "a+")
with open(file, "r") as f:
	line = f.readline()
	while line:
		if(line.strip() == '---' and not frontmatter):
			frontmatter = True
		elif(line.strip() == '---' and frontmatter):
			frontmatter = False
			line = f.readline()

		if(len(line) == 0 or frontmatter):
			line = f.readline()
			continue
		line = re.sub(re_point,'', line)
		line = re.sub(re_header,'', line)
		m = re.match(re_link, line.strip())
		if m:
			for match in m.groups():
				line = line.replace(match,'')
		m = re.match(re_toc, line.strip())
		if m:
			for match in m.groups():
				line = line.replace(match,'')
		o.write(line)
		line = f.readline()
		# Format the line before writing it to file

o.close()