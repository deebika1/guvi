const readline=require('readline')
const imp=readline.createInterface({
  input:process.stdin
});
var user=[];
imp.on("line",(data)=>{
  user.push(data)
});
imp.on("close",()=>{
var a=user[0];
//console.log(a);
var b=a.substring(0,a.length/2);
//console.log(b);
var c=a.substring(a.length/2,a.length+1);
//console.log(c);
if(b==c)
{
    console.log("YES");
}
else
{
    console.log("NO");
}
});
