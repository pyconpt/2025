from os import walk

from django.shortcuts import render

from config.settings.base import APPS_DIR


def default_view(request, menu="home", submenu=None):
    path = APPS_DIR.__str__() + "/content/" + menu + ("/" + submenu if submenu else "")
    page = ""
    ctx = {"menu": (submenu if submenu else menu).capitalize().replace("_", " ")}
    files = []

    for _dirpath, _dirname, filenames in walk(path):
        files.extend(filenames)
        break

    ctx["files"] = []
    for f in sorted(files):
        content = f"{path}/{f}"
        ctx["files"].append(content)

    if menu == "home":
        page += "pages/" + menu
    elif len(files) == 0:
        page += "404"
    else:
        page += "pages/" + "default"

    return render(request, page + ".html", ctx)
