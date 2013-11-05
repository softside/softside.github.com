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
