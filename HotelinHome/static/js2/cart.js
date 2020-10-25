var count1 = 1;
var countEl = document.getElementById("count1");
var total_count = document.getElementById("total_count"); //추가
var total_count_view = document.getElementById("total_count_view"); //추가

function plus(){
  count1++;
  countEl.value = count1;
  total_count_view.value = total_count.value * countEl.value; //추가

//   calcul();

  }

// function calcul(){
//     alert(countEl.value);
// }



function minus(){
  
  if (count1 > 1) {
    count1--;
    countEl.value = count1;
    total_count_view.value = total_count_view.value - total_count.value; //추가  
  }  
}

var count2 = 1;
var countEl2 = document.getElementById("count2");
var total_count2 = document.getElementById("total_count2"); //추가
var total_count_view2 = document.getElementById("total_count_view2"); //추가

function plus2(){
  count2++;
  countEl2.value = count2;
  total_count_view2.value = total_count2.value * countEl2.value; //추가
}

function minus2(){
  
  if (count2 > 1) {
    count2--;
    countEl2.value = count2;
    total_count_view2.value = total_count_view2.value - total_count2.value; //추가  
  }  
}

function recalculate() {
    var price1=49*countEl.value;
    var price2=49*countEl2.value;
    subtotal_view.value=price1 + price2;
    
    realTotal();
}

function realTotal(){
    var discount = document.getElementById("discount_view").value;
    var tip = parseInt(document.getElementById("tip_view").value);
    realTotal_view.value=subtotal_view.value - discount + tip;
    // alert(realTotal_view.value);
}

function coupon(){
    document.querySelector('#disp_coupon').style.display = "block";
    discount_view.value=subtotal_view.value*0.1;
    realTotal();
}

function fivedollar(){
  tip_view.value="5";
  realTotal();
  
}

function tendollar(){
  tip_view.value="10";
  realTotal();
  
}