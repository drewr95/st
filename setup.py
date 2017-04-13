import platform

from setuptools import setup, find_packages

conditional_requires = []

arch = platform.architecture()
if arch[1].lower().startswith('win'):
    conditional_requires.append('pyqt5-tools')

setup(
    name="EPyQ",
    version="0.1",
    author="EPC Power Corp.",
    classifiers=[
        ("License :: OSI Approved :: "
         "GNU General Public License v2 or later (GPLv2+)")
    ],
    packages=find_packages(),
    entry_points={'gui_scripts': ['epyq = epyq.__main__:main']},
    install_requires=[
        'PyQt5==5.7.0',
        'PyQtChart==5.7.0',
        'SIP==4.18.1',
        *conditional_requires
    ],
    setup_requires=['vcversioner'],
    vcversioner={
        'version_module_paths': ['epyq/_version.py'],
        'vcs_args': ['git', '--git-dir', '%(root)s/.git', 'describe',
                     '--tags', '--long', '--abbrev=999']
    },
)
