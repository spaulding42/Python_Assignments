/* 
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods
*/

const str1 = "lim";
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// Order of the output array does not matter

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */
function generateAnagrams(str,anagrams = []) { //don't be afraid to add parameters!
    //Your code here
  // base case
  // do things
  
  if (anagrams.includes(str)){
    return anagrams
  }
  else{
    anagrams.push(str)
    for (i = 0;i < str.length-1;i++){
      pointer = str[i]
      pointer2 = str[i+1]
      new_string[i] = pointer2
      str[str.length-1] =  
    }
    anagrams = generateAnagrams(str,anagrams,pointer)

  }



  
  
}

console.log(generateAnagrams(str1)) //["ilm", "iml", "lim", "lmi", "mil", "mli"] (order may vary, that's okay)


// /*
//   Recursive Binary Search
//   Input: SORTED array of ints, int value
//   Output: bool representing if value is found
//   Recursively search to find if the value exists, do not loop over every element.
//   Approach:
//   Take the middle item and compare it to the given value.
//   Based on that comparison, narrow your search to a particular section of the array
// */

// const nums1 = [1, 3, 5, 6];
// const searchNum1 = 4;
// const expected1 = false;

// const nums2 = [4, 5, 6, 8, 12];
// const searchNum2 = 8;
// const expected2 = true;

// const nums3 = [3, 4, 6, 8, 12];
// const searchNum3 = 3;
// const expected3 = true;

// /**
//  * Add params if needed for recursion
//  * Recursively performs a binary search (divide and conquer) to determine if
//  * the given sorted nums array contains the given number to search for.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} sortedNums
//  * @param {number} searchNum
//  * @returns {boolean} Whether the searchNum was found in the sortedNums array.
//  */
//  function binarySearch(sortedNums, searchNum) {
//     //Termination/fail case
//     search_index = Math.floor((sortedNums.length)/2) 
//     if (sortedNums.length === 0){
//       return false
//     }
//     if (sortedNums[search_index] == searchNum){
//       return true
//     }
//     else if (searchNum > sortedNums[search_index]){
//       for (var i = 0; i <= search_index; i++){
//         sortedNums.shift()
//         search_index -=1
//       }
//       return binarySearch(sortedNums,searchNum)
//     }
//     else if(searchNum < sortedNums[search_index]) {
//       for (var i = sortedNums.length-1; i >= search_index;i--){
//         sortedNums.pop()
//       }
//       return binarySearch(sortedNums,searchNum)

//     }
    
    
//     //success/base case
//     // recursive call(s)
// }


// console.log(binarySearch(nums1, searchNum1)); // false
// console.log(binarySearch(nums2, searchNum2)); // true
// console.log(binarySearch(nums3, searchNum3)); // true



// /* 
//   Return the fibonacci number at the nth position, recursively.
//   fib(n) = fib(n - 1) + fib(n - 2)
//   Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
//   The next number is found by adding up the two numbers before it,
//   starting with 0 and 1 as the first two numbers of the sequence.
// */

// const num1 = 0;
// const expected1 = 0;

// const num2 = 1;
// const expected2 = 1;

// const num3 = 2;
// const expected3 = 1;

// const num4 = 3;
// const expected4 = 2;

// const num5 = 4;
// const expected5 = 3;

// const num6 = 4000;
// const expected6 = 21;

// /**
//  * Recursively finds the nth number in the fibonacci sequence.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {number} num The position of the desired number in the fibonacci sequence.
//  * @returns {number} The fibonacci number at the given position.
//  * memoization <------- 
//  */
// // function fibonacci(num) {
// //     // edge case?
// //     // base case?
// //     if (num == 0){
// //       return 0
// //     }
// //     if (num == 1){
// //       return 1
// //     }
// //     // recursive call(s)
// //     return fibonacci(num -1) + fibonacci(num - 2)
// // }
// function fibonacci(num, memo) {
//   memo = memo || {}
//   if(memo[num]){
//       return memo[num]
//   }
//   else {
//       if (num == 1) {
//           return 1
//       }
//       if (num == 0){
//           return 0
//       }
//       // console.log("we're memoing something! and it is" + memo[num])
//       return memo[num] = fibonacci(num-1,memo) +fibonacci(num-2,memo)
//   }
// }

