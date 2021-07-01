import setuptools

import setup_versioning

if __name__ == '__main__':
    with open("README.md", "r") as fh:
        long_description = fh.read()

    last_version = setup_versioning.get_last_version()
    version = setup_versioning.bump_patch(last_version)

    setuptools.setup(
        name="propsettings",
        version=version,
        author="Miguel Nicolás-Díaz",
        author_email="miguelcok27@gmail.com",
        description="A python package to define how a class member should be rendered in a UI.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/mnicolas94/propsettings",
        packages=['propsettings', 'propsettings.decorators', 'propsettings.setting_types'],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
        ],
        python_requires='>=3.6',
    )
