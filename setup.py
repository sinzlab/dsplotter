from setuptools import setup, find_packages

setup(
    name='dsplotter',                # Project name
    version='0.1.0',                    # Version
    packages=find_packages(),           # Automatically find packages
    install_requires=[                  # Dependencies
        'matplotlib',
        'geopandas',
        'folium',
        'seaborn'
    ],
    entry_points={
        'console_scripts': [
            'your_command=your_project.module1:main_function',
        ],
    },
    author='Dominik Becker',
    author_email='dominik.becker1@uni-goettinge.de',
    description='Contains a helper function to plot points on Goettingen map',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)