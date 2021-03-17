import os


def create_paths(dict_):
    paths = []
    for key in dict_:
        for value in dict_[key]:
            if type(value) is dict:
                paths.extend([os.path.join(key, path) for path in create_paths(value)])
            else:
                paths.append(os.path.join(key, value))
    return paths


if __name__ == '__main__':
    dir_names = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
    for dir_path in create_paths(dir_names):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
