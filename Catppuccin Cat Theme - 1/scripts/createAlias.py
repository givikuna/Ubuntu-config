alias = input('alias: ')
cmd = input('command: ')

toEcho = f"alias {alias}='{cmd}'"

try:
	with open(".bashrc", "a") as bashrc_file:
		bashrc_file.write(toEcho+'\n')
	print('Added the alias')
except Exception as e:
	print(f"Error occured: {e}")
