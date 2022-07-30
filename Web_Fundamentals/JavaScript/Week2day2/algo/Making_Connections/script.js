function Name_Change() {
    document.querySelector("#cardname").innerText = "John Deer";
}

function friendAccept(elem){
    if(elem == 1){
        const element = document.getElementById("connection1");
        element.remove();
        // subtract connection requests
        var connectionRequests = document.querySelector("#num_requests");
        var num = connectionRequests.innerText;
        num--;
        connectionRequests.innerText = num;
        // add to your connections
        var yourConnections = document.querySelector("#current_connections");
        num = yourConnections.innerText;
        num++;
        yourConnections.innerText = num;
    }
    if(elem == 2){
        const element = document.getElementById("connection2");
        element.remove();
        // subtract connection requests
        var connectionRequests = document.querySelector("#num_requests");
        var num = connectionRequests.innerText;
        num--;
        connectionRequests.innerText = num;
        // add to your connections
        var yourConnections = document.querySelector("#current_connections");
        num = yourConnections.innerText;
        num++;
        yourConnections.innerText = num;
    }
}


function friendDecline(elem){
    if(elem == 1){
        const element = document.getElementById("connection1");
        element.remove();
        // subtract connection requests
        var connectionRequests = document.querySelector("#num_requests");
        var num = connectionRequests.innerText;
        num--;
        connectionRequests.innerText = num;
    }
    if(elem == 2){
        const element = document.getElementById("connection2");
        element.remove();
        // subtract connection requests
        var connectionRequests = document.querySelector("#num_requests");
        var num = connectionRequests.innerText;
        num--;
        connectionRequests.innerText = num;
    }
}

