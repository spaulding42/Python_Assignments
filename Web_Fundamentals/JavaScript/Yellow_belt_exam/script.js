// increases the score depending on what team was clicked
function increase_Score(elem){
    var num = elem.innerText;
    num++;
    elem.innerText = num;
    if(elem.id == "sjScore"){
        document.querySelector("#mini_ninja_score").innerText = num;
    }
    if(elem.id == "nsScore"){
        document.querySelector("#mini_pirate_score").innerText = num;
    }
}

// removes the subscribe section when clicked
function sub(){
    document.querySelector("#sub_box").remove();
}

// alert that the game as ended
function game_ended(){
    alert("The game has ended! Ninjas Won!!");
}

// adjusts the value on the screen
function changeTimeRemaining(countdown){
    var current = document.querySelector("#miniTimer").innerText;
    current--;
    document.querySelector("#miniTimer").innerText = current;
    if (current == 9){
        document.querySelector("#pre-timer").innerText = "0:0";
    }
    console.log(current);
}
// Countdown----------------------------
console.log("Time Remaining: ");
setTimeout(changeTimeRemaining, 1000);
setTimeout(changeTimeRemaining, 2000);
setTimeout(changeTimeRemaining, 3000);
setTimeout(changeTimeRemaining, 4000);
setTimeout(changeTimeRemaining, 5000);
setTimeout(changeTimeRemaining, 6000);
setTimeout(changeTimeRemaining, 7000);
setTimeout(changeTimeRemaining, 8000);
setTimeout(changeTimeRemaining, 9000);
setTimeout(changeTimeRemaining, 10000);
setTimeout(changeTimeRemaining, 11000);
setTimeout(changeTimeRemaining, 12000);
setTimeout(changeTimeRemaining, 12900);

setTimeout(game_ended, 13000);
