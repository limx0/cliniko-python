"""
_setup.py_

Cirrus template setup.py that reads most of its business
from the cirrus.conf file. This lightweight setup.py should be used by
projects managed with cirrus.

"""
import setuptools

try:
    import ConfigParser as configparser
except ImportError:
    import configparser


def get_default(parser, section, option, default):
    """helper to get config settings with a default if not present"""
    try:
        result = parser.get(section, option)
    except (configparser.NoSectionError, configparser.NoOptionError):
        result = default
    return result


# Build a parser and fetch setup options
parser = configparser.RawConfigParser()
parser.read('cirrus.conf')
src_dir = get_default(parser, 'package', 'find_packages', '.')
excl_dirs = get_default(parser, 'package', 'exclude_packages', [])
requirements_filename = get_default(
    parser,
    'build',
    'requirements-file',
    'requirements.txt'
)
requirements_file = open(requirements_filename)

# Manually parse the requirements file. Pip 1.5.6 to 6.0 has a function
# behavior change for pip.req.parse_requirements. You must use the setuptools
# format when specifying requirements.
#  - https://pythonhosted.org/setuptools/setuptools.html#declaring-dependencies
# Furthermore, you can't use line continuations with the following:
requirements = requirements_file.read().strip().split('\n')


def install_deps():
    """Reads requirements.txt and preprocess it
    to be feed into setuptools.

    This is the only possible way (we found)
    how requirements.txt can be reused in setup.py
    using dependencies from private github repositories.

    Links must be appendend by `-{StringWithAtLeastOneNumber}`
    or something like that, so e.g. `-9231` works as well as
    `1.1.0`. This is ignored by the setuptools, but has to be there.

    Warnings:
        to make pip respect the links, you have to use
        `--process-dependency-links` switch. So e.g.:
        `pip install --process-dependency-links {git-url}`

    Returns:
         list of packages and dependency links.
    """
    default = open('requirements.txt', 'r').readlines()
    new_pkgs = []
    links = []
    for resource in default:
        if 'git+ssh' in resource or 'git+https' in resource:
            pkg = resource.split('#')[-1]
            links.append(resource.strip() + '-9876543210')
            new_pkgs.append(pkg.replace('egg=', '').rstrip())
        else:
            new_pkgs.append(resource.strip())
    return new_pkgs, links


pkgs, new_links = install_deps()

setup_args = {
    'description': parser.get('package', 'description'),
    'include_package_data': True,
    'install_requires': pkgs,
    'dependency_links': new_links,
    'name': parser.get('package', 'name'),
    'version': parser.get('package', 'version'),
    'url': get_default(parser, 'package', 'url', None),
    'author': get_default(parser, 'package', 'author', None),
    'author_email': get_default(parser, 'package', 'author_email', None),
}

if parser.has_section('console_scripts'):
    scripts = [
        '{0} = {1}'.format(opt, parser.get('console_scripts', opt))
        for opt in parser.options('console_scripts')
    ]
    setup_args['entry_points'] = {'console_scripts': scripts}

if src_dir:
    setup_args['packages'] = setuptools.find_packages(src_dir, exclude=excl_dirs)
    setup_args['provides'] = setuptools.find_packages(src_dir)
    setup_args['package_dir'] = {'': src_dir}
setuptools.setup(**setup_args)
