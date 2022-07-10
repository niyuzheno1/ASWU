# please input the python path you want to use
from glob import glob


python_path = "python"

# detect if a package is installed
def is_package_installed(package):
    global python_path
    import subprocess
    try:
        result = subprocess.check_output([python_path, "-m", "pip", "list"])
        if package + " " in str(result):
            return True
        else:
            return False
    except FileNotFoundError:
        return False

# install a package
def install_package(package):
    global python_path
    import subprocess
    subprocess.call([python_path, "-m", "pip", "install", package])

# is awscli installed
if is_package_installed("awscli"):
    print("awscli is installed")
else:
    print("awscli is not installed")
    print("installing awscli")
    install_package("awscli")

import awscli
from awscli.customizations.s3.s3 import S3
from awscli.customizations.s3.subcommands import ListCommand, WebsiteCommand
from awscli.customizations.s3.subcommands import CpCommand, MvCommand, RmCommand
from botocore import session
# from awscli.clidriver import main
from awscli.customizations.configure.configure import ConfigureCommand

session = session.get_session()

configure = ConfigureCommand(session)

configure([], None)

# main()
# session = session.get_session()
