python_path = "python"

def cp_file_recursively(src, dst):
    import subprocess
    try:
        result = subprocess.check_output([python_path, "-m", "awscli", "s3", "cp", src, dst, "--recursive"])
    except FileNotFoundError:
        return False
    return True

def rm_file_recursively(src):
    import subprocess
    try:
        result = subprocess.check_output([python_path, "-m", "awscli", "s3", "rm", src, "--recursive"])
    except FileNotFoundError:
        return False
    return True

def generate_s3_bucket_url(bucket_name):
    return "s3://" + bucket_name

# read from crednetial.json
import json
with open("credential.json") as f:
    data = json.load(f)

bucket_name = data["bucket_name"]
local_path = data["local_path"]
rm_file_recursively(generate_s3_bucket_url(bucket_name) )
cp_file_recursively(local_path, generate_s3_bucket_url(bucket_name))