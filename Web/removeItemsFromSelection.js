function deleteItems(){
    
    var color = event.target.id.toLowerCase();
    
    var colorSelect = document.getElementById("colorSelect");

    for (let i of colorSelect.options){
        console.log(i.value.toLowerCase(), color, i.value.toLowerCase() == color)
        if(i.value.toLowerCase() == color){
            console.log("actually deleted:" + i.value)
            colorSelect.remove(i.index);
            break;
        }
    }
}
