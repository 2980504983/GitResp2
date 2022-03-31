// 针对log页定义一个对象
var log = {
    startdt:"2019-8-5",
    enddt:"2019-9-5",
    updatedt:"2019-8-5",
    anchor:"QYZW"
}

// 由对象派生业务逻辑(通过点语法),中间层,对一些功能进行封装
log.submit={

    // 验证某个值是否为空,为空返回真,否则返回假
    check:function(v){
        // 如果v为空就返回true否则返回false
        var _v=(v=="")?true:false;
        return _v;
    },

    authohide: function(obj){
        setTimeout(function(){
            setTimeout(function(){
                obj.hide()
            }, 2000)
        })
    }

}


// 定义一个验证内容是否为空的函数
function checkvalue(){
    // 获取元素对象,并保存在变量中,每个变量名前都有一个$表示，是使用jquery进行定位的
    var $username=$("#username");
    var $password=$("#password");
    var $err1=$("#err1");
    var $err2=$("#err2");
    // 当用户名和密码都不为空时
    if($username.val()!=""&&$password.val()!=""){
        // 直接提交
        console.log(1);
        return true;
    }else{
        // 如果用户名为空时
        if($username.val()==""){
            $err1.show();
            // 通过点语法调用封装好的方法
            log.submit.authohide($err1);
            return false;
        // 密码为空时
        }else{
            $err2.show();
            log.submit.authohide($err2);
            return false;
        }
    }
        
}


// 绑定按钮单击事件,表单提交时触发
$(function(){
    var $form=$("form");
    var $btn=$(".btn>input");
})


// 定义一个基于列表页的业务逻辑
var lst={
    template:function(t,u,p1,p2){
        var _html = "";
            _html += '<div class="item">';
            _html += '<div class="title">';
            _html += '     <h3>Python'+t+'</h3>';
            _html += '</div>';
            _html += '<div class="con">';
            _html += '    <div class="cleft">';
            _html += '        <img src="'+u+'" alt="图片加载失败">';
            _html += '    </div>';
            _html += '    <div class="cright">';
            _html += '             <p class="ptop">'+p1+'</p>';
            _html += '             <p class="pbottom">'+p2+'</p>';
            _html += '    </div>';
            _html += '</div>';
            _html += '</div>';
            return _html;
    }
}
// 使用数组保存展示的数据
var arrDate=[
    {
        t:'python语言的优势',
        u:'./imgs/haaminCG_25.jpg',
        p1:'llllllll',
        p2:'iiiiiiiiiiiiiiiiiiiii'
    },
    {
        t:'python语言的优势',
        u:'./imgs/haaminCG_25.jpg',
        p1:'llllllllllllllllllll',
        p2:'iiiiiiiiiiiiiiiiiiiii'

    },
    {
        t:'web语言的优势',
        u:'./imgs/haaminCG_25.jpg',
        p1:'llllllllllllllllllll',
        p2:'iiiiiiiiiiiiiiiiiiiii'
    }]

// 使用流程
// 1 遍历数组获取每一项元素对象
// 2 将获取的元素对象填充到模板中
// 3 象页面元素追加模板
for(var i=0;i<arrDate.length;i++){
    // 通过模板生成新的列表数据
    var _HTML = lst.template(arrDate[i].t, arrDate[i].u, arrDate[i].p1, arrDate[i].p2);   
    // 将数据追加到页面中
    $(".lst").append(_HTML);
}


// 定义一个基于我的图片页的业务逻辑对象
var pics={
    template:function(u,n,t){
        var _html="";
        _html+='<div class="item">';
        _html+='<div class="imgs">';
        _html+='    <img src="'+u+'" alt="图片显示失败">';
        _html+='    <div class="tip">喜欢 | '+n+'</div>';
        _html+='</div>';
        _html+='<div class="title">';
        _html+='    <h3>'+t+'</h3>';
        _html+='</div>';
        _html+='</div>';
        return _html;
    }
}
// 定义一个包含三个对象内容的图片数组
var arrPics=[
    {
        u:'./imgs/haaminCG_05.jpg',
        n:2223,
        t:'wsbhzqcdxt'
    },{
        u:'./imgs/haaminCG_25.jpg',
        n:2223,
        t:'wsbhzqcdxt'
    },{
        u:'./imgs/MichinokuCG_07.jpg',
        n:2223,
        t:'wsbhzqcdxt'
    }]
for(var j=0;j<arrPics.length;j++){
    // 向模板中填充内容
    var _HTML=pics.template(arrPics[j].u, arrPics[j].n, arrPics[j].t)
    // 将模板追加到页面元素中
    $("#pics").append(_HTML);
}