from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bancario",
    version="0.0.1",
    author="Fernada Novais",
    author_email="my_email",
    description="Sistema Bancario",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fehhnovais/dio_projetos/blob/main/pacote_stm_bancario/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)