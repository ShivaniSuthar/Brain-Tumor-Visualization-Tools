# CREATING THE DROP DOWN OPTIONS
# UNABLE TO RUN PYCORTEX WITH THIS FILE. Copy and paste the below into IPython.

import cortex
import numpy as np
np.random.seed(1234)
volume1 = cortex.Volume.random(subject = 'S1', xfmname='fullhead', priority=1)
volume2 = cortex.Volume.random(subject = 'S1', xfmname='fullhead', priority=2)
volume3 = cortex.Volume.random(subject = 'S1', xfmname='fullhead', priority=3)
volume4 = cortex.Volume.random(subject = 'S1', xfmname='fullhead', priority=4)
volume5 = cortex.Volume.random(subject = 'S1', xfmname='fullhead', priority=5)
volumes = {'Lung': volume1, 'Breast': volume2, 'Kidney': volume3, 'Melanoma': volume4, 'Colorectal': volume5,}
cortex.webgl.show(data=volumes, port = 5000)

