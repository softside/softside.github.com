function getParameter(name){
    var search = document.location.search;
    var pattern = new RegExp("[?&]"+name+"\=([^&]+)", "g");
    var matcher = pattern.exec(search);
    var items = null;
    if(null != matcher){
        items = decodeURIComponent(matcher[1]);
    }
    return items;
}

function render_list(data){
    var source = $("#post_list_template").html();
    var template = Handlebars.compile(source)
    $("#list_container").html(template(data));
}

function show_post(name){
    $("#list_container").html("");
    $("#list_container").hide();
    $("#loading").show();
    $.get(
        "blogs/"+name,
        function(data){
            var converter = new Showdown.converter();
            var html = converter.makeHtml(data);
            $("#post-text").html(html);
            $("#post-content").show();
            $("#loading").hide();
            hljs.tabReplace = '    ';
            hljs.initHighlighting();
        }
    );
}

function show_index(){
    $("#loading").show();
    $("#post-text").html("");
    $("#post-content").hide();
    $.getJSON(
        "tag.json",
        function(data){
            $("#loading").hide();
            $("#list_container").show();
            render_list(data);
        }
    );
}

$(function(){
    var params=getParameter("p");
    if(_.isNull(params)){
        show_index();
    }else{
        show_post(params);
    }
}
 );
