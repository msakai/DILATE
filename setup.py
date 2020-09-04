import setuptools

setuptools.setup(
    name='DILATE',
    version='0.1.0',
    author='Vincent Le Guen',
    url="https://github.com/vincent-leguen/DILATE",
    description='Code for NeurIPS 2019 paper "Shape and Time Distortion Loss for Training Deep Time Series Forecasting Models"',
    license='MIT License',
    classifiers=[
        'OSI Approved :: MIT License',
    ],
    install_requires=['numpy', 'numba', 'torch'],  # tslearn is required only for main.py
    packages=setuptools.find_packages(),
)
