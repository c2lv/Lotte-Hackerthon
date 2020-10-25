function showAddress(){
    if (ship_different_address.style.display == "block"){ //열려있다면
        document.querySelector('#ship_different_address').style.display = "none";
    }
    else{
        document.querySelector('#ship_different_address').style.display = "block";
    }
}

function Checkbox(a){
  var obj=document.getElementsByName("checkbox1");
  for(var i=0; i<obj.length; i++){
    if(obj[i]!=a){
      obj[i].checked=false;
    }
  }
}
