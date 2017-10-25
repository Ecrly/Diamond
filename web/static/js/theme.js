/**
 * Created by guess on 2017/9/6.
 */
    //滚动检测，实现导航栏动态变化
    var nav_show = 0
    $(window).scroll(function () {
        var windows_heigh = window.innerHeight
        var scroll_height = document.body.scrollHeight
        var scrollTop = $(document).scrollTop()
        var a = scrollTop/(scroll_height - windows_heigh) * 100
        a = a + "%"
        $(".scroll-top").css('width', a);
        // if($(window).scrollTop() > 10 && nav_show == 0) {
        //     $(".head-logo-img").addClass("head-logo-img-animation")
        //     $(".head-logo").addClass("head-logo-animation")
        //     $(".head-nav").fadeIn(3000)
        //     nav_show = 1
        // }

    })

    //hide and show of nav
    //and the main's position is changed
    //but it can't change gradually
    var is_hide = 1;
    $(document).ready(function () {
        $(".nav-div").click(function () {
            if(is_hide == 1){
                $(".nav-body").animate({ left: '0px'}, 500)
                $(".nav-div").animate({ top: '30px', left: '200px'}, 500)
                $(".article-left").removeClass("col-lg-2").addClass("col-lg-4")
                $(".article-right").removeClass("col-lg-2")
                is_hide = 0
            }else{
                $(".nav-body").animate({ left: '-250px'}, 500)
                $(".nav-div").animate({ top: '30px', left: '50px'}, 500)
                $(".article-left").removeClass("col-lg-4").addClass("col-lg-2")
                $(".article-right").addClass("col-lg-2")
                is_hide = 1
            }
        })
    })

    //show a hert when we click on the page
    $(document).ready(function () {
        $("body,html").click(function (e) {
            var sc = $(document).scrollTop()
            var x = e.clientX
            var y = e.clientY + sc
            var span = $("<span><i class='fa fa-heart'></i></span>")
            span.css('position', 'absolute')
            span.css('top', y)
            span.css('left', x)
            span.css('display', 'none')
            span.css('color', '#FF00FF')
            $("body").append(span)
            span.fadeIn(500, function () {
                // span.fadeOut(1500)
                span.animate({fontSize: '0px', top: '-=10px'}, 500, function () {
                    delete(span)
                })
                // delete(span)
            })
        })
    })

    // change theme between gray and default
    var is_gray = 0
    $(document).ready(function () {
        $(".theme-gray").click(function () {
            if(is_gray == 0){
                $(".body").addClass("body-gray")
                is_gray = 1
            }else{
                $(".body").removeClass("body-gray")
                is_gray = 0
            }
        })
    })

    // to enlarge the img when we click
    var img_show = 0
    var width = 0
    var height = 0
    var top = 0;
    var window_height = window.innerHeight
    var window_width = window.innerWidth
    $(document).ready(function () {
        $("img[src*='media']").click(function () {
            if(img_show == 0){
                var img_dom = $(this).clone(true)
                width = img_dom.width()
                height = img_dom.height()
                top = img_dom.offset().top
                img_dom.css('position', 'absolute').css('left', (window_width - width)/2).css('top', (window_height - height)/2)
                $(".img-div").append(img_dom).show()
                img_dom.animate({width: width * 1.5, height: height * 1.5, top: (window_height - height * 1.5)/2 , left:  (window_width - width * 1.5)/2}, 200)
                img_show = 1
            }else{
                $(".img-div").children().animate({width: width, height: height, top: (window_height- height)/2, left: (window_width - width)/2}, 200, function () {
                    $(".img-div").hide().empty()
                })
                img_show = 0
            }
        })
    })

    // article slide in
    var article_list = $(".article-slide")
     function  init() {
        var window_height = window.innerHeight
            var scroll_height = document.body.scrollHeight
            var scrollTop = $(document).scrollTop()
            for(var i in article_list){
                var div = article_list[i]
                var offsetH = div.offsetTop
                if(window_height - ((offsetH + 580) - scrollTop) >= 100){
                       $(div).addClass("add")
                }
            }
    }
    init()
        $(window).scroll(function(event){
// {#    var wScrollY = window.scrollY; // 当前滚动条位置#}
// {#    var wInnerH = window.innerHeight; // 设备窗口的高度（不会变）#}
// {#    var bScrollH = document.body.scrollHeight; // 滚动条总高度#}
// {#    if (wScrollY + wInnerH >= bScrollH - 50) {#}
// {#        alert("en")#}
// {#    }#}
// {#        var scollY = window.scrollY#}
// {#        var scollTop = $(document).scrollTop()#}
// {#        var innerHeight = window.innerHeight#}
// {#        var scollHeight = document.body.scrollHeight#}
// {#        console.log("scollTop " + scollTop + " scollHight " + scollHeight + " scollY" + scollY)#}
            var window_height = window.innerHeight
            var scroll_height = document.body.scrollHeight
            var scrollTop = $(document).scrollTop()
            for(var i in article_list){
                var div = article_list[i]
                var offsetH = div.offsetTop
                if(window_height - ((offsetH+580) - scrollTop) >= 100){
                       $(div).addClass("add")
                }
            }
        });

    //
var RandomColor = function () {
            var rgb = "rgba(" + Math.random() * 255 + "," + Math.random() * 255 + "," + Math.random() * 255 + "," + "0.5)"
            return rgb
        }
        $(document).ready(function () {
            $(".category-name").each(function () {
                var rgba = RandomColor()
                $(this).css('background-color', rgba)
            })
        })

    $(".article-abstract").mouseover(function () {
        $(this).addClass("article-abstract-after")
    })
    $('.article-detail-btn').mouseover(function () {
        $(this).addClass("article-detail-btn-add")
    })
    $('.article-title').mouseover(function () {
        $(this).addClass("article-title-after")
    })
    $('.article-info span').mouseover(function () {
        $(this).addClass('article-info-after')
    })