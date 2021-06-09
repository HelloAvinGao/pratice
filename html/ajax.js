    //ajax model
    function ajax(url, method, msg, fn, id,innerHTMLId) {
        var xmlhttp;
        if(window.XMLHttpRequest){
            xmlhttp=new XMLHttpRequest();
        }else {
            xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange=function(){
            if(xmlhttp.readyState==4 && xmlhttp.status==200){
                fn(xmlhttp.responseText, url, id,innerHTMLId)
            }
        }
        xmlhttp.open(method,url,true);
        xmlhttp.send(msg);
    }