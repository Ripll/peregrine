from setuptools import setup, find_packages


setup(
    name='peregrinearb',
    version='1.8.1',
    description='A Python library which provides several algorithms to detect arbitrage opportunities across over 132 '
                'cryptocurrency markets in over 50 countries',
    author='Ward Bradt',
    author_email='wardbradt5@gmail.com',
    packages=find_packages(),
    install_requires=['git+git://github.com/wardbradt/networkx.git#egg=networkx',
                      'numpy',
                      'ccxt',
                      'web3'],
    license='MIT',
    url='https://github.com/Stakedllc/peregrine/',
)
