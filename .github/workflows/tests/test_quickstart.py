import os
import subprocess

def callsh(command):
  status = subprocess.run(command)
  status.check_returncode()
  print(status.stdout)

# callsh(['git', 'clone', 'https://github.com/name/repo_name'])
# os.chdir('repo_name')
# callsh(['bash', 'scripts/setup.sh'])
# callsh(['conda', 'create', '-n', 'testenv', 'python=3.8.12', 'cudatoolkit=9.2', 'cudnn', '-y'])
# callsh(['/opt/conda/envs/testenv/bin/pip', 'install', '-r', 'requirements.txt'])
# callsh(['/opt/conda/envs/testenv/bin/pytest', 'tests'])
# ......

# callsh(['conda', 'create', '-n', 'testenv', 'python=3.9', '-y'])
callsh(['pip', 'install', 'fastdup'])

import fastdup
print(f'fastdup version: {fastdup.__version__}')