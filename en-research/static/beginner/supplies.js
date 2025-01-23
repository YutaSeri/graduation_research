function validate() {
  var quantity = document.getElementById("quantity").value;
  if (quantity.trim() === "") {
    alert("数量を入力してください");
    return false; 
  }

  return true; 
}