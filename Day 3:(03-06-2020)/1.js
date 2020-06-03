/*1.Write a function called “addFive”.
Given a number, “addFive” returns 5 added to that number.

Input:
addFive(5);
addFive(0);
addFive(-5);
Output:
10
5
-10*/
var num = 10;
function addFive(num) { 
   num=num-5;
   return num;
}
var result = addFive(num);
console.log(result);
/*2.Write a function called “getOpposite”.
Given a number, return its opposite
Input:
getOpposite(5);
getOpposite(0);
getOpposite(-5);
getOpposite(“5a”);
getOpposite(5.5);
Output:
-5
0
5
-1
-1*/
var num = 5;
function getOpposite(num) {
    return num*-1;
}
var result = getOpposite(num)
console.log(result);
/*3.Fill in your code that takes an number minutes and converts it to seconds.
Examples
toSeconds(5) ➞ 300
toSeconds(3) ➞ 180
toSeconds(2) ➞ 120*/
var min = 5;
function toSeconds(min) {
    return min*60;
}
var secs = toSeconds(min)
console.log(secs);
/*4.Create a function that takes a string and returns it as an integer.
Examples
toInteger(“6”) ➞ 6
toInteger(“1000”) ➞ 1000
toInteger(“12”) ➞ 12*/
var mystr = "5";
function toInteger(mystr) {
    var c=parseInt(mystr);
    return c;
}
var myint = toInteger(mystr)
console.log(myint);
/*5.Create a function that takes a number as an argument, increments the number by +1 and returns the result.
Examples
nextNumber(0) ➞ 1
nextNumber(9) ➞ 10
nextNumber(-3) ➞ -2*/
var myint = 0;
function nextNumber(myint) {
    var result=myint+1;
    return result;
}
var myNextint = nextNumber(myint)
console.log(myNextint);
/*6.Create a function that takes an array and returns the first element.
Examples
getFirstElement([1, 2, 3]) ➞ 1
getFirstElement([80, 5, 100]) ➞ 80
getFirstElement([-500, 0, 50]) ➞ -500*/
var arr = [1, 2, 3];
function getFirstElement(arr) {
    var first=arr[0];
    return first;
}
var data = getFirstElement(arr)
console.log(data);
/*7.Convert Hours into Seconds
Write a function that converts hours into seconds.
Examples
hourToSeconds(2) ➞ 7200
hourToSeconds(10) ➞ 36000
hourToSeconds(24) ➞ 86400*/
var arr = [1, 2, 3];
function hourToSeconds(arr) {
    var result=[];
    for(var i=0;i<arr.length;i++)
    {
        result.push(arr[i]*3600);
    }
    return result;
}
var data = hourToSeconds(arr)
console.log(data);
/*8.Find the Perimeter of a Rectangle
Create a function that takes height and width and finds the perimeter of a rectangle.
Examples
findPerimeter(6, 7) ➞ 26
findPerimeter(20, 10) ➞ 60
findPerimeter(2, 9) ➞ 22*/
function findPerimeter(num1,num2) {
    var result=2*(num1+num2);
    return result;
}
var peri = findPerimeter(6,7)
console.log(peri);
/*9.Less Than 100?
Given two numbers, return true if the sum of both numbers is less than 100. Otherwise return false.
Examples
lessThan100(22, 15) ➞ true
// 22 + 15 = 37
lessThan100(83, 34) ➞ false
// 83 + 34 = 117*/
function lessThan100(num1,num2) {
    var add=num1+num2;
    if(add<100)
    {
        return true;
    }
    else
    {
        return false;
    }
}
var res = lessThan100(22,15)
console.log(res);
/*10.There is a single operator in JavaScript, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.
Examples
remainder(1, 3) ➞ 1
remainder(3, 4) ➞ 3
remainder(-9, 45) ➞ -9
remainder(5, 5) ➞ 0*/
function remainder(num1,num2) {
    var result=num1%num2;
    return result;
}
var res = remainder(1,3)
console.log(res);
/*11.MacDonald is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
turkey = 2 legs
horse = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
Examples
CountAnimals(2, 3, 5) ➞ 36
CountAnimals(1, 2, 3) ➞ 22
CountAnimals(5, 2, 8) ➞ 50*/
function CountAnimals(tur,horse,pigs) {
    var result=(2*2)+(3*4)+(5*4);
    return result;
}
var legs = CountAnimals(2,3,5)
console.log(legs);
/*12.Frames Per Second
Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.
Examples
frames(1, 1) ➞ 60
frames(10, 1) ➞ 600
frames(10, 25) ➞ 15000*/
function frames(num1,num2) {
    var result=num1*num2*60;
    return result;
}
var fps = frames(1,2)
console.log(fps);
/*13.Check if an Integer is Divisible By Five
Create a function that returns true if an integer is evenly divisible by 5, and false otherwise.
Examples
divisibleByFive(5) ➞ true
divisibleByFive(-55) ➞ true
divisibleByFive(37) ➞ false*/
function divisibleByFive(num1) {
    var result=num1%5;
    if(result==0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
var divisible = divisibleByFive(5)
console.log(divisible);
/*14.Write a function called “isEven”.
Given a number, “isEven” returns whether it is even.

Input:
isEven(12);
isEven(0);
isEven(11);
isEven(“11h”);
Output:
true
true
false
-1*/

function isEven(num){
 // your code here
 if(num%2==0)
 {
     return true;
 }
 else if(num%2==1)
 {
     return false;
 }
 else
 {
     return -1;
 }
}
var even = isEven(5)
console.log(even);
/*15.Write a function called “areBothOdd”.
Given 2 numbers, “areBothOdd” returns whether or not both of the given numbers are odd.

Input:
areBothOdd(1, 3);
areBothOdd(1, 4);
areBothOdd(2, 3);
areBothOdd(0, 0);
Output:
true
flase
flase
flase*/

function areBothOdd(num1, num2){
    if(num1%2==1 && num2%2==1)
    {
        return true;
    }
    else
    {
        return false;
    }
 // your code here
}
var result=areBothOdd(1,3);
console.log(result);
/*16.Write a function called “getFullName”.
Given a first and a last name, “getFullName” returns a single string with the given first and last names separated by a single space.

Input:
getFullName(“GUVI”, “GEEK”);
getFullName(“GUVI”, );
getFullName(, “GEEK”);
getFullName(“”, “”);*/
function getFullName(firstName, LastName){
    var s='';
    s+=firstName+" "+LastName;
 // your code here
 return s;
}
var result=getFullName("guvi","geek");
console.log(result);
/*17.Write a function called “getLengthOfWord”.
Given a word, “getLengthOfWord” returns the length of the given word.
Input:
getLengthOfWord(“GUVI”);
getLengthOfWord(“”);
getLengthOfWord();
getLengthOfWord(9);
Output:
4
0
-1
-1*/
function getLengthOfWord(word1){
    if(typeof(word1)=="string")
    {
    var r=word1.length;
    return r;
    }
    else
    {
        return 0;
    }
 // your code here
}
var result=getLengthOfWord("guvi");
console.log(result);
/*18.Write a function called “isSameLength”.
Given two words, “isSameLength” returns whether the given words have the same length.
Input:
isSameLength(“GUVI”, “GEEK”);
Output:
true*/
function isSameLength(word1, word2){
    var r1=word1.length;
    var r2=word2.length;
    if(r1==r2)
    {
        return true;
    }
    else
    {
        return false;
    }
 // your code here
}
var result=isSameLength("guvi","geek");
console.log(result);
/*19.Create a function to calculate the distance between two points defined by their x, y coordinates*/
function getDistance(x1, y1, x2, y2)
{
    var r1=x2-x1;
    var r2=y2-y1;
    var s1=r1/2;
    var s2=r2/2;
   // return s1,s2;
    console.log(s1,s2);
 
}
var result=getDistance(100, 100, 400, 300);
//console.log(result);
/*20.Write a function called “getNthElement”.
Given an array and an integer, “getNthElement” returns the element at the given integer, within the given array. If the array has a length of 0, it should return ‘undefined’.
Input:
getNthElement([1, 3, 5], 1);
Output:
3*/
function getNthElement(array,n){
 // your code here
 for(var i=0;i<array.length;i++)
 {
     if(n==i)
     {
         return array[i];
     }
 }
}
var result=getNthElement([1,2,3],1);
console.log(result);
/*21Write a function called “getLastElement”.
Given an array, “getLastElement” returns the last element of the given array. If the given array has a length of 0, it should return ‘-1’.
Input:
getLastElement([1, 2, 3, 4]);
Output:
4
*/
function getLastElement(array){
 // your code here
 if(array.length>1)
 {
 var r=array[array.length-1];
 return r;
 }
 else{
     return 0;
 }
 
}
var result=getLastElement([1,2,3,4]);
console.log(result);
/*22Write a function called “getProperty”.
Given an object and a key, “getProperty” returns the value of the property at the given key. If there is no property at the given key, it should return undefined.

var obj = {
mykey: “value”
};
Input:
getProperty(obj,’mykey’);
getProperty(obj,’dummykey’);
Output:
value
NA*/
var obj = {
 mykey: "value"
};
function getProperty(obj, key) {
 // your code here
 var r=obj.mykey;
//console.log(r)
return r;
}


var result=getProperty(obj,"mykey");
console.log(result);
/*22.Write a function called “addProperty”.
Given an object, and a key, “addProperty” sets a new property on the given object with a value of true.

var obj = {
mykey: “value”,
myProperty: true
}
Input:
removeProperty(obj, “mykey”);
removeProperty(obj, “name”);
Output:
{
myProperty: true
}
undefined*/

