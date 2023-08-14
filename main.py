import json
import ast
import subprocess

def parse_env(string):
    data_to_copy = ast.literal_eval(string)[0]["value"]

    platform = subprocess.check_output(["uname"]).strip().decode()
    if platform == "Linux":
        subprocess.run(["echo", "-n", data_to_copy], stdout=subprocess.PIPE, text=True)
    elif platform == "Darwin":
        subprocess.run(["pbcopy"], input=data_to_copy, stdout=subprocess.PIPE, text=True)
    elif platform == "Windows":
        subprocess.run(["clip"], input=data_to_copy, stdout=subprocess.PIPE, text=True)


if __name__ == "__main__":
    env_vars = "YOUR_ENV_VARS"
    parse_env(env_vars)
    print("Parameters successfully copied to a clipboard.")
