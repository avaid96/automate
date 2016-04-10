import pyperclip
import re

phonereg=re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''',re.VERBOSE)

emailreg=re.compile(r'''(
	[a-zA-z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for groups in phonereg.findall(text):
	phNO='-'.join([groups[1],groups[3],groups[5]])
	if groups[8]!='':
		phNO+=' x'+groups[8]
	matches.append(phNO)
for groups in emailreg.findall(text):
	matches.append(groups[0])

if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print 'Copied to clipboard:'
	print '\n'.join(matches)
else:
	print('No phone numbers of email addresses found')