import os
import subprocess

def callsh(command):
  status = subprocess.run(command, shell=True)
  status.check_returncode()
  print(status.stdout)

# callsh(['pip', 'install', 'fastdup', 'plotly', 'gdown'])
# callsh(['gdown', '--fuzzy', 'https://drive.google.com/file/d/1iSXVTlkV1_DhdYpVDqsjlT4NJFQ7OkyK/view'])
# callsh(['unzip', '-qq', 'coco_minitrain_25k.zip'])
# callsh(['cd', 'coco_minitrain_25k/annotations', '&&', 'gdown', '--fuzzy', 'https://drive.google.com/file/d/1i12p23cXlqp1QrXjAD_vu467r4q67Mq9/view'])

callsh("pip install fastdup plotly gdown")
callsh("gdown --fuzzy https://drive.google.com/file/d/1iSXVTlkV1_DhdYpVDqsjlT4NJFQ7OkyK/view")
callsh("unzip -qq coco_minitrain_25k.zip")
callsh("cd coco_minitrain_25k/annotations && gdown --fuzzy https://drive.google.com/file/d/1i12p23cXlqp1QrXjAD_vu467r4q67Mq9/view")

import fastdup
print(f'fastdup version: {fastdup.__version__}')

import pandas as pd
coco_csv = 'coco_minitrain_25k/annotations/coco_minitrain2017.csv'
coco_annotations = pd.read_csv(coco_csv, header=None, names=['filename', 'col_x', 'row_y',
                                                             'width', 'height', 'label', 'ext'])

coco_annotations['split'] = 'train'  # Only train files were loaded
coco_annotations['filename'] = coco_annotations['filename'].apply(lambda x: 'coco_minitrain_25k/images/train2017/'+x)
coco_annotations = coco_annotations.drop_duplicates()

input_dir = '.'
work_dir = 'fastdup_minicoco'

fd = fastdup.create(work_dir=work_dir, input_dir=input_dir)
fd.run(annotations=coco_annotations, overwrite=True, num_images=10000)

fd.vis.component_gallery(metric='size', max_width=900)
fd.vis.outliers_gallery()
fd.vis.component_gallery(num_images=25, slice='diff')
