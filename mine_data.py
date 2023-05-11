# Imports
# -------
import os
import json
import discord
import pandas as pd

from rdkit import Chem
from github import Github
from dotenv import load_dotenv

# Discord Environment
# --------------------

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

categories = [
  'Sex', 'Cannabis', 'Education', 'Environment',
  'Food', 'Global', 'Materials', 'Narcotics', 'Space',
  'War'
]
if __name__ == '__main__':

    github = Github(GITHUB_TOKEN)
    repo = github.get_repo("Global-Chem/Chemical-Ecosystem")
    open_issues = repo.get_issues(state='open')

    for category in categories:

        issues = []
        for issue in open_issues:
            if category in issue.title:
                issues.append(issue)

        smiles = []

        if len(issues) == 0:
            continue

        for i in issues:
            try:
              res = i.body
              res = res.strip('][').split(', ')
              smiles = smiles + res
            except:
              continue

        df = pd.DataFrame()
        df['smiles'] = smiles
        df.to_csv('chemical_universes/%s/%s_v100.csv' % (category.lower(), category.lower()))
