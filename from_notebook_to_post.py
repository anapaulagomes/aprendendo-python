import nbconvert
import os
import re


NOTEBOOK_PATTERN = re.compile(r'#>>(.*)<<#')
PLACEHOLDER_PATTERN = re.compile(r'#>>.*<<#')
posts_dir = f'{os.getcwd()}/content/posts/'
notebooks_dir = f'{os.getcwd()}/notebooks/'
exporter = nbconvert.MarkdownExporter()

for file_ in os.listdir(posts_dir):
    if file_.endswith('.md'):
        file_path = f'{posts_dir}{file_}'
        content = open(file_path).read()
        found = re.search(NOTEBOOK_PATTERN, content)
        if found:
            notebook_name = found.groups()[0]
            notebook_path = f'{notebooks_dir}{notebook_name}'
            print(f'>> {file_} {notebook_name}')
            (body, _) = exporter.from_filename(notebook_path)
            replaced_content = re.sub(found.group(), body, content)
            open(f'{file_path}', 'w').write(replaced_content)
