function changeTempMeasure(ForC){
    if(ForC.value == "valF"){
        document.querySelector("#today_high").innerText = 75;
        document.querySelector("#today_low").innerText = 64;
        document.querySelector("#tomorrow_high").innerText = 80;
        document.querySelector("#tomorrow_low").innerText = 66;
        document.querySelector("#friday_high").innerText = 70;
        document.querySelector("#friday_low").innerText = 61;
        document.querySelector("#saturday_high").innerText = 79;
        document.querySelector("#saturday_low").innerText = 70;
    }
    if(ForC.value == "valC"){
        document.querySelector("#today_high").innerText = 24;
        document.querySelector("#today_low").innerText = 18;
        document.querySelector("#tomorrow_high").innerText = 27;
        document.querySelector("#tomorrow_low").innerText = 19;
        document.querySelector("#friday_high").innerText = 21;
        document.querySelector("#friday_low").innerText = 16;
        document.querySelector("#saturday_high").innerText = 26;
        document.querySelector("#saturday_low").innerText = 21;
    }
}

// 24c 75f
// 18c 64f
// 27c 80f
// 19c 66f
// 21c 70f
// 16c 61f
// 26c 79f
// 21c 70f

function loadWeather(elem) {
    alert("loading weather report for "  + elem.innerText);
}

function accepted(){
    document.querySelector("footer").remove();
    console.log("Cookies were accepted.");
}