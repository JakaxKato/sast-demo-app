import subprocess
import shlex

def run_command(cmd):
    safe_cmd = shlex.split(cmd)
    subprocess.call(safe_cmd)
