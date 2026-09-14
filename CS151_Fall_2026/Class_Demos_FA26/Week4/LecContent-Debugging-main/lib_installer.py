import sys, subprocess

subprocess.run(
    [sys.executable, '-m', 'pip', 'install', '--user', 'pillow', 'pytest', 'requests', 'rich']
)
