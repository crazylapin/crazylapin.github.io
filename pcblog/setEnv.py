from jinja2 import Environment, PackageLoader,FileSystemLoader
app_name = "pcblog"
temp_path = "_layouts"
index_name = "index.html"
author = "CrazyLapin"
blog_name = "Lapin's Home"

loader = FileSystemLoader(temp_path)
env = Environment(loader=loader)

index_temp = env.get_template(index_name)
site = dict()
site["author"] = author
site["blog_name"] = blog_name
site["blog_nav"] = ["itme1","itme2","itme3"]
env.globals["site"] = site
posts = list()
posts.append({"title":"title1","text":"sdfsdqfezsfd","img":""}
)
posts.append({"title":"title2","text":"sdfsdqfezsfd","img":""}
)
posts.append({"title":"title3","text":"sdfsdqfezsfd","img":""}
)

print index_temp.render(posts=posts)



env = Environment(loader=PackageLoader(app_name,temp_path))
# 全局命名空间
# Environment.globals 字典中的变量是特殊的，它们对导入的模板也是可用的， 即使它们不通过上下文导入。这是你可以放置始终可访问的变量和函数的地方。此外， Template.globals 是那些对特定模板可用的变量，即对所有的 render() 调用可用。
env.globals["author"] = author

index_temp = env.get_template(index_name)

print index_temp.render(title=blog_name, go='here')

from jinja2 import BaseLoader, TemplateNotFound
from os.path import join, exists, getmtime

class CBlogLoader(BaseLoader):

    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
        mtime = getmtime(path)
        with file(path) as f:
            source = f.read().decode('utf-8')
        return source, path, lambda: mtime == getmtime(path)