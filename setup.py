from setuptools import setup, find_packages

__author__ = "Dax Mickelson"
__author_email = "dmickels@cisco.com"
__license__ = "BSD"

setup(
    name='zwende',
    version='20190716.0',
    description="Zero width character encoder/decoder.",
    long_description="""Sometimes it is beneficial to hide a 'plain text' message within plain text.  This module will
    do just that.'""",
    url='https://github.com/daxm/zwende',
    author='Dax Mickelson',
    author_email='dmickels@cisco.com',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    keywords='encode encoding zero-width decoder secret',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[],
    python_requires='>=3',
    package_data={},
    data_files=None,
)
