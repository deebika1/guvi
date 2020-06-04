/*3. Write a callback which is called
3.1. if the give number is even*/
function even(a,check)
{
var res=0;
if(check(a)==0)
{
return "even"
}
else
{
return "odd"
}
}
function checkCondition(a)
{
res=a%2
return res;
}
var res=even(3,checkCondition);
console.log(res);
/*3.2. if the given number is prime*/
function prime(a,check)
{
if(check(a)==a)
{
return "prime"
}
else
{
return "not prime"
}
}
function checkCondition(a)
{
    for(var i=2;i<a;i++)
    {
        var c=0;
        if(a%i==0)
        {
            c=1;
            break;
        }
    }
    if(c==0)
    {
        return a;
    }
    

}
var res=prime(5,checkCondition);
console.log(res);

/*3.3. if the number is palindrome*/


function palindrome(a,check)
{
var res=0;
var s='';
var n=[];
if(check(a)==a)
{
return "palindrome"
}
else
{
return "not a palindorme"
}
}
function checkCondition(a)
{
 //   console.log(a);
var rev=a.split("").reverse();
return rev;
}
var res=palindrome("hello",checkCondition);
console.log(res);
