var total;
function add()
{
total=document.getElementById("mybudget").value;
    console.log(total);
   document.getElementById("b").innerHTML="$"+total;

}
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}
var sum=0;
function newElement()
{
//var li = document.createElement("li");
var product = document.getElementById("t").value;
console.log(product);
var productprice = document.getElementById("price").value;
console.log(productprice);
var d=document.getElementById('d')

var deleteimg=document.createElement('img')
deleteimg.setAttribute('src','dollar.jpg')
d.appendChild(s)
//var t1= document.createTextNode(product);
//li.appendChild(t1);

if (product === '') {
  alert("You must write something!");
} else {
  var table=document.getElementsByTagName('table')[0];
  var newRow =table.insertRow(1);
  var cell1=newRow.insertCell(0);
  var cell2=newRow.insertCell(1);
  cell1.innerHTML=product;
  cell2.innerHTML=productprice;
  var cell3=newRow.insertCell(2);
  cell3.innerHTML=deleteimg;

  //document.getElementById("myUL").appendChild(li);
}

//var li = document.createElement("li");
//var productprice = document.getElementById("price").value;
//console.log(productprice);
//var t2= document.createTextNode(productprice);
sum+=parseInt(productprice);
console.log(sum);
document.getElementById("ex").innerHTML="$"+sum;
var balance=total-sum;
document.getElementById("bal").innerHTML=balance;
}
/*li.appendChild(t2);

if (productprice === '') {
  alert("You must write something!");
} else {
  document.getElementById("myUL2").appendChild(li);
}

document.getElementById("t").value=" ";
document.getElementById("price").value=" ";

var span = document.createElement("SPAN");
var txt = document.createTextNode("\u00D7");
span.className = "close";
span.appendChild(txt);
li.appendChild(span);
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    console.log("hi");
    var div = this.parentElement;
    div.style.display = "none";
  }
}

*/
