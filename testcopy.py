import sys
import subprocess

log_file = sys.argv[1]
#log_file = sys.argv[1]

# Викликайте  основний скрипт тут і передає значення log_file як аргумент командного рядка
subprocess.call(['python', 'gf_script.py', log_file])
print("hi new feature g")
