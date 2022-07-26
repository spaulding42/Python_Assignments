function odds(num){
    for(var i=0; i <= num; i++){
        if(i%2==1){
            console.log(i);
        }
    }
}

function multiples_of_three(num){
    for(var i = num; i >= 0; i--){
        if(i%3==0){
            console.log(i);
        }
    }
}

function print_sequence(num){
    while(num >= -3.5){
        console.log(num)
        num = num - 1.5;
    }
}

function sigma(num){
    var sum = 0;
    for(var i= 1; i <=num; i++){
        sum= sum + i;
    }
    console.log(sum);
}

function factorial(num){
    var product = 1;
    for(var i = 1; i <= num; i++){
        product = product * i;
    }
    console.log(product);
}

// odds(20);

// multiples_of_three(100);

// print_sequence(4);

// sigma(100);

factorial(12);