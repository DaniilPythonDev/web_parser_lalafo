from parser import get_page_data, tree, fullname
from json_editor import edit_tree_json
from write_to_file import WriteRead


def update_data(tree_update=False, fullname_update=False):
    if tree_update:
        tree_file_status = WriteRead().json_file(tree(), file_name='tree.json')
        print(tree_file_status)
    if fullname_update:
        fullname_file_status = WriteRead().json_file(fullname(), file_name='fullname.json')
        print(fullname_file_status)


def main():
    update_data()
    edit_tree_json()
    get_data = WriteRead().json_file(file_name="new_tree.json", mods='r')
    for i, k in get_data.items():
        p1 = get_page_data(k.get('id'), 1)
        print(p1)

if __name__ == '__main__':
    main()
