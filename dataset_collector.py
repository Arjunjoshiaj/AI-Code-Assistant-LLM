import requests
import json
import os
import re
from bs4 import BeautifulSoup
from github import Github

# GitHub API Token (Add your token)
GITHUB_TOKEN = "your_github_token"

def get_github_repos(query="machine learning", max_repos=10):
    """Fetch repositories from GitHub matching a query."""
    g = Github(GITHUB_TOKEN)
    repos = g.search_repositories(query=query)  
    repo_data = []
    
    for repo in repos[:max_repos]:
        repo_data.append({
            "name": repo.full_name,
            "url": repo.html_url,
            "description": repo.description,
            "language": repo.language
        })
    return repo_data

def get_stackoverflow_questions(tag="python"):
    """Scrape Stack Overflow for coding questions and answers."""
    url = f"https://stackoverflow.com/questions/tagged/{tag}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    questions = []
    for question in soup.select(".s-post-summary"):
        title = question.select_one(".s-link").text
        link = "https://stackoverflow.com" + question.select_one(".s-link")['href']
        questions.append({"title": title, "link": link})

    return questions

# Save Data
github_repos = get_github_repos()
stackoverflow_questions = get_stackoverflow_questions()

os.makedirs("datasets", exist_ok=True)

with open("datasets/github_repos.json", "w") as f:
    json.dump(github_repos, f, indent=4)

with open("datasets/stackoverflow_questions.json", "w") as f:
    json.dump(stackoverflow_questions, f, indent=4)

print("Dataset Collection Completed!")
