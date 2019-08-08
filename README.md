## FLASK RESTFUL API 模板 （含JWT）

### 初始化环境

    Pycharm增加本地虚拟开发环境venv，Python 3.6+

    打开Terminal输入pip install -r requirements.txt

    运行程序输入: export DATABASE_URL=''; python manage.py run

    运行测试 : python manage.py tests
    
    查看Swagger文档: 浏览器访问http://0.0.0.0:5000/

### 初始化环境Docker
	本机需要安装Docker,docker-compose
	
	docker-compose up

### 删除系统中多余的docker image
    docker image ls|grep '<none>'|awk '{print $3 }'|xargs docker image rm -

### time的约定
    model定义里面全部使用utcnow， 例如timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    程序里面时间定义全部使用utcnow(), 例如 registered_on=datetime.datetime.utcnow()

### 数据库反映射model表

	sqlacodegen --noviews --noconstraints --noindexes --outfile models.py mysql://user:pass@localhost/dbname
	
	将models.py 中的INTEGER(11) 替换成INTEGER
	
### 命名规范

<table rules="all" border="1" summary="Guidelines from Guido's Recommendations"
       cellspacing="2" cellpadding="2">

  <tr>
    <th>Type</th>
    <th>Public</th>
    <th>Internal</th>
  </tr>

  <tr>
    <td>Packages</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Modules</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code></td>
  </tr>

  <tr>
    <td>Classes</td>
    <td><code>CapWords</code></td>
    <td><code>_CapWords</code></td>
  </tr>

  <tr>
    <td>Exceptions</td>
    <td><code>CapWords</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Functions</td>
    <td><code>lower_with_under()</code></td>
    <td><code>_lower_with_under()</code></td>
  </tr>

  <tr>
    <td>Global/Class Constants</td>
    <td><code>CAPS_WITH_UNDER</code></td>
    <td><code>_CAPS_WITH_UNDER</code></td>
  </tr>

  <tr>
    <td>Global/Class Variables</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code></td>
  </tr>

  <tr>
    <td>Instance Variables</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code> (protected)</td>
  </tr>

  <tr>
    <td>Method Names</td>
    <td><code>lower_with_under()</code></td>
    <td><code>_lower_with_under()</code> (protected)</td>
  </tr>

  <tr>
    <td>Function/Method Parameters</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Local Variables</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

</table>

[阅读google python 风格指南](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

[阅读goolge python 风格指南中文版](https://github.com/zh-google-styleguide/zh-google-styleguide/blob/master/google-python-styleguide/python_style_rules.rst)
	

### HTTP 返回值
```python
HTTP_STATUS_CODES = {
    100:    'Continue',
    101:    'Switching Protocols',
    102:    'Processing',
    200:    'OK',
    201:    'Created',
    202:    'Accepted',
    203:    'Non Authoritative Information',
    204:    'No Content',
    205:    'Reset Content',
    206:    'Partial Content',
    207:    'Multi Status',
    226:    'IM Used',              # see RFC 3229
    300:    'Multiple Choices',
    301:    'Moved Permanently',
    302:    'Found',
    303:    'See Other',
    304:    'Not Modified',
    305:    'Use Proxy',
    307:    'Temporary Redirect',
    400:    'Bad Request',
    401:    'Unauthorized',
    402:    'Payment Required',     # unused
    403:    'Forbidden',
    404:    'Not Found',
    405:    'Method Not Allowed',
    406:    'Not Acceptable',
    407:    'Proxy Authentication Required',
    408:    'Request Timeout',
    409:    'Conflict',
    410:    'Gone',
    411:    'Length Required',
    412:    'Precondition Failed',
    413:    'Request Entity Too Large',
    414:    'Request URI Too Long',
    415:    'Unsupported Media Type',
    416:    'Requested Range Not Satisfiable',
    417:    'Expectation Failed',
    418:    'I\'m a teapot',  # see RFC 2324
    422:    'Unprocessable Entity',
    423:    'Locked',
    424:    'Failed Dependency',
    426:    'Upgrade Required',
    428:    'Precondition Required',  # see RFC 6585
    429:    'Too Many Requests',
    431:    'Request Header Fields Too Large',
    449:    'Retry With',  # proprietary MS extension
    451:    'Unavailable For Legal Reasons',
    500:    'Internal Server Error',
    501:    'Not Implemented',
    502:    'Bad Gateway',
    503:    'Service Unavailable',
    504:    'Gateway Timeout',
    505:    'HTTP Version Not Supported',
    507:    'Insufficient Storage',
    510:    'Not Extended'
}
```