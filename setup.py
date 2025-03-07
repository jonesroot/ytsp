import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytsp",
    version="2.0.0",
    author="Lucifer",
    license='MIT',
    author_email="",
    description="Search for YouTube videos, channels & playlists & get video information using link WITHOUT YouTube Data API v3\n\nFork From: [Here](https://github.com/step0ne/youtube-search-python)\nOriginal Source: [Here](https://github.com/alexmercerind/youtube-search-python.git)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonesroot/ytsp",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'httpx>=0.27.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
