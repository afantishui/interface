# -*- coding: utf-8 -*-
import requests
import json
import sys
sys.path.append("..") 
from lib.logger import Logger

logger = Logger(logger="interface_method").getlog()

class Request():
	def __init__(self):
		#请求头
		self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
	#get请求类型
	def get(self, url, params):
		try:
			r = requests.get(url, params = params, headers = self.headers)
			r.encoding = 'UTF-8' #设置文本编码
			json_response = json.loads(r.text) #str转成dict
			return json_response
		except Exception as e:
			logger.info("get请求出错，出错原因:%s" %e)
			return {}
	#get请求类型
	def post(self, url, params):
		data = json.dumps(params)#dict转成str
		try:
			r = requests.post(url, params = params, headers = self.headers)
			json_response = json.loads(r.text) #str转成dict
			return json_response
		except Exception as e:
			logger.info("post请求出错，出错原因:%s" %e)	
	#delete请求类型
	def delfile(self, url, params):
		try:
			del_word = requests.delete(url, params = params, headers = headers)
			json_response = json.loads(del_word.text)
			return json_response
		except Exception as e:
			logger.info("delete请求出错，出错原因:%s" %e)
			return {}

	#put请求类型
	def putfile(self, url, params):
		try:
			data = json.dumps(params) #dict转成str
			r = requests.put(url, data)
			json_response = json.loads(r.text) #str转成dict
			return json_response
		except Exception as e :
			logger.info("put请求出错，出错原因:%s" %e)
			return {}

reques = Request()
response = {}
class TestApi(object):

	def __init__(self,url,key,connent,re_type):
		self.url = url
		self.key = key
		self.connent = connent
		self.type = re_type

	def testapi(self):
		global response
		if self.type=='POST':
			self.parem = {'key': self.key, 'info': self.connent}
			response=reques.post(self.url,self.parem)
		elif self.type=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			response = reques.get(self.url, self.parem)
		return response
	#获得接口code
	def getcode(self):
		code=self.testapi()
		return code
	#获得接口json数据
	def getJson(self):
		json_data = self.testapi()
		return json_data