// // console.log(fibonacci(num1)) // Expected: 0
// // console.log(fibonacci(num2)) // Expected: 1
// // console.log(fibonacci(num3)) // Expected: 1
// // console.log(fibonacci(num4)) // Expected: 2
// // console.log(fibonacci(num5)) // Expected: 3
// console.log(fibonacci(4000)) // Expected: 21


// // /* 
// //   Recursive Factorial
// //   Input: integer
// //   Output: integer, product of ints from 1 up to given integer
  
// //   If less than zero, treat as zero.
// //   Bonus: If not integer, truncate (remove decimals).
  
// //   Experts tell us 0! is 1.
  
// //   rFact(3) = 6 (1*2*3)
// //   rFact(6.8) = 720 (1*2*3*4*5*6)
// // */

// const num1 = 3;
// const expected1 = 6;
// // Explanation: 1*2*3 = 6

// const num2 = 6.8;
// const expected2 = 720;
// // Explanation: 1*2*3*4*5*6 = 720

// const num3 = 0;
// const expected3 = 1;

// function factorial(n) {
//     if (n <= 1){
//       return 1
//     }
//     return factorial(Math.floor(n-1)) * Math.floor(n)
// }

// /*****************************************************************************/
// console.log(factorial(num1)) // 6
// console.log(factorial(num2)) // 720
// console.log(factorial(num3)) // 1

// /*
//   Sum To One Digit
//   Implement a function sumToOne(num)​ that,
//   given a number, sums that number’s digits
//   repeatedly until the sum is only one digit. Return
//   that final one digit result.
//   Tips:
//     to access digits from a number, need to convert it .toString() to access each digit via index
//     parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
//     isNaN(arg) used to check if something is NaN
// */

// const numA = 5;
// const expectedA = 5;

// const numB = 10;
// const expectedB = 1;

// const numC = 251;
// const expectedC = 7;

// const numD = 999; //9 + 9 + 9 = 27, 2 +7 = 9
// const expectedD = 9;
// /**
//  * Sums the given number's digits until the number becomes one digit.
//  * @param {number} num The number to sum to one digit.
//  * @returns {number} One digit.
//  */
// function sumToOneDigit(num) {
//     //Your code here
//     //Base case?
//     // Logic ?
//     // Recursive call / return
//   if(num < 10){
//     return num
//   }
//   const lastDigit = num %10;
//   const remainingNum = Math.floor(num/10)
//   return sumToOneDigit(lastDigit + sumToOneDigit(remainingNum))
// }

// console.log(sumToOneDigit(numA)) // 5
// console.log(sumToOneDigit(numB)) // 1
// console.log(sumToOneDigit(numC)) // 7
// console.log(sumToOneDigit(numD)) // 9

// 6
// const sumToOneDigit = (num) => {
//   if(num < 10){
//      return num;
//   }
//   const lastDigit = num % 10;
//   const remainingNum = Math.floor(num / 10);
//   return sumToOneDigit(lastDigit + sumToOneDigit(remainingNum));
// }

/*****************************************************************************/


// /* 
// Recursive Sigma
// Input: integer
// Output: sum of integers from 1 to Input integer
// */

// const num1 = 5;
// const expected1 = 15;
// // Explanation: (1+2+3+4+5)

// const num2 = 2.5;
// const expected2 = 3;
// // Explanation: (1+2)

// const num3 = -1;
// const expected3 = 0;

// /**
//  * Recursively sum the given int and every previous positive int.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {number} num
//  * @returns {number}
//  */

// function recursiveSigma(num) {
//     //Your code here
//     //Santize value?
//     //Base case?
//     if ( num < 1 ){
//         return 0
//     }
//     //Recursive call?
//     // num = Math.floor(num)
//     // return recursiveSigma(num-1)+num
//     return recursiveSigma(Math.floor(num-1))+Math.floor(num)
// }

// console.log(recursiveSigma(num1)); // 15
// console.log(recursiveSigma(num2)); // 3
// console.log(recursiveSigma(num3)); // 0

// /*****************************************************************************/

// /* 
//   Recursively sum an arr of ints
// */

// const numsA = [1, 2, 3];
// const expectedA = 6;

// const numsB = [1];
// const expectedB = 1;

// const numsC = [];
// const expectedC = 0;

