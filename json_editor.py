from write_to_file import WriteRead


class Edit:
    @staticmethod
    def tree_edit(dic):
        temp_dict = {}
        for o in dic.get('children'):
            temp_dict[f"{o.get('name')}"] = {}
            temp_dict[f"{o.get('name')}"]['id'] = o.get('id')
            temp_dict[f"{o.get('name')}"]['url'] = f"https://lalafo.kg/kyrgyzstan{o.get('url')}"
        return temp_dict


def edit_tree_json():
    read = WriteRead().json_file(file_name='tempfile/tree.json', mods='r')

    new_dict = {}
    for i in read:
        new_dict[f"{i.get('name')}"] = {}
        new_dict[f"{i.get('name')}"]['id'] = f"{i.get('id')}"
        new_dict[f"{i.get('name')}"]['image'] = f"{i.get('image')}"
        new_dict[f"{i.get('name')}"]['url'] = f"https://lalafo.kg/kyrgyzstan{i.get('url')}"
        k = Edit().tree_edit(i)
        for i2 in i.get('children'):
            k2 = Edit().tree_edit(i2)
            k[f'{i2.get("name")}']['subcatigories'] = k2
            for i3 in i2.get('children'):
                k3 = Edit().tree_edit(i3)
                k2[f'{i3.get("name")}']['subcatigories'] = k3
                for i4 in i3.get('children'):
                    k4 = Edit().tree_edit(i4)
                    k3[f'{i4.get("name")}']['subcatigories'] = k4
        new_dict[f"{i.get('name')}"]['subcatigories'] = k

    w = WriteRead().json_file(new_dict, file_name='new_tree.json')
    return w
