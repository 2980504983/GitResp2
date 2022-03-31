"""
    lxml模块的使用
"""
from lxml import etree
text = """
	<link rel="canonical" href="https://www.lagou.com">
		<!-- 公共样式 -->	<!-- header样式 -->	<!-- footer样式 -->	<!-- 页面样式 -->  <!-- 动态token，防御伪造请求，重复提交 -->
  <script type="text/javascript">
    window.X_Anti_Forge_Token = '';
    window.X_Anti_Forge_Code = '';
</script>

    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/lg-www-fed/dep/mCustomScrollbar/css/mCustomScrollbar_ac2fb8b.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/lg-www-fed/pkg/layout_ce89d6c.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/lg-www-fed/pkg/index/page/index/main.html_aio_0c815ff.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/lg-www-fed/pkg/widgets_52f84b9.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/lg-www-fed/pkg/index/page/index/main.html_aio_2_c5b6df3.css" />
</head>
<body>
		<!-- 公共html -->
	<!-- 页面公用结构、velocity变量 --><input type="hidden" value="" name="userid" id="userid" />
	<!-- 城市分站 -->	<!-- header -->
		<!--C端头部通栏广告位-->
	<div id="top_bannerC" style="height: px;">
        
    <a rel="nofollow"  href="https://zhuanti.lagou.com/2022shengzhiji.html?utm_source=2022QMSZJ&enter_type=pc_top_toast"  style="height: px; background: url(https://www.lgstatic.com/i/image6/M00/71/D4/CioPOWIOGMWAFwwpAAAxWuOy22A408.PNG) center center no-repeat; background-color:#0150e6" target="_blank" data-lg-tj-id="bd00" data-lg-tj-no="idnull" data-lg-tj-cid="23675" class="tj_exposure"></a>
</div>
"""

# 创建element对象
html = etree.HTML(text)

# 通过xpath语法从HTML中提取数据
print(html.xpath('//script[1]/text()'))