// /**
//  * Add params if needed for recursion <-------
//  * Recursively sums the given array.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} nums
//  * @returns {number} The sum of the given nums.
//  */
// function sumArr(nums, i=0) {
//     //Your code here

//     //Base case?
//     if (i === nums.length){
//       return 0
//     }
//     //Any more logic?
//     //Recursive call?
    
//     return sumArr(nums, i+1 ) + nums[i];
// }

// console.log(sumArr(numsA)) // 6
// console.log(sumArr(numsB)) // 1
// console.log(sumArr(numsC)) // 0
/*****************************************************************************/


// /* 
//   Given an int to represent how much change is needed
//   calculate the fewest number of coins needed to create that change,
//   using the standard US denominations
// */
// // quarter = 25 cents, dime = 10, nickel = 5, penny = 1
// const cents1 = 25;
// const expected1 = { quarter: 1 };

// const cents2 = 50;
// const expected2 = { quarter: 2 };

// const cents3 = 9;
// const expected3 = { nickel: 1, penny: 4 };

// const cents4 = 99;
// const expected4 = { quarter: 3, dime: 2, penny: 4 };

// /**
//  * Calculates the fewest coins of the standard American denominations needed
//  *    to reach the given cents amount.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {number} cents
//  * @param {string} sick
//  * @returns {Object<string, number>} - A denomination table where the keys are
//  *    denomination names and the value is the amount of that denomination
//  *    needed.
//  */
// function fewestCoinChange(cents) {
//     //Your code here
//     //for loop for each type of coin denomination
//     //going from largest to least type of coin type
//     //use modulo 0
//     //introduce empty dictionary and append 
//     let expected = {}
//     let counter = 0
//     while (cents >= 25){
//         counter += 1
//         cents -= 25
//     }
//     // expected = {'quarter': counter}
//     if(cents != 0 ){
//         expected['quarter'] = counter
//     }
//     counter = 0

//     while ( cents >= 10){
//         counter += 1
//         cents -= 10
//     }

//     // expected = {'dime': counter}
//     if(cents != 0 ){
//         expected['dime'] = counter
//     }
//     counter = 0
//     while ( cents >= 5){
//         counter += 1
//         cents -= 5
//     }

//     // expected = {'nickle': counter}
//     if(cents != 0 ){
//         expected['nickle'] = counter
//     }
//     counter = 0
    
//     // expected = {'penny': cents}
//     if(cents != 0 ){
//         expected['penny'] = cents
//     }
//     return expected
// }


// console.log(fewestCoinChange(cents1)) // { quarter: 1 }
// console.log(fewestCoinChange(cents2)) // { quarter: 2 }
// console.log(fewestCoinChange(cents3)) // { nickel: 1, penny: 4 }
// console.log(fewestCoinChange(cents4)) // { quarter: 3, dime: 2, penny: 4 }


/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

// const nums1 = [1, 3, 5, 6,7,8 ,9];
// const searchNum1 = 4;
// const expected1 = false;

// const nums2 = [4, 5, 6, 8, 12];
// const searchNum2 = 5;
// const expected2 = true; //1 for bonus

// const nums3 = [3, 4, 6, 8, 12];
// const searchNum3 = 3;
// const expected3 = true; //1 for bonus

// // bonus, how many times does the search num appear?
// const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
// const searchNum4 = 7;
// const expected4 = 4;

// /**
//  * Efficiently determines if the given num exists in the given array.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} sortedNums
//  * @param {number} searchNum
//  * @returns {boolean} Whether the given num exists in the given array.
//  */
// function binarySearch(sortedNums, searchNum) {
//     search_index = Math.floor(sortedNums.length/2)
//     previous_index = search_index
//     count = 0
//     while (sortedNums[search_index] != searchNum){
//         if (sortedNums[search_index] > searchNum){
//             search_index = Math.floor(search_index/2)
//         }
//         else{
//             search_index = Math.floor((sortedNums.length + search_index)/2)
//         }
//         if (sortedNums[search_index] == searchNum){
//             count ++
//             break
//         }
//         if (search_index == previous_index){
//             return false
//         }
//     }
//     spread = 1
//     while (sortedNums[search_index] == searchNum){
//         found = count
//         if (sortedNums[search_index - spread] == searchNum){
//             count++
//         }
//         if (sortedNums[search_index + spread] == searchNum){
//             count++
//         }
//         if(found == count){
//             return count
//         }
//         spread++
//     }
//     return count
// }


