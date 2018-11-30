from setuptools import setup

setup(
    name="camgear",
    version="0.1",
    license="MIT",
    python_requires=">=3.6",
    long_description=open("README.md").read(),
    url="http://dev.sigpipe.me/dashie/camgear",
    author="Dashie",
    author_email="dashie@sigpipe.me",
    install_requires=[
        "Flask",
        "SQLAlchemy",
        "WTForms",
        "WTForms-Alchemy",
        "SQLAlchemy-Searchable",
        "SQLAlchemy-Utils",
        "SQLAlchemy-Continuum",
        "Bootstrap-Flask",
        "Flask-DebugToolbar",
        "Flask-Login",
        "Flask-Mail",
        "Flask-Migrate",
        "Flask-Principal",
        "Flask-Security",
        "Flask-SQLAlchemy",
        "Flask-Uploads",
        "Flask-WTF",
        "bcrypt",
        "psycopg2-binary",
        "unidecode",
        "Flask_Babelex",
        "texttable",
        "python-slugify",
        "python-magic",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)
