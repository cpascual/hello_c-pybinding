from setuptools import Extension, setup
import glob

setup(
    ext_modules=[
        Extension(
            name="hello_c._c_api",  # as it would be imported
            sources=glob.glob("src/hello_c/*.c"),
        ),
    ]
)
