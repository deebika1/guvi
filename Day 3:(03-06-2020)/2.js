/*2. Do the below programs in anonymous function
2.1. Print odd numbers in an array*/
var array=[1,2,3,4,5];
var odd=function()
{
 var result=array.filter(function(a){
     return (a%2==1)
     })
     console.log(result);
}
odd();
/*2.2. Convert all the strings to title caps in a string array*/
var str1="deebika";
var title=function(){
    var first=str1[0].toUpperCase();
    //console.log(first);
    var s='';
    for(var i=1;i<str1.length;i++)
    {
        s+=str1[i];
    }
    first+=s;
    console.log(first);
    
}
title();
/*2.3. Sum of all numbers in an array*/
var array=[1,2,3,4,5];
var sum=function(){
    var add=array.reduce(function(sum1,a){
        //console.log(a);
        return sum1+=a
    })
    console.log(add);
    
}
sum();
/*2.4. Return all the prime numbers in an array*/
var array=[1,2,3,4,5];
var sum=function(){
    for(var i=0;i<array.length;i++)
    {
        var a=0;
        if(array[i]>1)
        {
        for(var j=2;j<=array[i];j++)
        {
            if(array[i]%j==0 && array[i]!=j)
            {
                a=1
                //console.log(array[i]);
            }
        }
        if(a==0)
        {
            console.log(array[i]);
        }
        }
    }
}
sum();
/*2.5. Return all the palindromes in an array*/
var str1="deebika";
var palindrome1=function(){
    var s='';
    for(var i=(str1.length)-1;i>=0;i--)
    {
        s+=str1[i];
    }
    //console.log(s);
    if(s==str1)
    {
        console.log("palindrome");
    }
    else
    {
        console.log("not palindrome");
    }
}

palindrome1();
/*2.7. Remove duplicates from an array*/
var array=[1,2,2,3,4];
var duplicate1=function(){
    var result=[];
    var c=0;
    for(var i=0;i<array.length;i++)
    {  c=0;
        for(var j=0;j<array.length;j++)
        {
            if(array[i]==array[j])
            {
                c=c+1;
            }
        }
        if(c<=1)
        {
            result.push(array[i]);
        }
        
    }
    console.log(result);
   
}
duplicate1();
/*2.8. Rotate an array by k times and return the rotated array*/
var array=[1,2,3,4,5];
var rotate1=function(){
    for(var i=0;i<2;i++)
    {
    var p=array.shift();
        //console.log(p);
        array.push(p);
    }
        console.log(array);
   
}
rotate1();
/*2.6 Return median of two sorted arrays of same size*/
var array1=[1,2,3,4,5];
var array2=[2,3,4,5,6];
var median=function(array1,array2){
    if(array1.length==array2.length)
    {
        var result1=array1.concat(array2);
        var a=result1[result1.length/2];
        var b=result1[result1.length/2-1];
        var median=(a+b)/2;
        console.log(median);
        
    }
}
median(array1,array2);
