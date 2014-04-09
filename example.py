from github import Github
g = Github()
org = g.get_organization("DemandCube")
for repo in org.get_repos():
    print repo.name
