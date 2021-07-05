from flask import Flask, request, jsonify
from github import Github

app = Flask(__name__)


@app.route('/api',methods=['GET'])
def hello():
   g = Github("ajith-m-doodlebug", "Ajith251")

    repo = g.get_user().get_repo("https://github.com/ajith-m-doodlebug/CoolMe")
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
    
    with open('/tmp/file.txt', 'r') as file:
        content = file.read()
        
    git_prefix = 'folder1/'
    git_file = git_prefix + 'file.txt'
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="master")
        print(git_file + ' CREATED')

if __name__ == '__main__':
    app.run()