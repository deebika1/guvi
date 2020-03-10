const readline=require ('readline');
const inp=readline.createInterface({
  input:process.stdin
});
const userInput=[];
inp.on("line",(data)=>{
  userInput.push(data)
});
inp.on("close",()=>{
    
  var b=userInput[1].split(" ");
        b.sort(function(a, b){
    return a - b;
});
    //console.log(b);
     var count=0;
    var d=[];
   for(var i=0;i<b.length;i++)
   {
          var index=(parseInt(b[i])+1);
          var value=parseInt(b[i+1]);
          if(value==index)
          {
              d.push(b[i]);
              d.push(b[i+1])
              //console.log(d);
              
          }
          else
          {
              break;
          }
      
          }
var s=[... new Set(d)];
//console.log(d);
console.log(s.length);
});
//
//8
//1 6 5 3 2 4 10 12
//1 2 3 4 5 6 10 12
