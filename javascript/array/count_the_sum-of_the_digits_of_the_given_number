/*Given a number 'N' print the sum of each digit to the power of number of digits in given input.
Example :
Input => 1234
=> ( 1 ^ 4 ) + ( 2 ^ 4 ) + ( 3 ^ 4 ) + ( 4 ^ 4 )
=> 1 + 16 + 81 + 256
Output => 354
N <=100000000000
Sample Testcase :
INPUT
1234
OUTPUT
354*/
const readline=require('readline');
const inp=readline.createInterface({
  input:process.stdin
});
const n=[];
inp.on('line',(data)=>{
  n.push(data);
});
var s=[];
var c=0;
var res=0;
var k;
var r;
inp.on('close',()=>{
  s=parseInt(n[0]);
  k=s;
  //console.log(s);
  while(s!=0)
  {
    c++;
    s=parseInt(s/10);
  }
  while(k!=0)
  {
    r=parseInt(k%10);
    //console.log(r);
    res=res+Math.pow(r,c);
    k=parseInt(k/10);
  }
  console.log(res);
    
  });
