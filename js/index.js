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


function show_post(name){
    $("#list_container").html("");
    $("#list_container").hide();
    $("#loading").show();
    show_tag();
    $.get("blogs/"+name,function(data){
        var converter = new Showdown.converter();
        var html = converter.makeHtml(data);
        $("#post-text").html(html);
        $("#post-content").show();
        $("#loading").hide();
    });
}

function show_index(){
    $("#loading").show();
    $("#post-text").html("");
    $("#post-content").hide();
    show_tag();
    show_list();
}

$(function(){
    var params=getParameter("p");
    if(_.isNull(params)){
        show_index();
    }else{
        show_post(params);
    }
});
