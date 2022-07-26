function pizzaOven(crustType, sauceType, cheeses, toppings){
    var order = [];
    order.crustType = crustType;
    order.sauceType = sauceType;
    order.cheeses = cheeses;
    order.toppings = toppings;
    return order;
}

function randomOrder(){
    var ranCrust = Math.floor(Math.random() * 2);
    var ranSauce = Math.floor(Math.random() * 2);
    var ranCheese = Math.floor(Math.random() * 3);
    var ranToppings = Math.floor(Math.random() * 4);
    var ranpizza =[];

    // crust generator
    if(ranCrust == 0){
        ranpizza.push("deep dish");
    }
    else{
        ranpizza.push("hand tossed");
    }
    // sauce generator
    if(ranSauce == 0){
        ranpizza.push("traditional");
    }
    else{
        ranpizza.push("marinara");
    }
    // cheese generator
    if(ranCheese == 0){
        ranpizza.push("mozarella");
    }
    else if (ranCheese == 1){
        ranpizza.push(["mozzarella", "feta"]);
    }
    else{
        ranpizza.push("cheddar");
    }
    // topping generatoor
    if(ranToppings == 0){
        ranpizza.push(["pepperoni", "sausage"]);
    }
    else if(ranToppings == 1){
        ranpizza.push(["mushrooms", "olives", "onions"]);
    }
    else if (ranToppings == 2){
        ranpizza.push(["ham", "pineapple"]);
    }
    else{
        ranpizza.push("anchovies");
    }
    if(ranCrust == 0 & ranSauce == 0 & ranToppings == 2 & ranCheese == 0){
        console.log("Congratulations! You've created a masterpiece!");
        console.log("Your skill in cooking has increased! (42)");
    }
    return ranpizza;
}
var order1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
console.log("order 1 is: ");
// console.log(order1);

var order2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log("order 2 is: ");
// console.log(order2);
var pizza3 = randomOrder();
var order3 = pizzaOven(pizza3[0], pizza3[1], pizza3[2], pizza3[3]);
console.log("random order is: ");
console.log(order3);