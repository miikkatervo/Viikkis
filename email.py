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
		# Remove the frontmatter
		if(line.strip() == '---' and not frontmatter):
			frontmatter = True
		elif(line.strip() == '---' and frontmatter):
			frontmatter = False
			line = f.readline()
		if(len(line) == 0 or frontmatter):
			line = f.readline()
			continue
		# Remove point tags and header tags
		line = re.sub(re_point,'', line)
		line = re.sub(re_header,'', line)
		# Remove link tags
		m = re.match(re_link, line.strip())
		if m:
			for match in m.groups():
				line = line.replace(match,'')
		# Remove table of content tags
		m = re.match(re_toc, line.strip())
		if m:
			for match in m.groups():
				line = line.replace(match,'')
		# Write the reformatted line to file
		o.write(line)
		line = f.readline()
o.close()