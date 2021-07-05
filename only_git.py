from github import Github
g = Github("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")

repo = g.get_user().get_repo("CoolMe")
all_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "xlsx":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

with open('Book1.xlsx', 'rb') as file:
    content = file.read()

# Upload to github
git_file = 'Book.xlsx'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha)
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content)
    print(git_file + ' CREATED')