
const del_url_id = (id) => {
    console.log("delete url was called!");
    console.log(`del url id was called with id ${id}`);
    var hxr = new XMLHttpRequest();
    hxr.open("GET", `/rurl/${id}`);
    hxr.send(null);
    location.reload();
}