import subprocess

link = 'https://www.instagram.com/'

flatpak_app_id = 'org.mozilla.firefox'

process = subprocess.Popen(["flatpak", "info", "--show-permissions", flatpak_app_id], stdout=subprocess.PIPE, text=True)
output, _ = process.communicate()

executable_path = None
for line in output.splitlines():
	if "app" in line and "firefox" in line:
		executable_path = line.split(":")[1].strip()
		break

if executable_path:
	subprocess.Popen([executable_path, link])
else:
	print("Executable path for firefox not found")