// console.log(binarySearch(nums1, searchNum1)); // false
// console.log(binarySearch(nums2, searchNum2)); // true (1 for bonus)
// console.log(binarySearch(nums3, searchNum3)); // true (1 for bonus)

// // bonus, how many times does the search num appear?
// console.log(binarySearch(nums4, searchNum4)); // 4




// /* 
//   Given two arrays, interleave them into one new array.
//   The arrays may be different lengths. The extra items should be added to the
//   back of the new array.
// */

// const arrA1 = [1, 2, 3];
// const arrB1 = ["a", "b", "c"];
// const expected1 = [1, "a", 2, "b", 3, "c"];

// const arrA2 = [1, 3];
// const arrB2 = [2, 4, 6, 8];
// const expected2 = [1, 2, 3, 4, 6, 8];

// const arrA3 = [1, 3, 5, 7];
// const arrB3 = [2, 4];
// const expected3 = [1, 2, 3, 4, 5, 7];

// const arrA4 = [];
// const arrB4 = [42, 0, 6];
// const expected4 = [42, 0, 6];

// /**
//  * Interleaves two arrays into a new array. Interleaving means alternating
//  * the items starting from the first array.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<any>} arr1
//  * @param {Array<any>} arr2
//  * @returns {Array<any>} A new array of interleaved items.
//  */
// function interleaveArrays(arr1, arr2) {
//   if (arr1.length >= arr2.length) {
//     first = arr1
//     second = arr2
//   }
//   else {
//     first = arr2
//     second = arr1
//   }
//   result = []
//   flag=0
//   for(var i = 0; i < second.length; i++){
//     result.push(arr1[i])
//     result.push(arr2[i])
//     flag++
//   }
//   for(var i = flag; i < first.length; i++){
//     result.push(first[i])
//   }
//   return result
// }

// console.log(interleaveArrays(arrA1, arrB1))
// console.log(interleaveArrays(arrA2, arrB2))
// console.log(interleaveArrays(arrA3, arrB3))
// console.log(interleaveArrays(arrA4, arrB4))



// /* 
// Given an array of ints representing a line of people where the space between
// indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
// that space,
// return whether or not there is at least 6 feet separating every person.
// Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
// */

// const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
// const expected1 = false;

// const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected2 = true;

// const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected3 = true;

// const queue4 = [];
// const expected4 = true;

// /**
//  * Determines whether each occupied space in the line of people is separated by
//  * 6 empty spaces.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<0|1>} queue
//  * @returns {Boolean}
//  */
// function socialDistancingEnforcer(queue) {
//  //Your code here
// }

// console.log(socialDistancingEnforcer(queue1)) // false
// console.log(socialDistancingEnforcer(queue2)) // true
// console.log(socialDistancingEnforcer(queue3)) // true
// console.log(socialDistancingEnforcer(queue4)) // true

// /* 
//   Balance Index
//   Here, a balance point is ON an index, not between indices.
//   Return the balance index where sums are equal on either side
//   (exclude its own value).
  
//   Return -1 if none exist.
  
// */
//             // 0   1  2  3  4
// const numsA = [-2, 5, 7, 0, 3];
// const expectedA = 2;

// const numsB = [9, 9];
// const expectedB = -1;


// /**
//  * Finds the balance index in the given array where the sum to the left of the
//  *    index is equal to the sum to the right of the index.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} nums
//  * @returns {number} The balance index or -1 if there is none.
//  */
// function balanceIndex(nums) {
//     //Your code here
// }

// console.log(balanceIndex(numsA)) // 2
// console.log(balanceIndex(numsB)) // -1

// /* 
//   Given an array of objects / dictionaries to represent new inventory,
//   and an array of objects / dictionaries to represent current inventory,
//   update the quantities of the current inventory
  
//   if the item doesn't exist in current inventory, add it to the inventory
//   return the current inventory after updating it.
// */

// const newInv1 = [
  
