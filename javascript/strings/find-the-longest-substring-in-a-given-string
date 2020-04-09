const readline=require('readline');
const imp=readline.createInterface({
  input:process.stdin
});
var user=[];
imp.on("line",(data)=>{
  user.push(data)
});
imp.on("close",()=>{
  var s=user[0].split(" ");
  var str1=s[0];
  var str2=s[1];
 var a=str1.includes(str2)
 if(a==true)
 {
   console.log(str2);
 }
  else
  {
    console.log("-1");
  }
});
