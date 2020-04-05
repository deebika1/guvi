/*Given a string and a number K.Print every kth character from the beginning.
Sample Testcase :
INPUT
string 3
OUTPUT
r g*/
const readline=require('readline');
const inp=readline.createInterface({
  input:process.stdin
});
const n=[];
inp.on('line',(data)=>{
  n.push(data);
});
var t=[];
var s;
var k;
var p='';
inp.on('close',()=>{
  t=n[0].split(" ");
  s=t[0].split("");
  k=parseInt(t[1]);
  console.log(s,k);
  for(var i=k-1;i<s.length;i=i+k)
  {
    p+=s[i]+' ';
  }
  console.log(p);
  
  
  });
