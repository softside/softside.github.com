function render_tag_item_list(data){
    var source = $("#post_list_template").html();
    var template = Handlebars.compile(source)
    $("#list_container").html(template(data));
}


function show_all_tags(){
    $("#loading").show();
    $.getJSON("tag.json",function(data){
        $("#loading").hide();
        $("#list_container").show();
        render_tag_item_list_list(data);
    });
}
function show_tag_item(params){
    $("#loading").show();
    $.getJSON("tag.json",function(data){
        var result;
        $("#loading").hide();
        result = data.data.filter(function(node){return node.name==params;});
        node = result[0];
        $("#list_container").show();
        node = {'data':[node]};
        render_tag_item_list(node);
    });
}

$(function(){
    var params=getParameter("tag");
    if(_.isNull(params)){
        show_all_tags();
    }else{
        show_tag_item(params);
    }
});
