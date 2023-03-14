from fastapi import FastAPI, HTTPException
from github import Github
import pygit2
import os
import subprocess

app = FastAPI()

GITHUB_TOKEN = "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"

@app.get("/")
async def root():
    try:
        # Create a Github object with the token
        g = Github(GITHUB_TOKEN)
        print(g)

        repo = g.get_repo("rakeshmulugu/test")
        print(repo)

        # Clone the repo to the "test" folder
        repoClone = pygit2.clone_repository(repo.git_url, "./test")
        os.chdir("./test")

        result = subprocess.run(["ls", "-lah"], capture_output=True)
        return {"message": result.stdout.decode('utf-8')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to clone repo: {str(e)}")
