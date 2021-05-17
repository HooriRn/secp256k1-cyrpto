from setuptools import setup , find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='secp256k1Crypto',
    packages=find_packages(),
    version='0.0.1',
    license='MIT',
    description='Multi OS supported secp256k1-py',
    author='HooriRn',
    author_email='HooriRn@protonmail.com',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/hoorin/secp256k1-py-multi-os',
    keywords=["secp256k1", "secp256k1-py","crypto"],
    install_requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python'
    ],
)
