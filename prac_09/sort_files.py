import os
import shutil

file_extensions = []
os.chdir('FilesToSort')


def version_1():
    find_all_file_endings()
    create_directories()
    sort_files()


def version_2():
    find_all_file_endings()
    categorised_extensions = categorise_extensions()
    sort_files_2(categorised_extensions)



def find_all_file_endings():
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = os.path.splitext(filename)[1]
        extension = extension.replace(".", "")
        if extension not in file_extensions:
            file_extensions.append(extension)


def create_directories():
    for extensions in file_extensions:
        try:
            os.mkdir(extensions)
        except FileExistsError:
            pass


def categorise_extensions():
    categorised_extensions = {}
    for extension in file_extensions:
        category = input("What folder would you like to sort {} files into?".format(extension))
        categorised_extensions[extension] = category
        try:
            os.mkdir(category)
        except FileExistsError:
            pass
    return categorised_extensions


def sort_files_2(categorised_extensions):
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = os.path.splitext(filename)[1]
        extension = extension.replace(".", "")
        location = categorised_extensions.get(extension)
        shutil.move(filename, "{}/{}".format(location, filename))


def sort_files():
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = os.path.splitext(filename)[1]
        extension = extension.replace(".", "")
        shutil.move(filename, "{}/{}".format(extension, filename))


version_2()