from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

#exts = cythonize([Extension("mag_calc", sources = ["mag_calc_cext.c", "mag_calc.pyx"])])

exts = [Extension("magcalc", 
                  sources = ["mag_calc_cext.c", "magcalc.pyx"],
                  extra_compile_args=['-fopenmp'], 
                  extra_link_args=['-fopenmp'])]

for e in exts:
    e.cython_directives = {"embedsignature":True}

setup(name = 'magcalc',
      version = '0.2.4',
      description = 'Package to compute SEDs for a semi-analytic model',
      author = 'Yisheng Qiu',
      author_email = 'yishengq@student.unimelb.edu.au',
      ext_modules = exts,
      cmdclass = {'build_ext': build_ext},
      packages = ['filters'],
      package_data = {'filters':['*.npy']})
