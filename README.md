# interface
* 这个使用Python的requests模块做请求判断返回参数的自动化测试框架
* 从automation_demo里面分离出来。(https://github.com/afantishui/python_automation_demo)

## 所需环境
* Python3
* unittest
* xlutils
* 还有一些其他模块，遇报错时对应安装即可

## 目录结构

#### config
* email -- 邮件配置
* report -- 报告配置
#### interface
* interface_method--封装requests的四个方法，get,post,del,put,常用的是get跟post
#### lib
* excel_report --excel报告脚本，可在此修改excel报告样式
* html -- html报告，可在此修改excel报告样式
* lib -- 封装一些公用方法
* logger -- 日志类，输出日志方法
* OperateFile -- 文件操作的方法
#### logs 
* 存放日志
#### test_report 
* 存放测试报告
#### testcases 
* 存放测试用例，这里使用excel
#### testsuites 
* 处理测试用例并执行，返回结果
#### RunTest 
* InterfaceRuntest.py 执行脚本，可选输出excel报告或html报告
#### 批处理快速脚本

### 小结
* 当时写的时候处于学习阶段，并未用于实际项目
* 现在看回所写代码有些冗余，长时间未曾更新

### jenkins调试
![Image text] (https://github.com/afantishui/interface/jk.png)
