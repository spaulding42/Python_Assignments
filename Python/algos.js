/* 
  Given a string,
  return a new string with the duplicate characters excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABCabcABCabcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

//bonus
const str5 = "aba"
const expected5 = "ba"

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
 function stringDedupe(str) {
    //Your code here
}

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));

/*****************************************************************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const strA = "hello";
const expectedA = "olleh";

const strB = "hello world";
const expectedB = "olleh dlrow";

const strC = "abc def ghi";
const expectedC = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */

 function reversewords(str) {
  let expected[ letter ] = str[ i ];
  for( let i = 0; < str.length; i++){
      let letter = str [ i ];
          if( expected[ letter ] ) {
              expected[ letter  ]++;
          }
          else expected [ letter ] = i
  }
}

function reversewords(str){
  
  // loops full array
  current_word = ""
  for(var i = 0; i < str.length;i++){
    
  }
}

console.log(reverseWords(strA)) //expectedA: olleh
console.log(reverseWords(strB)) //expectedB: olleh dlrow
console.log(reverseWords(strC)) //expectedC: cba fed ihg











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