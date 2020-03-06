<html>
<body>
<table>
<div class=title>calci</div>
<tr>
<input type="text" id="result">
</tr>
<tr>
    <td><input type="button" id="C" value="C" onclick="obj.clear()"></td>
    <td><input type="button" id="0" value="0" onclick="obj.equation(0)"></td>
    <td><input type="button" id="/" value="/" onclick="obj.equation('/')"></td>
    <td><input type="button" id="*" value="*" onclick="obj.equation('*')"></td>
</tr>
<tr>
    <td><input type="button" id="7" value="7" onclick="obj.equation(7)"></td>
    <td><input type="button" id="8" value="8" onclick="obj.equation(8)"></td>
    <td><input type="button" id="9" value="9" onclick="obj.equation(9)"></td>
    <td><input type="button" id="-" value="-" onclick="obj.equation('-')"></td>
</tr>
<tr>
    <td><input type="button" id="4" value="4" onclick="obj.equation(4)"></td>
    <td><input type="button" id="5" value="5" onclick="obj.equation(5)"></td>
    <td><input type="button" id="6" value="6" onclick="obj.equation(6)"></td>
    <td><input type="button" id="+" value="+" onclick="obj.equation('+')"></td>
</tr>
<tr>
    <td><input type="button" id="1" value="1" onclick="obj.equation(1)"></td>
    <td><input type="button" id="2" value="2" onclick="obj.equation(2)"></td>
    <td><input type="button" id="3" value="3" onclick="obj.equation(3)"></td>
    <td><input type="button" id="=" value="=" onclick="obj.equal()"></td>
</tr>
<tr>
    <td><input type="button" id="." value="." onclick="obj.equation('.')"></td>
</tr>
<script src="calculatoroops.js">
</script>
</table>
</body>
</html

// javascript

class calculator{
equation(a){
    document.getElementById("result").value+=a;
}

equal(){
    var b= document.getElementById("result").value;
    var c = eval(b);
    document.getElementById("result").value=c;
}

clear(){
    document.getElementById("result").value="";
}
}
var obj = new calculator();
