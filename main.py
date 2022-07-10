# detect if a package is installed
def is_package_installed(package):
    import subprocess
    try:
        subprocess.call(["python -m pip", "list", "--user", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        return False
    else:
        return True

# is awscli installed
if is_package_installed("awscli"):
    print("awscli is installed")
else:
    print("awscli is not installed")