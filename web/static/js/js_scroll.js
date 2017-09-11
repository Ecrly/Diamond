/**
 * Created by guess on 2017/9/6.
 */
//滚动检测，实现导航栏动态变化
    var nav_show = 0
    $(window).scroll(function () {
        if($(window).scrollTop() > 10 && nav_show == 0) {
            $(".head-logo-img").addClass("head-logo-img-animation")
            $(".head-logo").addClass("head-logo-animation")
            $(".head-nav").fadeIn(3000)
            nav_show = 1
        }
    })