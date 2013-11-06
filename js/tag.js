function render_tag_item_list(data){
    var source = $("#post_list_template").html();
    var template = Handlebars.compile(source)
    $("#list_container").html(template(data));
}


function show_tag_item(params){
    $("#loading").show();
    $.getJSON("list.json",function(data){
        var result;
        $("#loading").hide();
        result = data.data.filter(function(node){return _.contains(node.tags,params);});
        $("#list_container").show();
        node = {'data':result,'name':params};
        console.log(node)
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
