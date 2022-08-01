

// listening for movement input
document.addEventListener('keydown', function(event) {
    if (event.keyCode == 37) {
        console.log('Left was pressed');
        moveLeft();

    }
    else if (event.keyCode == 39) {
        console.log('right was pressed');
        moveRight();
    }
    else if(event.keyCode == 38){
        moveUp();
        console.log("up was pressed");
    }
    else if (event.keyCode == 40){
        moveDown();
        console.log("down was pressed");
    }
}, true);

// movement functions--------------------------------------
var box1 = document.querySelector("#box");
var x = 0;
var y = 0;

function moveLeft(){
    x -= 10;
    box1.style.left = x + "px";
}

function moveRight(){
    x += 10;
    box1.style.left = x + "px";
}

function moveUp(){
    y -= 10;
    box1.style.top =   y + "px";
}

function moveDown(){
    y += 10;
    box1.style.top =   y + "px";
}


// map Loading possibly??????????????????????????

