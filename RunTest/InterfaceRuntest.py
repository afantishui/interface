# -*- coding: utf-8 -*-
import unittest
import datetime
import time
import sys
import os

#if module_path not in sys.path:
sys.path.append('D:\GitHub\interface')
from testsuites.inter_test_case import test_interface
from lib.lib import getdata_excel
from lib.lib import sendemail
from lib.lib import save_result
from lib.html import createHtml
from lib.Excel_reportx import create_interface_report
# from lib.logger import Logger
import threading # 操作线程的模块
#logger = Logger(logger="run_interface_email").getlog()
case_path = os.path.abspath(os.getcwd() + '\\..')
def report_email():
	filepath1 = 'D:\GitHub\interface\\testcases\\inter_testcase.xlsx'
	starttime = datetime.datetime.now()#开始时间
	filetime  = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) # 获取日期
	path      = os.path.dirname(os.path.abspath('.')) #保存报告的相对路径
	case_id_list,case_name_list,case_key_list,case_con_list,case_url_list,case_type_list,case_expect_list = getdata_excel(filepath1)
	list_pass,list_fail,list_json,list_result,list_len = test_interface()
	# filepath = os.path.join(path + '\\test_report\\%s-interface-result.html' %filetime) # 拼接报告保存路径
	filepath  = 'D:\\GitHub\\interface\\test_report\\%s-interface_result.xls' %filetime
	if os.path.exists(filepath) is False:
		os.system(r'touch %s' % filepath)
	save_result(starttime,len(list_result),((list_pass)),list_fail) # 保存测试结果
	endtime = datetime.datetime.now()	
	createHtml(titles 	  = '接口测试报告',
				filepath  = filepath,
				starttime = starttime,
				endtime	  = endtime,
				passge    = list_pass,
				fail      = list_fail,
				id        = case_id_list,
				name      = case_name_list,
				key       = case_key_list,
				coneent   = case_con_list,
				url       = case_url_list,
				meth      = case_type_list,
				yuqi      = case_expect_list,
				json      = list_json,
				relusts   = list_result)
	sendemail(filepath)

def report_excel():

	filepath1 = 'D:\GitHub\interface\\testcases\\inter_testcase.xlsx'
	starttime = datetime.datetime.now()
	filetime  = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	basdir   = os.path.dirname(os.path.abspath('.')) #保存报告的相对路径
	case_id_list,case_name_list,case_key_list,case_con_list,case_url_list,case_type_list,case_expect_list = getdata_excel(filepath1)
	list_pass,list_fail,list_json,list_result,list_len = test_interface()
	# filepath  = os.path.join(basdir + '\\test_report\\%s-interface_result.xls' %filetime)
	filepath  = 'D:\\GitHub\\interface\\test_report\\%s-interface_result.xls' %filetime

	if os.path.exists(filepath) is False:
		os.system(r'touch %s' % filepath)
	save_result(starttime,len(list_result),((list_pass)),list_fail) #保存测试结果
	create_interface_report(filename=filepath,list_len=list_len,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=case_url_list,
			listkeys=case_key_list,listconeents=case_con_list, listtypes=case_type_list, listexpects=case_expect_list,
			listids=case_id_list, listresult=list_result, listnames=case_name_list)

def tThread():
	#参数target是一个可调用对象（也称为活动[activity]），在线程启动后执行
	m=threading.Thread(target=report_excel,args=())
	#m=threading.Thread(target=report_email,args=())
	m.run()
if __name__ == '__main__':
	tThread()

