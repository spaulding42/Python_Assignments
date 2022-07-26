function remove(elem){
elem.remove();
}

function login_state(elem){
    if(elem.innerText == "Login"){
        elem.innerText = "Logout"
    }
    else{
        elem.innerText = "Login"
    }
}