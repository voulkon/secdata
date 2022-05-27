import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secdata",
    
    version="0.0.3",
    
    author="Konstantinos Voulgaropoulos",
    
    author_email="voulkon93@gmail.com",
    
    description="Easily Download Financial Data reported to SEC",
    
    license="MIT",
    
    long_description=long_description,
    
    long_description_content_type="text/markdown",
    
    url="https://github.com/voulkon/secdata",
    
    #install_requires = ["pandas", "requests","json"],
    
    keywords = ["financial","reporting","us-gaap","gaap","sec","api"],
    
    project_urls = {"Source Code":"https://github.com/voulkon/secdata"},
    
    packages=setuptools.find_packages(),
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)