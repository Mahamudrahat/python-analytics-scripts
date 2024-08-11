# _*_ coding: utf-8
import os
import re
import shutil

import MySQLdb
import datetime
import xlsxwriter

mysql_connection = MySQLdb.connect('Host', 'User', 'Password', 'databaseName',
                                   charset='utf8')


cursor = mysql_connection.cursor(MySQLdb.cursors.DictCursor)
root_dir = 'FileName'
file_name = 'last_id_send_sms.txt'
total_sms_in_excel = 0


class ExcelCreation:
    __workbook = None

    def __init__(self, report_dir, excel_name):
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        file_name = "%s.xlsx" % (report_dir + os.sep + excel_name)
        self.__workbook = xlsxwriter.Workbook(file_name)

    @staticmethod
    def __add_data_to_worksheet(worksheet, data_dict):
        global total_sms_in_excel
        worksheet.write(0, 0, 'start')
        row = 1
        for data in data_dict:
            worksheet.write(row, 0, '88' + data['mobile_no'])
            worksheet.write(row, 1, u'%s' % data['message_body'])
            worksheet.write(row, 2, '%s' % data['upazilla_id'])
            total_sms_in_excel += 1
            row += 1
        worksheet.write(row, 0, 'end')

    def add_worksheet(self, data):
        worksheet = self.__workbook.add_worksheet('sms_excel')
        self.__add_data_to_worksheet(worksheet, data)

    def close_workbook(self):
        self.__workbook.close()


def get_sms_list(latest_pk_id):
    cursor = mysql_connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
           SELECT id, mobile_no, message_body, upazilla_id
           FROM tableName
           WHERE id > %s limit 100
       """ % latest_pk_id
    cursor.execute(query)
    sms_list = cursor.fetchall()
    cursor.close()
    return sms_list


def read_file():
    file = open("%s" % file_name, "r")
    last_id = None
    lines=file.read().split('\r\n')
    list_size=len(lines)
    #for data in file.readlines():
    for data in range(list_size):
        last_id = lines[data]
    file.close()
    return last_id


def write_to_txt_file(sms_excel_pk):
    write_file = open(file_name, 'a')
    write_file.write('\n' + str(sms_excel_pk))
    write_file.close()


def create_zip():
    now = datetime.datetime.now()
    dir_name = root_dir + os.sep
    base_path = now.strftime('%Y-%m-%d')
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    zip_file_name = now.strftime('%Y_%m_%d')
    zip_file_name += '_%s_%s_%s' % (now.hour, now.minute, now.second)
    shutil.make_archive(base_path + os.sep + zip_file_name, 'zip', root_dir=dir_name, base_dir=None)


if __name__ == '__main__':
    last_pk_id = read_file()
    print('latest pk id- %s' % last_pk_id)
    sms_list = get_sms_list(last_pk_id)
    sheet_no = 1
    start_index = 0
    end_index = 0
    max_size = 50000
    sms_size = len(sms_list)
    print('total-sms-count: %s' % sms_size)
    for index in range(0, sms_size, max_size):
        end_index += max_size
        if end_index > sms_size:
            end_index = sms_size
        excel = ExcelCreation(root_dir, 'sheet-%s' % sheet_no)
        excel.add_worksheet(sms_list[start_index:end_index])
        excel.close_workbook()
        sheet_no += 1
        start_index += max_size

    if end_index:
        write_to_txt_file(sms_list[end_index - 1]['id'])
        create_zip()
        shutil.rmtree(root_dir)
    print('total-sms-in-excel: %s' % total_sms_in_excel)
