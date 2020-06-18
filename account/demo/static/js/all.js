var func;
(function(){
func = {
        systeminfo:function(){
            let operatingInfo = navigator.userAgent;
            let isWin = (navigator.platform == "Win32") || (navigator.platform == "Windows");
            if (isWin) return 'Win';
            let isMac = (navigator.platform == "Mac68K") || (navigator.platform == "MacPPC") || (navigator.platform == "Macintosh") || (navigator.platform == "MacIntel");
            if (isMac) return "Mac";
            let isUnix = (navigator.platform == "X11") && !isWin && !isMac;
            if (isUnix) return "Unix";
            let isLinux = (String(navigator.platform).indexOf("Linux") > -1);
            if (isLinux) return "Linux";
            return "other";
        }
}
})()
