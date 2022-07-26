function increaseLikes(button){
    if (button == 1){
        var elem = document.querySelector("#likednum");
        var num = elem.innerText;
        num++;
        elem.innerText = num;
    } else if(button == 2){
        var elem = document.querySelector("#likednum2");
        var num = elem.innerText;
        num++;
        elem.innerText = num;
    }
    else{
        var elem = document.querySelector("#likednum3");
        var num = elem.innerText;
        num++;
        elem.innerText = num;
    }
}