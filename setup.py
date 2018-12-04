# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
        name='test-data-files',
        version='0.1.0',
        author='David Azócar',
        author_email='dazocar@centroenergia.cl',
        license='GPL',
        packages=find_packages(exclude=['tests*','use_cases*']),
        zip_safe=False,
        data_files=[
            ('configfiles',['files/config.json'])
            ],
        entry_points={
            'console_scripts':['test_load_config_file = config.__main__:test_load_config_file',
                               'test_read_config = config.__main__:test_read_config']
            }
        )


