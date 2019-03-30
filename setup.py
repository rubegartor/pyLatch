import setuptools

setuptools.setup(
  name='pyLatch',
  version='0.1.1',
  description='A simple and basic API wrapper for Latch written in Python',
  long_description='More information in GitHub page: http://github.com/rubegartor/pyLatch',
  license='MIT',
  packages=['pyLatch'],
  author='rubegartor',
  author_email='rubegartor@gmail.com',
  keywords=['Latch', 'Python3', 'Python', 'Latch API wrapper', 'ElevenPaths'],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  url='http://github.com/rubegartor/pyLatch',
  install_requires=[
   'requests'
  ]
)