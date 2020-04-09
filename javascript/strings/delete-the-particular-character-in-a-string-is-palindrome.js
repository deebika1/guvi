const readline=require('readline')
const imp=readline.createInterface({
  input:process.stdin
});
var user=[];
imp.on("line",(data)=>{
  user.push(data)
});
imp.on("close",()=>{
   var str=user[0];
function remove_character(str, char_pos) 
 {
  part1 = str.substring(0, char_pos);
  part2 = str.substring(char_pos + 1, str.length);
  return (part1 + part2);
 }
for(var i=0;i<str.length;i++)
{
var a=remove_character(str,i);
var b=a.split("");
//console.log("sub",b);
var s="";
//console.log(b[b.length-1]);
for(var j=b.length-1;j>=0;j--)
{ 
   // console.log("hello");
    s+=b[j];
    //console.log("reverse",s);
}
var rev=s;
//console.log(rev);
var s=0;
if(a===rev)
{
    s=1;
    break;
}
else
{
   s=0;
}
}
  if(s==1)
  {
      console.log("YES");
  }
  else
  {
      console.log("NO");
  }
});
