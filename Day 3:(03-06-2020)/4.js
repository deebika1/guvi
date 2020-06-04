/*4. Do the below programs in arrow functions
4.1. Print odd numbers in an array*/
var array=[1,2,3,4,5];
var odd=(array.filter(n =>n%2==1 ));
console.log(odd);
/*4.2. Convert all the strings to title caps in a string array*/
var str="deebika";
var s='';
for(var i=0;i<str.length;i++)
{
    if(i==0)
    {
        s+=str[i].toUpperCase();
    }
    else
    {
        s+=str[i];
    }
}
console.log(s);
/*4.3. Sum of all numbers in an array*/
var array=[1,2,3,4,5];
var s=0;
var odd=(array.reduce((s,n)=>s+=n));
console.log(odd);
/*4.4. Return all the prime numbers in an array*/
var array=[1,2,3,4,5];
var sum=(array)=>{
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
/*4.5 Return all the palindromes in an array*/
var str1="deebika";
var palindrome1=(str)=>{
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
