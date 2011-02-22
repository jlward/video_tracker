from setuptools import setup, find_packages

version = '0.1'

setup(
    name='video-tracker',
    version=version,
    description="video-tracker",
    long_description='video-tracker',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='video,django',
    author='Jason Ward',
    author_email='jason.ward@policystat.com',
    url='',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

