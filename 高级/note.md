# 1 模块
- 一个模块就是一个包含python代码的文件,后缀名就是.py就可以.模块就是个python文件
- 模块的作用
   - 程序太大,,编写维护非常不方便,需要拆分
   - 模块可以增加代码复用
   - 当做命名空间使用,避免命名冲突
- 如何定义模块
   - 模块就是一个普通文件,所以任何代码可以直接书写
   - 不过根据模块的规范,最好在模块中编写一下内容
        - 函数(单一功能)
        - 类(相似功能的组合,或者类似业务模块)
        - 测试代码

- 如何使用模块
   - 模块直接导入
       - 假如模块名称直接以数字开头,需要借助importlib帮助
   - 语法
       
          import moudule_name
          moudle-name.function_name
         moudule_name.class_name
         
# 异常处理
- 执行try下面的语句
- 如果出现异常,则在except语句里查找对应常病进行处理
- 如果没有异常,则执行else语句
- 最后,不管是否出现异常,都要执行finally语句



# 调试技术
- 调试流程:单元测试->集成测试->交测试部
- 分类:
  - 静态调试:
  - 动态调试
# pdb调试
# pycharm调试
- run/debug模式
- 断点:程序在debug模式下,遇到断点就会暂停

# 单元测试


# LOG
- logging模块提供模块级别的函数记录日志
- 四大组件

# 日志相关概念
- 日志级别（level)
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARINT
    - ERROR
    - CRITTCAL
    - ALERT
    - EMERGENCY
- IOC操作=>不要频繁
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - site
    - level
    - 内容
- 成熟的第三方
    - log4j
    - log4php
    - logging

# Logging模块
   - 日志级别
   - 级别可以自定义
- 初始化/写日志示实例需要指定级别，只有当级别等于或高于指定级别才被记录
- 使用方式

# logging.basicConfig(**kwargs)  对root logger进行一次性配置
  - 只在第一次调用时起作用
  - 不配置logging则使用默认值
     - 输出：  sys.stder
     - 级别   WARNING
     - 格式   level:log_name:content
     
# logging模块处理流程
  - 四大组件
     - 日志器（logger):产生日志的一个接口
     - 处理器（handler）把产生日志发生到相应目的地
     - 过滤器（filter） 更精细的控制那些日志输出
     - 格式器（formatter） 对输出信息进行格式化
- logger
  - 产生一个日志
  - 操作
  - 如何得到一个logger对象Logging.getlogger()
- Hanlder
  - 把log发送到指定位置
  - 方法
     - setlevel
     - setformat
     - addfilter,removefilter
  - 不需要直接使用，handler是基类
  
     