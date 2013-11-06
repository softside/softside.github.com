function show_post(name){
    $("#list_container").html("");
    $("#list_container").hide();
    $("#loading").show();
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
    $.getJSON("list.json",function(data){
        console.log(data);
        $("#loading").hide();
        $("#list_container").show();
        tags = data['tags'];
        posts = data['data'];
        console.log(tags);
        render_tag_list(tags);
        render_list(posts);
    });

}

$(function(){
    var params=getParameter("p");
    if(_.isNull(params)){
        show_index();
    }else{
        show_post(params);
    }
});