//   { name: "Peanut Butter", quantity: 50 },
//   { name: "Grain of Rice", quantity: 9000 },
//   { name: "Royal Jelly", quantity: 20 },
// ];
// const currInv1 = [
//   { name: "Peanut Butter", quantity: 20 },
//   { name: "Grain of Rice", quantity: 1 },
// ];
// const expected1 = [
//   { name: "Peanut Butter", quantity: 70 },
//   { name: "Grain of Rice", quantity: 9001 },
//   { name: "Royal Jelly", quantity: 20 },
// ];




// const newInv2 = [];
// const currInv2 = [{ name: "Peanut Butter", quantity: 20 }];
// const expected2 = [{ name: "Peanut Butter", quantity: 20 }];




// const newInv3 = [{ name: "Peanut Butter", quantity: 20 }];
// const currInv3 = [];
// const expected3 = [{ name: "Peanut Butter", quantity: 20 }];

// /**
// * @typedef {Object} Inventory
// * @property {string} Inventory.name The name of the item.
// * @property {number} Inventory.quantity The quantity of the item.
// */

// /**
// * Updates the current inventory based on the new inventory.
// * - Time: O(?).
// * - Space: O(?).
// * @param {Array<Inventory>} newInv A shipment of new inventory.
// *    An array of inventory objects.
// * @param {Array<Inventory>} currInv
// * @return The currInv after being updated.
// */
// function updateInventory(newInv, currInv) {
//   for (let invItem of newInv){
//     let match = false;
//     for(let currentItem of currInv){
//       if (currentItem['name'] == invItem['name']){
//         match = true;
//         currentItem['quantity'] += invItem['quantity'];
//         break
//       }
      
//     }
//     if (!match){
//       currInv.push(invItem)
//     }
//   }
//   return currInv
// }

// console.log(updateInventory(newInv1, currInv1))
// console.log(updateInventory(newInv2, currInv2))
// console.log(updateInventory(newInv3, currInv3))




// /* 
//   String: Rotate String
//   Create a standalone function that accepts a string and an integer,
//   and rotates the characters in the string to the right by that given
//   integer amount.
// */

// const str = "Hello World";

// const rotateAmnt1 = 0;
// const expected1 = "Hello World";

// const rotateAmnt2 = 1;
// const expected2 = "dHello Worl";

// const rotateAmnt3 = 2;
// const expected3 = "ldHello Wor";

// const rotateAmnt4 = 4;
// const expected4 = "orldHello W";

// const rotateAmnt5 = 13; 
// const expected5 = "ldHello Wor";
// /* 
// Explanation: this is 2 more than the length so it ends up being the same
// as rotating it 2 characters because after rotating every letter it gets back
// to the original position.
// */

// /**
//  * Rotates a given string's characters to the right by the given amount,
//  * wrapping characters to the beginning.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @param {number} amnt The amount of characters in the given str to rotate to the
//  *    right.
//  * @returns {string} The string rotated by the given amount.
//  */
// function rotateStr(str, amnt) {
//     //Your code here
// }

// console.log(rotateStr(str, rotateAmnt1)); // expected: "Hello World"
// console.log(rotateStr(str, rotateAmnt2)); // expected: "dHello Worl"
// console.log(rotateStr(str, rotateAmnt3)); // expected: "ldHello Wor"
// console.log(rotateStr(str, rotateAmnt4)); // expected: "orldHello W"
// console.log(rotateStr(str, rotateAmnt5)); // expected: "ldHello Wor"


// /*****************************************************************************/

// /* 
//   Create the function isRotation(str1,str2) that
//   returns whether the second string is a rotation of the first.
// */

// const strA1 = "ABCD";
// const strA2 = "CDAB";
// // Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
// const expectedA = true;

// const strB1 = "ABCD";
// const strB2 = "CDBA";
// // Explanation: all same letters in 2nd string, but out of order
// const expectedB = false;

// const strC1 = "ABCD";
// const strC2 = "BCDAB";
// // Explanation: same letters in correct order but there is an extra letter.
// const expectedC = false;

// /**
//  * Determines whether the second string is a rotated version of the first.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} s1
//  * @param {string} s2
//  * @returns {boolean} Whether the second string is a rotated version of the 1st.
//  */
// function isRotation(s1, s2) {
// //Your code here
// }

// // console.log(isRotation(strA1, strA2)); // expected: true
// // console.log(isRotation(strB1, strB2)); // expected: false
// // console.log(isRotation(strC1, strC2)); // expected: false









