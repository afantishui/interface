# _*_ coding:utf-8 _*_
'''
	导入模块
'''
import sys
import xlrd
import xlwt
import unittest
import os.path
import time 
import smtplib
from xlutils.copy import copy
from  email.mime.text import MIMEText
from email.utils import formataddr,parseaddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
sys.path.append("..")
from lib.logger import Logger
from interface.interface_method import Request

logger = Logger(logger="lib").getlog()
dir = os.path.dirname(os.path.abspath('.')) 
#print(dir + "/config/email.yaml")
#..\\testcases\\test_Data.xlsx
'''
	发送邮件
'''
def sendemail(filepath):
	import yaml
	path = dir + "/config/email.yaml"

	with open(r'..\\config\\email.yaml',"r",encoding='UTF-8') as f:
		datas = yaml.load(f)
	#data_file = open(r".\\config\\email.yaml","r")
	#datas = yaml.load(data_file)
	#data_file.close()

	from_addr = datas['fromemail']
	password  = datas['password']
	to_addr   = datas['toeamil']
	mail_con  = datas['title']

	msg = MIMEMultipart() #定义内嵌资源的邮件体
	msg['Subject'] = '接口自动化测试报告' #邮件标题
	msg['From']    = '自动化测试平台' #发件人署名
	msg['To']      = to_addr  #收件人
	msg['Date']    = time.strftime('%a, %d %b %Y %H:%M:%S %z') #发送时间
	#三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
	att = MIMEText(open(r'%s'%filepath, 'rb').read(), 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'  
	att["Content-Disposition"] = 'attachment; filename="pyresult.html"' #filename="pyresult.html 邮件附件名
	tex = MIMEText("这是测试报告的邮件，详情见附件",'plain','gb2312')
	msg.attach(tex)  # MIMEMultipart 对象附加 MIMEText 对象实例的内容
	msg.attach(att)
	try:
		smtp = smtplib.SMTP()
		server = smtplib.SMTP_SSL("smtp.qq.com",465)
		server.login(from_addr,password)
		server.sendmail(from_addr,to_addr,msg.as_string())
		logger.info('邮件发送成功')
		server.quit()
	except NameError as e:
		logger.error("Failed to quit the browser with %s" % e)

'''
	判断方法
'''

def assert_in(expect,json):
	if len(expect.split('=')) > 1:
		data = expect.split('&')
		result = dict([(item.split('=')) for item in data])
		value1=([(str(json[key])) for key in result.keys()])
		value2=([(str(value)) for value in result.values()])
		if value1==value2:
			return  'pass'
		else:
			return 'fail'
	else:
		#raise ('请填写期望值')
		print('请填写期望值')

'''
	获取excel数据操作
'''
def getdata_excel(filepath):
	#filepath = '..\\testcases\\inter_testcase.xlsx'
	f = xlrd.open_workbook(filepath)
	ex = f.sheets()[0]
	nrows = ex.nrows
	case_id_list     = []	#用例ID
	case_name_list   = []	#用例名称
	case_key_list    = []	#用例key
	case_con_list    = []	#用例内容
	case_url_list    = []	#用例url
	case_type_list   = []	#用例请求方式
	case_expect_list = []	#用例期望值
	case_result_list = []	#用例测试结果
	for i in range(1,nrows):
		case_id_list.append(ex.cell(i,0).value)
		case_name_list.append(ex.cell(i,1).value)
		case_key_list.append(ex.cell(i,2).value)
		case_con_list.append(ex.cell(i,3).value)
		case_url_list.append(ex.cell(i,4).value)
		case_type_list.append(ex.cell(i,5).value)
		case_expect_list.append(ex.cell(i,6).value)
	return case_id_list,case_name_list,case_key_list,case_con_list,case_url_list,case_type_list,case_expect_list

'''
	记录测试结果
'''
def save_result(time,total,passnum,fail):
	try:
		with open('..\\test_report\\result.txt','a') as f:
			f.write("%s|%s|%s|%s \n"%(time,total,passnum,fail))
	except:
		logger.info("'记录测试结果失败'")
