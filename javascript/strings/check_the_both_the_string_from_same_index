const readline=require('readline')
const imp=readline.createInterface({
  input:process.stdin
});
var user=[];
imp.on("line",(data)=>{
  user.push(data)
});
imp.on("close",()=>{
  var a=user[0].split(" ");
  var s1=a[0].split("");
  var s2=a[1].split("");
  var c=0;
  for(var i=0;i<s1.length;i++)
  {
    for(var j=0;j<s2.length;j++)
    {
      if(s1[i]==s2[j])
      {
        c=1;
        break;
      }
    }
    if(c==0)
    {
      break;
    }
  }
  if(c==0)
  {
    console.log("false");
  }
  else
  {
    console.log("true");
  }

  
});
