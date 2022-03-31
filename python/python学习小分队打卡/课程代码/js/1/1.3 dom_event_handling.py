"""
    dom event handling:
        event: refers(指向) to user's behavior or element's state(状态). Listen to related event by specified(指定) element
                and bind the event handler.
        event handler(处理): element listen to event, and executes(执行) automatically when an event occurs(发生)

        1 Event function classification(分类):
            1 mouse event:
                onclick
                ondblclick(双击)
                onmouseover(鼠标移入)
                onmouseout(鼠标移出)
                onmousemove(鼠标移动)
            2 document or element loaded:
                onload (元素或文档加载完毕)

            3 form control(控件) state monitoring(监听):
                onfocus(文本框获取焦点)
                onblur(文本框失去焦点)
                oninput(实时监听输入)
                onchange(两次输入内容发生变化是触发,或元素状态改变时触发)
                onsubmit(form元素监听,点击提交按钮后触发)

        2 event bind:
            1 inline(内联):
                Bind the event name to the element as a label(标签) property(属性)
                for example:
                    <button onclick="alert()">click</button>

            2 dynameic(动态) bind:
                get element node, add event dynameiclly
                for example:
                    btn.onclick = function(){

                    };
            3 using of event func:
                1 onload:
                    Often used to wait for the document to load before proceeding(执行) to the next step
                2 mouse event:
                3 form event:
                    onchange:
                    onsubmit:

            


"""