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

function render_tag_list(tags){
    var source = $("#tag_list_template").html();
    var template = Handlebars.compile(source);
    $("#tag_list").html(template({'tags':tags}));
}

/* handle tags*/
function render_list(data){
    var source = $("#post_list_template").html();
    var template = Handlebars.compile(source)
    console.log(data);
    $("#list_container").html(template({'data':data}));
}
