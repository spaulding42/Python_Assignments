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