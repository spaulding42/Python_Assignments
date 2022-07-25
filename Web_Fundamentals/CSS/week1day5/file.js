function reverse(arr){
    var temp = 0;
    for(var i = 0; i < arr.length/2; i++){
        temp = arr[i];
        arr[i] = arr[arr.length-i-1];
        arr[arr.length-i-1] = temp;  
    }
    return array1;
}

var array1 = [1,2,3,4,5,6,7];
array1 = reverse(array1);

console.log("reversed");
console.log(array1);


temp = [];
for(var i = 0; i < array1.length; i++){
    temp.push(array1[array1.length-i-1]); 
}

console.log("re-reversed");
console.log(temp);