// /* 
//   Given a string,
//   return a new string with the duplicate characters excluded
//   Bonus: Keep only the last instance of each character.
// */

// const str1 = "abcABCabcABCabcABC";
// const expected1 = "abcABC";

// const str2 = "helloo";
// const expected2 = "helo";

// const str3 = "";
// const expected3 = "";

// const str4 = "aa";
// const expected4 = "a";

// //bonus
// const str5 = "aba"
// const expected5 = "ba"

// /**
//  * De-dupes the given string.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str A string that may contain duplicates.
//  * @returns {string} The given string with any duplicate characters removed.
//  */
//  function stringDedupe(str) {
//     //Your code here
// }

// console.log(stringDedupe(str1));
// console.log(stringDedupe(str2));
// console.log(stringDedupe(str3));
// console.log(stringDedupe(str4));
// console.log(stringDedupe(str5));

// /*****************************************************************************/

// /* 
//   Given a string containing space separated words
//   Reverse each word in the string.
//   If you need to, use .split to start, then try to do it without.
// */

// const strA = "hello";
// const expectedA = "olleh";

// const strB = "hello world";
// const expectedB = "olleh dlrow";

// const strC = "abc def ghi";
// const expectedC = "cba fed ihg";

// /**
//  * Reverses the letters in each words in the given space separated
//  * string of words. Does NOT reverse the order of the words themselves.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str Contains space separated words.
//  * @returns {string} The given string with each word's letters reversed.
//  */

//  function reversewords(str) {
//   let expected[ letter ] = str[ i ];
//   for( let i = 0; < str.length; i++){
//       let letter = str [ i ];
//           if( expected[ letter ] ) {
//               expected[ letter  ]++;
//           }
//           else expected [ letter ] = i
//   }
// }

// function reversewords(str){
  
//   // loops full array
//   current_word = ""
//   for(var i = 0; i < str.length;i++){
    
//   }
// }

// console.log(reverseWords(strA)) //expectedA: olleh
// console.log(reverseWords(strB)) //expectedB: olleh dlrow
// console.log(reverseWords(strC)) //expectedC: cba fed ihg











// /* 
//   Given in an alumni interview in 2021.
//   String Encode
//   You are given a string that may contain sequences of consecutive characters.
//   Create a function to shorten a string by including the character,
//   then the number of times it appears. 
  
  
//   If final result is not shorter (such as "bb" => "b2" ),
//   return the original string.
//   */

//   const str1 = "aaaabbcddd";
//   const expected1 = "a4b2c1d3";
  
//   const str2 = "";
//   const expected2 = "";
  
//   const str3 = "a";
//   const expected3 = "a";
  
//   const str4 = "bbcc";
//   const expected4 = "bbcc";
  
//   /**
//    * Encodes the given string such that duplicate characters appear once followed
//    * by a number representing how many times the char occurs. Only encode strings
//    * when the result yields a shorter length.
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {string} str The string to encode.
//    * @returns {string} The given string encoded.
//    */
//   function encodeStr(str) {
//       current = ""
//       counter = 1
//       for (i = 0; i < str.length; i++){
//           current = str[i]
//           if (current == str[i+1]){
//             counter ++
//           }
//         }
//   }
//   console.log(encodeStr(str1)); // "a4b2c1d3"
//   console.log(encodeStr(str2)); // ""
//   console.log(encodeStr(str3)); // "a"
//   console.log(encodeStr(str4)); // "bbcc"
  
//   /*****************************************************************************/
  
  
//   const strA = "a3b2c1d3";
//   const expectedA = "aaabbcddd";
  
//   const strB = "a3b2c12d10";
//   const expectedB = "aaabbccccccccccccdddddddddd";
  
//   /**
//    * Decodes the given string by duplicating each character by the following int
//    * amount if there is an int after the character.
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {string} str An encoded string with characters that may have an int
//    *    after indicating how many times the character occurs.
//    * @returns {string} The given str decoded / expanded.
//    */
//   //helpful built-ins : isNaN() .repeat() parseInt() 
//   function decodeStr(str) {
//       //Your code here
//   }
  
//   console.log(decodeStr(strA)) // Expected: aaabbcddd
//   console.log(decodeStr(strB)) // Expected: aaabbccccccccccccdddddddddd