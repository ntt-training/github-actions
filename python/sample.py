"""sample program"""
import os

if __name__ == "__main__":
    env = os.environ.get("GITHUB_WORKSPACE")
    print(env)
