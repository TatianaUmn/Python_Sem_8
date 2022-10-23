import model
import view
import os.path

def run():
    point = view.write_menu()
    if point == 1:
        try:
            f = open('data.csv')
            f.close()
            start = view.show_menu()
            if start == 1:
                res = model.data_open()
                view.show_res(res)
            elif start == 2:
                in_info = view.add_info()
                model.add_info(in_info)
            elif start == 3:
                index = view.delite()
                model.del_info(index)
            elif start == 4:
                index, tel = view.change_tel()
                model.update_info(index, tel)
            elif start == 5:
                index, surname = view.change_surname()
                model.update_surname(index, surname)
            elif start == 6:
                model.export_csv_txt()
        except FileNotFoundError:
            num = view.number_entries()
            for i in range(num):
                info = view.creating_info()
                model.writing_csv(info)
    else:
        print('До встречи!')