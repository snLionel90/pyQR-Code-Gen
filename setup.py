#setup / configuracion

import setuptools

with open ("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'pyQR Code Gen.',
    version = '1.0.0',
    author = 'sn.Lionel90 aka Lionel Sanchez',
    description = ("obtenga un codigo QR de una web o texto inclusio de una imagen"),
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url = 'https://github.com/snLionel90/pyQR Code Gen.',
    keywords=['QRCode', 'snLionel90', 'QR', 'lel'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: pyqrcode :: snLionel90 ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True, 
)
