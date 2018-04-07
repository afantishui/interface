# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
#from interface.testapi import TestApi
from interface.interface_method import TestApi
from lib.lib import getdata_excel
from lib.lib import assert_in
from lib.logger import Logger

filepath = '..\\testcases\\inter_testcase.xlsx'
logger = Logger(logger="inter_test_caseb").getlog()
case_id_list,case_name_list,case_key_list,case_con_list,case_url_list,case_type_list,case_expect_list = getdata_excel(filepath)

def test_interface():
	list_pass   = 0
	list_fail   = 0
	list_json   = []
	list_result = []
	list_len    = len(case_url_list)
	for i in range(len(case_url_list)):
		api = TestApi(url = case_url_list[i], 
					  key = case_key_list[i], 
					  connent = case_con_list[i], 
					  re_type = case_type_list[i])
		apicode = api.getcode()
		apijson = api.getJson()
		logger.info('inputdata>参数:%s, url:%s ,返回:%s,预期:%s'%(case_con_list[i],case_url_list[i],apijson,case_expect_list[i]))
		assert_re = assert_in(expect = case_expect_list[i], json = apijson)
		if assert_re == 'pass':
			list_json.append(apijson)
			list_result.append('pass')
			list_pass += 1
		else:
			list_fail += 1
			list_result.append('fail')
			list_json.append(apijson)
	return list_pass,list_fail,list_json,list_result,list_len
