Handlebars.registerHelper("prettifyDate", function(timestamp) {
    return timestamp.slice(0,10);
});

function show_tag(){
    $("#tag_list").html("");
    $.get("tag.json",function(data){
        render_tag_list(data);
    });
}
function render_tag_list(data){
    var source = $("#tag_list_template").html();
    var template = Handlebars.compile(source)
    console.log(template)
    $("#tag_list").html(template(data));
}

/* handle tags*/
function render_list(data){
    var source = $("#post_list_template").html();
    var template = Handlebars.compile(source)
    $("#list_container").html(template(data));
}

function show_list(){
    $.getJSON("list.json",function(data){
        $("#loading").hide();
        $("#list_container").show();
        render_list(data);
    });
}
