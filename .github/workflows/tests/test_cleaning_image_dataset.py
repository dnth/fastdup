import os
import subprocess

def callsh(command):
  status = subprocess.run(command)
  status.check_returncode()
  print(status.stdout)

callsh(['pip', 'install', 'fastdup'])
callsh(['wget', 'http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz'])
callsh(['tar', '-xf', 'food-101.tar.gz'])

import fastdup
print(f'fastdup version: {fastdup.__version__}')

fd = fastdup.create(work_dir="fastdup_work_dir/", input_dir="food-101/images/")
fd.run(num_images=1000)

fd.vis.duplicates_gallery(num_images=5)
fd.vis.component_gallery(num_images=5)
fd.vis.outliers_gallery(num_images=5)
fd.vis.stats_gallery(metric='dark', num_images=5)
fd.vis.stats_gallery(metric='bright', num_images=5)
fd.vis.stats_gallery(metric='blur', num_images=5)
